from flask import render_template, redirect, url_for, request

from asset_app import app, DB_PATH
from asset_app.modul.models import Violation, Intruder, Fine, addViolation, finesUser


@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html')

@app.route('/list_fines')
def list():
    current_fine = finesUser()
    return render_template('list_fines.html', current_fine=current_fine)


@app.route('/fines', methods=['GET', 'POST'])
def fine_forms():
    form = Violation()
    if form.validate_on_submit():
        name = form.name.data
        number_plate = form.number_plate.data
        violations = form.violations.data
        sum_fine = form.sum_fine.data
        date_violation = form.date_violations.data
        intruder = Intruder(name, number_plate)
        fines = Fine(violations, sum_fine, date_violation)
        addViolation(intruder, fines)

        return redirect(url_for('list')) # не работает
    return render_template('fine.html', form=form)
