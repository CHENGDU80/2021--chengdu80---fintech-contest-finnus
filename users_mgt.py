from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import engine

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Integer)


userTable = Table('user', User.metadata)


def create_user_table():
    User.metadata.create_all(engine)


def add_user(username, password, email, admin):
    hashed_password = generate_password_hash(password, method='sha256')

    insert_stmt = userTable.insert().values(
        username=username, email=email, password=hashed_password, admin=admin
    )

    conn = engine.connect()
    conn.execute(insert_stmt)
    conn.close()


def update_password(username, password):
    hashed_password = generate_password_hash(password, method='sha256')

    update = userTable.update().\
        values(password=hashed_password).\
        where(userTable.c.username==username)

    conn = engine.connect()
    conn.execute(update)
    conn.close()


def show_users():
    select_stmt = select([userTable.c.id,
                        userTable.c.username,
                        userTable.c.email,
                        userTable.c.admin])

    conn = engine.connect()
    results = conn.execute(select_stmt)

    users = []

    for result in results:
        users.append({
            'id' : result[0],
            'username' : result[1],
            'email' : result[2],
            'admin' : str(result[3])
        })

    conn.close()

    return users

# add_user('sidharthmittal25', 'admin', 'sidharth.mittal@u.nus.edu', 1)
# add_user('bella_nus', 'admin2bella', 'isabella.poh@u.nus.edu', 0)
# add_user('corporate_user', 'corporate_user', 'tester@gmail.com', 1)
# add_user('individual_user', 'individual_user', 'tester2@gmail.com', 2)