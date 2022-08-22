from db.run_sql import run_sql
from models.gym_class import GymClass
import datetime

def save(gymclass):
    sql = "INSERT INTO classes (name, date, price, capacity, premium) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [gymclass.name, gymclass.date, gymclass.price, gymclass.capacity, gymclass.premium]
    results = run_sql(sql, values)
    id = results[0]['id']
    gymclass.id = id
    return gymclass

def select_all():
    classes = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)
    for row in results:
        class_date = str(row['date'])
        date = datetime.date(int(class_date[0:3]), int(class_date[9:10]), int(class_date[6:7]))
        gym_class = GymClass(row['name'], date, row['price'], row['capacity'], row['premium'], row['id'])
        classes.append(gym_class)
    return classes

def select(id):
    gym_class = None 
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        gym_class = GymClass(result['name'], result['date'], result['price'], result['capacity'], result['premium'], result['id'])
    return gym_class

def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)

#UPDATE
def update(gym_class):
    sql = "UPDATE classes SET (name, date, price, capacity, premium) = (%s, %s, %s, %s, %s)  WHERE id = %s"
    values = [gym_class.name, gym_class.date, gym_class.price, gym_class.capacity, gym_class.premium, gym_class.id]
    run_sql(sql, values)