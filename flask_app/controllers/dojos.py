from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def show_dojos():
    dojo = Dojo.get_all()
    return render_template("dojos.html", all_dojos = dojo)

@app.route('/dojocreate', methods=["POST"])
def add_dojos():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:iddojo>')
def show_ninjas(iddojo):
    data = {
        "iddojo": iddojo
    }
    dojo = Dojo.join(data)
    return render_template("ninjalist.html", dojo=dojo)