# FastAPI-SQLAlchemy
Databases ---- Any relational database ---ORM Library ---- SQLAlchemy
Structure ----
create_user ---> UserRequest(Schema)---> Database User (Model)---> create

            <------create user data------>
Database checklist 
1. Database Definition ------ database.py
2. model Definition ------ models.py
3. Create database ----- main.py
4. schema definition ---- schemas.py
5. ORM functionality ---- db_user.py
6. API functionality ---- user.py