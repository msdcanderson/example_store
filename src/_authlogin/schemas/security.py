from ma import ma
from authlogin.models.user import Group


class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        load_only = ()
        dump_only = ("id",)  # only show ID when dumping
        load_instance = True
        include_fk = True
