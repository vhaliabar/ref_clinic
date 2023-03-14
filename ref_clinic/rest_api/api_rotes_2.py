from flask import jsonify, request
from ref_clinic.models import Doctor, Record
from ref_clinic import main
from flask_marshmallow import Marshmallow
from ref_clinic import db

ma=Marshmallow(main)


class DoctorSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "email","years_xp","name","specialization","_links")
    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("update_doctor", values=dict(doc_id="<id>")),
            "collection": ma.URLFor("doctor_list"),
        }
    )

class RecordSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "data","last_name","first_name","date","doctor_id","_links")
    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("record_update", values=dict(rec_id="<id>")),
            "collection": ma.URLFor("records_list"),
        }
    )

doctor_schema=DoctorSchema()
doctors_schema=DoctorSchema(many=True)
record_schema=RecordSchema()
records_schema=RecordSchema(many=True)

@main.route('/api/first')
def first():
    """ first try """
    return jsonify(message='You are good to make the same, Danylo!')


@main.route('/api/doctor/<int:doctor_id>', methods=['GET'])
def doctor(doctor_id:int):
    """ first try """
    my_doctor=Doctor.query.filter_by(id=doctor_id).first()
    print(type(my_doctor))
    if my_doctor:
            return jsonify(doctor_schema.dump(my_doctor))
    else:
        return jsonify(message='This doctor doesn\'t exist'), 404


@main.route('/api/doctors')
def doctors():
    """ shows all doctors in json format """
    all_doctors=Doctor.query.all()
    print(all_doctors)
    return jsonify(doctors_schema.dump(all_doctors))


@main.route('/api/add_doctor', methods=['POST'])
def add_doctor():
    email = request.form['email']
    test = Doctor.query.filter_by(email=email).first()
    if test:
        return jsonify(message='That email already exists'), 409
    else:
        name = request.form['name']
        years_xp = request.form['years_xp']
        specialization = request.form['specialization']
        new_doc = Doctor(name=name,
                    years_xp=years_xp,
                    specialization=specialization,
                    email=email)
        db.session.add(new_doc)
        db.session.commit()
        return jsonify(message= f'A Doctor \'{name}\' created successfully!'),201


@main.route('/api/records')
def records():
    """ first try """
    all_records=Record.query.all()
    return jsonify(records_schema.dump(all_records))

@main.route('/api/record/<int:record_id>', methods=['GET'])
def record(record_id:int):
    """ first try """
    my_record=Record.query.filter_by(id=record_id).first()
    if my_record:
            return jsonify(record_schema.dump(my_record))
    else:
        return jsonify(message='This recond doesn\'t exist'), 404
