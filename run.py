from flask import Flask

from app.rest.integral_controller import integral_blueprint

app = Flask(__name__)
app.register_blueprint(integral_blueprint)

app.run()
