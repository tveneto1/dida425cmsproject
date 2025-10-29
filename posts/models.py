from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic

#to check if the uploaded file is valid:
ext_validator = FileExtensionValidator(['png', 'jpg', 'jpeg'])
def validate_file_mimetype(file):
    accept = ['image/png', 'image/jpg', 'image/jpeg']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in accept:
        raise ValidationError("Unsupported file type, only upload .png, .jpg, or .jpeg")



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/', validators=[ext_validator, validate_file_mimetype])
    
    def __str__(self):
        return self.title

#overriding built in model delete
#means that the deleted file also gets deleted from images folder within project -> but it isnt
# ^ doesn't have to delete from folder, only from sqlite databsae which it does yay
    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete(save=False)
        super().delete(*args, **kwargs)

