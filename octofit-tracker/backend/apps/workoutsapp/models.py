from django.db import models
from django.contrib.auth.models import User

class WorkoutSuggestion(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_suggestions')
	title = models.CharField(max_length=120)
	description = models.TextField()
	difficulty = models.CharField(max_length=20, default='beginner')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
