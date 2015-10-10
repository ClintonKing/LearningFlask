from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config.from_object('config')

from app import views

with app.test_request_context():
	url_for('static', filename='css/styles.css')
