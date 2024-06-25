from flask import Flask, send_from_directory
from entity import db, register_models
from web.controller import controller

app = Flask(__name__)

app.register_blueprint(controller)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nanshens@localhost:5432/aq_validator'
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
register_models()

with app.app_context():
    db.create_all()

# @app.route("/")
# def server():
#     return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)