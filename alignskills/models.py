# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone


# ----------------------------- #
# 1. Custom User Model
# ----------------------------- #

class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)
    student_number = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def set_username(self, new_username):
        """Custom method to validate and set username"""
        if not new_username:
            raise ValidationError("Username cannot be empty")

        if CustomUser.objects.exclude(pk=self.pk).filter(username=new_username).exists():
            raise ValidationError("This username is already taken")

        if len(new_username) > 150:
            raise ValidationError("Username is too long (max 150 characters)")

        self.username = new_username
        self.save()

# ----------------------------- #
# 2. Course Model
# ----------------------------- #

class Course(models.Model):
    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=255, default="untitled")
    description = models.TextField()
    price = models.CharField(max_length=50, default="Free Of Cost")
    project_info = models.TextField(default="Hands-on project at the end of the course")
    certificate_info = models.TextField(default="Certificate will be provided")
    image = models.ImageField(upload_to='course_images/')
    course_link = models.URLField()

    created_at = models.DateTimeField(default=timezone.now)  # ✅ added
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.title

# ----------------------------- #
# 3. FAQ Model (Course Specific)
# ----------------------------- #

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

# ----------------------------- #
# 4. User Stats Model (Progress Tracking)
# ----------------------------- #

class UserStats(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_graduate = models.BooleanField(default=False)
    is_certified = models.BooleanField(default=False)
    is_enrolled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s stats"

# ----------------------------- #
# 5. Banner Model (Course Promotions)
# ----------------------------- #

class Banner(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='banners/', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Banner for {self.course.title if self.course else 'No Course'}"

# ----------------------------- #
# 6. Chapter Model
# ----------------------------- #

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='chapter_images/', null=True, blank=True)
    position = models.PositiveIntegerField(default=0)  # for ordering

    def __str__(self):
        return f"{self.title} ({self.course.title})"

    class Meta:
        ordering = ['position']

# ----------------------------- #
# 7. Lecture Model
# ----------------------------- #

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    chapter = models.ForeignKey(Chapter, related_name='lectures', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

    # Navigation helpers
    def get_previous_by_order(self):
        return Lecture.objects.filter(
            chapter=self.chapter,
            order__lt=self.order
        ).order_by('-order').first()

    def get_next_by_order(self):
        return Lecture.objects.filter(
            chapter=self.chapter,
            order__gt=self.order
        ).order_by('order').first()

# ----------------------------- #
# 8. Lecture Content Model
# ----------------------------- #

class LectureContent(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('heading1', 'Main Heading (h1)'),
        ('heading2', 'Sub Heading (h2)'),
        ('heading3', 'Sub-sub Heading (h3)'),
        ('paragraph', 'Paragraph'),
        ('list', 'List'),
    ]

    lecture = models.ForeignKey(Lecture, related_name='contents', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    text = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_content_type_display()} for {self.lecture.title}"

# ----------------------------- #
# 9. Quiz & Question Models
# ----------------------------- #

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True, default=2)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.question_text

# ----------------------------- #
# 10. Project & ProjectRequirement Models
# ----------------------------- #

class Project(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='project')
    project_name = models.CharField(max_length=255, default='name')
    title = models.CharField(max_length=255, default='same as the course title')
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    link_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class ProjectRequirement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='requirements', null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    example_links = models.TextField(blank=True, help_text="Enter links as HTML anchor tags")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.project}"


from django.db import models
from django.conf import settings
from django.utils import timezone

# ----------------------------- #
# 1. Enrollment Model
# ----------------------------- #

class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE , related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.email} enrolled in {self.course.title}"

    @classmethod
    def enroll_student(cls, student, course):
        """Enroll a student in a course if not already enrolled."""
        enrollment, created = cls.objects.get_or_create(student=student, course=course)
        return created  # Returns True if a new enrollment was created

# ----------------------------- #
# 2. Course Comment Model
# ----------------------------- #

class Comment(models.Model):
    message = models.TextField('Message')
    date_comment = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Course Comment'
        verbose_name_plural = 'Course Comments'

    def __str__(self):
        if self.course:
            return f"Comment by {self.user.username} on {self.course.title}"
        return f"Comment by {self.user.username} (no course assigned)"

# ----------------------------- #
# 3. Contact Message Model
# ----------------------------- #

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

# ----------------------------- #
# 4. About Page Comment Model
# ----------------------------- #

class Comment_about_page(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    rating = models.FloatField(default=5.0)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", default="default.jpg")

    def __str__(self):
        return f"{self.user.username}: {self.text[:50]}"

# ----------------------------- #
# 5. Project Submission Model
# ----------------------------- #

class ProjectSubmission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    CATEGORY_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('IT', 'Information Technology'),
        ('DB', 'Database'),
        ('js', 'JavaScript'),
        ('py', 'Python'),
        ('ccn', 'Computer Network'),
    ]

    student_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_file = models.FileField(upload_to='projects/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='AI')
    course_title = models.ForeignKey('Course', default=1, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.get_status_display()}"

# ----------------------------- #
# 6. Student Model
# ----------------------------- #

class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('graduate', 'Graduate'),
    ]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    certified = models.BooleanField(default=False)
    certification_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

# ----------------------------- #
# 7. Newsletter Subscriber
# ----------------------------- #

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

