from db.run_sql import run_sql
from models.gym_class import GymClass

def save(gymclass):
    sql = "INSERT INTO classes (name, date, price, capacity, premium) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [gymclass.name, gymclass.date, gymclass.price, gymclass.capacity, gymclass.premium]
    results = run_sql(sql, values)
    id = results[0]['id']
    gymclass.id = id

def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)