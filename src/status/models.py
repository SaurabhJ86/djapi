from django.conf import settings
from django.db import models

# Create your models here.

def upload_image(instance,filename):
	return "updates/{user}/{filename}".format(user=instance.user,filename=filename)


class StatusQuerySet(models.QuerySet):
	pass

class StatusManager(models.Manager):
	def get_queryset(self):
		return StatusQuerySet(self.model,using=self._db)

class Status(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	content 	= models.TextField(null=True,blank=True)
	image 		= models.ImageField(upload_to=upload_image,null=True,blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	objects = StatusManager()

	class Meta:
		verbose_name = 'Status post'
		verbose_name_plural = 'Status posts'

	def __str__(self):
		return self.content[:50]


