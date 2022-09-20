from flask import render_template, redirect, url_for, request

from asset import app
from asset.prog.models import User, UserForm, listUser, UserFast, listFast


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
        listUser.append(user)
        print(len(listUser))
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
        name = form.name.data
        headerLogo = form.headerLogo.data
        date = form.date.data
        message = form.message.data
        files = form.files.data
        fastes = UserFast(name, headerLogo, date, message, files)
        listFast.append(fastes)
        return redirect(url_for('hello'))
    return render_template("fastForms.html", form=form)


    # if request.method == 'POST':
    #     name = request.form.get('header_fast')
    #     fast = request.form.get('fast')
    #     author = request.form.get('user')
    #     date = request.form.get('date')
    #     fastes = UserFast(name, fast, author, date)
    #     listFast.append(fastes)
    #     return redirect(url_for('hello'))
        # for i in listUser:
        #     if i.name == author:
        #         listFast.append(fastes)
        #         return redirect(url_for('hello'))
        # else:
        #     print('No')
        #     return redirect(url_for('forms'))
    # return render_template("fastForms.html")

