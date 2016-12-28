from django.db import models
from django.contrib.staticfiles.templatetags.staticfiles import static

class MaterialDefCategory(models.Model):
	name = models.CharField(max_length=100)

class MaterialDef(models.Model):
	"""
		TODO: Export metadata to a new model
	"""
	name     = models.CharField(max_length=100)
	category = models.ForeignKey(MaterialDefCategory)
	# quantity = models.IntegerField() # Not relevant for SD card and the rest (date)
	acquisition_date = models.DateField(null=True)

	infos    = models.TextField(default='')
	photo    = models.ImageField(upload_to='uploads/stocklist/photos/', default=static('images/default_material_photo.jpg'))
	price    = models.FloatField(default=0)

	comments = models.TextField(default='')

