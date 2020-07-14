from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from dotenv import load_dotenv

from extensions import babel, jwt, login_manager, authorize 


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


    from authlogin.models.user import User, Group, Role
    
    @app.before_first_request
    def create_tables():
        db.create_all()
        businessowner_user = User(name="Business Owner", email="businessowner@example.com", password="1234")
        db.session.add(businessowner_user)
        db.session.commit()
        businessowner_group = Group(name="Business Owner")
        db.session.add(businessowner_group)
        db.session.commit()
        businessowner_user.groups = [businessowner_group]
        # create_store_role = Role(
        #     name='Create Store',
        #     restrictions=dict(
        #     stores=['create'],
        #         )
        #     )
        # businessowner_user.roles = [create_store_role]
        # db.session.add(create_store_role)
        # db.session.commit()
     
        # area1manager = User(name="Area 1 Manager", email="area1manager@example.com", password="1234")
        # db.session.add(area1manager)
        # db.session.commit()
        # area2manager = User(name="Area 2 Manager", email="area2manager@example.com", password="1234")
        # db.session.add(area2manager)
        # db.session.commit()
        # store1manager = User(name="Store 1 Manager", email="store1manager@example.com", password="1234")
        # db.session.add(store1manager)
        # db.session.commit()
        # store2manager = User(name="Store 2 Manager", email="store2manager@example.com", password="1234")
        # db.session.add(store2manager)
        # db.session.commit()
        # store3manager = User(name="Store 3 Manager", email="store3manager@example.com", password="1234")
        # db.session.add(store3manager)
        # db.session.commit()
        # store4manager = User(name="Store 4 Manager", email="store4manager@example.com", password="1234")
        # db.session.add(store4manager)
        # db.session.commit()
        # store1employee = User(name="Store 1 Employee", email="store1employee@example.com", password="1234")
        # db.session.add(store1employee)
        # db.session.commit()
        # store2employee = User(name="Store 2 Employee", email="store2employee@example.com", password="1234")
        # db.session.add(store2employee)
        # db.session.commit()
        # store3employee = User(name="Store 3 Employee", email="store3employee@example.com", password="1234")
        # db.session.add(store3employee)
        # db.session.commit()

        # store1 = Group(name="Store 1")
        # db.session.add(store1)
        # db.session.commit()
        # store2 = Group(name="Store 2")
        # db.session.add(store2)
        # db.session.commit()
        # store3 = Group(name="Store 3")
        # db.session.add(store3)
        # db.session.commit()

        # area1manager.groups = [store1, store2]
        # area2manager.groups = [store3]
        # store1manager.groups = [store1]
        # store2manager.groups = [store2]
        # store3manager.groups = [store3]
        # store4manager.groups = [store1, store2]
        # store1employee.groups = [store1]
        # store2employee.groups = [store2]
        # store3employee.groups = [store3]
        

        
        # areamanagerrole = Role(
        #     name='Area Manager Role',
        #     restrictions=dict(
        #     stores=['read', 'update', 'delete'],
        #         )
        #     )
        # area1manager.roles = [areamanagerrole]
        # area2manager.roles = [areamanagerrole]
        # db.session.add(areamanagerrole)
        # db.session.commit()
        
        # storemanagerrole = Role(
        #     name='Store Manager Role',
        #     restrictions=dict(
        #     stores=['read', 'update'],
        #         )
        #     )
        # store1manager.roles = [storemanagerrole]
        # store2manager.roles = [storemanagerrole]
        # store3manager.roles = [storemanagerrole]
        # store4manager.roles = [storemanagerrole]
        # db.session.add(storemanagerrole)
        # db.session.commit()

        # employeerole = Role(
        #     name='Employee Role',
        #     restrictions=dict(
        #     stores=['read'],
        #         )
        #     )
        # store1employee.roles = [employeerole]
        # store2employee.roles = [employeerole]
        # store3employee.roles = [employeerole]
        # db.session.add(employeerole)
        # db.session.commit()
        

    @app.route("/")
    def index():
        return jsonify({"hello": "world"})

    with app.app_context():
        db.init_app(app)
        ma.init_app(app)

        login_manager.init_app(app)
        authorize.init_app(app)

        jwt.init_app(app)
        babel.init_app(app)

        from authlogin.resources.user import UserRegister, UserLogin, UserLogout

        api.add_resource(UserRegister, "/register")
        api.add_resource(UserLogin, "/login")
        api.add_resource(UserLogout, "/logout")

        from main.resources.store import NewStore, Store, StoreList

        api.add_resource(NewStore, "/store")
        api.add_resource(Store, "/store/<int:_id>")
        api.add_resource(StoreList, "/stores")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, debug=True)