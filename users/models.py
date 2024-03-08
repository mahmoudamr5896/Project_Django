from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, RegexValidator



class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator()])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r"^01[0-9]{9}$",
                message="Phone number must be entered in the format: '01123456789'.",
            )
        ],
    )
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.username = self.email 
        super().save(*args, **kwargs)
        profile, status = Profile.objects.get_or_create(user=self)
        profile.first_name = self.first_name
        profile.last_name = self.last_name
        profile.profile_picture = self.profile_picture
        profile.mobile = self.mobile
        profile.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r"^01[0-9]{9}$",
                message="Phone number must be entered in the format: '01123456789'.",
            )
        ],
    )
    profile_picture = models.ImageField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    facebook_profile = models.URLField(max_length=200, blank=True)
    country = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.user.username
