from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=50)
    translator = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    price = models.IntegerField()
    introduction = models.TextField()
    create_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='create_user', default='pbpressadmin')
    created_date = models.DateTimeField(default=timezone.now)
    update_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='update_user', default='pbpressadmin')
    updated_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title