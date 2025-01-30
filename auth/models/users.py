from auth import db
from hmac import compare_digest



class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable = False, unique = True)
    username = db.Column(db.String(30), unique=False, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)





