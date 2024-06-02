from flask import Flask
from .home.routes import home



def create_app():
	app = Flask(__name__)
	# ------- Settings ---------- #
	app.config['SECRET_KEY'] = 'I am Yusee Programmer'

	app.register_blueprint(home)

	return app