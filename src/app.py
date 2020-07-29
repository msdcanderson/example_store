from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from dotenv import load_dotenv

from extensions import babel, jwt, login_manager #, authorize 


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
        

    @app.route("/")
    def index():
        return jsonify({"hello": "world"})


    db.init_app(app)
    ma.init_app(app)

    login_manager.init_app(app)
    # authorize.init_app(app)

    jwt.init_app(app)
    babel.init_app(app)

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