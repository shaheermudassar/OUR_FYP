from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from alignskills.forms import CustomUserCreationForm, ContactMessageForm, ProjectSubmissionForm
from alignskills.models import CustomUser, ContactMessage, ProjectSubmission

class FormTests(TestCase):

    def test_custom_user_creation_form_valid(self):
        # Test for a valid form submission
     form_data = {
      'username': 'testuser',
      'email': 'testuser@example.com',
      'password1': 'MyStrongP@ssw0rd123',
      'password2': 'MyStrongP@ssw0rd123'
     }
     form = CustomUserCreationForm(data=form_data)
     if not form.is_valid():
          print(form.errors)

    def test_custom_user_creation_form_invalid(self):
        # Test for invalid form (password mismatch)
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password124'  # Passwords don't match
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Password mismatch error

    def test_contact_message_form_valid(self):
        # Test for a valid contact message form
        form_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message.'
        }
        form = ContactMessageForm(data=form_data)
        self.assertTrue(form.is_valid())

 
    def test_project_submission_form_valid(self):
    # Create a dummy file for testing
     test_file = SimpleUploadedFile("test_project.txt", b"file content")
    
    # Use the file in the form data
     form_data = {'project_file': test_file}
     form = ProjectSubmissionForm(data=form_data)
     if not form.is_valid():
        print(form.errors)  # Print the errors for debugging
     self.assertTrue(form.is_valid())
    def test_project_submission_form_invalid(self):
        # Test for invalid project submission (missing file)
        form_data = {}
        form = ProjectSubmissionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # File field is required

