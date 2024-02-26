from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class Myuser(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    conf_password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    profile_pic = models.ImageField(null=True, blank=True)

    fname_regex = RegexValidator(
        regex=r'^.+$',
        message=_('First name must be a non-empty string'),
    )

    lname_regex = RegexValidator(
        regex=r'^.+$',
        message=_('Last name must be a non-empty string'),
    )

    email_regex = RegexValidator(
        regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',
        message=_('Please enter a valid email'),
    )

    password_regex = RegexValidator(
        regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
        message=_('Password should contain capital and small letters and number and special character'),
    )

    phone_regex = RegexValidator(
        regex=r'^01\d{9}$',
        message=_('Please enter a valid phone number'),
    )
