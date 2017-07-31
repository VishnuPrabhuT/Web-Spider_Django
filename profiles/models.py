from django.db import models

# Create your models here.
class Requester(models.Model):
	name=models.CharField(max_length=250)
	department=models.CharField(max_length=200)
	field=models.CharField(max_length=200)
	start_time=models.DateTimeField(auto_now_add=True)

	# def  __str__(self):
		# return "{0} - {1} - {2}".format(self.name,self.department,self.field)