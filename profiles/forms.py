from django.forms import ModelForm
from profiles.models import Requester

# Create your models here.
class RequesterForm(ModelForm):
	class Meta:
		model=Requester
		fields = '__all__'

	# def  __str__(self):
		# return "{0} - {1} - {2}".format(self.name,self.department,self.field)