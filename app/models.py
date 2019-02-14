from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, loginmanager


class Player(UserMixin, db.Model):

    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True,nullable = False)
    username = db.Column(db.String(60), index=True, unique=True,nullable = False)
    first_name = db.Column(db.String(60), index=True,nullable = False)
    last_name = db.Column(db.String(60), index=True,nullable = False)
    password_hash = db.Column(db.String(128))
    position = db.Column(db.String(25),nullable = False)
    is_admin = db.Column(db.Boolean, default=False,nullable = False)

    @property
    def password(self):
        '''
        prevent password from being accessed
        '''
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # set up user_loader
    @loginmanager.user_loader
    def user_loader(user_id):
        return Player.query.get(int(user_id))


class MatchPlayed(db.Model):

    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    opponent = db.Column(db.String(60), nullable = False)
    goal_scored = db.Column(db.Integer, nullable = False)
    goal_against = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<Opponent: {}>'.format(self.opponent)

