# Spa_Booking_fastAPI
Botio:Backend internship test

# Initial Setup
for window
 - $python -m venv env
 - $env\Scripts\activate
 - $pip install -r requirements.txt

# Step by Step:

1. In the "main.py" file, define an entry point for running the application
2. A base route in "server/app.py"
3. Run the entry point file from your console: $python main.py
4. Navigate to http://localhost:8000 in your browser. You should see: { "message": "Welcome to my API" }
5. You can also view the interactive API documentation at http://localhost:8000/docs

# Routes:

6. We'll be building a simple API for storing Spa Booking data with the CRUD routes.
   -get
   -post
   -put
   -delete

# Schema:

7. Let's define the Schema for which our data will be based on, which will represent how data is stored in the MongoDB database.
8. In the "server/models" folder, you'll see a file schema (user_schema.py)

# MongoDB:

8. In this section, we'll wire up MongoDB and configure our API to communicate with it.

# Motor Setup:

9. Next, we'll configure Motor, an asynchronous MongoDB driver, to interact with the database.
10. Back in the server folder, we add the database connection info to "server/database/" and add the database. For ex. "user_database.py"

# Database CRUD Operations

11. Start by importing the ObjectId method from the bson package at the top of the "user_database.py" file.
12. Next, add each of the following functions for the CRUD operations, you'll see in the file "user_database.py, spa_database.py, spa_booking_database.py"

# CRUD Routes

13. In this section, we'll add the routes to complement the database operations in the database file. You'll see in the "routes" folder ex. "user_route.py"
14. Next, wire up the user_route in server/app.py.

# Create

15. Back in the routes file, add the following handler for creating a new user.

# Read

16. Moving right along, let's add routes to retrieve all users, spas and a single user, spa.

# Update

17. Next, write the individual route for updating the user data.

# Delete

18. Finally, add the delete route.

# JWT Authentication
- JWT Handler
19. In this section, we'll create a JWT token handler and a class to handle bearer tokens. You'll see in the "server/auth" folder.
20. The JWT handler will be responsible for signing, encoding, decoding, and returning JWT tokens. In the "/serverauth" folder, in a file called "auth_handler.py"
- JWT Secret and Algorithm
21. Next, create an environment file called .env in the base directory
22. In .env file
    - secret=please_update_me_please
    - algorithm=HS256
23. Back in "auth_handler.py", add the function for signing the JWT string.
                                                                          
