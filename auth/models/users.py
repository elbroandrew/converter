from initialize import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable = False, index=True, unique = True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)
    # is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



