from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX - list all members
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)

#Add a new member
@members_blueprint.route("/add_member")
def add_member():
    return render_template("/members/new.html")

#Update members with the new member
@members_blueprint.route("/members", methods = ['POST'])
def new_member():
    member_name = request.form['name']
    premium_status = True if 'premium' in request.form else False
    active_status = True if 'active' in request.form else False
    new_member = Member(member_name, premium_status, active_status)
    member_repository.save(new_member)
    return redirect("/members")

#Edit member
@members_blueprint.route("/members/<id>/update")
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)

#Update member
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    premium = True if 'premium' in request.form else False
    active = True if 'active' in request.form else False
    member = Member(name, premium, active, id)
    member_repository.update(member)
    return redirect("/members")