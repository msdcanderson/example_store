from ma import ma

from main.models.store import StoreModel


class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StoreModel
        # load_only = ("created_on", "updated_on", "other_permissions", "owner_id", "owner_permissions", "group_id", "group_permissions")
        load_only = ("created_on", "updated_on")
        dump_only = ("id",)  # only show ID when dumping
        load_instance = True
