from django.conf import settings
from django.db import models

from django.contrib.auth import get_user_model
from django.utils import timezone
User=get_user_model()



# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=250)
    destination = models.CharField(max_length=50)
    dest_type = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None)
    content = models.TextField()

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)
