from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.user import user_bp
from routes.product import product_bp

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(product_bp, url_prefix='/products')

if __name__ == '__main__':
    app.run(debug=True)
