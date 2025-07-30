from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication = models.IntegerField()

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    email = models.EmailField()
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
REQUIRED_FIELDS = ['username', 'email', 'date_of_birth']

class CustomUserManager(BaseUserManager):
    def create_user(self,date_of_birth,profile_photo, email, username):
        if not date_of_birth:
            raise ValueError('Use the correct date formart')
        
        
        if not profile_photo:
            raise ValueError('Allows only images')
        
        if not email:
            raise ValueError('Must be a valid email address')
        
        if not username:
            raise ValueError('Allows characters only')
        
        user = self.model(
              email = self.normalize_email(email),
              username = username, 
              date_of_birth = date_of_birth,
              profile_photo = profile_photo     
        )
        permission = Permission.objects.get('can_view', 'can_edit')
        
        user.user_permissions.add(permission)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, date_of_birth, profile_photo):
        user = self.create_user(
              email = self.normalize_email(email),
              username = username, 
              date_of_birth = date_of_birth,
              profile_photo = profile_photo     
        )
        permission = Permission.objects.get('can_create', 'can_delete', 'can_view', 'can_edit')
        user.user_permissions.add(permission)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
    
