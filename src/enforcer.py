import sys
import casbin

sys.path.append("../../flask-authz")
from flask_authz_mine import CasbinEnforcer


class UpdatedCasbinEnforcer(CasbinEnforcer):
    def __init__(self, app=None, adapter=None, watcher=None):
        self.app = app
        self.adapter = adapter
        if app is not None and adapter is not None:
            self.init_app(app, adapter, watcher)

    def init_app(self, app, adapter, watcher=None):
        self.app = app
        self.adapter = adapter
        self.e = casbin.Enforcer(app.config.get("CASBIN_MODEL"), self.adapter, True)
        if watcher:
            self.e.set_watcher(watcher)



# class UpdatedCasbinEnforcer(CasbinEnforcer):
# 	def __init__(self, app=None, adapter=None, watcher=None):
# 		self.app = app
# 		self.adapter = adapter
#         if app is not None and adapter is not None:
#             self.init_app(app, adapter, watcher)
# ​
# 	def init_app(self, app, adapter, watcher=None):
# 		self.app = app
# 		self.adapter = adapter
# 		self.e = casbin.Enforcer(app.config.get("CASBIN_MODEL"), self.adapter, True)
# 		if watcher:
# 			self.e.set_watcher(watcher)