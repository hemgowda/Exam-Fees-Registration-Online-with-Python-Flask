from flask_wtf import Form 
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField 
from wtforms import validators, ValidationError 
from flask import Flask, render_template, request, flash
 
class ContactForm(Form): 
 name = TextField("Name ",[validators.Required("Please enter your name.")]) 
 usn = TextField("USN",[validators.Required("Please enter your usn.")])  
 email = TextField("Email",[validators.Required("Please enter your email address."),  validators.Email("Please enter your email address.")]) 
 branch = SelectField('Branch', choices = [('ISE', 'ISE'),('CSE', 'CSE'),('TCE', 'TCE'),('ME', 'ME'),('CV', 'CV'),('ECE', 'ECE'),('EEE', 'EEE')]) 
 year =SelectField('Year', choices = [('1', '1st YEAR'),('2', '2nd YEAR'),('4', '3rd YEAR'),('4', '4th YEAR')])
 college=SelectField('College', choices = [('JNNCE', 'JNNCE'),('NITK', 'NITK'),('MCE', 'MCE'),('BMS', 'BMS'),('PES', 'PES')])  
 submit = SubmitField("Submit") 