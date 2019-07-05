from django.db import models



# Dependencies for date time field
import datetime
from django.utils import timezone




#  MODELS

class Service(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	# pub_date = models.DateTimeField('date published')
	# exp_date = models.DateTimeField('date expired')
	def __str__(self):
		return self.title
# To add more
# ?to add 'service type' and link to a drop-down menu?/other object class

