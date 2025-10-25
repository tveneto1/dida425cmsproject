from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title

#overriding built in model delete
#means that the deleted file also gets deleted from images folder within project
    def delete(self, *args, **kwargs):
        self.title.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
