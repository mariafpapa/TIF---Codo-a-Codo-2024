from flask import Flask
from flask import render_template, request, redirect, send_from_directory
from datetime import datetime
import os

#Conexión con Base de Datos MySQL
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_DB'] = 'click'

# Guardamos la ruta de la carpeta "uploads" en nuestra app
UPLOADS = os.path.join('uploads')
app.config['CARPETA'] = UPLOADS 

mysql = MySQL(app)

# Acceso a la carpeta uploads
@app.route('/uploads/<nombreImagen>')
def uploads(nombreImagen):
    return send_from_directory(app.config['CARPETA'],nombreImagen)

# Ruta a la raíz del sitio
@app.route('/')
def index():
    
    sql = "Select * from `click`.`productos`;"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    
    db_productos = cursor.fetchall()
    
    cursor.close()
    
    return render_template('productos/index.html', productos = db_productos)

# Función para eliminar un registro
@app.route('/delete/<int:id>')
def delete(id):
    
    sql = "Delete from `click`.`productos` where id=%s"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql,(id,))
    conn.commit()
    return redirect("/")

@app.route('/edit/<int:id>')
def edit(id):
    
    sql = "select * from `click`.`productos` where id=%s"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql,(id,))
    productos = cursor.fetchall()
    cursor.close()
    return render_template('productos/edit.html', productos = productos)

# Ruta para actualizar los datos de un producto
@app.route('/update', methods = ['POST'] )
def update():
    _titulo = request.form['txtTitulo']
    _descripcion = request.form['txtDescripcion']
    _precio = request.form['txtPrecio']
    _imagen = request.files['txtImagen']
    _cantidad = request.form['txtCantidad']
    _categoria = request.form['txtCategoria']
    _id = request.form['txtId']
    
    conn = mysql.connection
    cursor = conn.cursor()
    
    sql = "UPDATE `click`.`productos` SET titulo=%s,descripcion=%s,precio=%s,cantidad=%s,categoria=%s \
    WHERE id=%s;"
    datos = (_titulo,_descripcion,_precio,_cantidad,_categoria,_id)
    cursor.execute(sql,datos)
    
    if _imagen.filename != '':
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        nuevoNombreImagen = tiempo+_imagen.filename
        _imagen.save('TIF---Codo-a-Codo-2024/uploads/'+nuevoNombreImagen)
        
        # Consultamos la foto anterior para borrarla del servidor
        sql="SELECT imagen FROM `click`.`productos` WHERE id=%s"
        cursor.execute(sql,(_id,))
        fila = cursor.fetchone()
        
        if fila and fila[0] is not None:
            nombreImagenAnterior = fila[0]
            rutaImagenAnterior = os.path.join(app.config['CARPETA'],nombreImagenAnterior)
            
            if os.path.exists('TIF---Codo-a-Codo-2024/'+rutaImagenAnterior):
                    os.remove('TIF---Codo-a-Codo-2024/'+rutaImagenAnterior)
       
        # Actualizamos la base de datos con el nuevo nombre de la foto
            sql="UPDATE `click`.`productos` SET imagen=%s WHERE id=%s"
            cursor.execute(sql,(nuevoNombreImagen, _id)) 
                    
    conn.commit()
    cursor.close()
    
    return redirect("/")

# Ruta para ingresar un producto
@app.route('/create')
def create():
    return render_template('productos/create.html')

# Función para recibir los datos de los productos ingresados
@app.route('/store', methods = ['POST'] )
def storage():
    _titulo = request.form['txtTitulo']
    _descripcion = request.form['txtDescripcion']
    _precio = request.form['txtPrecio']
    _imagen = request.files['txtImagen']
    _cantidad = request.form['txtCantidad']
    _categoria = request.form['txtCategoria']
    
    if _imagen.filename != '':
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        nuevoNombreImagen = tiempo+_imagen.filename
        _imagen.save('TIF---Codo-a-Codo-2024/uploads/'+nuevoNombreImagen)
    
    datos = (_titulo,_descripcion,_precio,nuevoNombreImagen,_cantidad,_categoria)

    sql = "INSERT INTO `click`.`productos`(`id`,`titulo`,`descripcion`,`precio`,`imagen`,\
       `cantidad`,`categoria`) VALUES (NULL, %s, %s, %s, %s, %s, %s);"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)