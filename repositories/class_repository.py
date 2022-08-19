from db.run_sql import run_sql
from models.gym_class import GymClass

def save(gymclass):
    sql = "INSERT INTO classes (name, date, price, capacity, premium) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [gymclass.name, gymclass.date, gymclass.price, gymclass.capacity, gymclass.premium]
    results = run_sql(sql, values)
    id = results[0]['id']
    gymclass.id = id

def select_all():
    classes = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)
    for row in results:
        gym_class = GymClass(row['name'], row['date'], row['price'], row['capacity'], row['premium'], row['id']).__dict__
        classes.append(gym_class)
    return classes

def select(id):
    gym_class = None 
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        gym_class = GymClass(result['name'], result['date'], result['price'], result['capacity'], result['premium'], result['id']).__dict__
    return gym_class

def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)