from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    user_status = models.CharField(max_length=20, default='Active')  # Active, Inactive

    def __str__(self):
        return self.username
        
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True)
    age_section = models.CharField(max_length=100, blank=True, null=True)  # Optional age section
    description = models.TextField(blank=True, null=True)  # Category description

    def __str__(self):
        return self.category_name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255, blank=True, null=True)  # Optional publisher
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)  # Date field for published date
    is_available = models.BooleanField(default=True)  # Book availability status
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Foreign key to Category

    def __str__(self):
        return f"{self.title} by {self.author}"
        
class BorrowRecord():
    borrow_record_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField()
    return_status = models.BooleanField()
    #borrow_limit

class BooksBorrowed():
    borrow_record_id = models.ForeignKey(BorrowRecord, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)

class Fine():
    fine_id = models.AutoField(primary_key=True)
    borrow_record_id = models.ForeignKey(BorrowRecord, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    outstanding_balance = models.DecimalField(max_digits=5, decimal_places=2)
    borrow_date = models.ForeignKey(BorrowRecord, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
