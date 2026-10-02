from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

user = User.objects.get(username="@gmail.com")

print(user.username)
print(user.email)




