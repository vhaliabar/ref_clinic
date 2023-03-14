""" all the view functions are placed in potes.py """
from flask import redirect, request, render_template, flash, url_for, Blueprint
from sqlalchemy.sql import func
from ref_clinic.models import Doctor, Record
from ref_clinic.extentions import db
from .forms import DoctorForm, SearchForm
main = Blueprint("", __name__)
# pylint: disable=E1101
# pylint: disable=no-else-return

@main.route('/')
def welcome():
    """ simply returns rendered index file """
    return render_template('index.html')


@main.context_processor
def navbar():
    """ function allows to add veriables to the all list of html files in templates/ """
    form=SearchForm()
    return {"form": form}


@main.route('/search', methods=['POST'])
def search():
    """ search for the doctor using search form """
    form=SearchForm()
    searched = form.searched.data
    if searched == "":
        flash('Please try another search pattern', category='error')
        return render_template('empty_results.html')
    doctors=Doctor.query.filter(Doctor.name.like('%'+searched+'%'))
    doctors=doctors.order_by(Doctor.years_xp).all()
    if not doctors:
        flash('Please try another search pattern', category='error')
        return render_template('empty_results.html')
    return render_template('search_result.html',
                    form=form,
                    doctors=doctors)


@main.route('/create_doctor', methods=['GET', 'POST'])
def create_doctor():
    """ create a new doctor """
    form = DoctorForm()
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        years_xp=request.form['years_xp']
        specialization=request.form['specialization']
        new_doctor = Doctor(name=name,
                            email=email,
                            years_xp=years_xp,
                            specialization=specialization)
        db.session.add(new_doctor)
        db.session.commit()
        flash(f'{name} has been added successfully!', category='success')
        return redirect(url_for('doctor_list'))
    return render_template("/create_doctor.html", form=form)


@main.route('/doctor_list', methods=['GET','POST'])
def doctor_list():
    """ returns the list off all doc's in DB """
    doctors_list = Doctor.query.all()
    doc_count = Doctor.query.count()
    return render_template('doctor_list.html', doctors_list=doctors_list, doc_count=doc_count)


@main.route('/delete_doctor/<int:doc_id>', methods=['GET','POST'])
def delete_doctor(doc_id):
    """ deletes specific doctor """
    doctor_to_delete = Doctor.query.get_or_404(doc_id)
    try:
        db.session.delete(doctor_to_delete)
        db.session.commit()
        flash(f'Doctor ({doctor_to_delete.name}) has been deleted successfully!',
              category='success')
        return redirect('/doctor_list')
    except ValueError:
        flash('Doctor has been deleted successfully!', category='error')
        return 'There was a problem deleting this task'


@main.route('/update/<int:doc_id>', methods = ['GET', 'POST'])
def update_doctor(doc_id):
    """ update doctor instance by ID """
    doctor_to_update = Doctor.query.get_or_404(doc_id)
    if request.method == 'POST':
        doctor_to_update.name=request.form.get('name')
        doctor_to_update.email=request.form.get('email')
        doctor_to_update.specialization=request.form.get('specialization')
        doctor_to_update.years_xp=request.form.get('years_xp')
        db.session.commit()
        flash(f'{doctor_to_update.name} has been updated successfully!', category='success')
        return redirect('/doctor_list')
    return render_template('doctor_update.html', doctor=doctor_to_update)

@main.route('/create_record', methods=['GET','POST'])
def create_record():
    """ create an appointment with a doctor """
    option_list=[]
    results = db.session.query(Doctor.name).all()
    for result in results:
        option_list.append(result[0])
    if request.method == 'POST':
        current_doctor_choice=request.form.get('doctor_id')
        doctor_id = db.session.query(Doctor).filter(
            Doctor.name == current_doctor_choice).first().id

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        data = request.form.get('data')
        new_record = Record(data=data,
                            first_name=first_name,
                            last_name=last_name,
                            doctor_id=doctor_id)
        db.session.add(new_record)
        db.session.commit()
        flash('Application has been added successfully!', category='success')
        return redirect(url_for('records_list'))
    return render_template("/create_appointment.html", option_list=option_list)


@main.route('/records_list')
def records_list():
    """ shows all appointments in a table """
    all_records = Record.query.all()
    return render_template('appointments_list.html', records_list=all_records)

@main.route('/record_update/<int:rec_id>', methods = ['GET', 'POST'])
def record_update(rec_id):
    """ updates specific item in database by its id """
    option_list=[]
    results = db.session.query(Doctor.name).all()
    for result in results:
        option_list.append(result[0])
    record_to_update = Record.query.get_or_404(rec_id)
    if request.method == 'POST':
        current_doctor_choice=request.form.get('doctor_id')
        try:
            doctor_id = db.session.query(Doctor).filter(
                Doctor.name == current_doctor_choice).first().id
            if doctor_id is not None:
                record_to_update.doctor_id=doctor_id
        except ValueError:
            flash('You didn\'t select a doctor', category='error')
            return redirect(f'/record_update/{record_to_update.id}')
        record_to_update.first_name=request.form.get('first_name')
        record_to_update.last_name=request.form.get('last_name')
        record_to_update.data=request.form.get('data')
        record_to_update.date=func.now()
        db.session.commit()
        flash(f'Record \'{record_to_update.id}\' has been updated successfully!',
              category='success')
        return redirect('/records_list')
    else:
        return render_template('record_update.html',
                               record=record_to_update, option_list=option_list)


@main.route('/delete_record/<int:rec_id>', methods=['GET','POST'])
def delete_record(rec_id):
    """ function deletes specific record by its id """
    record_to_delete = Record.query.get_or_404(rec_id)
    try:
        db.session.delete(record_to_delete)
        db.session.commit()
        flash(f'Record \"{record_to_delete.id}\" has been deleted successfully!',
              category='success')
        return redirect('/records_list')
    except ValueError:
        return f'There was a problem deleting this record\"{record_to_delete.id}\"'
