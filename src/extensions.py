from flask_babel import Babel
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_authorize import Authorize

from authlogin.models.user import User


login_manager = LoginManager()

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

authorize = Authorize()

babel = Babel()

jwt = JWTManager()


