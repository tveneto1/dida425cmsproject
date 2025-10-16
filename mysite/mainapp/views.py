from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import ImageUploadForm

def home(request):
    return render(request, 'mainapp/home.html')

def upload_list(request):
    posts = Post.objects.all()
    return render(request, 'mainapp/upload.html', {'object_list': posts})

@login_required
def upload_image(request):
    if not request.user.is_staff:  # Only allow admin/staff
        return redirect('home')
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploads')
    else:
        form = ImageUploadForm()
    
    return render(request, 'mainapp/upload_form.html', {'form': form})