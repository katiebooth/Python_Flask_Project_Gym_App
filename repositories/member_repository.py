from db.run_sql import run_sql
from models.member import Member

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