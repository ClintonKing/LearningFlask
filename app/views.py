from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index(name=None):
    user = {'nickname': 'Clinton'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland.'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'I just saw a great movie.'
        }
    ]

    return render_template('home.html', title='Home - FlaskTest', user=user, posts=posts)

@app.route('/hello')
def hello():
	return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
