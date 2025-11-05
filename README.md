# Django CMS Project 
### Taylor Veneto, Aliana Slaven, Kaymora Roberts, Lillian Pulaski 

This project is a **Content Management System (CMS)** built with **Django**.  
It allows **administrators** to manage users and permissions, while **content editors** can upload and manage slides that appear on the display interface.  
The system provides a secure and efficient way to handle digital display content for multiple users.



##  Features

- Role-based access control (Administrators vs. Editors)
- Secure authentication and session management
- Slide upload and organization system
- Automatic incorporation of uploaded slides into the display rotation
- Simple, clean user interface
- Scalable structure for future enhancements


##  Project Walkthrough

The Django project is organized into several key components that together support the CMS’s functionality:

- **`cms425veneto/`** – Contains the main project configurations and settings.
- **`accounts/`** – Manages user authentication and registration, including login and signup functionality.
- **`posts/`** – Handles image uploads and display features.
- **`media/`** – Stores all uploaded images that are managed through the system.

Users interact with the system through a set of HTML templates located in the **`templates/`** directory:

- **`signup.html`** and **`login.html`** – Handle user registration and authentication processes.
- **`home.html`** – Serves as the user dashboard, welcoming users and providing navigation buttons to other pages.
- **`post.html`** – An admin-only page featuring a form interface for uploading slide images.
- **`uploaded_images.html`** – Displays all uploaded images and includes a delete button for removing entries from the database.
- **`display.html`** – Presents a full-screen view of the most recently uploaded image, with planned functionality to cycle through all uploaded images automatically.

Together, these components form a cohesive Django-based CMS where authenticated users can upload, view, and manage display content securely.

##  Sources

Below are the main tutorials and documentation used in the development of this Django CMS project:

### User Authentication & Permissions
- [Django Authentication and Permissions – MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Authentication)  
- [Django Login, Logout, and Signup Tutorial – LearnDjango](https://learndjango.com/tutorials/django-login-and-logout-tutorial)

### Django Setup & Environment
- [Django CMS Installation Guide](https://docs.django-cms.org/en/latest/introduction/01-install.html)
- [General Django Tutorials – W3Schools](https://www.w3schools.com/django/index.php)
- [Django in Visual Studio Code Tutorial – Microsoft Docs](https://code.visualstudio.com/docs/python/tutorial-django)
- [Official Django Documentation (v5.2)](https://docs.djangoproject.com/en/5.2/)
- [Creating a Django Project in VS Code – YouTube](https://www.youtube.com/watch?v=U8Ak8iqjFxQ)

### Image Upload & Admin Features
- [Uploading Images in Django – GeeksforGeeks](https://www.geeksforgeeks.org/python/python-uploading-images-in-django/)
- [Uploading Images to Django Server – YouTube](https://www.youtube.com/watch?v=GNsuF4xB80E)
- [Creating and Customizing Admin Pages – Django Docs](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)

