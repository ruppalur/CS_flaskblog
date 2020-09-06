from flask import escape, request, render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog import app

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html', posts=posts, title='RAMU')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('homepage'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'you have logged in !','success')
            return redirect(url_for('homepage'))
        else:
            flash('login unsuccessful, please login again','danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/Logout')
def logout():
    return render_template('logout.html')
