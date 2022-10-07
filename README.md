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

# Screenshots
Homepage:
![9EAF2BEA-0856-4DC0-ABF8-D31E2A9C248A](https://user-images.githubusercontent.com/107416924/194517337-29f6d220-516f-4e7f-8566-fabb5ca74148.jpeg)

Make a booking page:
![AA202D28-F974-4554-9012-6653F8B64EE1](https://user-images.githubusercontent.com/107416924/194517400-0c0c07d4-b3d8-4f73-b4b1-50f703625134.jpeg)

View bookings page:
![A8FDF3ED-48F1-42E8-AD20-05ABA1A5605A](https://user-images.githubusercontent.com/107416924/194517585-748bc8ac-aead-4d30-ac52-7d4747b557aa.jpeg)

View members page:
![53EDF16F-5558-472F-A22D-B22F15D0A400](https://user-images.githubusercontent.com/107416924/194517620-8ecda6a0-dc47-446b-a460-7297e36afb8e.jpeg)


# **Instructions to run the app**
1. Create the database and load the data. Run the following in the terminal:
 - createdb gym_app
 - psql -d <gym_app> -f <gym_app>
2. Extract the required data from the database using SQL. Run the following in the terminal:
 - python3 console.py
3. Load the webpage. Run the following in the terminal:
 - flask run
4. Open the webpage provided in the return from step 3.

# **Navigating the app**
The homepage shows a dashboard displaying upcoming classes in date order. The class information can be viewed and edited using the corresponding button for each class. This displays a new screen from which members booked onto the class can be changed, class details can be edited or the class can be deleted.
The information on the right hand side of the screen (member and financial info) will dynamically update when new members are added and classes are booked.
The functionality desribed in the section above can be accessed through the buttons on the top of the homepage, labelled accordingly.
