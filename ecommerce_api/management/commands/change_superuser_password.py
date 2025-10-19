from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Change production superuser password'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        user = User.objects.get(username='FutureDevGuy')
        user.set_password('DevAdmin1')  
        user.save()
        self.stdout.write(self.style.SUCCESS('Password updated successfully!'))
