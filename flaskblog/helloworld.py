from flask import Flask, escape, request

app = Flask(__name__)

#Hello world of flask
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

#Hello world with variable Rules - String
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hello %s!' % escape(username)

#Hello world with variable Rules - Integer
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, id is an integer
    return 'You are looking for Post %s!' % post_id

#Hello world with variable Rules - subpaths = /etc/bin
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

#If you access the URL without a trailing slash, Flask redirects
#you to the canonical URL with the trailing slash.
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'
