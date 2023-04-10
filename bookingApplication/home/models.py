from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# Create your models here.


class Hotels(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logos", 
                             default="sample.png",validators=[FileExtensionValidator(["png", "jpg"])])
    wifi = models.BooleanField()
    pickup = models.BooleanField()
    water = models.BooleanField()
    allService = models.BooleanField()
    telephone = models.BooleanField()

    def __str__(self):
        return self.name



class Accomodations(models.Model):
    name = models.CharField(max_length=100)
    hotel = models.ForeignKey(to=Hotels, on_delete=models.CASCADE)
    price = models.FloatField()
    desc = models.TextField()
    image1 = models.ImageField(upload_to="suites", 
                             default="sample_suite.png",validators=[FileExtensionValidator(["png", "jpg"])])
    image2 = models.ImageField(upload_to="suites", 
                             default="sample_suite.png",validators=[FileExtensionValidator(["png", "jpg"])])
    image3 = models.ImageField(upload_to="suites", 
                             default="sample_suite.png",validators=[FileExtensionValidator(["png", "jpg"])])


    def __str__(self):
        return self.name
    

choices = (
    ("Booked","Booked"),
    ("In Process","In Process"),
    ("Cancled", "Cancled")
)


class booking(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    accomodation = models.ForeignKey(to=Accomodations, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=100, choices=choices, default="In Process")


    def __str__(self) -> str:
        return f"{self.user.username}'s {self.accomodation.name} Booking"