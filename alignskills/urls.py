from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import home, user_stats_view

urlpatterns = [
    # ✅ Home Page
    path('', user_stats_view, name='home'),  # یا views.home, اگر یہی homepage 
 # ✅ Course Detail Pages
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/Python/<int:course_id>/', views.course_detail, name='Python_course'),
    path('course/javascript/<int:course_id>/', views.course_detail, name='js_course'),

    # ✅ Social Auth
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('report/', views.enrollment_report_pdf, name='report'),




    # ✅ User Authentication
    path('login-signup/', views.signup, name='user_login'),  # Custom sign-up + login
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # ✅ Alternatively, use Django built-in login/logout views
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

  path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    path('resume-main-page/', views.resume_main_page, name='resume_main_page'),
    path('search/', views.search, name='search'),
    path('about-us/', views.aboutus, name='about-us'),
    path('contact-us/', views.contactus, name='contact-us'),
    path('student-panel/', views.student_panel, name='student-panel'),
    path('profile/', views.profile, name='profile'),
    path('enroll/<int:course_id>/', views.enroll_in_course, name='enroll_course'),
    path('account-menu/', views.account_menu, name='account_menu'),
]
