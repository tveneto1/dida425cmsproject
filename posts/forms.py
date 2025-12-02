from django import forms
from .models import Post

class ImageSlideForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover']
    
    def clean_cover(self):
        cover = self.cleaned_data.get('cover')
        if not cover:
            raise forms.ValidationError("Please upload an image.")
        return cover


class CustomContentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'link']
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description or description.strip() == '':
            raise forms.ValidationError("Please add a description.")
        return description
    

ImageUploadForm = ImageSlideForm
