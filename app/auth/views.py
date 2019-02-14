from flask import render_template, flash, redirect, url_for

from .forms import RegisterForm, LoginForm
from . import auth
from ..models import Player
from .. import db


@auth.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        player = Player(
            email= form.email.data,
            username = form.username.data,
            first_name= form.first_name.data,
            last_name= form.last_name.data,
            position = form.position.data
        )
        db.session.add(player)
        db.session.commit()
        flash('You have successfully registered! You may now login.')
        return redirect(url_for('auth.login'))


    return render_template('auth/register.html', form=form, title='Register')