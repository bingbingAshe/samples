from app import app
from flask import render_template
from flask import render_template
@app.route('/')
@app.route('/<index>')
def index(index = None):
    user ={'name':'杨冰冰'}
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("helloworld.html",
                           user = user,
                           index = index,
                           posts = posts)