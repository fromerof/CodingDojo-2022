from flask import Flask, render_template,request,redirect
# importar la clase de friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Friend.get_all()
    return render_template("index.html",friends=friends)
            

@app.route("/create_friend", methods=["POST"])
def create_friend():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    Friend.save(data)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)