from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from dotenv import load_dotenv
import sys
sys.path.append('../../flask-authz')
from flask_authz_mine import CasbinEnforcer
from casbin.persist.adapters import FileAdapter

from extensions import babel, jwt, login_manager#, casbin_enforcer #, authorize 


from db import db
from ma import ma


def create_app():
    load_dotenv(".env", verbose=True)
    app = Flask(__name__)
    app.config.from_object("default_config")
    app.config.from_envvar("APPLICATION_SETTINGS")
    api = Api(app)

    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation(err):
        return jsonify(err.messages), 400

 
    @app.before_first_request
    def create_tables():
        db.create_all()
        

    db.init_app(app)
    ma.init_app(app)

    login_manager.init_app(app)
    # authorize.init_app(app)

    jwt.init_app(app)
    babel.init_app(app)

    # Set up Casbin model config
    app.config['CASBIN_MODEL'] = './src/casbinmodel.conf'
    # Set headers where owner for enforcement policy should be located
    app.config['CASBIN_OWNER_HEADERS'] = {'Authorization'}
    # Set up Casbin Adapter
    adapter = FileAdapter('./src/security_policy.csv')
    casbin_enforcer = CasbinEnforcer(app, adapter)
    # casbin_enforcer.init_app(app, adapter)


    @app.route("/")
    @casbin_enforcer.enforcer
    def index():
        return jsonify({"hello": "world"})


    from authz.resources.user import UserRegister, UserLogin, UserLogout

    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserLogout, "/logout")

    # from authlogin.resources.security import NewGroup, GroupResource, UserGroup

    # api.add_resource(NewGroup, "/group")
    # api.add_resource(GroupResource, "/group/<int:_id>")
    # api.add_resource(UserGroup, "/usergroup/<int:_id>")
    # # api.add_resource(UserGroup, "/usergroup")


    from main.resources.store import NewStore, Store, StoreList

    api.add_resource(NewStore, "/store")
    api.add_resource(Store, "/store/<int:_id>")
    api.add_resource(StoreList, "/stores")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, debug=True)