from flask_restful import Resource
from werkzeug.security import safe_str_cmp
from flask_login import login_user, logout_user, login_required
from flask import request, session
from flask_babel import gettext
from werkzeug.exceptions import Unauthorized

from extensions import authorize
from authlogin.schemas.security import GroupSchema
from authlogin.models.user import Group, User


group_schema = GroupSchema()
gorup_list_schema = GroupSchema(many=True)


class NewGroup(Resource):
    @classmethod
    # @login_required
    def post(cls):
        group_json = request.get_json()
        group = group_schema.load(group_json)

        group.save_to_db()
        return {"message": gettext("GROUP_CREATED")}, 201


class GroupResource(Resource):
    @classmethod
    @login_required
    # @authorize.read(StoreModel)
    def get(cls, _id: int):
        group = Group.find_by_id(_id)
        if not group:
            return {"message": gettext("GROUP_NOT_FOUND")}, 404
        
        # if not authorize.read(group):
        #     raise Unauthorized
        
        return group_schema.dump(group), 200

    @classmethod
    @login_required
    def patch(cls, _id: int):
        group_json = request.get_json()
        group_json["allowances"] = group_json["allowances"].replace("\\", "")
        group = Group.find_by_id(_id)

        # if not authorize.update(group):
        #     raise Unauthorized

        if group:
            group.name = group_json["name"]
            group.allowances = group_json["allowances"]
        else:
            return {"message": gettext("GROUP_NOT_FOUND")}, 404

        group.save_to_db()
        return group_schema.dump(group), 200

    @classmethod
    #@login_required
    # @authorize.delete
    def delete(cls, _id: int):
        group = Group.find_by_id(_id)
        if not group:
            return {"message": gettext("GROUP_NOT_FOUND")}, 404

        # if not authorize.delete(group):
        #     raise Unauthorized

        group.delete_from_db()
        return {"message": gettext("GROUP_DELETED")}, 200


class GroupList(Resource):
    @classmethod
    def get(cls):
        return (
            {
                "groups": group_list_schema.dump(
                    Group.find_all()
                )
            },
            200,
        )

# TODO change this to patch request and pass the group-ids for the user
class UserGroup(Resource):
    @classmethod
    # @login_required()
    def post(cls):
        usergroup_json = request.get_json()
        groups = []

        # for _id in usergroup_json["group"]:
        #     print(_id)
        #     groups.append(_id)

        # usergroup = User(user=usergroup_json["user"], groups=groups, name="mike", email="mike@example.com", password="1234")
        user = User(name="mike1", email="mike1@example.com", password="1234", groups=[1])
        user.save_to_db()
        return {"message": gettext("USERGROUP_PERMISSION_CREATED")}, 201