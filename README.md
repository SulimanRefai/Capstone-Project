# Capstone-Project

# Events Calendar
# Project Description:
The Events Calendar is a web-based application that allows users to manage and organize their personal events efficiently. Users can create, edit, and delete events, as well as view them in a list sorted by date and time. Each event can be assigned a category, such as Meeting, Study, Personal, or Travel, to help organize and filter events. The application includes user authentication, ensuring that each user's events are private and secure. Built with Django for the backend and HTML/CSS for the frontend, it provides a responsive and user-friendly interface for managing daily schedules.

# User Stories:

As a user, I want to sign up and log in so that I can have a personal account for my events.

As a user, I want to create a new event so that I can organize my schedule.

As a user, I want to view a list of my events sorted by date and time so that I can see upcoming events.

As a user, I want to edit an event so that I can update its details.

As a user, I want to delete an event if it is no longer needed.

As a user, I want to assign a category to each event so that I can organize them by type.

As a user, I want to filter events by category so that I can quickly find the type of event I’m looking for.

# ERD :

Table users {
  username varchar(50) [pk]  
  email varchar(100)
  password varchar(255)
}

Table categories {
  id int [pk, increment]      
  name varchar(50)             
}

Table events {
  id int [pk, increment]       
  title varchar(100)            
  description text             
  date date                    
  time time                     
  user_username varchar(50) [ref: > users.username]  
  category_id int [ref: > categories.id]            
}
