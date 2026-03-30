from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction

from apps.teamspaceapp.models import Team
from apps.activitylogapp.models import ActivityLog
from apps.leaderboardapp.models import LeaderboardEntry
from apps.workoutsapp.models import WorkoutSuggestion

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        ActivityLog.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        WorkoutSuggestion.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        marvel = Team.objects.create(name='Team Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='Team DC', description='DC superheroes')

        users = [
            User(username='ironman', email='ironman@marvel.com'),
            User(username='spiderman', email='spiderman@marvel.com'),
            User(username='batman', email='batman@dc.com'),
            User(username='wonderwoman', email='wonderwoman@dc.com'),
        ]
        for u in users:
            u.set_password('password')
            u.save()

        marvel.members.add(User.objects.get(username='ironman'))
        marvel.members.add(User.objects.get(username='spiderman'))
        dc.members.add(User.objects.get(username='batman'))
        dc.members.add(User.objects.get(username='wonderwoman'))

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        ActivityLog.objects.create(user=User.objects.get(username='ironman'), activity_type='run', duration_minutes=30, calories_burned=300, performed_at='2026-03-01T10:00:00Z')
        ActivityLog.objects.create(user=User.objects.get(username='spiderman'), activity_type='walk', duration_minutes=45, calories_burned=200, performed_at='2026-03-02T11:00:00Z')
        ActivityLog.objects.create(user=User.objects.get(username='batman'), activity_type='strength', duration_minutes=60, calories_burned=400, performed_at='2026-03-03T12:00:00Z')
        ActivityLog.objects.create(user=User.objects.get(username='wonderwoman'), activity_type='run', duration_minutes=50, calories_burned=350, performed_at='2026-03-04T13:00:00Z')

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        LeaderboardEntry.objects.create(user=User.objects.get(username='ironman'), points=100, rank=1)
        LeaderboardEntry.objects.create(user=User.objects.get(username='spiderman'), points=90, rank=2)
        LeaderboardEntry.objects.create(user=User.objects.get(username='batman'), points=80, rank=3)
        LeaderboardEntry.objects.create(user=User.objects.get(username='wonderwoman'), points=70, rank=4)

        self.stdout.write(self.style.SUCCESS('Creating workout suggestions...'))
        WorkoutSuggestion.objects.create(user=User.objects.get(username='ironman'), title='HIIT Cardio', description='High intensity interval training', difficulty='advanced')
        WorkoutSuggestion.objects.create(user=User.objects.get(username='spiderman'), title='Yoga Flex', description='Flexibility and balance', difficulty='beginner')
        WorkoutSuggestion.objects.create(user=User.objects.get(username='batman'), title='Strength Circuit', description='Full body strength', difficulty='intermediate')
        WorkoutSuggestion.objects.create(user=User.objects.get(username='wonderwoman'), title='Endurance Run', description='Long distance running', difficulty='advanced')

        self.stdout.write(self.style.SUCCESS('Database populated with superhero test data!'))
