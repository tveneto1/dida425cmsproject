from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


#uploading image
#class HomePageView(ListView):
 #   model = Post
  #  template_name = "home.html"

def display(request): #Get the most recent uploaded image (eventually make this into featured list, choose what to display)
    latest_post = Post.objects.order_by('-id').first()
    return render(request, 'posts/display.html', {'post': latest_post})


class CreatePostView(CreateView):  
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = reverse_lazy("home")

#@login_required
def upload_image(request):
    if not request.user.is_staff:  # Only allow admin/staff to upload the image bc in the posts app
        return redirect('home') #goes back to homepage im guessing
    
    if request.method == 'POST':
        form = Post(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploads')
    else:
        form = Post()
    
    return render(request, 'posts/post.html', {'form': form})


#come back to this, put post.html as request as per geeksforgeeks resource and I think i got it url-wise
