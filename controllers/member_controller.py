from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repository

member_blueprint = Blueprint("member", __name__)

# INDEX - list all members
@member_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)