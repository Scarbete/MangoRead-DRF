from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, password=None):
        user = self.model()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None):
        user = self.create_user(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
