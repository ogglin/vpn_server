# -*- coding: utf-8 -*-
import os
from sys import platform
from flask import render_template, redirect, flash
from flask import request
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from kamvpn import app
from kamvpn.models import Users


@app.route('/')
def index():
    title = 'main'
    name = None
    return render_template('index.html', title=title, name=name)


@app.route('/login', methods=['POST', 'GET'])
def login_page():
    title = 'Авторизация'
    login = request.form.get('login')
    password = request.form.get('password')
    error = None
    if login and password:
        user = Users.query.filter_by(login=login).first()
        print(user.login)
        print(user.password)
        hash_pwd = generate_password_hash(password)
        print(hash_pwd)
        if check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            print('success')
            flash('Успешно')
            return redirect('/admin')
        else:
            flash('Не верный логин или пароль')
            return render_template('login.html', error=error, title=title)
    else:
        flash('Необходимо указать логин и пароль')
        return render_template('login.html', error=error, title=title)


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route("/admin")
@login_required
def settings():
    show_ips = ''
    if platform.startswith('linux'):
        show_ips = os.system('iptables -L')
    title = 'Admin Panel'
    return render_template('admin.html', title=title, show_ips=show_ips)
