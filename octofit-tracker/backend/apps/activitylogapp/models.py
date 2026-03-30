from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
	ACTIVITY_CHOICES = [
		('run', 'Running'),
		('walk', 'Walking'),
		('strength', 'Strength Training'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
	duration_minutes = models.PositiveIntegerField()
	calories_burned = models.PositiveIntegerField(default=0)
	performed_at = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} {self.activity_type}"
