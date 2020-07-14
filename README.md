# example_store

## Set up

```
pipenv install
```

## Instructions to run

```bash
pipenv shell
python .\src\app.py
```

## Flask-Authorize example app

Use this as an example to test the RBAC / ACL provided by the extension [flask-authorize](https://github.com/bprinty/Flask-Authorize).

Requirements for store permissions:

- Users
    - Business Owner, has full permissions
    - Area Manager (1 & 2), can add/update/delete/view all stores in their area
    - Store 1 Manager, can view all stores in area 1, and update store 1 details
    - Store 1 Employee, can view store 1 details in area 1
    - Store 2 Manager, can view all stores in area 1, and update store 2 details
    - Store 2 Employee, can view store 2 details in area 1
    - Store 3 Manager, can view all stores in area 2, and update store 3 details
    - Store 3 Employee, can view store 3 details in area 2
    - Store 4 Manager, can view & update all stores 1 & 2

- Groups
    - Store 1
    - Store 2
    - Store 3

- Roles
    - add (write - w)
    - update
    - delete
    - view (read - r)

## Summary of permissions

| User             | Role       | Group      | Description                                          |
| ---------------- | ---------- | ---------- | ---------------------------------------------------- |
| Business Owner   | w, r, u, d | Admin      | Can do everything, in all areas                      |
| Area 1 Manager   | w, r, u, d | Area 1     | Can add stores, update stores, view stores in area 1 |
| Area 2 Manager   | w, r, u, d | Area 2     | Can add stores, update stores, view stores in area 1 |
| Store 1 Manager  | r, u       | Store 1    | Can update & view store 1                            |
| Store 2 Manager  | r, u       | Store 2    | Can update & view store 2                            |
| Store 3 Manager  | r, u       | Store 3    | Can update & view store 2                            |
| Store 4 Manager  | r, u       | Store 1, 2 | Can update & view stores 1 & 2                       |
| Store 1 Employee | r          | Store 1    | Can view store 1                                     |
| Store 2 Employee | r          | Store 2    | Can view store 2                                     |
| Store 3 Employee | r          | Store 3    | Can view store 3                                     |

## Permissions Broken down by table

| Role           | Permission |
| -------------- | ---------- |
| Business Owner | w, r, u, d |
| Area Manager   | w, r, u    |
| Store Manager  | r, u       |
| Employee       | r          |

| Group   | Users                                                              |
| ------- | ------------------------------------------------------------------ |
| Admin   | Business Owner                                                     |
| Store 1 | Area 1 Manager, Store 1 Manager, Store 4 Manager, Store 1 Employee |
| Store 2 | Area 1 Manager, Store 2 Manager, Store 4 Manager, Store 2 Employee |
| Store 3 | Area 2 Manager, Store 3 Manager, Store 3 Employee                  |

| Stores | Group          |
| ------ | -------------- |
| 1      | Admin, Store 1 |
| 2      | Admin, Store 2 |
| 3      | Admin, Store 3 |


## Intro to permission

https://www.imperva.com/learn/data-security/role-based-access-control-rbac/