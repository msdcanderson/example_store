from ma import ma
from authlogin.models.user import Group


# TODO code is duplicated - there might be a better way of doing this.
# Duplicated code: This is because I only want users to have to use an email address 
# when they login no need to use name and email address and password 
class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        load_only = ()
        dump_only = ("id",)  # only show ID when dumping
        load_instance = True
        include_fk = True