from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
from models.gym_class import GymClass
from models.member import Member
import repositories.booking_repository as booking_repository
import repositories.class_repository as class_repository
import repositories.member_repository as member_repository

booking_blueprint = Blueprint("booking", __name__)

#book a member onto a class - input form
@booking_blueprint.route("/booking/new")
def create_booking():
    members = member_repository.select_all()
    gym_classes = class_repository.select_all()
    return render_template("/bookings/new.html", members = members, gym_classes = gym_classes)

#once booking form completed, update information in the individual class
@booking_blueprint.route("/booking", methods = ['POST'])
def make_booking():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    member = member_repository.select(member_id)
    gym_class = class_repository.select(gym_class_id)
    booking = Booking(member, gym_class)
    booking_repository.save(booking)
    return redirect("/")

