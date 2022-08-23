from db.run_sql import run_sql
from models.gym_class import GymClass
import datetime
import repositories.member_repository as member_repository

def save(gymclass):
    sql = "INSERT INTO classes (name, date, time, price, capacity, premium) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [gymclass.name, gymclass.date, gymclass.time, gymclass.price, gymclass.capacity, gymclass.premium]
    results = run_sql(sql, values)
    id = results[0]['id']
    gymclass.id = id
    return gymclass

def select_all():
    classes = []
    sql = "SELECT * FROM classes ORDER BY date"
    results = run_sql(sql)
    for row in results:
        date = datetime.datetime.fromisoformat(str(row['date']))
        date = datetime.datetime.strftime(date,'%d %b')
        spaces_remaining = row['capacity'] - len(member_repository.list_all_members_for_class(row['id']))
        gym_class = GymClass(row['name'], date, row['time'], row['price'], spaces_remaining, row['premium'], row['id'])
        classes.append(gym_class)
    return classes

def select(id):
    gym_class = None 
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        date = datetime.datetime.fromisoformat(str(row['date']))
        date = datetime.datetime.strftime(date,'%d %b')
        gym_class = GymClass(row['name'], date, row['time'], row['price'], row['capacity'], row['premium'], row['id'])
    return gym_class

def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)

def delete_class(id):
    sql = "DELETE FROM classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


#UPDATE
def update(gym_class):
    sql = "UPDATE classes SET (name, date, time, price, capacity, premium) = (%s, %s, %s, %s, %s, %s. %s)  WHERE id = %s"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.price, gym_class.capacity, gym_class.premium, gym_class.id]
    run_sql(sql, values)