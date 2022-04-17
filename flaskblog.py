from distutils.log import debug
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Akshit Chugh',
        'title' : 'Blog Post One',
        'content' : 'I detect little communism',
        'date_posted' : 'April 17, 2022'
    },
    {
        'author' : 'John Doe',
        'title' : 'Blog Post Two',
        'content' : 'Ain\'t he right?',
        'date_posted' : 'April 18, 2022'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts =  posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug = True)
