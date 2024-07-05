from flask import Flask, render_template, request, redirect, send_from_directory 
from flask_mysqldb import MySQL
from datetime import datetime
import os

# Creación de la aplicación
app = Flask(__name__)

# Inicialización de la extensión MySQL
mysql = MySQL()

# Creación de la conexión con la base de datos
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_BD"]="click"

# Guardamos la ruta de la carpeta "uploads" en nuestra app
UPLOADS = os.path.join("uploads")
app.config["UPLOADS"]=UPLOADS

mysql.init_app(app)

# Acceso a la carpeta uploads
@app.route('/uploads/<nameImage>')
def uploads(nameImage):
 return send_from_directory(app.config['UPLOADS'], nameImage)

# Ruta a la raíz del sitio
@app.route("/")
def index():
    
    sql = "SELECT * FROM `click`.`products`"

    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    
    db_products = cursor.fetchall()
    print("-"*60)
    for product in db_products:
        print(product)
        print("-"*60)
    
    cursor.close()

    return render_template("products/index.html", products=db_products)

# Función para eliminar un registro
@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connection  
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `click`.`products` WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    return redirect('/')

# Función para editar un registro
# edit

# Ruta para actualizar los datos de un producto
@app.route("/update", methods=['POST'])
def update():
    _id = request.form['txtID']
    _title = request.form['txtTitle']
    _description = request.form['txtDescription']
    _price = request.form['txtPrice']
    _count = request.form['txtCount']
    _category = request.form['txtCategory']
    _image = request.files['txtImage']
    
    sql = "UPDATE click.products SET title=%s, description=%s, price=%s, count=%s, category=%s WHERE id=%s"
    data = (_title, _description, _price, _count, _category, _id)
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, data)
    
    if _image.filename != "":
        now = datetime.now()
        date = now.strftime("%Y%H%M%S")
        newNameImage = date + _image.filename
        _image.save("uploads/" + newNameImage)
        
        cursor.execute("SELECT image FROM click.products WHERE id=%s", (_id,))
        row = cursor.fetchone()
        if row and row[0] is not None:
            namePreviousImage = row[0]
            pathPreviousImage = os.path.join(app.config["UPLOADS"], namePreviousImage)
            if os.path.exists(pathPreviousImage):
                os.remove(pathPreviousImage)
        cursor.execute("UPDATE click.products SET image=%s WHERE id=%s", (newNameImage, _id))
    
    conn.commit()
    cursor.close()
    return redirect("/")

# Ruta para ingresar un producto
@app.route("/create")
def create():
    return render_template("products/create.html")

# Función para recibir los datos de los productos ingresados
# storage


if __name__ =="__main__":
    app.run(debug=True) 