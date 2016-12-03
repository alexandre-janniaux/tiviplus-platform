from django.db import models
from django.conf import settings
from stocklist.models import MaterialDef

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Event(models.Model):
	author     = models.ForeignKey(AUTH_USER_MODEL)
	title      = models.CharField(max_length=150)
	desc       = models.TextField()
	valid      = models.BooleanField(default=False)


class MaterialLoan(models.Model):

	REQUEST_STATUS = (
		(0, 'Not processed'),
		(1, 'Accepted'),
		(2, 'Refused')
	)

	borrower    = models.ForeignKey(AUTH_USER_MODEL)
	material    = models.ForeignKey(MaterialDef)
	number      = models.IntegerField(default=0)
	request_date = models.DateTimeField(auto_now_add=True)

	date        = models.DateTimeField('borrow date')
	end_date    = models.DateTimeField('excepted return date')
	
	reason      = models.ForeignKey(Event)

	returned    = models.BooleanField(default=False)
	material_status = models.TextField(default='')
	request_status  = models.IntegerField(choices=REQUEST_STATUS)
