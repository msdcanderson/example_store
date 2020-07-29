from ma import ma
from authz.models.user import User


# TODO code is duplicated - there might be a better way of doing this.
# Duplicated code: This is because I only want users to have to use an email address 
# when they login no need to use name and email address and password 
class UserRegisterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ("password",)
        dump_only = ("id",)  # only show ID when dumping
        load_instance = True
        # include_fk = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ("password",)
        dump_only = ("id","name")  # only show ID when dumping
        load_instance = True