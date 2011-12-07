from flask import Flask
app = Flask(__name__, static_folder='static')
from flask import render_template

@app.route("/index/")
def index():
    return ''.join(open('data/circle_html/index.html', 'r').readlines())




@app.route('/index/circles<int:post_id>.html')
def return_circle(post_id):
    return ''.join(open('data/circle_html/circles{0}.html'.format(post_id)).readlines())


if __name__ == "__main__":
    app.run(debug=True)
