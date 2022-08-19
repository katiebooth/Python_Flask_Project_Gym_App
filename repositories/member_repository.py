from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, premium, active) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.premium, member.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id

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
        member = Member(result['name'], result['premium'], result ['active'], result['id']).__dict__
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)