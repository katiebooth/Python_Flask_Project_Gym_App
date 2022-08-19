from db.run_sql import run_sql
from models.booking import Booking
from models.gym_class import GymClass
from models.member import Member
import repositories.class_repository as class_repository
import repositories.member_repository as member_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, classes_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.gym_class.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        gym_class = class_repository.select(result["class_id"])
        booking = Booking(member, gym_class, result["id"])
        bookings.append(booking)
    return bookings


def select(id):
    booking = None 
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        member = member_repository.select(result["member_id"])
        gym_class = class_repository.select(result["class_id"])
        booking = Booking(member, gym_class, result["id"])
    return result

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

