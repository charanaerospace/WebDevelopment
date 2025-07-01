#The Realtor model represents a real estate agent in the system.
#It includes fields for the agent's name, photo, description, phone number, email address,
#whether they are a "Most Valuable Professional" (MVP) realtor, and their hire date.
#The model is ordered by hire date in descending order, and the string representation of the model is the agent's name.


from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator


class Realtor(models.Model):
    name = models.CharField(max_length=200, verbose_name="Full Name")
    photo_realtor = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Photo")
    description = models.TextField(blank=True, verbose_name="Description")
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number.")],
        verbose_name="Phone Number"
    )
    email = models.EmailField(max_length=50, verbose_name="Email Address")
    is_mvp = models.BooleanField(default=False, verbose_name="MVP Realtor")
    hire_date = models.DateTimeField(default=now, blank=True, verbose_name="Hire Date")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-hire_date']
        verbose_name = "Realtor"
        verbose_name_plural = "Realtors"
