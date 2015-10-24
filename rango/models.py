from django.db.models import Model
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(Model):
	name = models.CharField(max_length = 128, unique = True)
	views = models.IntegerField(default = 0)
	likes = models.IntegerField(default = 0)
	slugs = models.CharField(max_length = 128, unique = True)

	def save(self, *args , **kwargs):
		if not self.id:
			print " i am here "
			print self.name
			self.slugs = slugify(self.name)
		print "i am not here"
		print self.name
		super(Category,self).save(*args,**kwargs)

	def __unicode__(self):
		return self.name

class Page(Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return	self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank = True)
	pic = models.ImageField(upload_to = 'profile_images', blank = True)  		##conjoinde with MEDIA_ROOT setting !

	def __unicode__(self):
		return self.user.username