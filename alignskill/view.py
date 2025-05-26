from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from alignskills.models import Course, Enrollment, Comment

# 🧠 Chatbot page
def chatbot_page(request):
    return render(request, "include/chatbot.html")

# 🏠 Home page
def homePage(request):
    return render(request, 'home.html', {'user_logged_in': request.user.is_authenticated})

# ℹ️ About us page
def aboutus(request):
    return render(request, 'about.html')

# 👤 Profile page (edit profile)
def edit_profile(request):
    return render(request, 'profile.html')  # fixed the space in file name

# 🧑‍🎓 Student panel main page
def studentPanel(request):
    return render(request, 'student-panel.html')

# 🔍 Search courses
def search(request):
    query = request.GET.get('search_box', '')
    return render(request, 'search_results.html', {'query': query})

# 📚 All courses page
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})



# 📊 Student dashboard with enrolled course count
@login_required
def student_dashboard(request):
    enrolled_courses_count = Enrollment.objects.filter(student=request.user).count()
    return render(request, 'student-panel/dashboard.html', {
        'enrolled_courses_count': enrolled_courses_count
    })

# 📞 Contact us (alt version)
def contactus(request):
    return render(request, 'contact.html')

# 📄 Resume Builder main page
def resumeBulider(request):
    return render(request, 'resume_main_page.html')

# 🎨 Resume template selector
def chooseTemplate(request):
    return render(request, "choose_template.html")

# Resume templates (🧾 Different styles)
def modernResumeTemplate(request):
    return render(request, "resumeTemplates/modern_template.html")

def classicResumeTemplate(request):
    return render(request, "resumeTemplates/classic_resume_template.html")

def creativeResumeTemplate(request):
    return render(request, "resumeTemplates/creative_resume_template.html")

def professionalResumeTemplate(request):
    return render(request, "resumeTemplates/professional_resume_template.html")

def ElegantResumeTemplate(request):
    return render(request, "resumeTemplates/Elegant_resume_template.html")

def minimalResumeTemplate(request):
    return render(request, "resumeTemplates/minimal_resume_template.html")

def boldResumeTemplate(request):
    return render(request, "resumeTemplates/bold_resume_template.html")

def modernlightResumeTemplate(request):
    return render(request, "resumeTemplates/modern_light_template.html")

def arthticResumeTemplate(request):
    return render(request, "resumeTemplates/arthtic_resume_template.html")

def techieResumeTemplate(request):
    return render(request, "resumeTemplates/techie_resume_template.html")

# 📜 Certificate page (static if not dynamic)
def certificate(request):
    return render(request, 'certificate.html')




















from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.shortcuts import render

# Custom Password Reset View
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('password_reset_done')  # URL after successful reset request
