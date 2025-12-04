from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic
from pdf2image import convert_from_path
import os
from django.core.files.base import ContentFile
from io import BytesIO

# To check if the uploaded file is valid:
ext_validator = FileExtensionValidator(['png', 'jpg', 'jpeg', 'pdf'])

def validate_file_mimetype(file):
    accept = ['image/png', 'image/jpg', 'image/jpeg', 'application/pdf']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    file.seek(0)
    if file_mime_type not in accept:
        raise ValidationError("Unsupported file type, only upload .png, .jpg, .jpeg, or .pdf")


class Post(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('image', 'Image Slide'),
        ('custom', 'Custom Content'),
    ]
    
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, default='image')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    cover = models.FileField(
        upload_to='images/', 
        validators=[ext_validator, validate_file_mimetype],
        blank=True, 
        null=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.cover and self.cover.name.lower().endswith('.pdf'):
            pdf_path = self.cover.path
            pages = convert_from_path(pdf_path, dpi=200)
            first_page = pages[0]
            buffer = BytesIO()
            first_page.save(buffer, format="PNG")
            buffer.seek(0)
            new_filename = os.path.splitext(self.cover.name)[0] + '.png'
            self.cover.save(new_filename, ContentFile(buffer.read()), save=False)
            super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.get_content_type_display()} - {self.title}"
    
    # Overriding built-in model delete
    # Means that the deleted file also gets deleted from database
    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete(save=False)
        super().delete(*args, **kwargs)
