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

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)