-- -- STORE 1 belongs to group 1, other_permissions is NULL
-- UPDATE stores
-- SET other_permissions = NULL
-- WHERE
-- id = 1;
-- -- USER 2 belongs to group 2, and should not be able to do anything with store 1 - THIS WORKS

-- NOW SET GROUP to be restriction mixin, role to allowance, 
-- remove group permissions from store
-- give user2 group 2
-- user should not be able to do anything - THIS WORKS

-- UPDATE stores
-- SET other_permissions = NULL
-- WHERE
-- id = 1;

-- INSERT INTO roles (name, allowances)
-- VALUES('store_owner', '{"stores": ["read"]}');

-- INSERT INTO user_role (user_id, role_id)
-- VALUES (2,1);

-- make user2 part of group 1, should be able to do the group permissions - this WORKS

-- Make group permissions for store NULL, see what happens, since user has role of read
-- User can't read
-- UPDATE stores
-- SET group_permissions = NULL
-- WHERE
-- id = 1;

-- Make group restriction 'read' 
-- USER still can't read

-- UPDATE groups
-- SET restrictions = '{"users": [], "groups": [], "roles": [], "stores": ["read"]}'
-- WHERE id = 1;

-- make group allowance - but empty it out 
-- USER is part of GROUP 2 
-- USER can't view GROUP 1 stores - THIS WORKS

-- UPDATE stores
-- SET other_permissions = NULL
-- WHERE
-- id = 1;

-- REMOVE STORE GROUP PERMISSIONS
-- SET USER to GROUP 1
-- USER should be able to see, the GROUP table has these permissions - THIS DOESN't WORK

-- UPDATE stores
-- SET group_permissions = NULL
-- WHERE
-- id = 1;


-- ADD ROLE to VIEW
-- SET USER to VIEWER ROLE - THIS DOESN:T SHOW THE USER ANYTHING


-- INSERT INTO roles (name, allowances)
-- VALUES('store_owner', '{"stores": ["read"]}');

-- INSERT INTO user_role (user_id, role_id)
-- VALUES (2,1);

-- CHANGE THE STORE PERMISSION MIXIN TO ALLOWANCES
-- THIS DOESN'T LET YOU SET OWNERS/GROUPS


-- SO I THINK WE NEED TO SET STORE GROUP PERMISSIONS TO ALLOW EVERYTHING
-- THEN GROUP PERMiSSSIONS TO ALLOW EVERYTHING
-- THEN RESTRICT ROLE  

-- update store other permissions to null 

-- INSERT INTO roles (name, restrictions)
-- VALUES('store_owner', '{"stores": ["read"]}');

-- INSERT INTO user_role (user_id, role_id)
-- VALUES (2,1);

UPDATE roles
SET restrictions = '{"stores": ["read", "update"]}'
WHERE id = 1