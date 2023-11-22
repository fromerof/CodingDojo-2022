from flask import Flask # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return render_template("index.html") # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:flask>')
def say(flask):
    return f"!Hola, {(flask.capitalize())}!"

@app.route('/repeat/<int:num>/<string:flask>')
def repeat(flask,num):
    for i in range(0,num):
        return f"!Hola, {flask*num}!" 


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

