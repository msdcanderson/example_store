-- -- Groups

-- INSERT INTO user_group (user_id, group_id)
-- VALUES(1,1);

-- UPDATE user_group
-- SET user_id = 1,
--     group_id = 2
-- WHERE
--     group_id = 2; 


-- -- Roles

-- INSERT INTO roles (name, restrictions)
-- VALUES('store_owner', '{"stores":["create"]');


-- UPDATE roles
-- SET restrictions = '{"stores":["create", "read", "delete"]'
-- WHERE 
--     id = 1;


INSERT INTO user_role (user_id, role_id)
VALUES (2,1);




-- -- Store

-- UPDATE stores
-- SET other_permissions = NULL
-- WHERE
-- id = 1;