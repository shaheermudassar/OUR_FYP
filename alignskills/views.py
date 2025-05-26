from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.forms import PasswordChangeForm

# Models
from .models import Course, ContactMessage, Comment_about_page, NewsletterSubscriber, UserStats, ProjectSubmission, Enrollment, Comment, Banner, FAQ, Project, Quiz, Lecture, Chapter

# From other app (alignskills)
from alignskills.models import Course as AlignskillsCourse, Enrollment as AlignskillsEnrollment, CustomUser

# Forms
from .forms import CommentForm, ProjectSubmissionForm, NewsletterForm

# Third-party imports
import requests
import json
from urllib.parse import unquote  # For URL decoding
from django.contrib.auth.hashers import make_password, check_password


# alignskills/views.py

from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_admin(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(username="admin", email="admin@example.com", password="admin123")
        return HttpResponse("Superuser created!")
    return HttpResponse("Admin already exists.")


# --------------------------------------  stat view ---------------------------------------



def user_stats_view(request):
    # Get the count of students marked as active
    active_students = UserStats.objects.filter(is_active=True).count()

    # Get the count of students marked as graduates
    graduate_students = UserStats.objects.filter(is_graduate=True).count()

    # Get the count of students marked as certified
    certified_students = UserStats.objects.filter(is_certified=True).count()

    # Create a context dictionary to pass the counts to the template
    context = {
        'active_students': active_students,
        'graduate_students': graduate_students,
        'certified_students': certified_students,
    }

    # Render the 'home.html' template with the provided context
    return render(request, 'home.html', context)

def mark_as_graduate(request):
    # Check if the user is logged in
    if request.user.is_authenticated:

        # Get the user's UserStats instance
        stats = request.user.userstats

        # Set the is_graduate field to True
        stats.is_graduate = True

        # Save the updated stats to the database
        stats.save()

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success'})

    # If the user is not authenticated, return an error response
    return JsonResponse({'status': 'error'}, status=401)







# --------------------------------------  signup ---------------------------------------





    # This function handles new user registration
def signup(request):    

    # Only process if form is submitted (POST request)
    if request.method == 'POST':
        # Get and clean form data
        username = request.POST.get('username', '').strip()  # Remove extra spaces
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # Check if any field is empty
        if not username or not email or not password:
            # messages.error(request, "All fields are required!")# Show error message if any field is empty
            return redirect('/registration/login-signup/')

        # Get the correct User model (CustomUser in your case)
        User = get_user_model()

        # Check if email already exists in database
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already used ", extra_tags='signup')# Show error if email is taken
            return redirect('/registration/login-signup/')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already used",extra_tags='signup')# Show error if username exists
            return redirect('/registration/login-signup/')

        # Create new user account
        # create_user() automatically:
        # 1. Hashes the password (turns it into secure code)
        # 2. Saves to database
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password
        )

        # Required for custom user models - tells Django how to authenticate
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        
        login(request, user)# Automatically log the user in after signup

        # messages.success(request, "Signup successful! You are now logged in.")# Show success message

        return redirect('/')# Send user to homepage

    # If not POST request, show empty signup form
    return render(request, 'registration/login-signup.html')







# --------------------------------------  user_login ---------------------------------------







User = get_user_model()  # Ensure CustomUser is used instead of auth.User
@csrf_protect # Protects against Cross-Site Request Forgery attacks(fake form submission block)
def user_login(request):
    if request.method == "POST":

        # Get and clean the identifier (email/username) and password
        identifier = request.POST.get('identifier', '').strip()#.strip() removes whitespace
        password = request.POST.get('password', '').strip()
        
        User = get_user_model()
        
         # SECURITY:no empty Field
        if not identifier or not password: # Basic validation - check if fields are empty
            messages.error(request, "Both email/username and password are required!",extra_tags='login')
            return redirect('/registration/login-signup/')

        try:
            # Find user by email or username(identifier Can be either email or username)
            if "@" in identifier:# If it contains @, treat as email
                user = User.objects.get(email=identifier)
                username = user.username
            else:
                user = User.objects.get(username=identifier)
                username = identifier

            # FIRST SECURITY layer: Verify password hash match
            if not user.check_password(password):
                messages.error(request, "Invalid login credentials",extra_tags='login')
                return redirect('/registration/login-signup/')
            
             # SECURITY LAYER 2: Full Django authentication
            authenticated_user = authenticate(request, username=username, password=password)
            
            if authenticated_user is None:# If authentication failed
                messages.error(request, "Authentication failed",extra_tags='login')
                return redirect('/registration/login-signup/')
            
            # SECURITY LAYER 3: Final confirmation
            if authenticated_user.check_password(password):
                login(request, authenticated_user)# All checks passed - log the user in


                # Security: Generate new session key to prevent session fixation(after login session id refresh)
                request.session.cycle_key()  
                messages.success(request, "Login successful!", extra_tags='login')
                return redirect('/')
            else:
                messages.error(request, "Access denied",extra_tags='login')
                return redirect('/registration/login-signup/')

        except User.DoesNotExist:
            messages.error(request, "Account not found",extra_tags='login')
            return redirect('/registration/login-signup/')

    return render(request, 'registration/login-signup.html')



def user_logout(request):
    logout(request)
    return redirect('/')







from django.shortcuts import render
@login_required
def home(request):
    return render(request, 'home.html')

def aboutus(request):  # Check if this is 'aboutus' instead of 'about'
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def contactus(request):  # Check if this is 'contactus'
    return render(request, 'contact.html')
def resume_main_page(request):
    return render(request,'resume_main_page.html')
def profile(request):
    return render(request, 'profile.html') 

@login_required
def student_panel(request):
    user = request.user  # Get the logged-in user
    enrollments = Enrollment.objects.filter(student=user)  # Fetch enrolled courses
    
    return render(request, 'student-panel.html', {'enrollments': enrollments})





# --------------------------------------enrol  courses ---------------------------------------




@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user = request.user



    # Debugging lines to confirm
    print(f"Attempting to enroll user: {user.username} in course: {course.title}")

    if not getattr(user, 'email_verified', False):  # Ensure email is verified
        messages.error(request, "Please verify your email before enrolling.")
        return redirect('course-detail', course_id=course.id)

    if request.method == "POST":
        # Check if the user is already enrolled
        if Enrollment.objects.filter(student=user, course=course).exists():
            messages.warning(request, "You are already enrolled in this course!")
        else:
            # Create the enrollment and confirm
            enrollment = Enrollment.objects.create(student=user, course=course)
            print(f"Enrollment created: {enrollment}")  # Debugging line to check creation
            messages.success(request, "Successfully enrolled in the course!")

    return redirect('course-detail', course_id=course.id)  # Redirect to course detail page







def user_project_count(request):
    user = request.user  # Get the logged-in user
    project_count = user.projects.count()  # Count the number of projects submitted by the user
    return render(request, 'profile.html', {'project_count': project_count})





def account_menu(request):
    return render(request, 'registration/account.html' )


# -------------------------------------- chat bot ---------------------------------------


@csrf_exempt  # Disables CSRF protection for this view, allowing it to handle requests without a CSRF token.
def ai_chat(request):  # Defines the ai_chat view function that processes user messages.
    if request.method == "POST":  # Only processes POST requests.
        data = json.loads(request.body)  # Parses the JSON data from the request body into a Python dictionary.
        user_message = data.get("message", "")  # Extracts the user's message from the parsed JSON. Defaults to an empty string if not found.

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyC-xTDYWG-TZ3e8rpwXovOp2BXU56ac2Jc"  # API URL for the AI service.
        headers = {"Content-Type": "application/json"}  # Sets the header to indicate the content type is JSON.
        payload = {  # Prepares the payload, wrapping the user message in the required format for the AI service.
            "contents": [{"parts": [{"text": user_message}]}]
        }

        response = requests.post(url, headers=headers, json=payload)  # Sends a POST request to the AI service with the message.
        ai_reply = response.json()  # Parses the JSON response from the AI service.

        try:  # Attempts to extract the AI-generated response.
            reply_text = ai_reply["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):  # Catches errors if the response structure is incorrect.
            reply_text = "Error: Could not generate response."  # Sets a default error message if extraction fails.

        return JsonResponse({"response": reply_text})  # Returns the AI-generated response in a JSON format to the client.

    return JsonResponse({"error": "Invalid request"}, status=400)  # Returns an error message if the request is not a POST request.








# -------------------------------------- contact us page ---------------------------------------






def contact_us_page(request):  # Defines the contact_us_page view function that handles contact form submissions.
    if request.method == "POST":  # Only processes POST requests, which are used when the form is submitted.
        print("✅ Form submitted!")  # Prints a confirmation message to the console that the form has been submitted.

        name = request.POST.get("name")  # Retrieves the 'name' field from the POST data.
        email = request.POST.get("email")  # Retrieves the 'email' field from the POST data.
        subject = request.POST.get("subject")  # Retrieves the 'subject' field from the POST data.
        message = request.POST.get("message")  # Retrieves the 'message' field from the POST data.

        print(f"Received data: Name={name}, Email={email}, Subject={subject}, Message={message}")  # Prints the received data to the console.

        # Validate all required fields (Name, Email, and Message)
        if not all([name, email, message]):  # Checks if any of the required fields are missing.
            print("❌ Missing required fields!")  # Prints an error message to the console if any fields are missing.
            messages.error(request, "Please fill in all required fields (Name, Email, Message)")  # Displays an error message to the user.
            return render(request, "contact.html", {  # Re-renders the form page with the input values pre-filled.
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            })

        try:
            # Try to save the contact message to the database.
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            print("✅ Message saved successfully!")  # Prints a confirmation message to the console when the message is successfully saved.
            messages.success(request, "Your message has been sent successfully!")  # Displays a success message to the user.
            return redirect("contact")  # Redirects to the contact page (usually to show the success message).

        except Exception as e:  # Catches any exceptions that occur while saving the message.
            print(f"❌ Error saving message: {str(e)}")  # Prints the error message to the console.
            messages.error(request, "An error occurred while sending your message. Please try again.")  # Displays an error message to the user.
            return render(request, "contact.html", {  # Re-renders the form page with the input values pre-filled.
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            })

    return render(request, "contact.html")  # If the request method is not POST, simply renders the contact form page.







# -------------------------------------- comment on about page ---------------------------------------



def get_comments(request):  # Defines the get_comments view function that handles fetching the comments.
    comments = Comment_about_page.objects.select_related("user").all()  # Retrieves all the comments from the Comment_about_page model and prefetches the related user data to reduce database queries.
    
    data = {  # Creates a dictionary to structure the response data.
        "comments": [  # A list of comment data will be added under the 'comments' key.
            {  # For each comment in the queryset, a dictionary with relevant information is created.
                "text": comment.text,  # The text of the comment.
                "rating": comment.rating,  # The rating given in the comment.
                "user__username": comment.user.username,  # The username of the user who posted the comment.
                "user__profile_picture": request.build_absolute_uri(comment.profile_picture.url)  # Builds the absolute URL for the user's profile picture if it exists.
                if comment.profile_picture else request.build_absolute_uri(settings.MEDIA_URL + "default.jpg")  # If no profile picture exists, use the default profile picture URL.
            }
            for comment in comments  # Iterates through each comment in the comments queryset.
        ]
    }
    
    return JsonResponse(data)  # Returns the structured data as a JSON response to the client.






# -------------------------------------- search courses ---------------------------------------




def search_courses(request):
    query = request.GET.get('q', 'none')
    print(f"Search Query: {query}")  # Debugging: Check if query is being passed

    courses = Course.objects.filter(title__icontains=query)  # Filter by title
    courses = Course.objects.filter(shorttitle__icontains=query)  # Filter by title
    print(f"Courses Found: {courses}")  # Debugging: Check if courses are found

    return render(request, 'search_results.html', {'courses': courses, 'query': query})




def search(request):
    query = request.GET.get('q')
    print(f"search query: {query}")
    courses = Course.objects.filter(title__icontains=query)
    courses = Course.objects.filter(short_title__icontains=query)

    print(f"search results: {courses.count()}")
    return render(request, 'search_results.html', {
        'courses': courses,
        'query': query
    })














# -------------------------------------- submit project  ---------------------------------------




@login_required  # Ensures that only authenticated users can access this view.
def submit_project(request, project_id):  # Defines the view function that handles submitting a project.
    project_instance = get_object_or_404(Project, pk=project_id)  # Retrieves the project instance from the database or returns a 404 error if not found.
    print("🔍 View function triggered!")  # Debugging print statement to track when the view is called.

    if request.method == 'POST':  # Checks if the request method is POST (form submission).
        form = ProjectSubmissionForm(request.POST, request.FILES)  # Creates a form instance with the submitted data and any files.
        
        if form.is_valid():  # Validates the form data.
            submission = form.save(commit=False)  # Saves the form data without committing it to the database yet.
            submission.student_name = request.user  # Assigns the currently logged-in user as the student who is submitting the project.
            submission.save()  # Commits the data to the database.
            messages.success(request, "Your project has been submitted successfully!")  # Sends a success message to the user.
            return redirect(f"{reverse('submit_project', args=[project_id])}?submitted=true")  # Redirects to the same page with a query parameter indicating the submission was successful.
        else:
            print("❌ Form validation failed!", form.errors)  # Debugging print statement for form validation errors.

    else:  # If the request method is GET, it's the first time loading the page or the page is being refreshed.
        print("🔵 GET request - Loading form.")  # Debugging print statement for GET requests (initial form load).
        form = ProjectSubmissionForm()  # Creates an empty form instance to display to the user.

    return render(request, 'projects/project.html', {  # Renders the project submission page.
        'form': form,  # Passes the form to the template for rendering.
        'project': project_instance,  # Passes the project instance to the template, ensuring the correct project is shown.
    })






# -------------------------------------- dashbort project  ---------------------------------------



def student_projects(request):  # Defines the view function for displaying the student's projects.
    if not request.user.is_authenticated:  # Checks if the user is authenticated.
        return redirect('login')  # If the user is not logged in, redirects them to the login page.

    # Get projects ONLY for the current user
    user_projects = ProjectSubmission.objects.filter(student_name=request.user)  # Filters the ProjectSubmission model to get only projects related to the currently logged-in user.
    
    # Filter from user's projects, not all projects
    approved_projects = user_projects.filter(status='approved')  # Filters the user's projects to show only those that are approved.
    rejected_projects = user_projects.filter(status='rejected')  # Filters the user's projects to show only those that are rejected.

    if request.method == 'POST':  # If the request method is POST, it indicates that the user is submitting a form.
        project_id = request.POST.get('project_id')  # Gets the project ID from the submitted form data.
        
        try:
            project = user_projects.get(id=project_id)  # Attempts to get the project from the user's submissions by the provided project ID.
            form = ProjectSubmissionForm(request.POST, request.FILES, instance=project)  # Creates a form with the existing project data to allow for editing.

            if form.is_valid():  # Checks if the form is valid.
                resubmitted_project = form.save(commit=False)  # Saves the form data without committing it to the database yet.
                resubmitted_project.status = 'pending'  # Sets the project status to 'pending' to indicate it needs to be reviewed again.
                resubmitted_project.save()  # Saves the project to the database with the new status.
                messages.success(request, "Your project has been resubmitted for review.")  # Sends a success message to the user.
                return redirect('student_projects')  # Redirects the user back to the student projects page after successful submission.

        except ProjectSubmission.DoesNotExist:  # Catches the exception if the project does not exist in the user's submissions.
            messages.error(request, "Project not found or you don't have permission.")  # Sends an error message if the project is not found or the user tries to edit a project they don't own.
    else:
        form = ProjectSubmissionForm()  # If the request is not a POST (i.e., a GET request), it initializes an empty form.

    return render(request, 'projects/student-projects.html', {  # Renders the student projects page.
        'approved_projects': approved_projects,  # Passes the list of approved projects to the template.
        'rejected_projects': rejected_projects,  # Passes the list of rejected projects to the template.
        'form': form  # Passes the form instance to the template for rendering.
    })




# -------------------------------------- dashbort courses ---------------------------------------






@login_required  # Ensures that only authenticated users can access this view (the user must be logged in).
def dashboard_courses(request):  # Defines the view function for the dashboard that displays enrolled courses.
    
    # Corrected from request.use to request.user
    enrolled_courses = Enrollment.objects.filter(student=request.user)  # Filters the Enrollment model to get courses that the current user is enrolled in.
    enrolled_count = enrolled_courses.count()  # Counts the number of courses the user is enrolled in.

    context = {  # Prepares the context dictionary that will be passed to the template.
        'enrolled_courses': enrolled_courses,  # Passes the list of enrolled courses to the template.
        'enrolled_count': enrolled_count,  # Passes the count of enrolled courses to the template.
    }
    
    return render(request, 'dashboard_courses.html', context)  # Renders the 'dashboard_courses.html' template, passing the context dictionary to it.




# -------------------------------------- dashbort comments ---------------------------------------





def dashboard_comments(request):  # Defines the view function for the dashboard that displays comments by the logged-in user.
    
    # Fetch comments for the logged-in user
    comments = Comment.objects.filter(user=request.user)  # Filters the Comment model to get all comments where the 'user' is the currently logged-in user.
    
    # Optionally, count the number of comments
    project_count = comments.count()  # Counts the total number of comments made by the logged-in user.

    # Renders the dashboard_comments.html template, passing the comments and the count to the context.
    return render(request, 'dashboard_comments.html', {
        'comments': comments,  # Passes the list of comments made by the user to the template.
        'project_count': project_count  # Passes the count of comments made by the user to the template.
    })




    # --------------------------------------footer subscrtaion ---------------------------------------






def ajax_subscribe_newsletter(request):  # Defines the view function to handle AJAX subscription requests for the newsletter.

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':  
        # Checks if the request is a POST request and if it's an AJAX request (by checking the 'x-requested-with' header).
        
        form = NewsletterForm(request.POST)  # Creates a form instance with the POST data sent in the request.
        
        if form.is_valid():  # Checks if the form data is valid (e.g., email is properly formatted).
            email = form.cleaned_data['email']  # Extracts the cleaned email address from the form data.
            
            if not NewsletterSubscriber.objects.filter(email=email).exists():  
                # Checks if the email already exists in the NewsletterSubscriber model.
                
                NewsletterSubscriber.objects.create(email=email)  # Creates a new record in the NewsletterSubscriber model for the email.
                return JsonResponse({'status': 'success', 'message': 'Subscribed successfully!'})  
                # Returns a JSON response indicating successful subscription.

            else:
                return JsonResponse({'status': 'info', 'message': 'This email is already subscribed.'})  
                # Returns a JSON response indicating the email is already subscribed.

        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid email address.'})  
            # Returns a JSON response indicating that the email provided is invalid.

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})  
    # If the request is not a valid POST request or not an AJAX request, returns an error response.



# --------------------------------------change password ---------------------------------------



@login_required
def change_password(request):  # Defines the view function to handle password change requests.
    if request.method == 'POST':  # Checks if the request method is POST (form submission).
        form = PasswordChangeForm(user=request.user, data=request.POST)  
        # Creates an instance of PasswordChangeForm, passing the current user and the POST data from the form.
        
        if form.is_valid():  # Checks if the form data is valid (i.e., if the new password meets the criteria).
            form.save()  # Saves the new password to the user's account.
            
            update_session_auth_hash(request, form.user)  # Updates the session to maintain the user’s login state after password change.
            
            messages.success(request, 'Your password has been changed successfully!')  
            # Displays a success message indicating that the password has been successfully changed.
            
            return redirect('profile')  # Redirects the user to their profile page after a successful password change.
        else:
            # If the form is not valid (e.g., password is not strong enough), display an error message.
            messages.error(request, 'There was an error changing your password. Your password is not strong enough. Please try again.')
            return redirect('profile')  # Redirects the user back to the profile page even if the password change failed.
    else:
        form = PasswordChangeForm(user=request.user)  
        # If the request is not a POST (i.e., it's a GET request), create a form for the password change.

    return render(request, 'profile.html', {'form': form})  
    # Renders the profile page with the password change form. If the request was GET, the form will be empty; if POST, it will be populated with validation errors if any.






# -------------------------------------- edit profile  ---------------------------------------

from django.views.decorators.http import require_POST


@require_POST  # This decorator ensures that the view only accepts POST requests.
@login_required  # This decorator ensures the user must be logged in to access this view.
def edit_profile(request):  # Defines the view function to handle the profile editing logic.
    # Ensure this is an AJAX request
    if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':  
        # Checks if the request is an AJAX request by looking for the header 'X-Requested-With'.
        return JsonResponse(
            {'status': 'error', 'message': 'Invalid request type'},  
            # Returns an error JSON response with a message indicating the request is not valid.
            status=400,  
            content_type='application/json'  # Explicitly sets the content type to JSON.
        )

    try:
        user = request.user  # Retrieves the current logged-in user.
        new_username = request.POST.get('username', '').strip()  
        # Gets the new username from the POST data and strips any leading/trailing whitespace.

        # Validation
        if not new_username:  # If the new username is empty, return an error.
            return JsonResponse(
                {'status': 'error', 'message': 'Username cannot be empty'},  
                status=400  # Returns an error response with a message about the empty username.
            )

        if user.username == new_username:  # If the username hasn't changed, return a message stating no changes were made.
            return JsonResponse(
                messages.success(request, 'Your password has been changed successfully!')  
            )

        # Check if the new username is already taken by another user
        if CustomUser.objects.exclude(pk=user.pk).filter(username=new_username).exists():  
            # Excludes the current user's record and checks if any other user has the new username.
            return JsonResponse(
                {'status': 'error', 'message': 'Username already taken'},  
                status=400  # Returns an error response if the username is already taken.
            )

        # Update user
        user.username = new_username  # Updates the username of the current user with the new username.
        user.save()  # Saves the changes to the user instance.

        # Update session
        from django.contrib.auth import update_session_auth_hash  # Imports the session update function.
        update_session_auth_hash(request, user)  # Updates the session to keep the user logged in after changing the username.
        request.session.save()  # Saves the session to persist changes.

        # Return success response with new username and initials
        return JsonResponse({
            'status': 'success',  
            'message': 'Username updated successfully!',  
            'new_username': new_username,  # Includes the new username in the response.
            'initials': new_username[:2].upper()  # Provides the first two letters of the new username as initials.
        })

    except Exception as e:  # If an exception occurs (any unexpected error), return an error message.
        return JsonResponse(
            {'status': 'error', 'message': str(e)},  # Includes the exception message in the error response.
            status=500  # Returns a 500 internal server error status for unexpected issues.
        )





from django.contrib.auth.decorators import login_required  # Importing the login_required decorator to restrict access to logged-in users only.
from django.shortcuts import render, get_object_or_404, redirect  # Importing useful Django shortcut functions for rendering views, fetching objects, and redirecting.
from django.urls import reverse  # Importing the reverse function to generate the URL for redirecting.
from .models import Course, Lecture, Comment, Enrollment, Project  # Importing relevant models for courses, comments, etc.
from .forms import CommentForm  # Importing the form for submitting comments.


# --------------------------------------course detail ---------------------------------------



@login_required(login_url='/accounts/login/')  # This decorator ensures that only logged-in users can access this view.
def course_detail(request, course_id):  # Defines the view function for displaying the details of a course.
    course = get_object_or_404(Course, id=course_id)  # Fetches the course object using the course_id, or returns a 404 if not found.
    print(f"\n[DEBUG] Loading Course: {course.id} - {course.title}")  # Debugging output to log course loading.

    # Comments
    comments = Comment.objects.filter(course_id=course).order_by('-date_comment')  # Fetches comments related to the course, ordered by date (latest first).
    print(f"[DEBUG] Found {comments.count()} comments for this course")  # Debugging output to log the number of comments.

    if request.method == 'POST':  # Checks if the request method is POST (i.e., a comment is being submitted).
        form = CommentForm(request.POST)  # Creates a form instance with the posted data.
        if form.is_valid():  # Validates the form.
            comment = form.save(commit=False)  # Saves the form data but does not commit it to the database yet.
            comment.user_id = request.user  # Associates the comment with the logged-in user.
            comment.course_id = course  # Associates the comment with the current course.
            comment.save()  # Saves the comment to the database.
            print(f"[DEBUG] Saved comment for course {course.id}")  # Debugging output to log the saving of the comment.
            return redirect(reverse('course_detail', kwargs={'course_id': course.id}) + '?tab=comments')  # Redirects to the same course detail page, appending a query parameter to navigate to the comments tab.
    else:
        form = CommentForm()  # Creates an empty form if the request method is not POST (e.g., GET request for loading the page).

    # Chapters and lectures count
    chapters = course.chapters.all()  # Fetches all chapters related to the course.
    
    # Enrollment check
    is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()  # Checks if the current user is enrolled in the course.

    # Project (if any)
    try:
        project = Project.objects.get(course=course)  # Tries to fetch the project related to the course.
    except Project.DoesNotExist:
        project = None  # If no project exists for the course, sets the project to None.

    # Context data to pass to the template
    context = {
        'course': course,  # Passes the course object to the template.
        'chapters': chapters,  # Passes the list of chapters to the template.
        'comments': comments,  # Passes the list of comments to the template.
        'form': form,  # Passes the comment form to the template.
        'is_enrolled': is_enrolled,  # Passes a boolean indicating whether the user is enrolled in the course.
        'project': project,  # Passes the project related to the course (if any) to the template.
    }

    return render(request, 'course_detail.html', context)  # Renders the 'course_detail.html' template with the provided context.









# -------------------------------------- course enrollment  ---------------------------------------




def course_enrollment(request, course_id):
    if not request.user.is_authenticated:
        return redirect('login') 
    # Get the course
    course = Course.objects.get(id=course_id)

    # Check if the user is enrolled in the course
    is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()

    # Get all comments for the course
    comments = Comment.objects.filter(course=course).order_by('-created_at')

    # Get all FAQs for the course
    faqs = FAQ.objects.filter(course=course)

    # Filter banners based on the course
    banner = Banner.objects.filter(course=course).first()

    # Calculate total chapters and lectures
    total_chapters = course.chapters.count()
    total_lectures = Lecture.objects.filter(chapter__course=course).count()

    # Pass the data to the template
    return render(request, 'enroll-course-pages/enrolment.html', {
        'course': course,
        'is_enrolled': is_enrolled,
        'comments': comments,
        'faqs': faqs,
        'banner': banner,
        'total_chapters': total_chapters,
        'total_lectures': total_lectures,
    })




# --------------------------------------enroll page ---------------------------------------





@login_required  # Ensure the user is logged in to access this view
def enroll_page(request, course_title):  # Defines the view function for the enrollment page, which takes a course title as a parameter.
    # Get the course based on title (case-insensitive match)
    course = get_object_or_404(Course, title__iexact=course_title)  # Fetches the course using case-insensitive matching for the title. If the course doesn't exist, it raises a 404 error.

    # Handle both enrollment and comments in one view
    if request.method == "POST":  # Checks if the request method is POST (form submission).
        
        if 'enroll_now' in request.POST:  # Checks if the 'enroll_now' key is in the POST data, indicating the user is attempting to enroll.
            try:
                enrolled = Enrollment.enroll_student(request.user, course)  # Calls the `enroll_student` method (assumed to be a custom method for enrollment).
                if enrolled:
                    messages.success(request, "🎉 Successfully enrolled in the course!")  # If enrollment is successful, show a success message.
                    return redirect('enroll_page', course_title=course.title)  # Redirects back to the enrollment page for the same course to refresh the view.
                else:
                    messages.info(request, "ℹ️ You're already enrolled!")  # If the user is already enrolled, show an info message.
            except Exception as e:  # If there is an exception during enrollment, show an error message.
                messages.error(request, f"❌ Enrollment error: {str(e)}")
                return redirect('enroll_page', course_title=course.title)  # Redirects back to the same page to display the error.

        elif 'comment_text' in request.POST:  # Checks if the 'comment_text' key is in the POST data, indicating the user is submitting a comment.
            comment_text = request.POST.get('comment_text', '').strip()  # Gets the comment text, removing any surrounding whitespace.
            if len(comment_text) > 0:  # Checks if the comment text is not empty.
                Comment.objects.create(  # Creates a new Comment instance and saves it to the database.
                    user=request.user,  # Sets the current logged-in user as the comment's author.
                    course=course,  # Associates the comment with the current course.
                    message=comment_text  # Sets the comment text.
                )
                messages.success(request, "💬 Comment posted successfully!")  # Shows a success message after posting the comment.
            else:
                messages.warning(request, "⚠️ Please write a comment before submitting")  # Shows a warning message if the comment is empty.
            return redirect('enroll_page', course_title=course.title)  # Redirects back to the enrollment page to refresh the view.

    # Get banner and FAQs for the course
    banner = Banner.objects.filter(course=course).first()  # Fetches the first Banner object associated with the course, if any.
    faqs = FAQ.objects.filter(course=course)  # Fetches all FAQs related to the course.

    # Prepare context data
    context = {
        'course': course,  # Passes the course object to the template.
        'is_enrolled': Enrollment.objects.filter(student=request.user, course=course).exists(),  # Checks if the current user is enrolled in the course and passes the result to the template.
        'comments': Comment.objects.filter(course=course).order_by('-created_at')[:50],  # Fetches the latest 50 comments for the course and orders them by creation date.
        'banner': banner,  # Passes the banner object to the template.
        'faqs': faqs,  # Passes the FAQs related to the course to the template.
    }

    return render(request, "enroll-course-pages/enrolment.html", context)  # Renders the 'enrolment.html' template with the provided context data.



# --------------------------------------certificate ---------------------------------------



def view_certificate(request, course_title):
    course = get_object_or_404(Course, title__iexact=course_title)
    return render(request, 'certificate.html', {'course': course})

# --------------------------------------lecture page---------------------------------------




def lecture_page(request, chapter_title, lecture_id=None):
    # Fetch the chapter based on its title. If not found, raise a 404 error.
    chapter = get_object_or_404(Chapter, title=chapter_title)  
    course = chapter.course  # Get the course related to this chapter.

    # Get the first quiz associated with the chapter (if any).
    quiz = chapter.quiz_set.first()  # Fetches the first quiz related to the chapter.

    # Get all lectures related to the chapter.
    lectures = chapter.lectures.all()  

    # If a lecture ID is provided, get that specific lecture. If not, use the first lecture in the list.
    if lecture_id:
        current_lecture = get_object_or_404(Lecture, id=lecture_id, chapter=chapter)  # Fetch the specified lecture in this chapter.
    else:
        current_lecture = lectures.first() if lectures else None  # Get the first lecture if no ID is provided. If no lectures exist, set it to None.

    # If a lecture is found, try to fetch the previous and next lectures in order.
    if current_lecture:
        try:
            previous_lecture = current_lecture.get_previous_by_order()  # Fetch the previous lecture based on order.
        except Lecture.DoesNotExist:
            previous_lecture = None  # If there's no previous lecture, set it to None.

        try:
            next_lecture = current_lecture.get_next_by_order()  # Fetch the next lecture based on order.
        except Lecture.DoesNotExist:
            next_lecture = None  # If there's no next lecture, set it to None.
    else:
        # If no lecture is found, set previous and next lectures to None.
        previous_lecture = None
        next_lecture = None

    # Render the lecture page template with all necessary data.
    return render(request, 'lecture_page.html', {
        'chapter': chapter,  # Pass the current chapter to the template.
        'course': course,  # Pass the course related to the chapter.
        'lectures': lectures,  # Pass all lectures related to the chapter.
        'current_lecture': current_lecture,  # Pass the current lecture.
        'previous_lecture': previous_lecture,  # Pass the previous lecture (if any).
        'next_lecture': next_lecture,  # Pass the next lecture (if any).
        'quiz': quiz  # Pass the quiz related to the chapter (if any).
    })


# --------------------------------------lecture content---------------------------------------




def lecture_content(request, lecture_id):
    # Fetch the lecture by its ID. If not found, raise a 404 error.
    lecture = get_object_or_404(Lecture, id=lecture_id)
    
    # Retrieve the chapter related to the lecture.
    chapter = lecture.chapter  # 🔹 chapter object
    
    # Get the title of the chapter.
    chapter_title = chapter.title  # 🔹 title string

    # Attempt to fetch the previous lecture in the order.
    try:
        previous_lecture = lecture.get_previous_by_order()  # Try to get the previous lecture.
    except Lecture.DoesNotExist:
        previous_lecture = None  # If no previous lecture, set to None.

    # Attempt to fetch the next lecture in the order.
    try:
        next_lecture = lecture.get_next_by_order()  # Try to get the next lecture.
    except Lecture.DoesNotExist:
        next_lecture = None  # If no next lecture, set to None.

    # Render the lecture_content template, passing necessary context data.
    return render(request, 'lecture_content.html', {
        'lecture': lecture,  # The current lecture object.
        'chapter': chapter,  # The chapter associated with the lecture.
        'chapter_title': chapter_title,  # The title of the chapter.
        'previous_lecture': previous_lecture,  # The previous lecture (if any).
        'next_lecture': next_lecture,  # The next lecture (if any).
    })


# --------------------------------------lecture detail---------------------------------------




def lecture_detail(request, lecture_id):
    # Fetch the lecture by its ID. If the lecture doesn't exist, it raises a 404 error.
    lecture = get_object_or_404(Lecture, id=lecture_id)
    
    # Debugging section: Print out all lectures in the chapter, ordered by 'order'
    print("All lectures in chapter:")
    for l in lecture.chapter.lectures.order_by('order'):  # Loop through all lectures in the same chapter
        print(f"  {l.order}: {l.title}")  # Print each lecture's order and title
    
    # Debugging: Print the previous lecture based on the order.
    print("\nPrevious query results:")
    print(lecture.get_previous_by_order())  # Get and print the previous lecture by order.
    
    # Debugging: Print the next lecture based on the order.
    print("\nNext query results:")
    print(lecture.get_next_by_order())  # Get and print the next lecture by order.
    
    # Render the template with the lecture details and navigation.
    return render(request, 'lecture_content.html', {
        'lecture': lecture,  # Pass the current lecture to the template.
        'previous_lecture': lecture.get_previous_by_order(),  # Pass the previous lecture (if exists).
        'next_lecture': lecture.get_next_by_order(),  # Pass the next lecture (if exists).
        'all_lectures': lecture.chapter.lectures.order_by('order'),  # Pass all lectures in the chapter, ordered by 'order'.
    })



# ---------------------------------quiz page--------------------------------------------
import json
from django.shortcuts import render, get_object_or_404
from .models import Quiz

def quiz_page(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    chapter = quiz.chapter
    course = chapter.course
    questions = quiz.questions.all()

    # JSON data for JavaScript
    questions_data = [
        {
"question": q.question_text,
            "option_a": q.option_a,
            "option_b": q.option_b,
            "option_c": q.option_c,
            "option_d": q.option_d,
            "answer": q.correct_answer
        }
        for q in questions
    ]

    return render(request, 'quiz_page.html', {
        'quiz': quiz,
        'chapter': chapter,
        'course': course,
        'questions_json': json.dumps(questions_data),
    })








# ------------------------------project detail -----------------------------------





def project_detail(request, project_id):
    # Fetch the project based on the provided project_id. 
    # It uses prefetch_related to optimize fetching related 'requirements' for the project in a single query.
    project = get_object_or_404(Project.objects.prefetch_related('requirements'), id=project_id)
    
    # Prepare the context to pass to the template. Here, we're passing the project object.
    context = {
        'project': project,  # Pass the project object to the template
    }
    
    # Render the 'project.html' template, passing the context with the project data.
    return render(request, 'projects/project.html', context)




from django.db.models import Count, Q, F, FloatField, ExpressionWrapper, Case, When, Value, Sum
from django.db.models.functions import Now
from django.utils import timezone
from datetime import timedelta
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

from alignskills.models import Course,UserStats

from django.db.models import Count, Q, F, FloatField, ExpressionWrapper, Case, When, Value
from django.db.models.functions import Now
from django.utils import timezone
from datetime import timedelta

def enrollment_report_pdf(request):
    now = timezone.now()
    last_month = now - timedelta(days=30)
    last_year = now - timedelta(days=365)

    report = Course.objects.annotate(
        total_enrollments=Count('enrollments', distinct=True),

        average_enrollment_per_month=ExpressionWrapper(
            Count('enrollments', distinct=True) / Case(
                When(created_at__isnull=False,
                     then=ExpressionWrapper((Now() - F('created_at')) / Value(30), output_field=FloatField())),
                default=Value(1),
                output_field=FloatField()
            ),
            output_field=FloatField()
        ),

        project_requirements_count=Count('project__requirements', distinct=True),
        comments_count=Count('comment', distinct=True),

        revenue=ExpressionWrapper(
            Count('enrollments', distinct=True) * F('price'),
            output_field=FloatField()
        )
    ).values(
        'title',
        'total_enrollments',
        'average_enrollment_per_month',
        'project_requirements_count',
        'comments_count',
        'revenue'
    )

    # overall totals
    total_courses = Course.objects.count()
    total_enrollments = Course.objects.aggregate(total=Count('enrollments'))['total'] or 0
    total_comments = Course.objects.aggregate(total=Count('comment'))['total'] or 0

    # یہاں active_students calculate کریں
    from alignskills.models import Enrollment  # فرض کریں Enrollment کا ماڈل ہے

    active_students = UserStats.objects.filter(
    is_active=True
).count()



    context = {
        'report': report,
        'total_courses': total_courses,
        'total_enrollments': total_enrollments,
        'total_comments': total_comments,
        'active_students': active_students,  # یہ بھی پاس کریں
    }

    template = get_template("report.html")
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation failed', status=500)
    return response











