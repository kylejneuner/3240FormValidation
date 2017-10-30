from django.db import models

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length = 20, blank = True, null = True)
