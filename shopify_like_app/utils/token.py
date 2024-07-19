from flask_jwt_extended import JWTManager

def create_token(identity):
    return create_access_token(identity=identity), create_refresh_token(identity=identity)
