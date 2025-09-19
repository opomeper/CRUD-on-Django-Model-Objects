# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


# Your code starts from here:
instructor_yan = Instructor.objects.get(first_name='Yan')
print("1. Find a single instructor by first name 'Yan'")
print(instructor_yan)
print("\n")

try:
    instructor_andy = Instructor.objects.get(first_name='Andy')
except Instructor.DoesNotExist:
    print("2. Try to find a non-existing instructor with first name Andy")
    print("Instructor Andy does not exist")
    print("\n")

partimer = Instructor.objects.filter(full_time=False)
print("3. Find all part time instructors")
print(partimer)
print("\n")

fulltimer_y = Instructor.objects.exclude(full_time=False).filter(first_name__startswith='Y').filter(total_learners__gt=30000)
print("4. Find all full time instructors with First Name starts with Y and learners count greater than 30000")
print(fulltimer_y)
print("\n")

fulltimer_y2 = Instructor.objects.filter(full_time=True, first_name__startswith='Y', total_learners__gt=30000)
print("5. Find all full time instructors with First Name starts with Y and learners count greater than 30000 using multiple parameters")
print(fulltimer_y2)

