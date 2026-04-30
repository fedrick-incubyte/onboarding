from flask import Flask, request, url_for
from markupsafe import escape
from blueprints.blueprint_test import test_bp

app = Flask(__name__)
app.register_blueprint(test_bp)

@app.route('/')
def index():
    return 'Index Page'

@app.route("/hello")
def hello_world():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"



with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello_world'))
    print(url_for('test.show_user_profile', username='John Doe'))
    print(url_for('test.show_post', post_id=123))
    print(url_for('test.show_subpath', subpath='example/1'))

