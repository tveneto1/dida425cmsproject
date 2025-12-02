from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic

# To check if the uploaded file is valid:
ext_validator = FileExtensionValidator(['png', 'jpg', 'jpeg'])

def validate_file_mimetype(file):
    accept = ['image/png', 'image/jpg', 'image/jpeg']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in accept:
        raise ValidationError("Unsupported file type, only upload .png, .jpg, or .jpeg")


class Post(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('image', 'Image Slide'),
        ('custom', 'Custom Content'),
    ]
    
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, default='image')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    cover = models.ImageField(
        upload_to='images/', 
        validators=[ext_validator, validate_file_mimetype],
        blank=True, 
        null=True
    )
    
    def __str__(self):
        return f"{self.get_content_type_display()} - {self.title}"
    
    # Overriding built-in model delete
    # Means that the deleted file also gets deleted from images folder within project
    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete(save=False)
        super().delete(*args, **kwargs)
