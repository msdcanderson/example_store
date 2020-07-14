-- SQLite
SELECT users.id, 
email, 
password, 
users.name, 
roles.name AS 'role name', 
roles.restrictions, 
groups.name AS 'group name', 
groups.allowances
FROM users
LEFT JOIN user_role ON
user_role.user_id = users.id
LEFT JOIN user_group ON
user_group.user_id = users.id
LEFT JOIN roles ON
roles.id = user_role.role_id
LEFT JOIN groups ON
groups.id = user_group.group_id;
