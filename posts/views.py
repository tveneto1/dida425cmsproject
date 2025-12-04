from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import ImageSlideForm, CustomContentForm, ImageUploadForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.conf import settings
import os
from django.contrib import messages


class HomePageView(ListView):
    model = Post
    template_name = "uploaded_images.html"


def display(request):
    """Get the most recent uploaded image"""
    latest_post = Post.objects.order_by('-id').first()
    return render(request, 'display.html', {'post': latest_post})


def all_images_view(request):
    """Display all posts (images and custom content)"""
    posts = Post.objects.all().order_by('-id')
    return render(request, "uploaded_images.html", {'object_list': posts})


def upload_image(request):
    """NEW: Handle both image slide and custom content uploads"""
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        # Check which form was submitted
        if 'image_submit' in request.POST:
            form = ImageSlideForm(request.POST, request.FILES)
            if form.is_valid():
                content = form.save(commit=False)
                content.content_type = 'image'
                content.save()
                messages.success(request, 'Image slide uploaded successfully!')
                return redirect('all_images')
            else:
                messages.error(request, 'Please correct the errors in the image form.')
        
        elif 'custom_submit' in request.POST:
            form = CustomContentForm(request.POST)
            if form.is_valid():
                content = form.save(commit=False)
                content.content_type = 'custom'
                content.save()
                messages.success(request, 'Custom content uploaded successfully!')
                return redirect('all_images')
            else:
                messages.error(request, 'Please correct the errors in the custom content form.')
    
    return render(request, 'post.html')


def delete_image(request, pk):
    """Delete images or custom content"""
    if request.method == "POST": 
        post = Post.objects.filter(id=pk) 
        post.delete() 
    return redirect('all_images')


def slidedisplay(request):
    """Function to show both images and custom content in slideshow"""
    posts = Post.objects.all().order_by('id')  
    return render(request, 'display.html', {'posts': posts})


def read_dateline(request):
    """Viewing dateline reader after refresh from display"""
    return render(request, "dateline_reader.html")


def fetch_json_view(request):
    """To actually fetch json file"""
    try:
        file_path = os.path.join(settings.BASE_DIR, 'templates', 'dateline_announcements.json')
        
        # Debugging
        print(f"=== FETCH JSON DEBUG ===")
        print(f"BASE_DIR: {settings.BASE_DIR}")
        print(f"Looking for file at: {file_path}")
        print(f"File exists: {os.path.exists(file_path)}")
        
        if not os.path.exists(file_path):
            print(f"ERROR: File not found!")
            return JsonResponse({'error': 'File not found', 'path': file_path}, status=404)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"Successfully loaded {len(data)} announcements")
        return JsonResponse(data, safe=False)
        
    except json.JSONDecodeError as e:
        print(f"JSON DECODE ERROR: {e}")
        return JsonResponse({'error': 'Invalid JSON', 'details': str(e)}, status=500)
    except Exception as e:
        print(f"UNEXPECTED ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': 'Server error', 'details': str(e)}, status=500)


# FUNCTIONS FOR MANAGE USERS PAGE
def manage_users(request):
    users = User.objects.all().order_by('username')
    return render(request, 'manage_users.html', {'users': users})


def toggle_superuser(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        user.is_superuser = not user.is_superuser
        user.save()
    return redirect('manage_users')


def weather_view(request):
    """Viewing weather"""
    return render(request, "weather/weather.html")

    
