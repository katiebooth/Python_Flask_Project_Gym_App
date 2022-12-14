from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import GymClass
# from console import *
import repositories.class_repository as class_repository
import repositories.member_repository as member_repository

classes_blueprint = Blueprint("classes", __name__)

# DASHBOARD - list all classes
@classes_blueprint.route("/")
def all_classes():
    classes_to_show = class_repository.select_all()
    no_active_members = len(member_repository.active_members())
    no_inactive_members = len(member_repository.inactive_members())
    total_no_members = len(member_repository.select_all())
    no_standard_members = len(member_repository.standard_members())
    no_premium_members = len(member_repository.premium_members())
    no_active_standard_members = len(member_repository.active_standard_members())
    no_inactive_standard_members = len(member_repository.inactive_standard_members())
    no_active_premium_members = len(member_repository.active_premium_members())
    no_inactive_premium_members = len(member_repository.inactive_premium_members())
    total_revenue = member_repository.calculate_total_revenue()
    return render_template("/dashboard.html", classes=classes_to_show, 
                            no_active_members = no_active_members, 
                            no_inactive_members = no_inactive_members, 
                            total_no_members = total_no_members,
                            total_revenue=total_revenue,
                            no_standard_members = no_standard_members,
                            no_premium_members = no_premium_members,
                            no_active_standard_members = no_active_standard_members,
                            no_inactive_standard_members = no_inactive_standard_members,
                            no_active_premium_members = no_active_premium_members,
                            no_inactive_premium_members = no_inactive_premium_members
                            )

# DISPLAY INDIVIDUAL CLASS
@classes_blueprint.route("/<id>")
def show_class(id):
    class_to_show = class_repository.select(id)
    members_to_show = member_repository.list_all_members_for_class(id)
    spaces_remaining = class_to_show.capacity - len(members_to_show)
    return render_template("/classes/index.html", gym_class = class_to_show, members_to_show = members_to_show, spaces_remaining = spaces_remaining)

#Add new class
@classes_blueprint.route("/add_class")
def add_class():
    return render_template("/classes/new.html")

#Update the class list
@classes_blueprint.route("/", methods = ['POST'])
def new_class():
    class_name = request.form['name']
    class_date = request.form['date']
    class_time = request.form['time']
    price = request.form['price']
    capacity = request.form['capacity']
    premium_status = True if 'premium' in request.form else False
    new_class = GymClass(class_name, class_date, class_time, price, capacity, premium_status)
    class_repository.save(new_class)
    return redirect("/")

@classes_blueprint.route("/<id>/update")
def edit_class(id):
    gym_class = class_repository.select(id)
    return render_template('classes/edit.html', gym_class=gym_class)

#Update class
@classes_blueprint.route("/<id>", methods=["POST"])
def update_class(id):
    class_name = request.form['name']
    class_date = request.form['date']
    class_time =request.form['time']
    price = request.form['price']
    capacity = request.form['capacity']
    premium_status = True if 'premium' in request.form else False
    new_class = GymClass(class_name, class_date, class_time, price, capacity, premium_status, id)
    class_repository.update(new_class)
    return redirect("/")

#Delete class
@classes_blueprint.route("/<id>/delete", methods = ['POST'])
def delete_class(id):
    class_repository.delete_class(id)
    return redirect('/')

