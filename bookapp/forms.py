from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired
class Signupform(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="your fullname is required")])
    
    email = StringField(" Email",validators=[Email()])
    password = PasswordField("password",validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password",validators=[EqualTo('password',message="confirm password must be equal to password")])
   
    btn = SubmitField("Sign up!")
 
  
class Profileform(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="your fullname is required")])
    
    pix = FileField("Display picture",validators=[FileRequired(), FileAllowed(['jpg','png'], 'images only!')])
    btn = SubmitField("upload")
 
    
    
    
     
    

