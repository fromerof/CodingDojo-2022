import email
from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    if 'key_name' in session:
        print('la llave existe!')
    else:
        print("la llave 'key_name' NO existe")
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def create_user():
    print("Gost Post info")
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show') # cuando no se menciona ningun method se asume 'GET' - por eso aqui el redirect seria GET.

@app.route('/show')
def show_user():
    return render_template("show.html")


if __name__ == '__main__':
    app.run(debug=True)