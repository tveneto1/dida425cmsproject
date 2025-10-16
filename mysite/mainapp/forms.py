from django import forms
from .models import Post

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'cover': forms.FileInput(attrs={'class': 'form-input'}),
        }