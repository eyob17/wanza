# models.py

# models.py


from django.db import models

class MyUser(models.Model):
  USER_TYPES = (('user', 'User'), ('student', 'Student'))

  username = models.CharField(max_length=255) 
  user_type = models.CharField(max_length=10, choices=USER_TYPES, default='user')
  
