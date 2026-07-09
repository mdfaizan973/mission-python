## 1. Employee Management Portal
Problem Statement

Create a Flask application for an Employee Management Portal.

Create a home page.
Create a route to display all employees.
Create a dynamic route to display a specific employee using their employee ID.
Store employee information in a dictionary.
If the employee ID does not exist, display an appropriate message.
Create an admin page that is accessible only when the user is an admin; otherwise, redirect to an access denied page.


## 2. Online Food Ordering System
Problem Statement

Develop a Flask application for an Online Food Ordering System.

Create a home page.
Store food items with their name, price, and category in a dictionary.
Create a route to display all available food items.
Create a dynamic route to display details of a selected food item using its ID.
If the requested food item is unavailable, display an appropriate message.
Add an admin route that redirects unauthorized users to a login page.

## 3. Movie Ticket Booking Portal
Problem Statement

Build a Flask application for a Movie Ticket Booking Portal.

Create routes for Home, Movies, Theaters, and Contact.
Store movie details in a dictionary.
Create a dynamic route to display movie information using the movie ID.
Display a custom message if the movie is not found.
Create an admin dashboard that is protected using a simple admin check.
Use redirects wherever appropriate.

## 4. Hospital Management System
Problem Statement

Develop a Flask application for a Hospital Management System.

Create pages for Home, Doctors, Patients, Appointments, and Emergency.
Store patient details in a dictionary.
Create a dynamic route to fetch patient information using the patient ID.
Display an error message if the patient record is unavailable.
Restrict access to the admin dashboard using a function that checks admin privileges and redirects unauthorized users.

## 5. Library Management System (Level Up)
Problem Statement

Create a Flask application for a Library Management System.

Create routes for Home, Books, Authors, Categories, Members, and Contact.
Store book details in a dictionary with book ID, title, author, category, and availability status.
Create a dynamic route to display book details using the book ID.
If the book does not exist, display a custom "Book Not Found" message.
Create a route to check whether a book is available or already issued.
Protect the admin panel using an admin verification function and redirect unauthorized users to the login page.
Use url_for() and redirect() wherever required.