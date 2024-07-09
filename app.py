from flask import Flask
from flask import render_template, request, redirect, send_from_directory
from datetime import datetime
import os

# Conexión con Base de Datos MySQL
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_DB"] = "click"

# Guardamos la ruta de la carpeta "uploads" en nuestra app
UPLOADS = os.path.join("./uploads")
app.config["CARPETA"] = UPLOADS

mysql = MySQL(app)

# Acceso a la carpeta uploads
@app.route("/uploads/<nombreImagen>")
def uploads(nombreImagen):
    return send_from_directory(app.config["CARPETA"], nombreImagen)

# Ruta a la raíz del sitio
@app.route("/")
def index():
    sqlInformatica = "Select * from productos Where categoria like 'Informatica';"
    sqlAudio = "Select * from productos Where categoria like 'Audio';"
    sqlVideo = "Select * from productos Where categoria like 'Video';"
    sqlGaming = "Select * from productos Where categoria like 'Gaming';"
    sqlTelefonia = "Select * from productos Where categoria like 'Telefonia';"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sqlInformatica)
    db_informatica = cursor.fetchall()
    cursor.execute(sqlAudio)
    db_audio = cursor.fetchall()
    cursor.execute(sqlVideo)
    db_video = cursor.fetchall()
    cursor.execute(sqlGaming)
    db_gaming = cursor.fetchall()
    cursor.execute(sqlTelefonia)
    db_telefonia = cursor.fetchall()
    cursor.close()
    return render_template(
        "index.html",
        informatica=db_informatica,
        audio=db_audio,
        video=db_video,
        gaming=db_gaming,
        telefonia=db_telefonia,
    )

# Ruta raiz de productos
@app.route("/products")
def indexProductos():
    sql = "Select * from `click`.`productos`;"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    db_productos = cursor.fetchall()
    cursor.close()
    return render_template("productos/index.html", productos=db_productos)

# Función para eliminar un registro
@app.route("/products/delete/<int:id>")
def delete(id):
    sqlImagen = "Select imagen from `click`.`productos` where id=%s"
    sql = "Delete from `click`.`productos` where id=%s"
    conn = mysql.connection
    cursor = conn.cursor()
    
    cursor.execute(sqlImagen, (id,))
    fila = cursor.fetchone()

    if fila and fila[0] is not None:
        nombreImagenAnterior = fila[0]
        rutaImagenAnterior = os.path.join(app.config["CARPETA"], nombreImagenAnterior)

        if os.path.exists("./" + rutaImagenAnterior):
            os.remove("./" + rutaImagenAnterior)   
    
    cursor.execute(sql, (id,))
    conn.commit()
    return redirect("/products")

@app.route("/products/edit/<int:id>")
def edit(id):
    sql = "select * from `click`.`productos` where id=%s"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    productos = cursor.fetchall()
    cursor.close()
    return render_template("productos/edit.html", productos=productos)

# Ruta para actualizar los datos de un producto
@app.route("/products/update", methods=["POST"])
def update():
    _titulo = request.form["txtTitulo"]
    _descripcion = request.form["txtDescripcion"]
    _precio = request.form["txtPrecio"]
    _imagen = request.files["txtImagen"]
    _cantidad = request.form["txtCantidad"]
    _categoria = request.form["txtCategoria"]
    _id = request.form["txtId"]

    conn = mysql.connection
    cursor = conn.cursor()

    sql = "UPDATE `click`.`productos` SET titulo=%s,descripcion=%s,precio=%s,cantidad=%s,categoria=%s \
    WHERE id=%s;"
    datos = (_titulo, _descripcion, _precio, _cantidad, _categoria, _id)
    cursor.execute(sql, datos)

    if _imagen.filename != "":
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        nuevoNombreImagen = tiempo + _imagen.filename
        _imagen.save("./uploads/" + nuevoNombreImagen)

        # Consultamos la foto anterior para borrarla del servidor
        sql = "SELECT imagen FROM `click`.`productos` WHERE id=%s"
        cursor.execute(sql, (_id,))
        fila = cursor.fetchone()

        if fila and fila[0] is not None:
            nombreImagenAnterior = fila[0]
            rutaImagenAnterior = os.path.join(app.config["CARPETA"], nombreImagenAnterior)

            if os.path.exists("./" + rutaImagenAnterior):
                os.remove("./" + rutaImagenAnterior)

            # Actualizamos la base de datos con el nuevo nombre de la foto
            sql = "UPDATE `click`.`productos` SET imagen=%s WHERE id=%s"
            cursor.execute(sql, (nuevoNombreImagen, _id))

    conn.commit()
    cursor.close()

    return redirect("/products")


# Ruta para ingresar un producto
@app.route("/products/create")
def create():
    return render_template("productos/create.html")


# Función para recibir los datos de los productos ingresados
@app.route("/products/store", methods=["POST"])
def storage():
    _titulo = request.form["txtTitulo"]
    _descripcion = request.form["txtDescripcion"]
    _precio = request.form["txtPrecio"]
    _imagen = request.files["txtImagen"]
    _cantidad = request.form["txtCantidad"]
    _categoria = request.form["txtCategoria"]

    if _imagen.filename != "":
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        nuevoNombreImagen = tiempo + _imagen.filename
        _imagen.save("./uploads/" + nuevoNombreImagen)

    datos = (_titulo, _descripcion, _precio, nuevoNombreImagen, _cantidad, _categoria)

    sql = "INSERT INTO `click`.`productos`(`id`,`titulo`,`descripcion`,`precio`,`imagen`,\
       `cantidad`,`categoria`) VALUES (NULL, %s, %s, %s, %s, %s, %s);"

    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return redirect("/products")


if __name__ == "__main__":
    app.run(debug=True)
