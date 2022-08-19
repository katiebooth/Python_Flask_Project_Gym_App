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