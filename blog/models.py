from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'image/')

    def __str__(self):
        return self.title

    def preview(self):
        return self.body[:50]


    def date(self):
        return self.pub_date.strftime('%Y %b %-m')
