

# Create your models here.
# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return self.name , self.price



# from django.db import models
# from django.core.validators import MinValueValidator

# class Product(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     price = models.DecimalField(
#         max_digits=6, 
#         decimal_places=2,
#         validators=[MinValueValidator(0.01)]  # Ensures price > 0
#     )
#     image = models.ImageField(upload_to='products/')  # Requires Pillow (run: `pip install pillow`)
#     description = models.TextField(blank=True, null=True)
#     stock = models.PositiveIntegerField(default=10)
#     available = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} - ₹{self.price}"
    
# from django.db import models
# from django.contrib.auth.models import User
# from django.conf import settings

# class Cart(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
#     session_key = models.CharField(max_length=40, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = [['user', 'session_key']]

#     def __str__(self):
#         if self.user:
#             return f"Cart for {self.user.username}"
#         return f"Anonymous cart ({self.session_key})"


from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AppUserManager(BaseUserManager):
    def create_user(self, email, name,phone, address, gender, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field is mandatory')       
        # converting email with lower case
        email= self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone=phone,
            address= address,
            gender= gender,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
   
    def create_superuser(self, email, name, phone, address, gender, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if not password:
            raise ValueError("Superusers must have a password.")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, name, phone, address, gender, password, **extra_fields)


class AppUser(AbstractUser):


    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    # redefine the email to be unique
    email = models.EmailField(unique=True)


    # Adding extra field  inside the custom user class
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # removing the username field
    username= None
    objects = AppUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'address', 'gender']


    def __str__(self):
        return self.email
