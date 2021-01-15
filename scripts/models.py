from datetime import datetime
from scripts import db

class student(db.Model):
    student_id = db.Column('student_id', db.Integer, primary_key=True)
    student_name = db.Column('student_name', db.String(20), nullable=False)
    student_phone = db.Column('student_phone', db.String(12))
    student_email = db.Column('student_email', db.String(20), nullable=False)
    student_mark = db.Column('student_mark', db.Integer)
    student_dept = db.Column('student_dept', db.String(3), nullable=False)
    
    proj_id = db.Column('proj_id', db.String(4), db.ForeignKey('fyp.proj_id'), nullable=False)
    sv_id = db.Column('sv_id', db.Integer, db.ForeignKey('supervisor.sv_id'), nullable=False)
    examiner_id = db.Column('ex_id', db.Integer, db.ForeignKey('examiner.ex_id'), nullable=False)

    def __repr__(self):
        return f"student('{self.student_id}', '{self.proj_id}')"

class supervisor(db.Model):
    sv_id = db.Column('sv_id', db.Integer, primary_key=True)
    sv_name = db.Column('sv_name', db.String(20), nullable=False)
    sv_niche = db.Column('sv_niche', db.String(20))
    sv_phone = db.Column('sv_phone', db.String(12), unique=True)
    sv_email = db.Column('sv_email', db.String(20), unique=True, nullable=False)
    sv_dept = db.Column('sv_dept', db.String(3), nullable=False)
    
    students = db.relationship('student', backref='supervisor', lazy=True)
    
    def __repr__(self):
        return f"supervisor('{self.sv_id}', '{self.sv_email}')"

class fyp(db.Model):
    proj_id = db.Column('proj_id', db.String(4), primary_key=True)
    proj_title = db.Column('proj_title', db.String(50))
    proj_type = db.Column('proj_type', db.String(11))
    proj_level = db.Column('proj_level', db.String(4))

    cd_id = db.Column('cd_id', db.Integer, db.ForeignKey('coordinator.cd_id'), nullable=False)

    students = db.relationship('student', backref='fyp', lazy=True)

    def __repr__(self):
        return f"fyp('{self.proj_id}', '{self.proj_title}')"

class coordinator(db.Model):
    cd_id = db.Column('cd_id', db.Integer, primary_key=True)
    cd_name = db.Column('cd_name', db.String(20), nullable=False)
    cd_dept = db.Column('cd_dept', db.String(3), nullable=False)
    cd_phone = db.Column('cd_phone', db.String(12))
    cd_email = db.Column('cd_email', db.String(20), unique=True, nullable=False)

    projects = db.relationship('fyp', backref='coordinator', lazy=True)
    
    def __repr__(self):
        return f"fyp('{self.cd_id}', '{self.cd_email}')"

class examiner(db.Model):
    ex_id = db.Column('ex_id', db.Integer, primary_key=True)
    ex_name = db.Column('ex_name', db.String(20), nullable=False)

    students = db.relationship('student', backref='examiner', lazy=True)

    def __repr__(self):
        return f"examiner('{self.ex_id}', '{self.ex_name}')"
