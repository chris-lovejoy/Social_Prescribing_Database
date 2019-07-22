from django.db import models



# Dependencies for date time field
import datetime
from django.utils import timezone




#  MODELS

class Services(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=1000)
	telephone = models.CharField(max_length=15, null=True)
	email = models.CharField(max_length=40, null=True)
	website = models.CharField(max_length = 50, null=True)
	image_url = models.CharField(max_length = 250, default="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg")
	image = models.ImageField(upload_to='service_images', default="service_images/no_image.svg")
	referral_route = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	# exp_date = models.DateTimeField('date expired')
	def __str__(self):
		return self.title
# To add more
# ?to add 'service type' and link to a drop-down menu?/other object class

