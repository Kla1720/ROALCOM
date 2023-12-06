from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL
from chat import get_response

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'roalcom'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

def obtener_resultados(termino_busqueda):
    connection = mysql.connect()
    cursor = connection.cursor()

    cursor.execute("SELECT nombre, imagen FROM productos WHERE nombre LIKE %s", ('%' + termino_busqueda + '%',))
    resultados = cursor.fetchall()

    connection.close()
    return resultados


 
@app.route("/")
def index_get():
    if request.method == 'POST':
         termino_busqueda = request.form['termino_busqueda']
         resultados = obtener_resultados(termino_busqueda)
    conn=mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Productos')  # Modifica la consulta para seleccionar el nombre del producto y la URL de la imagen
    data = cursor.fetchall()
    conn.commit()
    return render_template('base.html', productos=data, resultados=resultados)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


 
    
@app.route('/producto/<int:id>')
def ver_producto(id):
        conn=mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Productos WHERE id=%s',id)  # Modifica la consulta para seleccionar el nombre del producto y la URL de la imagen
        data = cursor.fetchall()
        conn.commit()
        conn=mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Productos')  # Modifica la consulta para seleccionar el nombre del producto y la URL de la imagen
        data2 = cursor.fetchall()
        conn.commit()
        
        return render_template('producto.html', productos=data,productossim=data2)
    
 
@app.route('/nosotros')
def nosotros():
    return render_template('roalcom/nosotros.html')
 
@app.route('/vision')
def vision():
    return render_template('roalcom/vision.html')
 
@app.route('/mision')
def mision():
    return render_template('roalcom/mision.html')
 
@app.route('/contacto')
def contacto():
    return render_template('roalcom/contacto.html')
 
@app.route('/productos')
def productos():
    conn=mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos;')  # Modifica la consulta para seleccionar el nombre del producto y la URL de la imagen
    data = cursor.fetchall()
    conn.commit()
    return render_template('roalcom/productos.html', productos=data)



 
@app.route('/categoria/<string:categoria>')
def mostrar_categoria(categoria):
    conn=mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos WHERE Categoria=%s',categoria)  # Modifica la consulta para seleccionar el nombre del producto y la URL de la imagen
    data = cursor.fetchall()
    conn.commit()
    # Aquí puedes agregar más categorías según sea necesario
    if categoria == 'abrazaderas':
        conn=mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM productos;')  # Modifica la consulta para seleccionar el nombre del producto y la URL de la imagen
        data = cursor.fetchall()
        conn.commit()
        return render_template('categoria/abrazaderas.html' , productos=data)
    elif categoria == 'bridas':
        return render_template('categoria/bridas.html')
    elif categoria == 'codos':
        return render_template('categoria/codos.html')
    elif categoria == 'cajas':
        return render_template('categoria/cajas.html')
    elif categoria == 'marcos':
        return render_template('categoria/marcos.html')
    elif categoria == 'tapas':
        return render_template('categoria/tapas.html')
    elif categoria == 'adaptadores':
        return render_template('categoria/adaptadores.html')
    elif categoria == 'coplas':
        return render_template('categoria/coplas.html')
    elif categoria == 'hidrantes':
        return render_template('categoria/hidrantes.html')
    elif categoria == 'juntas':
        return render_template('categoria/juntas.html')
    elif categoria == 'valdes':
        return render_template('categoria/valdes.html')
    elif categoria == 'medidores':
        return render_template('categoria/medidores.html')
    elif categoria == 'reducciones':
        return render_template('categoria/reducciones.html')
    elif categoria == 'tees':
        return render_template('categoria/tees.html')
    elif categoria == 'uniones':
        return render_template('categoria/uniones.html')
    elif categoria == 'valvulas':
        return render_template('categoria/valvulas.html')
    elif categoria == 'giacomini':
        return render_template('categoria/giacomini.html')
    elif categoria == 'productos_G':
        return render_template('categoria/productos_G.html')
    else:
        return render_template('categoria/error_categoria.html')
    


    
 
if __name__ == "__main__":
    app.run(debug=True)