import os 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)




class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    team_name = db.Column(db.String(255), unique = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    project_name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = True)
    completed = db.Column(db.Boolean, default = False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable = False)
    



if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to db...")