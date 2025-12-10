# CMS425
### Lillian Pulaski, Kaymora Roberts, Aliana Slaven, Taylor Veneto

This project is a **Content Management System (CMS)** built with **Django**.  
It allows **administrators** to manage users and permissions, while **standard users** can upload and manage slides that appear on the display interface.  
The system provides a secure and efficient way to handle digital display content for multiple users.

This file will walk through some basic features implemented in the project, the different files within the project, various resources used, and finally the documentation to explain _how_ these features work in action.



##  Features

- Role-based access control (Admin vs. Standard)
- Secure authentication and session management
- Slide upload and organization system
- Automatic incorporation of uploaded slides into the display rotation
- Simple, clean user interface
- Scalable structure for future enhancements


##  Project Files 

The Django project is organized into several key components that together support the CMS’s functionality:

- **`cms425veneto/`** – Contains the main project configurations and settings.
- **`accounts/`** – Manages user authentication and registration, including login and signup functionality.
- **`posts/`** – Handles image uploads and display features.
- **`media/`** – Stores all uploaded images that are managed through the system.

Users interact with the system through a set of HTML templates located in the **`templates/`** directory:

- **`dateline_reader.html`** – Reads the scraped B-line data from **`dateline_announcements.json`** one at a time in a randomized order.
- **`display.html`** – Presents a full-screen, rotating view of all uploaded content.
- **`home.html`** – Serves as the user dashboard, welcoming users and providing navigation buttons to other pages.
- **`manage_users.html`** – Provides admin users with the functions to upgrade/downgrade user permissions and to create new users.
- **`post.html`** – Features a form interface for uploading image slides and custom text content.
- **`uploaded_images.html`** – Displays all uploaded content and includes a delete button for removing entries from the slideshow.

The **`registration/`** subdirectory handles all user registration and password changing processes.

The **`static`** subdirectory stores the CSS and JavaScript files necessary to stylize the **`weather.html`** file, which is found within the **`weather`** subdirectory.

Together, these components form a cohesive Django-based CMS where authenticated users can upload, view, and manage display content securely.

##  Sources

Below are the main tutorials and documentation used in the development of this Django CMS project:


### Django Setup & Environment
- [Django CMS Installation Guide](https://docs.django-cms.org/en/latest/introduction/01-install.html)
- [General Django Tutorials – W3Schools](https://www.w3schools.com/django/index.php)
- [Django in Visual Studio Code Tutorial](https://code.visualstudio.com/docs/python/tutorial-django)
- [Official Django Documentation (v5.2)](https://docs.djangoproject.com/en/5.2/)
- [Creating a Django Project in VS Code](https://www.youtube.com/watch?v=U8Ak8iqjFxQ)
- [url - Django Template Tag](https://www.geeksforgeeks.org/python/url-django-template-tag/)

### Image Upload & Slideshow Display
- [Uploading Images in Django](https://www.geeksforgeeks.org/python/python-uploading-images-in-django/)
- [Uploading Images to Django Server](https://www.youtube.com/watch?v=GNsuF4xB80E)
- [Deleting Uploaded Files - Django File Upload Tutorial - Part 4](https://www.youtube.com/watch?v=roYopMO4Eo8&list=PLLxk3TkuAYnpm24Ma1XenNeq1oxxRcYFT&index=3)
- [Django Media Files - Restricting Uploadable File Types with Validators and python-magic](https://www.youtube.com/watch?v=UcUm82jWeKc)
- [python-magic 0.4.27](https://pypi.org/project/python-magic/)
- [About Saving PDF Previews](https://www.djangotricks.com/tricks/4AiKVoFrEkmv/)
- [In Django How to Convert An Uploaded PDF...](https://stackoverflow.com/questions/66069902/in-django-how-to-convert-an-uploaded-pdf-file-to-an-image-file-and-save-to-the-c)
- [Model (PDF to Image)](https://forum.djangoproject.com/t/model-pdf-to-image/8076)
- [pdf2image Official Documentation](https://pdf2image.readthedocs.io/en/latest/installation.html)
- [Fetch](https://happycoding.io/tutorials/javascript/fetch#json)
- [How to Manage Static Files](https://docs.djangoproject.com/en/5.2/howto/static-files/)
- [Leaflet-Providers (OpenStreetMap.HOT)](https://leaflet-extras.github.io/leaflet-providers/preview/#filter=OpenStreetMap.HOT)

### User Authentication, Permissions, and Interaction
- [Django Authentication and Permissions – MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Authentication)  
- [Creating and Customizing Admin Pages – Django Docs](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)
- [How to Override and Extend Basic Django Admin Templates](https://www.geeksforgeeks.org/python/how-to-override-and-extend-basic-django-admin-templates/)
- [Django Login, Logout, and Signup Tutorial – LearnDjango](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
- [How to Add Fields to Registration Form - Django Blog #20](https://www.youtube.com/watch?v=TBGRYkzXiTg)
- [Django_010: Simple Login and Logout with Built-In Authentication](https://medium.com/@staytechrich/django-010-simple-login-and-logout-with-built-in-authentication-5521353015af)
- [Django Password Reset Tutorial](https://www.youtube.com/watch?v=ZR8Ymkx30p0)
- [How To - Hoverable Dropdown](https://www.w3schools.com/howto/howto_css_dropdown.asp)


## HOW IT WORKS (DOCUMENTATION) 

### Download / Access
To download CMS425, start by cloning the project’s GitHub repository and ensuring that Django and all required dependencies are installed on your device. Once the server is running, the CMS can be accessed through any web browser using the project’s URL. When connecting to the Raspberry Pi, users must first be signed into the Tailscale VPN, as the Raspberry Pi is only reachable through its Tailscale network address. If accessing the Raspberry Pi’s files from a Mac, users can also open Finder, press Command + K, and enter the Pi’s Tailscale URL to connect. This provides an easy way to locate the device and verify that the server is available.

Alternatively, download this repository as a .zip file, and extract all files where the .zip files downloads to on the personal device. This should create a folder with all the necessary project files. Open that extracted folder in any preferred code editing platform (note: this documentation will use Visual Studio Code as the preferred platform). In order to run the project in a web browser, first open the terminal. In Visual Studio Code, this is done by going to the three dots at the top, selecting _Terminal_, and finally _Create New Terminal_. [Pip install Django](https://docs.djangoproject.com/en/5.2/topics/install/) within that terminal using the proper command based on the operating system of the personal device; the commands are found at the hyperlink to the official Django documentation. Once Django is installed, stay in the terminal and run the command **`python manage.py runserver 0.0.0.0.8002`**. Follow the link starting with **`http://0.0.0.0`** that generates as part of the output. If an issue with port connection arises, change the number at the end of the **`runserver`** command to a port that is not in use.

After following these steps, CMS425 is now accessible within the web browser. If the connection breaks, simply run **`python manage.py runserver`** again in the terminal with the selected port number at the end.

### User Permissions and Accounts
CMS425 includes two different types of users, each with different permissions. A **standard user** can upload content, delete content, and test the slideshow capabilities. An **admin user** can do these actions as well, but they also have the ability to **create** users, **upgrade** a standard user to admin status, or **downgrade** an admin user to standard. Dealing with the other user permissions is the key difference between admin users and standard users.

If an admin user needs to create a new user, the page to do so is found in the hamburger dropdown menu, under **Manage Users**. This option does not appear for standard users. Once on that page, the user sees a table with usernames, email addresses, superuser (admin) status, and a button to either upgrade or downgrade a specific user. Upgrading a user gives it admin status, while downgrading a user takes that status away. 

Beneath the table, there is a **create user** button, which goes to a sign up box. Each field — email, username, password, and password confirmation — is required to create a user. The email address is necessary for any potential password resets, which will be explained in depth below. As of right now, deleting users is not possible.

_**IMPORTANT TO NOTE:**_ when a user is created, it only has **standard permissions**. If this new user needs admin capabilities, it must then be **upgraded**.

A **password change/reset** can happen if a user is logged in or not. If the user is logged in, one can find that option in the hamburger dropdown menu. It is also available on the log in page. After pressing either button, the user will be prompted to input the email address associated with that account, in order to recieve an email with a reset link. Follow the steps in the email, and once the password is reset, the user can log in with their new password.


### Home Screen
Once the user is logged in, they are brought to the CMS425 home screen. The user can access all the functions of the website from here, the most important being the three square buttons in the center of the screen: **Upload Content**, **Manage Slides**, and **Start Display**. The footer includes the yeaar of publication, as well as a link to this GitHub (About CMS425).


### Upload Content 
There are two different types of content a user can upload: **image slides** and **custom content**. When within this webpage, the user can only do one type of upload at a time, because after the submission goes through, the page redirects to Manage Slides.

The **Image Upload** is on the left side of the screen, and requires both the **title** and **choose file** fields to be completed for a valid submission. The title should be used as a description for the image. It will not appear anywhere within the slideshow, only in the table of uploaded content to help with organization. The choose file field is where the image itself is chosen. This particular field only accepts **.png**, **.jpg**, **.jpeg**, and **.pdf** files. Anything else will lead to a failed submission attempt. Both horizontal and vertical images can be accepted and displayed without issue.

_**Important note for .pdf uploads**_: only the first page of a PDF file will be included in the slideshow, regardless of how many pages it may contain.

The **Custom Content** input is on the right side of the screen, and requires both the **title** and **description** fields, with the optional **link** field at the bottom. These text boxes let the user type in the text they wish to display without the need to format it as an image file, allowing for quick and easy announcements to be added. Each field will be displayed as text within the slideshow rotation. The title is header text, the description is subheading text, and, if included, the link is body text.


### Manage Slides 
This page can be accessed directly from the home page, or after submitting content from Upload Content. It shows everything that has been uploaded in a table for easy viewing. **All items in this table will be in the slideshow**. If necessary, the user can navigate back to Upload Content via the green button above the table.

The **file type** column specifies if the uploaded content is an image slide or custom content. For image slides only, there is a **preview** of what the image will look like in the slideshow rotation. For custom content, that column will be empty. The **description** column includes the title from Upload Content, and for custom content, also has the input from the description and link fields.

On the far right, a user can **delete** the uploaded content. Doing so removes that item from the table, and also from the slideshow rotation. If an item was deleted accidentally, it can be uploaded again.

**_TO REITERATE AN IMPORTANT POINT_: all items in this table will be featured in the slideshow. If an item needs to removed from the slideshow, it must be deleted within Manage Slides.**


### Start Display
The Start Display button launches the slideshow within the browser for the user to test what it will look like after adding or deleting any content. To return to the home screen, press the back arrow by the URL bar until at the desired location. 

This rotating carousel display has three main features. The first is all of the uploaded content visible in Manage Slides. The slideshow will automatically display each of these items one at a time, with the images fitting the height of the screen, and the Custom Content input displayed as white text on a green background for easier readability. It begins with the item at the bottom of the Manage Slides table, and works it way up to the most recently submitted content.

After going through all of the uploaded content, the slideshow changes to the automatically scraped B-Line announcements for the day. These are randomly chosen from their stored file, and shown, once again, one at a time in the same rotating fashion as the uploaded content. Three of these will be displayed, and then the carousel changes one final time to the Binghamton weather. This dashboard has a dynamic radar map, as well as the temperature and weather conditions for the present day, present night, and next day. Once the weather slide times out, the whole rotation begins again.

This slideshow is what will be on the DiDa department television, but having a way to test it within the user's browser is beneficial to double check that all the necessary information has made it into the display, or to see if an item needs to be deleted. 
