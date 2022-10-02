from flask import render_template, redirect, url_for, request
import datetime
from asset import app
from asset.prog.models import User, UserForm, listUser, UserFast, listFast, Fast, addUser


@app.route('/')
@app.route('/hello')
def hello():
    return render_template('fast.html', listFast=listFast)


@app.route("/forms", methods=['GET', 'POST'])
def forms():
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(name, email, password)
        addUser(user)
        listUser.append(user)
        return redirect(url_for('user'))
    return render_template("forms.html", form=form, User=User)


@app.route('/user')
def user():
    sorting = request.args.get('sorting')
    if sorting == 'name':
            return render_template("user.html", listUser=sorted(listUser, key=lambda user: user.name))
    elif sorting == 'surname':
            return render_template("user.html", listUser=sorted(listUser, key=lambda user: user.surname))
    elif sorting == 'email':
            return render_template("user.html", listUser=sorted(listUser, key=lambda user: user.email))
    else:
        return render_template("user.html", listUser=listUser)


@app.route('/fastForms',  methods=['GET', 'POST'])
def fast_forms():
    form = UserFast()
    if form.validate_on_submit():
        now = datetime.datetime.now()
        name = form.name.data
        headerLogo = form.headerLogo.data
        message = form.message.data
        files = form.files.data
        fastes = Fast(name, headerLogo, message, files, now)
        for i in listUser:
            if i.name == name:
                listFast.append(fastes)
                return redirect(url_for('hello'))
        else:
            print('No')
            return redirect(url_for('forms'))
    return render_template("fastForms.html", form=form)



