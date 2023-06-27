from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Admin(db.Model):
    admin_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_username=db.Column(db.String(20),nullable=True)
    admin_pwd=db.Column(db.String(200),nullable=True)

class Category(db.Model):
    cat_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    cat_name=db.Column(db.String(20),nullable=True)
    bookdeets = db.relationship("Book", back_populates="catdeets")


class Book(db.Model):
    book_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    book_title = db.Column(db.Text(),nullable=False)
    book_desc = db.Column(db.Text())
    book_cover = db.Column(db.String(100))
    book_publication =db.Column(db.Date())
    book_catid = db.Column(db.Integer, db.ForeignKey('category.cat_id'),nullable=False)  
    book_status =db.Column(db.Enum('1','0'),nullable=False, server_default=("0"))  
    
    #set relationships
    catdeets = db.relationship("Category", back_populates="bookdeets")
    bookreviews = db.relationship("Reviews", back_populates="thebook",cascade="all, delete-orphan")
    

class Reviews(db.Model):
    rev_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    rev_title = db.Column(db.String(255),nullable=False)
    rev_text = db.Column(db.String(255),nullable=False)
    rev_date =db.Column(db.DateTime(), default=datetime.utcnow)
    rev_userid = db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable=False)  
    rev_bookid =db.Column(db.Integer, db.ForeignKey('book.book_id'),nullable=False)  
    
    #set relationships
    reviewby = db.relationship("User", back_populates="user_reviews")
    thebook = db.relationship("Book", back_populates="bookreviews")
    
      
class User(db.Model):  
    user_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    user_fullname = db.Column(db.String(100),nullable=False)
    user_email = db.Column(db.String(120)) 
    user_pwd=db.Column(db.String(120),nullable=True)
    user_pix=db.Column(db.String(120),nullable=True) 
    user_datereg=db.Column(db.DateTime(), default=datetime.utcnow)#default 
    
    #set relationship    
    user_reviews=db.relationship("Reviews",back_populates='reviewby')    
  
    
class Donation(db.Model):
    don_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    don_amt = db.Column(db.Float, nullable=False)  
    don_userid = db.Column(db.Integer,db.ForeignKey("user.user_id"),nullable=True)
    don_fullname = db.Column(db.String(100),nullable=True)
    don_email = db.Column(db.String(100),nullable=True)

    don_refno=db.Column(db.String(20), nullable=False)
    don_paygate_response=db.Column(db.Text())

    don_date = db.Column(db.DateTime(), default=datetime.utcnow)
    don_status =db.Column(db.Enum('pending','failed','paid'),nullable=False, server_default=("pending"))  
    #set relationship
    donor = db.relationship('User',backref='mydonations')

