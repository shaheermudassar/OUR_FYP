from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import view
from alignskills import views
from alignskills.views import (
    student_panel, enroll_in_course, ai_chat, contact_us_page, get_comments, 
    course_detail, search_courses, student_projects, ajax_subscribe_newsletter
)

admin.site.site_header = "Alignskill"
admin.site.site_title = "Alignskill"
admin.site.index_title = "Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alignskills.urls')),  # Include app-level URLs
    path('', view.homePage),  # Homepage
    path("create-admin/", views.create_admin),



    # General pages
    path('about-us', view.aboutus, name='about_us'),
    path('contact/', contact_us_page, name='contact'),
    path('contact-us', view.contactus, name='contact-us'),

    # Courses
    path('courses', view.courses, name='courses'),
    path('courses/<int:course_id>/', course_detail, name='course_detail'),
    path('search/', search_courses, name='search_courses'),
    path("get_comments/", get_comments, name="get_comments"),

    # Enrollment
    path('enroll/<int:course_id>/', enroll_in_course, name='enroll_in_course'),
    path('enroll/<str:course_title>/', views.enroll_page, name='enroll_page'),
    path('enroll-course-pages/<int:course_id>/', views.course_enrollment, name='course_enrollment'),

    # Authentication and user
    path('registration/', include('alignskills.urls')),
    path('registration/login-signup/', include('allauth.urls')),
    path('profile/', view.edit_profile, name='edit_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile_api'),
    path('change-password/', views.change_password, name='change_password'),

    # Dashboard
    path('dashboard/', views.dashboard_courses, name='dashboard_courses'),
    path('dashboard-comments/', views.dashboard_comments, name='dashboard_comments'),

    # Student Panel & Projects
    path('student-panel/', student_panel, name='student_panel'),
    path('student-projects/', student_projects, name='student_projects'),
    path('submit_project/<int:project_id>/', views.submit_project, name='submit_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),

    # Resume Builder
    path('resume-main-page', view.resumeBulider, name='resume-main-page'),
    path('choose_template', view.chooseTemplate, name='choose_template'),
    path('resumeTemplates/modern_template', view.modernResumeTemplate, name='modern_template'),
    path('resumeTemplates/classic_resume_template', view.classicResumeTemplate, name='classic_resume_template'),
    path('resumeTemplates/creative_resume_template', view.creativeResumeTemplate, name='creative_resume_template'),
    path('resumeTemplates/professional_resume_template', view.professionalResumeTemplate, name='professional_resume_template'),
    path('resumeTemplates/Elegant_resume_template', view.ElegantResumeTemplate, name='Elegant_resume_template'),
    path('resumeTemplates/minimal_resume_template', view.minimalResumeTemplate, name='minimal_resume_template'),
    path('resumeTemplates/modern_light_template', view.modernlightResumeTemplate, name='modern_light_template'),
    path('resumeTemplates/bold_resume_template', view.boldResumeTemplate, name='bold_resume_template'),
    path('resumeTemplates/arthtic_resume_template', view.arthticResumeTemplate, name='arthtic_resume_template'),
    path('resumeTemplates/techie_resume_template', view.techieResumeTemplate, name='techie_resume_template'),

    # AI Chat and Assistant
    path("ai-chat/", ai_chat, name="ai_chat"),
    path("chatbot/", view.chatbot_page, name="chatbot"),

    # Lectures and Quizzes
    path('chapter/<str:chapter_title>/', views.lecture_page, name='lecture_page'),
    path('lecture/<int:lecture_id>/content/', views.lecture_content, name='lecture_content'),
    path('course/<str:chapter_title>/', views.lecture_page, name='lecture_page'),
    path('course/<str:chapter_title>/lecture/<int:lecture_id>/', views.lecture_page, name='lecture_page_with_lecture'),
    path('course/<str:chapter_title>/quiz/', views.quiz_page, name='quiz_page'),
    path('quiz/<int:quiz_id>/', views.quiz_page, name='quiz_page'),

    # Course detail inside registration
    path('registration/course/<int:course_id>/<str:chapter_title>/', views.course_detail, name='course_detail'),

    # Certificate
    path('certificate/<str:course_title>/', views.view_certificate, name='view_certificate'),

    # Newsletter
    path('subscribe/', ajax_subscribe_newsletter, name='ajax_subscribe_newsletter'),







    path('password-reset/', view.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),









]

# Static & media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
