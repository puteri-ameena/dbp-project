from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from scripts.models import schedule, student, supervisor, fyp, coordinator, examiner
from scripts import app, db



@app.route('/')
def home():
    return render_template('0_home.html')

@app.route('/students')
def students():
    # students = student.query.all()
    return render_template('1_students.html', students=student.query.all())

@app.route('/projects')
def projects():
    return render_template('2_projects.html', projects=fyp.query.all())

@app.route('/schedules')
def schedules():
    return render_template('3_schedule.html')

@app.route('/supervisors')
def supervisors():
    return render_template('4_supervisors.html')

@app.route('/coordinators')
def coordinators():
    return render_template('5_coordinators.html')

@app.route('/examiners')
def examiners():
    return render_template('6_examiners.html')