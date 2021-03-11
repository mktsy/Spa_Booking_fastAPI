# Spa_Booking_fastAPI
Botio:Backend internship test

# Initial Setup
for window
 Shell: >python -m venv env
        >env\Scripts\activate
        >pip install -r requirements.txt


# Step by Step:

1. In the "main.py" file, define an entry point for running the application
2. A base route in "server/app.py"
3. Run the entry point file from your console: >python main.py
4. Navigate to http://localhost:8000 in your browser. You should see: { "message": "Welcome to my API" }
5. You can also view the interactive API documentation at http://localhost:8000/docs

# Routes:

6. We'll be building a simple API for storing Spa Booking data with the CRUD routes
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

# 
