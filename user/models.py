from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def image_tag(self):  # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.photo))
