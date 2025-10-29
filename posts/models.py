from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title

#overriding built in model delete
#means that the deleted file also gets deleted from images folder within project -> but it isnt
#try w/o *args
    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete(save=False)
        super().delete(*args, **kwargs)

