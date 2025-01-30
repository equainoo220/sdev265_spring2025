from django.db import models

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
