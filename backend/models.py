from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt, generate_password_hash
from app import db
import datetime  # Import the datetime module

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(100))  # Optional field
    created_by = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_by = db.Column(db.String(100))
    modified_date = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf-8')
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Grievance(db.Model):
    __tablename__ = 'grievances'
    grievance_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=True) 
    sentiment = db.Column(db.String(50), nullable=True)  # New field for sentiment
    priority = db.Column(db.String(50), nullable=True)
    file_path = db.Column(db.String(255), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    created_by = db.Column(db.String(100), nullable=True)
    modified_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    modified_by = db.Column(db.String(100), nullable=True)
    
    def __init__(self, student_id, category, description, status, sentiment=None, file_path=None, priority=True, created_date=True, created_by=True, modified_date=True, modified_by=True):
        self.student_id = student_id
        self.category = category
        self.description = description
        self.status = status
        self.sentiment = sentiment
        self.priority = priority
        self.file_path = file_path
        self.created_date = created_date
        self.created_by = created_by
        self.modified_date = modified_date
        self.modified_by = modified_by
        