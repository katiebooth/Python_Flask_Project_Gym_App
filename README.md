# **Project Overview and Technologies Used** 
This Python project is a web application to be used by employees of a gym. The technologies used are:
- PostgreSQL 
- Python
- HTML
- CSS
- Flask to communicate between the back end and front end

# **Project Brief** 
The project brief was to build a web application for a gym. The application should allow employees of the gym to manage members and classes. Additional functionality is added to the homepage (dashboard) to allow management of the gym to view basic member and financial information. The app uses a many-to-many relationship i.e. members can be booked onto multiple classes and a class holds multiple members.

Features of the app:
 - Add new members
 - View and edit member information e.g. change active/inactive or standard/premium member status 
 - Add new classes
 - View and edit class information e.g. date, time, price, standard/premium class
 - Delete classes
 - Book members onto classes. This takes into account whether:
    a) The member is active
    b) The class is premium/standard and whether the member has the corresponding membership
    c) The class has spaces available (class has a set capacity)
    d) The member is already booked onto the class
 - View summary table of members split by active/inactive and standard/premium membership
 - View the projected revenue for the classes currently booked

# **Instructions to run the app**
1. Create the database and load the data. Run the following in the terminal:
 - createdb gym_app
 - psql -d <gym_app> -f <gym_app>
2. Extract the required data from the database using SQL. Run the following in the terminal:
 - run_sql.py
3. Load the webpage. Run the following in the terminal:
 - flask run
4. Open the webpage provided in the return from step 3.

# **Navigating the app**
The homepage shows a dashboard displaying upcoming classes in date order. The class information can be viewed and edited using the corresponding button for each class. This displays a new screen from which members booked onto the class can be changed, class details can be edited or the class can be deleted.
The information on the right hand side of the screen (member and financial info) will dynamically update when new members are added and classes are booked.
The functionality desribed in the section above can be accessed through the buttons on the top of the homepage, labelled accordingly.