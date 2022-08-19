from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, premium, active) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.premium, member.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)