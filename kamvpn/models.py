from flask_login import UserMixin

from kamvpn import db, manager


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username


@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
