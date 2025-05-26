# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse,resolve
# from alignskills.views import get_comments ,ai_chat ,submit_AI_project,submit_DB_project,submit_IT_project,student_projects,course_detail,save_basic_info,ajax_subscribe_newsletter,courses
# from alignskill.view import chatbot_page,aboutus,studentPanel,courses ,contactus,enroll_DB_page,resumeBulider,chooseTemplate,minimalResumeTemplate,modernlightResumeTemplate,modernResumeTemplate,arthticResumeTemplate,boldResumeTemplate,techieResumeTemplate,classicResumeTemplate,ElegantResumeTemplate,creativeResumeTemplate,professionalResumeTemplate,chapter_detail_AI,chapter_detail_CCN,chapter_detail_DB,chapter_detail_IT,chapter_detail_js,chapter_detail_python,project_of_AI,project_of_CCN,project_of_DB,project_of_it,project_of_js,project_of_python,certificate,Python_Ch1_lec,Python_Ch2_lec,Python_Ch3_lec,Python_Ch4_lec,Python_Ch5_lec,Python_Ch6_lec,CCN_Ch1_lec1,CCN_Ch2_lec,CCN_Ch3_lec,CCN_Ch4_lec,CCN_Ch5_lec,CCN_Ch6_lec,CCN_Ch7_lec,CCN_Ch8_lec,AI_Ch1_lec,AI_Ch2_lec,AI_Ch3_lec,AI_Ch4_lec,AI_Ch5_lec,AI_Ch6_lec,IT_Ch1_lec,IT_Ch2_lec,IT_Ch3_lec,IT_Ch4_lec,IT_Ch5_lec,JS_Ch1_lec,JS_Ch3_lec,JS_Ch2_lec,JS_Ch4_lec,JS_Ch5_lec,JS_Ch6_lec

# CustomUser = get_user_model()

# class TestUrls(TestCase):
#     def setUp(self):
#         # Create a user and log them in
#         self.user = CustomUser.objects.create_user(username='testuser', password='password')
#         self.client.login(username='testuser', password='password')

    # def test_admin_panels_url(self):
    #     response = self.client.get('/admin-panels/')
    #     self.assertEqual(response.status_code, 200)
#     def test_home_page_url(self):
        
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200) 
        
#     def test_edit_profile_url(self):
#         # Test the edit profile URL
#         response = self.client.get('/profile/')
#         self.assertEqual(response.status_code, 200)  
#     def test_root_url_includes_alignskills_urls(self):
       
#         response = self.client.get('/')
      
#         self.assertEqual(response.status_code, 200)
#     def test_get_comments_url_resolves(self):
#         url = reverse('get_comments')
#         self.assertEqual(resolve(url).func, get_comments)
#     def test_ai_chat_url_resolves(self):
#         url = reverse('ai_chat')
#         self.assertEqual(resolve(url).func, ai_chat)

#     def test_chatbot_url_resolves(self):
#         url = reverse('chatbot')
#         self.assertEqual(resolve(url).func, chatbot_page)


#     def test_get_comments_url_resolves(self):
#         url = reverse('get_comments')
#         self.assertEqual(resolve(url).func, get_comments)

#     def test_submit_AI_project_url_resolves(self):
#         url = reverse('submit_AI_project')
#         self.assertEqual(resolve(url).func, submit_AI_project)

#     def test_submit_IT_project_url_resolves(self):
#         url = reverse('submit_IT_project')
#         self.assertEqual(resolve(url).func, submit_IT_project)

#     def test_submit_DB_project_url_resolves(self):
#         url = reverse('submit_DB_project')
#         self.assertEqual(resolve(url).func, submit_DB_project)
#     def test_student_projects_url_resolves(self):
#         url = reverse('student_projects') 
#         self.assertEqual(resolve(url).func, student_projects)

#     def test_course_detail_url_resolves(self):
#         url = reverse('course-detail', args=[1])  
#         self.assertEqual(resolve(url).func, course_detail)  

#     def test_save_basic_info_url_resolves(self):
#         url = reverse('save_basic_info')  
#         self.assertEqual(resolve(url).func, save_basic_info)  

#     def test_ajax_subscribe_newsletter_url_resolves(self):
#         url = reverse('ajax_subscribe_newsletter')  
#         self.assertEqual(resolve(url).func, ajax_subscribe_newsletter) 

#     def test_about_us_url_resolves(self):
#         url = reverse('about_us')  
#         self.assertEqual(resolve(url).func, aboutus)  

#     def test_student_panel_url_resolves(self):
#         url = reverse('student-panel')  
#         self.assertEqual(resolve(url).func, studentPanel)  

#     def test_courses_url_resolves(self):
#         url = reverse('courses')  
#         self.assertEqual(resolve(url).func, courses)  
#     
#     def test_contact_us_url_resolves(self):
#         url = reverse('contact-us')  
#         self.assertEqual(resolve(url).func, contactus) 
#     def test_resume_main_page_url_resolves(self):
#         url = reverse('resume-main-page') 
#         self.assertEqual(resolve(url).func, resumeBulider) 
#     def test_choose_template_url_resolves(self):
#         url = reverse('choose_template')  
#         self.assertEqual(resolve(url).func, chooseTemplate) 





#     def test_modern_template_url_resolves(self):
#         url = reverse('modern_template')
#         self.assertEqual(resolve(url).func, modernResumeTemplate)

#     def test_classic_resume_template_url_resolves(self):
#         url = reverse('classic_resume_template')
#         self.assertEqual(resolve(url).func, classicResumeTemplate)

#     def test_creative_resume_template_url_resolves(self):
#         url = reverse('creative_resume_template')
#         self.assertEqual(resolve(url).func, creativeResumeTemplate)

#     def test_professional_resume_template_url_resolves(self):
#         url = reverse('professional_resume_template')
#         self.assertEqual(resolve(url).func,professionalResumeTemplate)

#     def test_elegant_resume_template_url_resolves(self):
#         url = reverse('Elegant_resume_template')
#         self.assertEqual(resolve(url).func, ElegantResumeTemplate)

#     def test_minimal_resume_template_url_resolves(self):
#         url = reverse('minimal_resume_template')
#         self.assertEqual(resolve(url).func, minimalResumeTemplate)

#     def test_modern_light_template_url_resolves(self):
#         url = reverse('modern_light_template')
#         self.assertEqual(resolve(url).func, modernlightResumeTemplate)

#     def test_bold_resume_template_url_resolves(self):
#         url = reverse('bold_resume_template')
#         self.assertEqual(resolve(url).func, boldResumeTemplate)

#     def test_arthtic_resume_template_url_resolves(self):
#         url = reverse('arthtic_resume_template')
#         self.assertEqual(resolve(url).func, arthticResumeTemplate)

#     def test_techie_resume_template_url_resolves(self):
#         url = reverse('techie_resume_template')
#         self.assertEqual(resolve(url).func, techieResumeTemplate)
#     def test_chapter_detail_CCN_url_resolves(self):
#         url = reverse('chapter_detail_CCN')
#         self.assertEqual(resolve(url).func, chapter_detail_CCN)

#     def test_chapter_detail_IT_url_resolves(self):
#         url = reverse('chapter_detail_IT')
#         self.assertEqual(resolve(url).func, chapter_detail_IT)

#     def test_chapter_detail_AI_url_resolves(self):
#         url = reverse('chapter_detail_AI')
#         self.assertEqual(resolve(url).func, chapter_detail_AI)

#     def test_chapter_detail_DB_url_resolves(self):
#         url = reverse('chapter_detail_DB')
#         self.assertEqual(resolve(url).func, chapter_detail_DB)

#     def test_chapter_detail_js_url_resolves(self):
#         url = reverse('chapter_detail_js')
#         self.assertEqual(resolve(url).func, chapter_detail_js)

#     def test_chapter_detail_python_url_resolves(self):
#         url = reverse('chapter_detail_python')
#         self.assertEqual(resolve(url).func, chapter_detail_python)









#     def test_project_of_it_url_resolves(self):
#         url = reverse('project_of_it')
#         self.assertEqual(resolve(url).func, project_of_it)

#     def test_project_of_CCN_url_resolves(self):
#         url = reverse('project_of_CCN')
#         self.assertEqual(resolve(url).func, project_of_CCN)

#     def test_project_of_AI_url_resolves(self):
#         url = reverse('project_of_AI')
#         self.assertEqual(resolve(url).func, project_of_AI)

#     def test_project_of_DB_url_resolves(self):
#         url = reverse('project_of_DB')
#         self.assertEqual(resolve(url).func, project_of_DB)

#     def test_project_of_python_url_resolves(self):
#         url = reverse('project_of_python')
#         self.assertEqual(resolve(url).func, project_of_python)

#     def test_project_of_js_url_resolves(self):
#         url = reverse('project_of_js')
#         self.assertEqual(resolve(url).func, project_of_js)



#     def test_certificate_url_resolves(self):
#      url = reverse('certificate')
#      self.assertEqual(resolve(url).func, certificate)


# class TestUrls(TestCase):
#     def setUp(self):
#         # Create a user and log them in
#         self.user = CustomUser.objects.create_user(username='testuser', password='password')
#         self.client.login(username='testuser', password='password')

#     def test_python_ch1_lec_url_resolves(self):
#         url = reverse('python_ch1_lec')
#         self.assertEqual(resolve(url).func, Python_Ch1_lec)

#     def test_python_ch2_lec_url_resolves(self):
#         url = reverse('python_ch2_lec')
#         self.assertEqual(resolve(url).func,Python_Ch2_lec)

#     def test_python_ch3_lec_url_resolves(self):
#         url = reverse('python_ch3_lec')
#         self.assertEqual(resolve(url).func, Python_Ch3_lec)

#     def test_python_ch4_lec_url_resolves(self):
#         url = reverse('python_ch4_lec')
#         self.assertEqual(resolve(url).func, Python_Ch4_lec)

#     def test_python_ch5_lec_url_resolves(self):
#         url = reverse('python_ch5_lec')
#         self.assertEqual(resolve(url).func, Python_Ch5_lec)

#     def test_python_ch6_lec_url_resolves(self):
#         url = reverse('python_ch6_lec')
#         self.assertEqual(resolve(url).func, Python_Ch6_lec)
#     def test_CCN_Ch1_lec1_url_resolves(self):
#      url = reverse('CCN_Ch1_lec1')
#      self.assertEqual(resolve(url).func,CCN_Ch1_lec1)

#     def test_CCN_Ch2_lec_url_resolves(self):
#       url = reverse('CCN_Ch2_lec')
#       self.assertEqual(resolve(url).func,CCN_Ch2_lec)

#     def test_CCN_Ch3_lec_url_resolves(self):
#       url = reverse('CCN_Ch3_lec')
#       self.assertEqual(resolve(url).func,CCN_Ch3_lec)

#     def test_CCN_Ch4_lec_url_resolves(self):
#       url = reverse('CCN_Ch4_lec')
#       self.assertEqual(resolve(url).func,CCN_Ch4_lec)

#     def test_CCN_Ch5_lec_url_resolves(self):
#       url = reverse('CCN_Ch5_lec')
#       self.assertEqual(resolve(url).func,CCN_Ch5_lec)

#     def test_CCN_Ch6_lec_url_resolves(self):
#       url = reverse('CCN_Ch6_lec')
#       self.assertEqual(resolve(url).func,CCN_Ch6_lec)

#     def test_CCN_Ch7_lec_url_resolves(self):
#       url = reverse('CCN_Ch7_lec')
#       self.assertEqual(resolve(url).func ,CCN_Ch7_lec)

#     def test_CCN_Ch8_lec_url_resolves(self):
#       url = reverse('CCN_Ch8_lec')
#       self.assertEqual(resolve(url).func, CCN_Ch8_lec)




#     def test_AI_Ch1_lec_url_resolves(self):
#      url = reverse('AI_Ch1_lec')
#      self.assertEqual(resolve(url).func, AI_Ch1_lec)

#     def test_AI_Ch2_lec_url_resolves(self):
#      url = reverse('AI_Ch2_lec')
#      self.assertEqual(resolve(url).func, AI_Ch2_lec)

#     def test_AI_Ch3_lec_url_resolves(self):
#      url = reverse('AI_Ch3_lec')
#      self.assertEqual(resolve(url).func, AI_Ch3_lec)

#     def test_AI_Ch4_lec_url_resolves(self):
#      url = reverse('AI_Ch4_lec')
#      self.assertEqual(resolve(url).func, AI_Ch4_lec)

#     def test_AI_Ch5_lec_url_resolves(self):
#      url = reverse('AI_Ch5_lec')
#      self.assertEqual(resolve(url).func, AI_Ch5_lec)

#     def test_AI_Ch6_lec_url_resolves(self):
#      url = reverse('AI_Ch6_lec')
#      self.assertEqual(resolve(url).func, AI_Ch6_lec)



#     def test_JS_Ch1_lec_url_resolves(self):
#      url = reverse('JS_Ch1_lec')
#      self.assertEqual(resolve(url).func, JS_Ch1_lec)

#     def test_JS_Ch2_lec_url_resolves(self):
#      url = reverse('JS_Ch2_lec')
#      self.assertEqual(resolve(url).func, JS_Ch2_lec)

#     def test_JS_Ch3_lec_url_resolves(self):
#      url = reverse('JS_Ch3_lec')
#      self.assertEqual(resolve(url).func, JS_Ch3_lec)

#     def test_JS_Ch4_lec_url_resolves(self):
#      url = reverse('JS_Ch4_lec')
#      self.assertEqual(resolve(url).func, JS_Ch4_lec)

#     def test_JS_Ch5_lec_url_resolves(self):
#      url = reverse('JS_Ch5_lec')
#      self.assertEqual(resolve(url).func, JS_Ch5_lec)

#     def test_JS_Ch6_lec_url_resolves(self):
#      url = reverse('JS_Ch6_lec')
#      self.assertEqual(resolve(url).func, JS_Ch6_lec)


#     def test_IT_Ch1_lec_url_resolves(self):
#      url = reverse('IT_Ch1_lec')
#      self.assertEqual(resolve(url).func, IT_Ch1_lec)

#     def test_IT_Ch2_lec_url_resolves(self):
#      url = reverse('IT_Ch2_lec')
#      self.assertEqual(resolve(url).func, IT_Ch2_lec)

#     def test_IT_Ch3_lec_url_resolves(self):
#      url = reverse('IT_Ch3_lec')
#      self.assertEqual(resolve(url).func, IT_Ch3_lec)

#     def test_IT_Ch4_lec_url_resolves(self):
#      url = reverse('IT_Ch4_lec')
#      self.assertEqual(resolve(url).func, IT_Ch4_lec)

#     def test_IT_Ch5_lec_url_resolves(self):
#      url = reverse('IT_Ch5_lec')
#      self.assertEqual(resolve(url).func, IT_Ch5_lec)






# from django.test import TestCase, Client

# class AICourseURLTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.urls = [
#             # Chapter 1
#             'AI_course/chapter1_lectures/lecture1_page1.html',
#             'AI_course/chapter1_lectures/lecture1_page2.html',
#             'AI_course/chapter1_lectures/lecture2_page1.html',
#             'AI_course/chapter1_lectures/lecture2_page2.html',
#             'AI_course/chapter1_lectures/lecture3_page1.html',
#             'AI_course/chapter1_lectures/lecture3_page2.html',
#             'AI_course/chapter1_lectures/lecture4_page1.html',
#             'AI_course/chapter1_lectures/lecture5_page1.html',
#             'AI_course/chapter1_lectures/lecture5_page2.html',
#             'AI_course/chapter1_lectures/lecture6_page1.html',
#             'AI_course/chapter1_lectures/quiz.html',

#             # Chapter 2
#             'AI_course/chapter2_lectures/lecture1_page1.html',
#             'AI_course/chapter2_lectures/lecture2_page1.html',
#             'AI_course/chapter2_lectures/lecture3_page1.html',
#             'AI_course/chapter2_lectures/lecture4_page1.html',
#             'AI_course/chapter2_lectures/lecture5_page1.html',
#             'AI_course/chapter2_lectures/lecture6_page1.html',
#             'AI_course/chapter2_lectures/lecture7_page1.html',
#             'AI_course/chapter2_lectures/quiz.html',

#             # Chapter 3
#             'AI_course/chapter3_lectures/lecture1_page1.html',
#             'AI_course/chapter3_lectures/lecture2_page1.html',
#             'AI_course/chapter3_lectures/lecture3_page1.html',
#             'AI_course/chapter3_lectures/lecture3_page2.html',
#             'AI_course/chapter3_lectures/lecture4_page1.html',
#             'AI_course/chapter3_lectures/lecture4_page2.html',
#             'AI_course/chapter3_lectures/quiz.html',

#             # Chapter 4
#             'AI_course/chapter4_lectures/lecture1_page1.html',
#             'AI_course/chapter4_lectures/lecture2_page1.html',
#             'AI_course/chapter4_lectures/lecture3_page1.html',
#             'AI_course/chapter4_lectures/lecture3_page2.html',
#             'AI_course/chapter4_lectures/lecture4_page1.html',
#             'AI_course/chapter4_lectures/lecture5_page1.html',
#             'AI_course/chapter4_lectures/lecture6_page1.html',
#             'AI_course/chapter4_lectures/lecture7_page1.html',
#             'AI_course/chapter4_lectures/lecture8_page1.html',
#             'AI_course/chapter4_lectures/quiz.html',

#             # Chapter 5
#             'AI_course/chapter5_lectures/lecture1_page1.html',
#             'AI_course/chapter5_lectures/lecture2_page1.html',
#             'AI_course/chapter5_lectures/lecture3_page1.html',
#             'AI_course/chapter5_lectures/lecture4_page1.html',
#             'AI_course/chapter5_lectures/lecture4_page2.html',
#             'AI_course/chapter5_lectures/quiz.html',

#             # Chapter 6
#             'AI_course/chapter6_lectures/lecture1_page1.html',
#             'AI_course/chapter6_lectures/lecture2_page1.html',
#             'AI_course/chapter6_lectures/lecture3_page1.html',
#             'AI_course/chapter6_lectures/lecture3_page2.html',
#             'AI_course/chapter6_lectures/lecture4_page1.html',
#             'AI_course/chapter6_lectures/lecture5_page1.html',
#             'AI_course/chapter6_lectures/quiz.html',
#         ]

#     def test_ai_course_urls_return_200(self):
#         for url in self.urls:
#             with self.subTest(url=url):
#                 response = self.client.get(f'/{url}')
#                 self.assertEqual(response.status_code, 200, msg=f"Failed at {url}")

    

# class TestITCourseURLs(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.urls = [
#             # IT Chapter 1
#             'IT_course/chapter1_lectures/lecture1-page1.html',
#             'IT_course/chapter1_lectures/lecture1-page2.html',
#             'IT_course/chapter1_lectures/lecture2-page1.html',
#             'IT_course/chapter1_lectures/lecture2-page2.html',
#             'IT_course/chapter1_lectures/lecture3-page1.html',
#             'IT_course/chapter1_lectures/lecture3-page2.html',
#             'IT_course/chapter1_lectures/lecture3-page3.html',
#             'IT_course/chapter1_lectures/lecture4-page1.html',
#             'IT_course/chapter1_lectures/lecture4-page2.html',
#             'IT_course/chapter1_lectures/lecture4-page3.html',
#             'IT_course/chapter1_lectures/quiz.html',

#             # IT Chapter 2
#             'IT_course/chapter2_lectures/lecture1-page1.html',
#             'IT_course/chapter2_lectures/lecture1-page2.html',
#             'IT_course/chapter2_lectures/lecture2-page1.html',
#             'IT_course/chapter2_lectures/lecture2-page2.html',
#             'IT_course/chapter2_lectures/lecture2-page3.html',
#             'IT_course/chapter2_lectures/lecture2-page4.html',
#             'IT_course/chapter2_lectures/lecture2-page5.html',
#             'IT_course/chapter2_lectures/lecture3-page1.html',
#             'IT_course/chapter2_lectures/lecture3-page2.html',
#             'IT_course/chapter2_lectures/lecture4-page1.html',
#             'IT_course/chapter2_lectures/lecture4-page2.html',
#             'IT_course/chapter2_lectures/lecture4-page3.html',
#             'IT_course/chapter2_lectures/lecture5-page1.html',
#             'IT_course/chapter2_lectures/lecture5-page2.html',
#             'IT_course/chapter2_lectures/lecture6-page1.html',
#             'IT_course/chapter2_lectures/lecture6-page2.html',
#             'IT_course/chapter2_lectures/quiz.html',

#             # IT Chapter 3
#             'IT_course/chapter3_lectures/lecture1-page1.html',
#             'IT_course/chapter3_lectures/lecture1-page2.html',
#             'IT_course/chapter3_lectures/lecture2-page1.html',
#             'IT_course/chapter3_lectures/lecture2-page2.html',
#             'IT_course/chapter3_lectures/lecture2-page3.html',
#             'IT_course/chapter3_lectures/lecture2-page4.html',
#             'IT_course/chapter3_lectures/lecture3-page1.html',
#             'IT_course/chapter3_lectures/lecture3-page2.html',
#             'IT_course/chapter3_lectures/lecture3-page3.html',
#             'IT_course/chapter3_lectures/lecture4-page1.html',
#             'IT_course/chapter3_lectures/lecture4-page2.html',
#             'IT_course/chapter3_lectures/lecture4-page3.html',
#             'IT_course/chapter3_lectures/lecture5-page1.html',
#             'IT_course/chapter3_lectures/lecture5-page2.html',
#             'IT_course/chapter3_lectures/lecture5-page3.html',
#             'IT_course/chapter3_lectures/quiz.html',

#             # IT Chapter 4
#             'IT_course/chapter4_lectures/lecture1-page1.html',
#             'IT_course/chapter4_lectures/lecture1-page2.html',
#             'IT_course/chapter4_lectures/lecture1-page3.html',
#             'IT_course/chapter4_lectures/lecture2-page1.html',
#             'IT_course/chapter4_lectures/lecture2-page2.html',
#             'IT_course/chapter4_lectures/lecture2-page3.html',
#             'IT_course/chapter4_lectures/lecture3-page1.html',
#             'IT_course/chapter4_lectures/lecture3-page2.html',
#             'IT_course/chapter4_lectures/lecture3-page3.html',
#             'IT_course/chapter4_lectures/lecture4-page1.html',
#             'IT_course/chapter4_lectures/lecture4-page2.html',
#             'IT_course/chapter4_lectures/lecture5-page1.html',
#             'IT_course/chapter4_lectures/lecture5-page2.html',
#             'IT_course/chapter4_lectures/lecture5-page3.html',
#             'IT_course/chapter4_lectures/lecture6-page1.html',
#             'IT_course/chapter4_lectures/lecture6-page2.html',
#             'IT_course/chapter4_lectures/lecture6-page3.html',
#             'IT_course/chapter4_lectures/quiz.html',

#             # IT Chapter 5
#             'IT_course/chapter5_lectures/lecture1-page1.html',
#             'IT_course/chapter5_lectures/lecture1-page2.html',
#             'IT_course/chapter5_lectures/lecture2-page1.html',
#             'IT_course/chapter5_lectures/lecture2-page2.html',
#             'IT_course/chapter5_lectures/lecture2-page3.html',
#             'IT_course/chapter5_lectures/lecture3-page1.html',
#             'IT_course/chapter5_lectures/lecture3-page2.html',
#             'IT_course/chapter5_lectures/quiz.html',
#         ]

#     def test_it_course_urls(self):
#         for url in self.urls:
#             with self.subTest(url=url):
#                 response = self.client.get(f'/{url}')
#                 self.assertEqual(response.status_code, 200)



# from django.test import TestCase

# class JavaScriptCourseTests(TestCase):

#     def test_javascript_urls(self):
#         # List of all JavaScript course URLs
#         urls = [
#             # Chapter 1
#             '/javascript/chapter1_lectures/lecture1-page1.html',
#             '/javascript/chapter1_lectures/lecture1-page2.html',
#             '/javascript/chapter1_lectures/lecture2-page1.html',
#             '/javascript/chapter1_lectures/lecture2-page2.html',
#             '/javascript/chapter1_lectures/lecture3-page1.html',
#             '/javascript/chapter1_lectures/lecture3-page2.html',
#             '/javascript/chapter1_lectures/lecture3-page3.html',
#             '/javascript/chapter1_lectures/quiz.html',

#             # Chapter 2
#             '/javascript/chapter2_lectures/lecture1-page1.html',
#             '/javascript/chapter2_lectures/lecture1-page2.html',
#             '/javascript/chapter2_lectures/lecture1-page3.html',
#             '/javascript/chapter2_lectures/lecture2-page1.html',
#             '/javascript/chapter2_lectures/lecture2-page2.html',
#             '/javascript/chapter2_lectures/lecture3-page1.html',
#             '/javascript/chapter2_lectures/lecture3-page2.html',
#             '/javascript/chapter2_lectures/lecture3-page3.html',
#             '/javascript/chapter2_lectures/lecture4-page1.html',
#             '/javascript/chapter2_lectures/lecture4-page2.html',
#             '/javascript/chapter2_lectures/lecture4-page3.html',
#             '/javascript/chapter2_lectures/quiz.html',

#             # Chapter 3
#             '/javascript/chapter3_lectures/lecture1-page1.html',
#             '/javascript/chapter3_lectures/lecture1-page2.html',
#             '/javascript/chapter3_lectures/lecture1-page3.html',
#             '/javascript/chapter3_lectures/lecture2-page1.html',
#             '/javascript/chapter3_lectures/lecture2-page2.html',
#             '/javascript/chapter3_lectures/lecture2-page3.html',
#             '/javascript/chapter3_lectures/lecture3-page1.html',
#             '/javascript/chapter3_lectures/lecture3-page2.html',
#             '/javascript/chapter3_lectures/lecture3-page3.html',
#             '/javascript/chapter3_lectures/quiz.html',

#             # Chapter 4
#             '/javascript/chapter4_lectures/lecture1-page1.html',
#             '/javascript/chapter4_lectures/lecture1-page2.html',
#             '/javascript/chapter4_lectures/lecture1-page3.html',
#             '/javascript/chapter4_lectures/lecture2-page1.html',
#             '/javascript/chapter4_lectures/lecture2-page2.html',
#             '/javascript/chapter4_lectures/lecture2-page3.html',
#             '/javascript/chapter4_lectures/lecture3-page1.html',
#             '/javascript/chapter4_lectures/lecture3-page2.html',
#             '/javascript/chapter4_lectures/lecture3-page3.html',
#             '/javascript/chapter4_lectures/lecture4-page1.html',
#             '/javascript/chapter4_lectures/lecture4-page2.html',
#             '/javascript/chapter4_lectures/lecture4-page3.html',
#             '/javascript/chapter4_lectures/quiz.html',

#             # Chapter 5
#             '/javascript/chapter5_lectures/lecture1-page1.html',
#             '/javascript/chapter5_lectures/lecture1-page2.html',
#             '/javascript/chapter5_lectures/lecture2-page1.html',
#             '/javascript/chapter5_lectures/lecture2-page2.html',
#             '/javascript/chapter5_lectures/lecture2-page3.html',
#             '/javascript/chapter5_lectures/lecture3-page1.html',
#             '/javascript/chapter5_lectures/lecture3-page2.html',
#             '/javascript/chapter5_lectures/lecture3-page3.html',
#             '/javascript/chapter5_lectures/lecture3-page4.html',
#             '/javascript/chapter5_lectures/lecture4-page1.html',
#             '/javascript/chapter5_lectures/lecture4-page2.html',
#             '/javascript/chapter5_lectures/lecture4-page3.html',
#             '/javascript/chapter5_lectures/quiz.html',

#             # Chapter 6
#             '/javascript/chapter6_lectures/lecture1-page1.html',
#             '/javascript/chapter6_lectures/lecture1-page2.html',
#             '/javascript/chapter6_lectures/lecture1-page3.html',
#             '/javascript/chapter6_lectures/lecture2-page1.html',
#             '/javascript/chapter6_lectures/lecture2-page2.html',
#             '/javascript/chapter6_lectures/lecture2-page3.html',
#             '/javascript/chapter6_lectures/lecture3-page1.html',
#             '/javascript/chapter6_lectures/lecture3-page2.html',
#             '/javascript/chapter6_lectures/lecture3-page3.html',
#             '/javascript/chapter6_lectures/lecture4-page1.html',
#             '/javascript/chapter6_lectures/lecture4-page2.html',
#             '/javascript/chapter6_lectures/quiz.html',
#         ]

#         # Loop through the URLs and test each one
#         for url in urls:
#             response = self.client.get(url)
#             self.assertEqual(response.status_code, 200)
#             # Add more checks as necessary (e.g., for content)



# from django.test import TestCase

# class PythonCourseTests(TestCase):

#     def test_python_urls(self):
#         # List of all Python course URLs
#         urls = [
#             # Chapter 1
#             '/python/chapter1_lectures/lecture1-page1.html',
#             '/python/chapter1_lectures/lecture2-page1.html',
#             '/python/chapter1_lectures/lecture3-page1.html',
#             '/python/chapter1_lectures/lecture4-page1.html',
#             '/python/chapter1_lectures/lecture4-page2.html',
#             '/python/chapter1_lectures/quiz.html',

#             # Chapter 2
#             '/python/chapter2_lectures/lecture1-page1.html',
#             '/python/chapter2_lectures/lecture1-page2.html',
#             '/python/chapter2_lectures/lecture2-page1.html',
#             '/python/chapter2_lectures/lecture2-page2.html',
#             '/python/chapter2_lectures/lecture2-page3.html',
#             '/python/chapter2_lectures/lecture3-page1.html',
#             '/python/chapter2_lectures/lecture3-page2.html',
#             '/python/chapter2_lectures/lecture4-page1.html',
#             '/python/chapter2_lectures/lecture4-page2.html',
#             '/python/chapter2_lectures/quiz.html',

#             # Chapter 3
#             '/python/chapter3_lectures/lecture1-page1.html',
#             '/python/chapter3_lectures/lecture1-page2.html',
#             '/python/chapter3_lectures/lecture2-page1.html',
#             '/python/chapter3_lectures/lecture2-page2.html',
#             '/python/chapter3_lectures/lecture2-page3.html',
#             '/python/chapter3_lectures/lecture2-page4.html',
#             '/python/chapter3_lectures/quiz.html',

#             # Chapter 4
#             '/python/chapter4_lectures/lecture1-page1.html',
#             '/python/chapter4_lectures/lecture2-page1.html',
#             '/python/chapter4_lectures/lecture2-page2.html',
#             '/python/chapter4_lectures/lecture3-page1.html',
#             '/python/chapter4_lectures/lecture3-page2.html',
#             '/python/chapter4_lectures/lecture4-page1.html',
#             '/python/chapter4_lectures/lecture4-page2.html',
#             '/python/chapter4_lectures/lecture5-page1.html',
#             '/python/chapter4_lectures/lecture5-page2.html',
#             '/python/chapter4_lectures/lecture5-page3.html',
#             '/python/chapter4_lectures/quiz.html',

#             # Chapter 5
#             '/python/chapter5_lectures/lecture1-page1.html',
#             '/python/chapter5_lectures/lecture2-page1.html',
#             '/python/chapter5_lectures/lecture2-page2.html',
#             '/python/chapter5_lectures/lecture3-page1.html',
#             '/python/chapter5_lectures/lecture3-page2.html',
#             '/python/chapter5_lectures/lecture4-page1.html',
#             '/python/chapter5_lectures/quiz.html',

#             # Chapter 6
#             '/python/chapter6_lectures/lecture1-page1.html',
#             '/python/chapter6_lectures/lecture1-page2.html',
#             '/python/chapter6_lectures/lecture2-page1.html',
#             '/python/chapter6_lectures/lecture2-page2.html',
#             '/python/chapter6_lectures/lecture3-page1.html',
#             '/python/chapter6_lectures/lecture3-page2.html',
#             '/python/chapter6_lectures/lecture4-page1.html',
#             '/python/chapter6_lectures/quiz.html',
#         ]

#         # Loop through the URLs and test each one
#         for url in urls:
#             response = self.client.get(url)
#             self.assertEqual(response.status_code, 200)
#             # You can add additional checks here for content or other validations.





# from django.test import TestCase

# class ComputerNetworksCourseTests(TestCase):

#     def test_computer_networks_urls(self):
#         # List of all Computer Networks course URLs
#         urls = [
#             # Chapter 1
#             '/computer_networks/chapter1_lectures/lecture1_page1.html',
#             '/computer_networks/chapter1_lectures/lecture1_page2.html',
#             '/computer_networks/chapter1_lectures/lecture2_page1.html',
#             '/computer_networks/chapter1_lectures/lecture2_page2.html',
#             '/computer_networks/chapter1_lectures/lecture3_page1.html',
#             '/computer_networks/chapter1_lectures/lecture4_page1.html',
#             '/computer_networks/chapter1_lectures/lecture4_page2.html',
#             '/computer_networks/chapter1_lectures/lecture5_page1.html',
#             '/computer_networks/chapter1_lectures/lecture6_page1.html',
#             '/computer_networks/chapter1_lectures/lecture6_page2.html',

#             # Chapter 2
#             '/computer_networks/chapter2_lectures/lecture1_page1.html',
#             '/computer_networks/chapter2_lectures/lecture2_page1.html',
#             '/computer_networks/chapter2_lectures/lecture2_page2.html',
#             '/computer_networks/chapter2_lectures/lecture3_page1.html',
        
#         ]

#         # Loop through the URLs and test each one
#         for url in urls:
#             response = self.client.get(url)
#             self.assertEqual(response.status_code, 200)
#             # Additional checks can be added for content or other validations.
























# class EndUrlsTestUrls(TestCase):
#     def setUp(self):
#         # Create a user and log them in
#         self.user = CustomUser.objects.create_user(username='testuser', password='password')
#         self.client.login(username='testuser', password='password')
#     def test_login_signup(self):
#      response = self.client.get('/registration/login-signup/login/')
#      self.assertEqual(response.status_code, 302)  # چونکہ یہ redirect کرتا ہے





# from django.test import TestCase
# from django.urls import reverse
# from alignskills.models import Course  # اپنے model کا import کریں

# class EnrollPagesTests(TestCase):

#     def setUp(self):
#         # Common course create کریں جسے templates use کریں
#         Course.objects.create(id=1, title='Python Course')
#         Course.objects.create(id=2, title='JavaScript Course')
#         Course.objects.create(id=3, title='AI Course')
#         Course.objects.create(id=4, title='CCN Course')
#         Course.objects.create(id=5, title='IT Course')
#         Course.objects.create(id=6, title='Database Course')

#     def test_enroll_course_pages(self):
#         url_names = [
#             'enroll_js_page',
#             'enroll_AI_page',
#             'enroll_ccn_page',
#             'enroll_python_page',
#             'enroll_it_page',
#             'enroll_DB_page',
#         ]
#         for name in url_names:
#             with self.subTest(name=name):
#                 url = reverse(name)
#                 response = self.client.get(url)
#                 self.assertEqual(response.status_code, 200)







# # # # class TestURLResponses(TestCase):

# # # #     def test_get_comments_url_returns_200(self):
# # # #         response = self.client.get(reverse('get_comments'))
# # # #         self.assertEqual(response.status_code, 200)





