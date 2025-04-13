

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


from django.db import models