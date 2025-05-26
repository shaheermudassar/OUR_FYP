# Import Django's built-in admin interface
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Import your custom models from the current app
from .models import CustomUser, Course, Enrollment, Comment, ContactMessage, Comment_about_page, \
    ProjectSubmission, FAQ, Student, Chapter, Lecture, UserStats, NewsletterSubscriber, LectureContent





# Customize admin panel for CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser  # Specify the model
    list_display = ('username', 'email', 'is_staff', 'is_active')  # Columns to show in the list view

# Register the customized CustomUser admin
admin.site.register(CustomUser, CustomUserAdmin)

# Register the Course model directly (default admin interface)
admin.site.register(Course)





# Customize the admin for Enrollment model
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')  # Display these fields in the admin list
    search_fields = ('student__email', 'course__title')  # Enable searching by related fields

# Register the customized Enrollment admin
admin.site.register(Enrollment, EnrollmentAdmin)






# Customize the admin for FAQ model
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'course', 'created_at')  # Display these fields
    list_filter = ('course', 'created_at')  # Add filters by course and creation time

# Register the customized FAQ admin
admin.site.register(FAQ, FAQAdmin)






# Customize the admin for Student model
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'certified')  # Show student's name, status, and certification
    list_filter = ('status', 'certified')  # Add filters
    search_fields = ('name',)  # Search by student name

# Register the customized Student admin
admin.site.register(Student, StudentAdmin)







# Import Banner model (separately placed here)
from .models import Banner

# Customize admin for Banner model
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'alt_text')  # Display image and its alt text

# Register Banner with admin site
admin.site.register(Banner, BannerAdmin)













# Import quiz models
from .models import Quiz, Question

# Inline question model inside quiz (adds questions directly while editing quiz)
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Show 1 empty row by default







# Customize admin for Quiz with inline questions
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Register Quiz with custom admin
admin.site.register(Quiz, QuizAdmin)







# Customize Project model
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('course',)
    search_fields = ('title', 'description')









# Import ProjectRequirement and Project models
from alignskills.models import ProjectRequirement, Project

# Customize admin for ProjectRequirement
class ProjectRequirementAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'order', 'is_active')  # Show these columns
    list_editable = ('order', 'is_active')  # Make order and is_active editable in list
    list_filter = ('project', 'is_active')  # Add filters
    search_fields = ('title', 'description', 'project__project_name')  # Search using related project field

# Register ProjectRequirement and Project models
admin.site.register(ProjectRequirement, ProjectRequirementAdmin)
admin.site.register(Project)









# Admin for Chapter model
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'description')  # Columns to show
    list_filter = ('course',)  # Filter by course
    search_fields = ('title', 'description')  # Enable search
    raw_id_fields = ('course',)  # Use raw ID input for course







# Customize Lecture and its nested content
from .models import Lecture, LectureContent
# Inline LectureContent inside Lecture
class LectureContentInline(admin.TabularInline):
    model = LectureContent
    extra = 1  # One extra empty form by default
    fields = ('order', 'content_type', 'text')  # Fields to show inline
    ordering = ('order',)

# Admin for Lecture model
@admin.register(Lecture)






class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'order')  # Show these columns
    list_filter = ('chapter',)  # Add chapter filter
    inlines = [LectureContentInline]  # Attach inline content editor
    ordering = ('chapter', 'order')  # Order by chapter then order

# Admin for LectureContent model
@admin.register(LectureContent)









class LectureContentAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'content_type', 'order')  # Show these columns
    list_filter = ('lecture', 'content_type')  # Add filters
    ordering = ('lecture', 'order')  # Order results







# Customize UserStats admin panel
class UserStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'is_graduate', 'is_certified', 'created_at')
    list_filter = ('is_active', 'is_graduate', 'is_certified')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')  # These fields cannot be edited
    list_per_page = 20  # Pagination size

# Register UserStats admin
admin.site.register(UserStats, UserStatsAdmin)





# Customize Comment admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'truncated_message', 'date_comment')  # Display short message
    list_filter = ('course', 'user', 'date_comment')  # Filters
    search_fields = ('message', 'user__username', 'course__title')  # Search fields

    def truncated_message(self, obj):
        # Show only first 50 characters of message
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message

    truncated_message.short_description = 'Message'  # Column header

# Register Comment admin
admin.site.register(Comment, CommentAdmin)

# Register Comment_about_page model (default admin)
admin.site.register(Comment_about_page)









# Customize ContactMessage admin using decorator
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')  # Display these columns
    search_fields = ('name', 'email', 'subject', 'message')  # Search by these fields










# Customize ProjectSubmission admin
class ProjectSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'status', 'submitted_at')
    list_filter = ('status',)  # Filter by submission status
    actions = ['approve_projects', 'reject_projects']  # Add custom actions

    # Custom action to approve selected projects
    def approve_projects(self, request, queryset):
        queryset.update(status='approved')
        self.message_user(request, "Selected projects have been approved.")

    # Custom action to reject selected projects
    def reject_projects(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, "Selected projects have been rejected.")

    # Short descriptions for admin actions
    approve_projects.short_description = "Approve selected projects"
    reject_projects.short_description = "Reject selected projects"

# Register customized ProjectSubmission admin
admin.site.register(ProjectSubmission, ProjectSubmissionAdmin)











# Customize NewsletterSubscriber admin
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')  # Show email and subscription time
    search_fields = ('email',)  # Search by email
    ordering = ('-subscribed_at',)  # Show latest subscribers first
