import random, string
from django.db import models

from account.models import CustomUser
# Create your models here.

class Gateway(models.Model):
	user 		= models.ForeignKey(CustomUser, related_name='gateways', on_delete=models.CASCADE, null=True)
	name 		= models.CharField(max_length=64, null=True)
	secret 		= models.CharField(max_length=13, null=True, blank=True)
	api_key 	= models.CharField(max_length=13, null=True, blank=True)

	def __str__(self):
		return f'{self.name} - {user}'

	def save(self, *args, **kwargs):
		# generate 13 alphanumeric character
		self.api_key = ''.join(random.choices(string.ascii_letters + string.digits, k=13))
		self.secret = ''.join(random.choices(string.ascii_letters + string.digits, k=13))
		super().save(*args, **kwargs)



class Task(models.Model):
	gateway 	= models.ForeignKey(Gateway, related_name='tasks', on_delete=models.CASCADE, null=True)
	to 			= models.CharField(max_length=32, null=True)
	message 	= models.TextField()

	def __str__(self):
		return f'{self.gateway.name} - {self.message[:20]}...'