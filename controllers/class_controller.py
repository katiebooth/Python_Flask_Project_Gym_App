from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import GymClass
import repositories.class_repository as class_repository

classes_blueprint = Blueprint("classes", __name__)

# DASHBOARD - list all classes
@classes_blueprint.route("/")
def all_classes():
    classes_to_show = class_repository.select_all()
    return render_template("/dashboard.html", classes=classes_to_show)

# DISPLAY INDIVIDUAL CLASS
@classes_blueprint.route("/<id>")
def show_class(id):
    class_to_show = class_repository.select(id)
    return render_template("/classes/index.html", gym_class = class_to_show)

#Add new class
@classes_blueprint.route("/add_class")
def add_class():
    return render_template("/classes/new.html")

#Update the class list
@classes_blueprint.route("/", methods = ['POST'])
def new_class():
    class_name = request.form['name']
    class_date = request.form['date']
    price = request.form['price']
    capacity = request.form['capacity']
    premium = request.form['premium']
    new_class = GymClass(class_name, class_date, price, capacity, premium)
    class_repository.save(new_class)
    return redirect("/")