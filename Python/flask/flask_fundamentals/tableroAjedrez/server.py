from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html") # ¡Fíjate en los 2 nuevos argumentos nombrados!

#@app.route('/chess')
#def chess():
#    return render_template("index.html")

@app.route('/chess/<int:num>')
def chess(num):
    return render_template("index.html",num=num)

#@app.route('/chess/<int:num>/<int:num>/<color>/<color>')
#def chess(num,color):
#    return render_template("index.html",num=num,color="color")


if __name__=="__main__":
    app.run(debug=True)
