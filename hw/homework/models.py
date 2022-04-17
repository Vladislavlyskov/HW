from django.db import models


# Create your models here.


class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    book = models.OneToOneField(
        "Book", null=True,
        related_name='student',
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.pk}, {self.firstname}, {self.book}"


class Book(models.Model):
    title = models.CharField(max_length=50, null=True, default=None)
    number_of_pages = models.PositiveIntegerField()

    def __str__(self):
        return f" {self.title}, {self.number_of_pages}"
