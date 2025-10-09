Events Calendar

ERD :

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
