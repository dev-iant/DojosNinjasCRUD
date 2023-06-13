from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/create', methods=["POST"])
def add_ninja():
    data = {
        "dojo_iddojo": request.form["iddojo"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    Ninja.save(data)
    return redirect('/dojos')

@app.route('/ninjas')
def display_form():
    dojos = Dojo.get_all()
    return render_template('newninja.html', dojos=dojos)