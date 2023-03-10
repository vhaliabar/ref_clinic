""" creating models for database """
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from ref_clinic.extentions import db


# Create a models
class Record(db.Model):
    """ creating record model """
    id = Column(Integer, primary_key=True)
    data = Column(String(1000))
    first_name = Column(String(100))
    last_name = Column(String(100))
    date = Column(DateTime(timezone=True), default=func.now())
    doctor_id = Column(Integer, ForeignKey('doctor.id'))


class Doctor(db.Model):
    """ creating doctor model """
    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True)
    years_xp = Column(Integer)
    name = Column(String(100))
    specialization = Column(String(100))
    records = relationship('Record', backref='recs')


# class Doctor(db.Model):
#     """ creating doctor model """
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     years_xp = db.Column(db.Integer)
#     name = db.Column(db.String(100))
#     specialization = db.Column(db.String(100))
#     records = db.relationship('Record', backref='recs')