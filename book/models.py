from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "author_table"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    create_date = models.DateField(auto_now=True)

    class Meta:
        db_table = "user_table"

class Book(models.Model):
    bookname=models.CharField(max_length=1000)
    author=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    published_date=models.DateField(auto_now=True)
    price=models.IntegerField()
    upload_image=models.ImageField(upload_to='images/')

    class Meta:
        db_table="book_table"