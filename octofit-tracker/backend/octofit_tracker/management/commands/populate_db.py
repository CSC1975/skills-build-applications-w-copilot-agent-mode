from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Create Activities
        Activity.objects.create(user=tony, activity_type='Running', duration=30, date='2024-01-01')
        Activity.objects.create(user=steve, activity_type='Cycling', duration=45, date='2024-01-02')
        Activity.objects.create(user=bruce, activity_type='Swimming', duration=60, date='2024-01-03')
        Activity.objects.create(user=clark, activity_type='Yoga', duration=20, date='2024-01-04')

        # Create Workouts
        w1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Hard')
        w2 = Workout.objects.create(name='Strength Builder', description='Weight training', difficulty='Medium')

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=100, rank=1)
        Leaderboard.objects.create(user=steve, points=90, rank=2)
        Leaderboard.objects.create(user=bruce, points=80, rank=3)
        Leaderboard.objects.create(user=clark, points=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
