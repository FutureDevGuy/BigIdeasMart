from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Create superuser on production if it doesn't exist"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ.get("SUPERUSER_USERNAME", "FutureDevGuy")
        email = os.environ.get("SUPERUSER_EMAIL", "philliposeikhuemen@gmail.com")
        password = os.environ.get("SUPERUSER_PASSWORD", "DevAdmin1")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully."))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
