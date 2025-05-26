from django.test import TestCase
from django.contrib.auth import get_user_model
from alignskills.models import Course, ContactMessage, Comment_about_page, ProjectSubmission,Student,BasicInfo
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from datetime import date


CustomUser = get_user_model()

# ----------------- CustomUser Tests -------------------
class CustomModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email="test@example.com",
            username="test_jhon",
            password="testpassword",
            student_number="12345",
            education="BSIT",
            skills="IT consultant",
            experience="none",
            phone="12345678912",
            address="234q block 345",
            links="https://www.youtube.com/watch?v=f_xiy70g6_0&t=1378s",
            email_verified=True
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "test_jhon")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.student_number, "12345")
        self.assertEqual(self.user.phone, "12345678912")
        self.assertEqual(self.user.skills, "IT consultant")
        self.assertTrue(self.user.email_verified)

    def test_str_method(self):
        self.assertEqual(str(self.user), self.user.username)

    def test_user_is_active_by_default(self):
        self.assertTrue(self.user.is_active)

    def test_user_permissions_fields(self):
        self.assertTrue(hasattr(self.user, "user_permissions"))
        self.assertTrue(hasattr(self.user, "groups"))

# ----------------- Course Model Tests -------------------
class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Operating_system_course",
            short_title="os",
            description="this is well knwn course to improve your skills",
            price="free of cost",
            project_info="Hands-on project at the end of the course",
            certificate_info="certificate will be provided",
            course_link="https://www.youtube.com/watch?v=f_xiy70g6_0&t=1378s",
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, "Operating_system_course")
        self.assertEqual(self.course.short_title, "os")
        self.assertEqual(self.course.description, "this is well knwn course to improve your skills")
        self.assertEqual(self.course.price, "free of cost")
        self.assertEqual(self.course.project_info, "Hands-on project at the end of the course")
        self.assertEqual(self.course.certificate_info, "certificate will be provided")
        self.assertEqual(self.course.course_link, "https://www.youtube.com/watch?v=f_xiy70g6_0&t=1378s")

    def test_str_method(self):
        self.assertEqual(str(self.course), "Operating_system_course")

# ----------------- ContactMessage Tests -------------------
class ContactMessageTestModel(TestCase):
    def setUp(self):
        self.contactmessage = ContactMessage.objects.create(
            name="test_user",
            email="test@example.com",
            subject="About alignskills",
            message="is the courses free"
        )

    def test_contactMessage_creation(self):
        self.assertEqual(self.contactmessage.name, "test_user")
        self.assertEqual(self.contactmessage.email, "test@example.com")
        self.assertEqual(self.contactmessage.subject, "About alignskills")
        self.assertEqual(self.contactmessage.message, "is the courses free")

    def test_created_at_timestamp(self):
        self.assertLessEqual(self.contactmessage.created_at, timezone.now())

    def test_str_method(self):
        self.assertEqual(str(self.contactmessage), "test_user - About alignskills")

# ----------------- Comment_about_page Tests -------------------
class CommentAboutPageTestModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="johndoe",
            email="john@example.com",
            password="password123"
        )
        self.comment = Comment_about_page.objects.create(
            user=self.user,
            text="I love alignskill",
            rating=5.0
        )

    def test_CommentAboutPage_creation(self):
        self.assertEqual(self.comment.user.username, "johndoe")
        self.assertEqual(self.comment.text, "I love alignskill")
        self.assertEqual(self.comment.rating, 5.0)
        self.assertTrue(self.comment.created_at)

    def test_created_at_timestamp(self):  # fixed method name + instance reference
        self.assertLessEqual(self.comment.created_at, timezone.now())

    def test_str_method(self):
        self.assertEqual(str(self.comment), f"{self.user.username}:{self.comment.text[:50]}")

# ----------------- ProjectSubmission Tests -------------------
class ProjectSubmissionTestModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="ammar",
            email="ammar@example.com",
            password="securepass"
        )
        self.project_file = SimpleUploadedFile("project.txt", b"project content")
        self.submission = ProjectSubmission.objects.create(
            student_name=self.user,
            project_file=self.project_file,
            category="AI",
            status="approved"
        )

    def test_ProjectSubmission_creation(self):
        self.assertEqual(self.submission.student_name.username, "ammar")
        self.assertEqual(self.submission.category, "AI")
        self.assertEqual(self.submission.status, "approved")

    def test_submitted_at_timestamp(self):
        self.assertLessEqual(self.submission.submitted_at, timezone.now())

    def test_str_method(self):
        self.assertEqual(str(self.submission), "ammar - Approved")
# ----------------- student Tests -------------------

class StudentModelTest(TestCase):

    def test_create_student(self):
        student = Student.objects.create(name="Ali")
        self.assertEqual(student.name, "Ali")
        self.assertEqual(student.status, "active")
        self.assertFalse(student.certified)
        self.assertIsNone(student.certification_date)

    def test_str_method(self):
        student = Student.objects.create(name="Zara")
        self.assertEqual(str(student), "Zara")

    def test_status_choices(self):
        student = Student.objects.create(name="Sara", status="graduate")
        self.assertEqual(student.status, "graduate")

    def test_certification_date_set(self):
        today = date.today()
        student = Student.objects.create(
            name="Ahmed", 
            certified=True, 
            certification_date=today
        )
        self.assertTrue(student.certified)
        self.assertEqual(student.certification_date, today)




# ----------------- basic info Tests -------------------
User = get_user_model()

class BasicInfoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_basic_info(self):
        basic_info = BasicInfo.objects.create(
            user=self.user,
            name="Ali",
            email="ali@example.com",
            nationality="Pakistani",
            phone="03001234567",
            language="Urdu"
        )
        self.assertEqual(basic_info.name, "Ali")
        self.assertEqual(basic_info.email, "ali@example.com")
        self.assertEqual(str(basic_info), "Ali")
        self.assertEqual(basic_info.user.username, "testuser")

    def test_email_uniqueness(self):
        BasicInfo.objects.create(
            user=self.user,
            name="Ali",
            email="ali@example.com",
            nationality="Pakistani",
            phone="03001234567",
            language="Urdu"
        )

        with self.assertRaises(Exception):
            # Create a second user with same email
            user2 = User.objects.create_user(username='seconduser', password='pass')
            BasicInfo.objects.create(
                user=user2,
                name="Zara",
                email="ali@example.com",  # same email
                nationality="Pakistani",
                phone="03009876543",
                language="Punjabi"
            )
