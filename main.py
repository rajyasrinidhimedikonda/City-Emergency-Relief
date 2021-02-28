from flask import Flask, render_template, request, redirect
from random import choice

web_site = Flask(__name__)

userDat = {"admin":"password", "1":"2"}

@web_site.route('/', methods=['GET'])
def welcome():
	return render_template('welcome.html')

@web_site.route('/home', methods=['GET'])
def home():
	return render_template('home.html')

@web_site.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('uname-log')
    password = request.form.get('psw-log')
    error = ''
    if username in userDat:
      if userDat[username] == password:
        return redirect('/location')
      else:
        error = 'Incorrect password.'
        return render_template('login.html', error=error)
    else:
      error = 'Username does not exist.'
      return render_template('login.html', error=error)

  return render_template('login.html')

@web_site.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form.get('uname-reg')
    passOne = request.form.get('psw-reg-one')
    passTwo = request.form.get('psw-reg-two')

    error = ''
    if username in userDat:
      error = 'Username already exists.'
      return render_template('register.html', error=error)
    else:
      if passOne != passTwo:
        error = 'Passwords did not match.'
        return render_template('register.html', error=error)
      else:
        userDat[username] = passOne
        return redirect('/location')

  return render_template('register.html')

@web_site.route('/location', methods=['GET', 'POST'])
def location():
  if request.method == 'POST':
    return redirect('/home')
  return render_template('location.html')

@web_site.route('/shelters', methods=['GET'])
def shelters():
  return render_template('shelters.html')

@web_site.route('/inventory', methods=['GET'])
def inventory():
  return render_template('inventory.html')

@web_site.route('/warming-centers', methods=['GET'])
def warming_centers():
  return render_template('warming-centers.html')

@web_site.route('/garbage-tracking', methods=['GET'])
def garbage_tracking():
  return render_template('garbage-tracking.html')

@web_site.route('/hospitals', methods=['GET'])
def hospitals():
  return render_template('hospitals.html')

@web_site.route('/items-needed', methods=['GET'])
def items_needed():
  return render_template('items-needed.html')

@web_site.route('/settings', methods=['GET'])
def settings():
  return render_template('settings.html')

web_site.run(host='0.0.0.0', port=8080)