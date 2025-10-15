# Capstone-Project

# Events Calendar
# Project Overview:

The main Idea is to help users organize their time and manage personal event easily.
Each user can create their own events such as meeting, study sessions, or reminders and view them in website.

# Tech stack 

Frontend : HTML, CSS and Django Template.

Backend : Python, Django and PostgreSQL.

# User Stories:

1.I want to sign up and log in so that I can have a personal account for my events.

2.I want to create a new event so that I can organize my schedule.

3.I want to view a list of my events sorted by date and time so that I can see upcoming events.

4.I want to edit an event so that I can update its details.

5.I want to delete an event if it is no longer needed.

6.I want to search bar to get Event I want.

# ERD :

<img width="796" height="424" alt="image" src="https://github.com/user-attachments/assets/bc1e0fdd-f777-458f-a02f-ee968b09988c" />

# Key Features Implemented:

1.User Authentication:
Secure login and registration system using Django built-in authentication.
Each user has a private calendar no shared access to other users events.

2.Event Management (CRUD):
Users can Create, Read, Update, and Delete their own events.
Each event includes a title, description, start time, and end time.

3.Dashboard Overview:
Personalized dashboard displaying all upcoming events for the logged-in user.
Events are ordered by date, showing the earliest events first.

4.Event Search:
Search functionality to quickly find events by title or keyword from the dashboard.

5.Event Table View:
Events are displayed neatly in a table for better readability and organization.

6.Navigation Bar:
Responsive navigation bar that includes quick access to the Dashboard, Add Event, and Logout.

# Installation Guide :

1.Install Django.

2.Install PostgreSQL.

3.pip Install, pipenv install, pipenv shell (Virtual Environment).

4.python manage.py makemigrations, python manage.py migrate (DB migrations).

5.python manage.py runserver.

# Challenges Encountered & Solutions :

Problem: 
Events were not sorted properly on the dashboard newer or upcoming events appeared randomly.

Solution:
I updated the query to order events by their start time.

# Future Enhancements :

1. Event Reminders & Notifications:
Add an automated reminder system that sends email or in-app notifications before an event starts.

2. Shared Calendars:
Allow users to create shared calendars where multiple users can view or edit the same events ideal for teams or family use.

