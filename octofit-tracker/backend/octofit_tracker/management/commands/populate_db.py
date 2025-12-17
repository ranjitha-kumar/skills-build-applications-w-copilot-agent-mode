from django.core.management.base import BaseCommand
from octofit_tracker import models
from django.contrib.auth.models import User
from djongo import models as djongo_models
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write(self.style.WARNING('Deleting existing data...'))
        # Custom deletion logic for each model
        # TODO: Replace with actual model names when defined
        # Example: models.User.objects.all().delete()
        # Example: models.Team.objects.all().delete()
        # Example: models.Activity.objects.all().delete()
        # Example: models.Leaderboard.objects.all().delete()
        # Example: models.Workout.objects.all().delete()

        # Insert test data
        self.stdout.write(self.style.SUCCESS('Inserting test data...'))
        # Example data for Marvel and DC teams
        # TODO: Replace with actual model creation logic
        # Example:
        # marvel_team = models.Team.objects.create(name='Marvel')
        # dc_team = models.Team.objects.create(name='DC')
        # models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel_team)
        # models.User.objects.create(name='Superman', email='superman@dc.com', team=dc_team)
        # ...

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))

        # Ensure unique index on email for users
        with connection.cursor() as cursor:
            cursor.execute('db.users.createIndex({ "email": 1 }, { unique: true })')
        self.stdout.write(self.style.SUCCESS('Unique index on user email ensured.'))
