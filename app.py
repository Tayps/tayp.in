from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Author',
        'title': 'Blog Post 1',
        'slug': '/Slug1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Author',
        'title': 'Blog Post 2',
        'slug': '/Slug1',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    }
]


@app.route("/")
@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/blog.html")
def blog():
    return render_template('archive.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
