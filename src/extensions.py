from flask_babel import Babel
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
# from flask_authorize import Authorize

# import sys
# sys.path.append('../../flask-authz')
# from flask_authz import CasbinEnforcer
from enforcer import UpdatedCasbinEnforcer

# from authlogin.models.user import User
from authz.models.user import User


login_manager = LoginManager()

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


casbin_enforcer = UpdatedCasbinEnforcer()
# casbin_enforcer = CasbinEnforcer(app, adapter)

# authorize = Authorize()
babel = Babel()
jwt = JWTManager()
