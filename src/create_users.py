"""
Store code on creating users here - not to be used until the authorization is working

I had it all in app.py - but it's messy
"""
    @app.before_first_request
    def create_tables():
        db.create_all()
        # businessowner_user = User(name="Business Owner", email="businessowner@example.com", password="1234")
        # db.session.add(businessowner_user)
        # db.session.commit()
        # businessowner_group = Group(name="Business Owner")
        # db.session.add(businessowner_group)
        # db.session.commit()
        # businessowner_user.groups = [businessowner_group]
        
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