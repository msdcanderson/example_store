from flask_restful import Resource
from flask import request
from flask_babel import gettext
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound, Unauthorized
# from app import casbin_enforcer
# from extensions import authorize

from main.models.store import StoreModel
from main.schemas.store import StoreSchema

from db import db

store_schema = StoreSchema()
store_list_schema = StoreSchema(many=True)


class NewStore(Resource):
    @classmethod
    @login_required
    # @authorize.create(StoreModel)    
    def post(cls):
        store_json = request.get_json()
        store = store_schema.load(store_json)

        store.owner_id = current_user.id
        store.group_id = 1

        store.save_to_db()
        return {"message": gettext("STORE_CREATED")}, 201


class Store(Resource):
    @classmethod
    @login_required
    # @casbin_enforcer.enforcer
    def get(cls, _id: int):
        store = StoreModel.find_by_id(_id)
        if not store:
            return {"message": gettext("STORE_NOT_FOUND")}, 404
        
        # if not authorize.read(store):
        #     raise Unauthorized
        
        return store_schema.dump(store), 200

    @classmethod
    @login_required
    def patch(cls, _id: int):
        store_json = request.get_json()
        store = StoreModel.find_by_id(_id)

        # if not authorize.update(store):
        #     raise Unauthorized

        if store:
            store.name = store_json["name"]
            store.description = store_json["description"]
        else:
            return {"message": gettext("STORE_NOT_FOUND")}, 404

        store.save_to_db()

        return store_schema.dump(store), 200

    @classmethod
    @login_required
    # @authorize.delete
    def delete(cls, _id: int):
        store = StoreModel.find_by_id(_id)
        if not store:
            return {"message": gettext("STORE_NOT_FOUND")}, 404

        # if not authorize.delete(store):
        #     raise Unauthorized

        store.delete_from_db()
        return {"message": gettext("STORE_DELETED")}, 200


class StoreList(Resource):
    @classmethod
    def get(cls):
 
        #  if not authorize.read(store):
        #     raise Unauthorized

        return (
            {
                "stores": store_list_schema.dump(
                    StoreModel.find_all()
                )
            },
            200,
        )
