from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import ImageUploadForm


class HomePageView(ListView): #upload image
    model = Post
    template_name = "uploaded_images.html"

def display(request): #Get the most recent uploaded image (eventually make this into featured list, choose what to display)
    latest_post = Post.objects.order_by('-id').first() #ID??
    return render(request, 'display.html', {'post': latest_post})


#UPDATE --> need to pass along images to the view pages
def all_images_view(request):
    return render (request, "uploaded_images.html")


#two funcs below are doing same thing???
class CreatePostView(CreateView):  
    model = Post
    form_class = ImageUploadForm
    template_name = "post.html"
    success_url = reverse_lazy("home") #UNCOMMENT, needs to know where to go after successful


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
