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
    booking.id = results[0]['id']
    return booking

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings ORDER BY id"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        gym_class = class_repository.select(result["classes_id"])
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
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete_booking(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

