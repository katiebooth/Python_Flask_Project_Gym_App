from db.run_sql import run_sql
from models.member import Member
import repositories.class_repository as class_repository

def save(member):
    sql = "INSERT INTO members (name, premium, active) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.premium, member.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['premium'], row ['active'], row['id']).__dict__
        members.append(member)
    return members

def select(id):
    member = None 
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        member = Member(result['name'], result['premium'], result ['active'], result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

#retrieve all members for a given class
def list_all_members_for_class(id):
    members_in_class = []
    sql = """SELECT * FROM members
            INNER JOIN bookings
            ON bookings.member_id = members.id
            WHERE classes_id = %s"""
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row["name"], row['id']).__dict__
        members_in_class.append(member)
    return members_in_class

#UPDATE
def update(member):
    sql = "UPDATE members SET (name, premium, active) = (%s, %s, %s)  WHERE id = %s"
    values = [member.name, member.premium, member.active, member.id]
    run_sql(sql, values)

#ACTIVE MEMBERS
def active_members():
    active_members = []
    sql = "SELECT * FROM members WHERE active = TRUE"
    results = run_sql(sql)
    for row in results:
        active_member = Member(row['name'], row['premium'], row ['active'], row['id']).__dict__
        active_members.append(active_member)
    return active_members

#INACTIVE MEMBERS
def inactive_members():
    inactive_members = []
    sql = "SELECT * FROM members WHERE active = FALSE"
    results = run_sql(sql)
    for row in results:
        inactive_member = Member(row['name'], row['premium'], row ['active'], row['id']).__dict__
        inactive_members.append(inactive_member)
    return inactive_members

#STANDARD MEMBERS
def standard_members():
    standard_members = []
    sql = "SELECT * FROM members WHERE premium = FALSE"
    results = run_sql(sql)
    for row in results:
        standard_member = Member(row['name'], row['premium'], row ['active'], row['id']).__dict__
        standard_members.append(standard_member)
    return standard_members

#PREMIUM MEMBERS
def premium_members():
    premium_members = []
    sql = "SELECT * FROM members WHERE premium = TRUE"
    results = run_sql(sql)
    for row in results:
        premium_member = Member(row['name'], row['premium'], row ['active'], row['id']).__dict__
        premium_members.append(premium_member)
    return premium_members

#STANDARD ACTIVE MEMBERS
def active_standard_members():
    active_standard_members = []
    sql = "SELECT * FROM members WHERE premium = FALSE AND active = TRUE"
    results = run_sql(sql)
    for row in results:
        active_standard_member = Member(row['name'], row['premium'], row ['active'], row['id']).__dict__
        active_standard_members.append(active_standard_member)
    return active_standard_members

#STANDARD INACTIVE MEMBERS
def inactive_standard_members():
    inactive_standard_members = []
    sql = "SELECT * FROM members WHERE premium = FALSE AND active = FALSE"
    results = run_sql(sql)
    for row in results:
        inactive_standard_member = Member(row['name'], row['premium'], row ['active'], row['id']).__dict__
        inactive_standard_members.append(inactive_standard_member)
    return inactive_standard_members

#PREMIUM ACTIVE MEMBERS
def active_premium_members():
    active_premium_members = []
    sql = "SELECT * FROM members WHERE premium = TRUE AND active = TRUE"
    results = run_sql(sql)
    for row in results:
        active_premium_member = Member(row['name'], row['premium'], row ['active'], row['id']).__dict__
        active_premium_members.append(active_premium_member)
    return active_premium_members

#PREMIUM INACTIVE MEMBERS
def inactive_premium_members():
    inactive_premium_members = []
    sql = "SELECT * FROM members WHERE premium = TRUE AND active = FALSE"
    results = run_sql(sql)
    for row in results:
        inactive_premium_member = Member(row['name'], row['premium'], row ['active'], row['id']).__dict__
        inactive_premium_members.append(inactive_premium_member)
    return inactive_premium_members


#CALCULATE REVENUE
def calculate_total_revenue():
    all_classes = class_repository.select_all()
    revenue = 0
    for gym_class in all_classes:
        revenue += gym_class.price * len(list_all_members_for_class(gym_class.id))
    return revenue