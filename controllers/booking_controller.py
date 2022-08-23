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

#once booking form completed, update information for the relevant class
#take the information of member and gym class ID from the form
#create a new instance of the booking class
#book the member onto the class as long as the following are true:
  #1. Member is not already booked onto class
  #2. Member has premium membership if class is premium
  #3. Class is not full

@booking_blueprint.route("/booking", methods = ['POST'])
def make_booking():
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    member_to_book = member_repository.select(member_id)
    gym_class = class_repository.select(gym_class_id)
    booking = Booking(member_to_book, gym_class)
    members_list = member_repository.list_all_members_for_class(gym_class.id)
    # for member in members_list:
    #     if member['name'] == member_to_book.name:
    #         return render_template("already_booked.html")
    #     else:  
    if member_to_book.active == False:
        return render_template("inactive_member.html")
    elif member_to_book.premium == False and gym_class.premium == True:
        return render_template("premium_class.html")
    elif len(members_list) >= gym_class.capacity:
        return render_template("class_full.html")           
    else:
         booking_repository.save(booking)
    return redirect("/")

