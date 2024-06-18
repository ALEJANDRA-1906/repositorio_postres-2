from flask import Flask, render_template

app = Flask(__name__)

#creamos decorador @app.route
@app.route('/') #ruta principal
def home(): #Las funciones vana  representar las vistas
    # return 'Página de Inicio'
    
    data = {
        'titulo':'Vanedilla',
    } #diccionario para enviar valores a nuestra plantilla html
    return render_template('index.html', data=data)



@app.route('/catalogo')
def catalogo():
    data = {
        'titulo': 'Catalogo de Postres',
    }
    datos = [
    {'postre': 'Cupcakes de chocolate','imagen': 'img/cupcakes_chocolates.jpg','descripcion': 'Deliciosos cupcakes de chocolate con frosting de vainilla.'},
    {'postre': 'Cupcakes de fresa','imagen': 'img/cupcakes_fresa.jpg','descripcion': 'Irresistibles cupcakes de fresa con crema batida.'},
    {'postre': 'Cupcakes de vainilla','imagen': 'img/cupcakes_vainilla.jpg','descripcion': 'Irresistibles cupcakes sabor a vainilla con crema batida.'},

    {'postre': 'Pastel de zanahoria', 'imagen': 'img/torta_zanahoria.jpg', 'descripcion': 'Jugoso pastel de zanahoria con glaseado de queso crema.'},
]
    # return 'Aquí se mostrarán los postres'
    return render_template('catalogo.html', data=data,datos=datos)




if __name__ == '__main__':
    app.run(debug=True)