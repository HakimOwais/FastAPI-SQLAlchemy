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

            <-----Process Overview----->

1. Import required libraries : sqlalchemy, passlib, bcrypt
2. Create database definition and run it in main.py
3. Create database models (tables)
4. Create functionality to write to database
5. Create schemas:
    a. Data from user: UserBase
    b. Response to user : UserDisplay
6. Create API operation

            <------CRUD Operations----->
1. Create
2. Read
3. Update
4. Delete

            <----- Relationship ----->
1. Retrieve elements from multiple tables in a single request.
2. Define relationship in models.
3. Add the elements we want to retrieve in schemas

