from django.db import models
from django.contrib.auth.models import User

class LeaderboardEntry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
	points = models.PositiveIntegerField(default=0)
	rank = models.PositiveIntegerField(default=1)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['rank', '-points']

	def __str__(self):
		return f"{self.user.username}: {self.points}"
