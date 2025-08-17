from django.db import models


#User model
class User(models.Model):
    name = models.CharField(max_length=100)
    
    
    
#Post Model
class Post (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

   