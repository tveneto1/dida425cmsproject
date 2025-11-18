from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import redirect
import json
from django.http import JsonResponse
from django.conf import settings
import os



class HomePageView(ListView): #upload image
    model = Post
    template_name = "uploaded_images.html"

def display(request): #Get the most recent uploaded image (eventually make this into featured list, choose what to display)
    latest_post = Post.objects.order_by('-id').first() #ID??
    return render(request, 'display.html', {'post': latest_post})

#UPDATED -> passes along images to template so can view uploaded
def all_images_view(request):
    posts = Post.objects.all().order_by('-id')  #get all posts, newest first
    return render(request, "uploaded_images.html", {'object_list': posts})


#two funcs below are doing same thing???
#yes but if we get rid of this one things go wrong so we're keeping it
#class CreatePostView(CreateView):  
 #   model = Post
  #  form_class = ImageUploadForm
   # template_name = "post.html"
#    success_url = reverse_lazy("home") #UNCOMMENT, needs to know where to go after successful


#UPDATED
def upload_image(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)  # Fixed: was UploadImageForm
        if form.is_valid():
            form.save()
            return redirect('all_images')  # Fixed: was 'post' REDIRECT BACK TO ALL IMAGES
    else:
        form = ImageUploadForm()  # Fixed: Create empty form
    
    return render(request, 'post.html', {'form': form})  # Fixed: Pass form to template


#deleting images
def delete_image(request, pk):
    if request.method == "POST": 
        post = Post.objects.filter(id=pk) 
        post.delete() 
    return redirect('all_images')

#function to make uploaded images show up on slideshow display
def slidedisplay(request):
    posts = Post.objects.all().order_by('id')  #gets all posts for slideshow
    return render(request, 'display.html', {'posts': posts})

#viewing dateline reader after refresh from display
def read_dateline(request):
    return render(request, "dateline_reader.html")

#to actually fetch json file bc django makes things difficult
def fetch_json_view(request):
    file_path = os.path.join(settings.BASE_DIR, 'templates', 'dateline_announcements.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)


#FUNCTIONS FOR MANAGE USERS PAGE
#@login_required
#@user_passes_test(lambda u: u.is_staff)
def manage_users(request):
    users = User.objects.all().order_by('username')
    return render(request, 'manage_users.html', {'users': users})

#@login_required
#@user_passes_test(lambda u: u.is_superuser)  # Only superusers can toggle
def toggle_superuser(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        user.is_superuser = not user.is_superuser
        user.save()
    return redirect('manage_users')
