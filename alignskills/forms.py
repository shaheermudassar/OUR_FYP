# Importing Django's built-in UserCreationForm to extend for custom user creation
from django.contrib.auth.forms import UserCreationForm

# Importing custom models: CustomUser, ContactMessage, and NewsletterSubscriber
from alignskills.models import CustomUser, ContactMessage, NewsletterSubscriber

# Getting the currently set user model (can be CustomUser or default User)
from django.contrib.auth import get_user_model

# Importing Django's forms module to define form fields
from django import forms

# Importing built-in password change form
from django.contrib.auth.forms import PasswordChangeForm

# Assign the custom user model to 'User' for reuse
User = get_user_model()







# -------------------------------
# Custom password change form using built-in PasswordChangeForm
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User  # Model to associate form with
        fields = ['new_password1', 'new_password2']  # Fields to show in the form







# -------------------------------
# Form for user registration using the custom user model
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ['username', 'email', 'password1', 'password2']  # Fields shown in signup









# -------------------------------
# Contact form for "Contact Us" page
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage  # Model linked to this form
        fields = ['name', 'email', 'subject', 'message']  # Fields to collect from user











# -------------------------------
# Project submission form
from .models import ProjectSubmission, Course  # Import models related to project submissions

class ProjectSubmissionForm(forms.ModelForm):
    class Meta:
        model = ProjectSubmission  # Connect this form to the ProjectSubmission model
        fields = ['project_file', 'course_title']  # Fields shown in the form
    
    # Customizing form behavior after it's initialized
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate course dropdown with all available courses
        self.fields['course_title'].queryset = Course.objects.all()
        # Add CSS class to course_title field for Bootstrap styling
        self.fields['course_title'].widget.attrs.update({'class': 'form-control'})
        # Restrict accepted file types for project upload
        self.fields['project_file'].widget.attrs.update({'accept': '.zip,.rar,.pdf,.docx'})

    # Custom validation for course_title field
    def clean_course_title(self):
        course_title = self.cleaned_data.get('course_title')
        if not course_title:
            raise forms.ValidationError("Please select a course title.")  # Raise error if empty
        return course_title  # Return valid data

    # Custom validation for uploaded file (can be extended later)
    def clean_project_file(self):
        file = self.cleaned_data.get('project_file')
        return file  # Just returns the file (you can add size/type checks if needed)









# -------------------------------
# Re-defined CustomPasswordChangeForm with custom validation for new password
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    # Custom password validation function
    def clean_new_password(self):
        password = self.cleaned_data.get("new_password")  # Get new password from form input
        
        # Enforce minimum password length
        if len(password) < 8:
            raise forms.ValidationError("This password is too short. It must contain at least 8 characters.")
        
        return password  # Return the valid password












# -------------------------------
# Comment form for adding course comments
from alignskills.models import Comment  # Import Comment model

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Connect to Comment model
        fields = ['message']  # Only allow editing the message field
        widgets = {
            'message': forms.Textarea(attrs={  # Use a textarea for message input
                'class': 'form-control',  # Bootstrap class for styling
                'rows': 3,  # Show 3 rows in the text box
                'placeholder': 'Share your thoughts about this course...',  # Placeholder text
                'maxlength': '500'  # Max character limit (frontend only)
            })
        }
        labels = {

            'message': 'Your Comment'  # Label for the message field
        }









# -------------------------------
# Newsletter subscription form
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber  # Connect to the NewsletterSubscriber model
        fields = ['email']  # Only ask for email
