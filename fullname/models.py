from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'

    def __str__(self):
        return self.full_name or self.username
