from django.db import models
from django.conf import settings
from stocklist.models import MaterialDef

from django.utils.translation import ugettext as _

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Event(models.Model):
	author     = models.ForeignKey(AUTH_USER_MODEL)
	title      = models.CharField(max_length=150)
	desc       = models.TextField()
	delete_on  = models.DateTimeField(null=True, blank=True)


class MaterialLoan(models.Model):

	REQUEST_STATUS = (
		(0, _('Not processed')),
		(1, _('Accepted')),
		(2, _('Refused'))
	)

	borrower    = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_('borrower'))
	material    = models.ForeignKey(MaterialDef, verbose_name=_('material'))
	number      = models.IntegerField(verbose_name=_('number'), default=1)
	request_date = models.DateTimeField(verbose_name=_('request date'), auto_now_add=True)

	date        = models.DateTimeField(verbose_name=_('borrow date'))
	end_date    = models.DateTimeField(verbose_name=_('excepted return date'))
	
	reason      = models.ForeignKey(Event, verbose_name=_('reason'))

	returned_date   = models.DateTimeField(_('returned date'), blank=True, null=True)
	material_status = models.TextField(_('material status'), default='')
	request_status  = models.IntegerField(_('request status'), choices=REQUEST_STATUS)
