from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from scripts.models import student, supervisor, fyp, coordinator, examiner
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

@app.route('/supervisors')
def supervisors():
    return render_template('3_supervisors.html', supervisors=supervisor.query.all())

@app.route('/coordinators')
def coordinators():
    return render_template('4_coordinators.html', coordinators=coordinator.query.all())

@app.route('/examiners')
def examiners():
    return render_template('5_examiners.html', examiners=examiner.query.all())