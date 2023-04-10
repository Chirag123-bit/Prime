from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="sample.png", upload_to="profiles", validators=[FileExtensionValidator(["png","jpg"])] )


    def __str__(self):
        return self.user.first_name + " " + self.user.last_name