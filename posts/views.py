from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import ImageUploadForm



#uploading image
class HomePageView(ListView):
    model = Post
    template_name = "uploaded_images.html"

def display(request): #Get the most recent uploaded image (eventually make this into featured list, choose what to display)
    latest_post = Post.objects.order_by('-id').first()
    return render(request, 'display.html', {'post': latest_post})


class CreatePostView(CreateView):  
    model = Post
    form_class = ImageUploadForm
    template_name = "post.html"
   # success_url = reverse_lazy("home")

def all_images_view(request):
    return render (request, "uploaded_images.html")


# @login_required
def upload_image(request):
    if not request.user.is_staff:  # Only allow admin/staff to upload the image bc in the posts app
        return redirect('home') #goes back to homepage im guessing
    
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post') 
    else:
        #form = Post()
        return render(request, 'post.html')


#come back to this, put post.html as request as per geeksforgeeks resource and I think i got it url-wise