import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

# enlace a base de datos vía sqlalchemy
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "EstudianteDataBase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

# modelado
class Estudiante(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    LastName = db.Column(db.String(25), unique=True, nullable=False)
    FirstName = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        return "<LastName: {}>".format(self.LastName), "<FirstName: {}>".format(self.FirstName)

# vistas
# @app.route("/")
@app.route("/", methods=["GET", "POST"])
def home():
    # return "My flask app"
    if request.form:
        print(request.form)
        estudiante = Estudiante(LastName=request.form.get("LastName"), FirstName=request.form.get("FirstName"))
        db.session.add(estudiante)
        db.session.commit()
    
    estudiantes = Estudiante.query.all()
    return render_template("home.html", estudiantes=estudiantes)
    #return render_template("home.html")
    
@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    idEstudiante = request.form.get("idEstudiante")
    estudiante = Estudiante.query.get(idlibro)
    estudiante.title = newtitle
    db.session.commit()
    return redirect("/")  
#
@app.route("/delete", methods=["POST"])
def delete():
    idEstudiante = request.form.get("idEstudiante")
    estudiante = Estudiante.query.get(idEstudiante)
    db.session.delete(estudiante)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)



