from django.db import models
class gg(models.Model):
	ggPath=models.FileField(upload_to='upload/')
	urlpath=models.CharField(max_length=100)
def __unicode__(self):
	return self.ggName
	