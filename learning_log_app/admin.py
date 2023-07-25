from django.contrib import admin

# Import the model we want to register.
# The dot (.models) is bc models.py is in the same directory as admin.py.
from .models import Topic

# Register your models here.
admin.site.register(Topic)