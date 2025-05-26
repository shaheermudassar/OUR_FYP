$(document).ready(function() {
  // All your code that interacts with DOM elements
  // Previous HTML code remains exactly the same until the script section 
      // Regex patterns for validation
      const strRegex = /^[a-zA-Z\s]*$/;
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      const phoneRegex = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
      
      // Form elements
      const mainForm = document.getElementById('cv-form');
      let firstnameElem = document.querySelector('.firstname'),
          middlenameElem = document.querySelector('.middlename'),
          lastnameElem = document.querySelector('.lastname'),
          imageElem = document.querySelector('.image'),
          designationElem = document.querySelector('.designation'),
          addressElem = document.querySelector('.address'),
          emailElem = document.querySelector('.email'),
          phonenoElem = document.querySelector('.phoneno'),
          summaryElem = document.querySelector('.summary');
      
      // Display elements
      let nameDsp = document.getElementById('fullname_dsp'),
          imageDsp = document.getElementById('image_dsp'),
          phonenoDsp = document.getElementById('phoneno_dsp'),
          emailDsp = document.getElementById('email_dsp'),
          addressDsp = document.getElementById('address_dsp'),
          designationDsp = document.getElementById('designation_dsp'),
          summaryDsp = document.getElementById('summary_dsp'),
          projectsDsp = document.getElementById('projects_dsp'),
          achievementsDsp = document.getElementById('achievements_dsp'),
          skillsDsp = document.getElementById('skills_dsp'),
          educationsDsp = document.getElementById('educations_dsp'),
          experiencesDsp = document.getElementById('experiences_dsp');
  
      // Collapsible sections
      document.querySelectorAll('.cv-form-row-title').forEach(title => {
          title.addEventListener('click', function() {
              this.classList.toggle('collapsed');
          });
      });
      
      // Initialize repeater
      $(document).ready(function () {
          $('.repeater').repeater({
              initEmpty: false,
              defaultValues: {
                  'achieve_description': '',
                  'edu_description': '',
                  'exp_description': '',
                  'proj_description': ''
              },
              show: function () {
                  $(this).slideDown();
                  generateCV();
              },
              hide: function (deleteElement) {
                  $(this).slideUp(deleteElement, function() {
                      generateCV();
                  });
              }
          });
  
          // Color picker functionality
          $('.color-option').click(function() {
              $('.color-option').removeClass('active');
              $(this).addClass('active');
              
              const primaryColor = $(this).data('primary');
              const secondaryColor = $(this).data('secondary');
              
              // Update CSS variables
              document.documentElement.style.setProperty('--primary-color', primaryColor);
              document.documentElement.style.setProperty('--secondary-color', secondaryColor);
              
              // Update button colors
              $('.btn-primary, .repeater-add-btn, .fab').css('background-color', secondaryColor);
              $('.btn-primary:hover, .repeater-add-btn:hover, .fab:hover').css('background-color', 'var(--hover)');
              $('.btn-outline').css({
                  'border-color': secondaryColor,
                  'color': secondaryColor
              });
              $('.btn-outline:hover').css('background-color', 'rgba(' + hexToRgb(secondaryColor) + ', 0.1)');
              
              generateCV();
          });
          
          // Step navigation
          $('.next-step').click(function() {
              const currentStep = $(this).closest('.form-step');
              const nextStepNum = $(this).data('next');
              
              // Validate current step before proceeding
              if (!validateStep(currentStep.data('step'))) {
                  return;
              }
              
              // Hide current step
              currentStep.removeClass('active');
              
              // Show next step
              $(`.form-step[data-step="${nextStepNum}"]`).addClass('active');
              
              // Show/hide welcome header
              toggleWelcomeHeader(nextStepNum);
              
              // Generate CV preview
              generateCV();
              
              // Scroll to top
              $('.form-section').scrollTop(0);
          });
          
          $('.prev-step').click(function() {
              const currentStep = $(this).closest('.form-step');
              const prevStepNum = $(this).data('prev');
              
              // Hide current step
              currentStep.removeClass('active');
              
              // Show previous step
              $(`.form-step[data-step="${prevStepNum}"]`).addClass('active');
              
              // Show/hide welcome header
              toggleWelcomeHeader(prevStepNum);
              
              // Scroll to top
              $('.form-section').scrollTop(0);
          });
          
          // Load saved data if exists
          loadCV();
      });
      
      // Helper function to convert hex to rgb
      function hexToRgb(hex) {
          // Remove # if present
          hex = hex.replace('#', '');
          
          // Parse r, g, b values
          var r = parseInt(hex.substring(0, 2), 16);
          var g = parseInt(hex.substring(2, 4), 16);
          var b = parseInt(hex.substring(4, 6), 16);
          
          return r + ',' + g + ',' + b;
      }
  
      // Function to toggle welcome header visibility
      function toggleWelcomeHeader(stepNumber) {
          if(stepNumber == 1) { // If going to theme selection
              $('#welcomeHeader').fadeIn(300);
          } else {
              $('#welcomeHeader').fadeOut(300);
          }
      }
  
      // Scroll to top function
      function scrollToTop() {
          $('html, body').animate({scrollTop: 0}, 'smooth');
      }
  
      // Show confirmation message
      function showConfirmation(message) {
          const elem = $('#confirmationMessage');
          elem.text(message).fadeIn();
          setTimeout(() => elem.fadeOut(), 3000);
      }
      
      // Validate specific step
      function validateStep(stepNum) {
          let isValid = true;
          
          // Reset error messages
          $(`.form-step[data-step="${stepNum}"] .form-text`).text('');
          
          // Step 2 validation (About section)
          if (stepNum == 2) {
              // Validate name fields
              if (!firstnameElem.value.trim()) {
                  firstnameElem.nextElementSibling.textContent = 'First name is required';
                  isValid = false;
              } else if (!strRegex.test(firstnameElem.value)) {
                  firstnameElem.nextElementSibling.textContent = 'Only letters and spaces allowed';
                  isValid = false;
              }
              
              if (middlenameElem.value && !strRegex.test(middlenameElem.value)) {
                  middlenameElem.nextElementSibling.textContent = 'Only letters and spaces allowed';
                  isValid = false;
              }
              
              if (!lastnameElem.value.trim()) {
                  lastnameElem.nextElementSibling.textContent = 'Last name is required';
                  isValid = false;
              } else if (!strRegex.test(lastnameElem.value)) {
                  lastnameElem.nextElementSibling.textContent = 'Only letters and spaces allowed';
                  isValid = false;
              }
              
              // Validate email
              if (!emailElem.value.trim()) {
                  emailElem.nextElementSibling.textContent = 'Email is required';
                  isValid = false;
              } else if (!emailRegex.test(emailElem.value)) {
                  emailElem.nextElementSibling.textContent = 'Invalid email format';
                  isValid = false;
              }
              
              // Validate phone
              if (!phonenoElem.value.trim()) {
                  phonenoElem.nextElementSibling.textContent = 'Phone number is required';
                  isValid = false;
              } else if (!phoneRegex.test(phonenoElem.value)) {
                  phonenoElem.nextElementSibling.textContent = 'Invalid phone number';
                  isValid = false;
              }
              
              // Validate designation
              if (!designationElem.value.trim()) {
                  designationElem.nextElementSibling.textContent = 'Designation is required';
                  isValid = false;
              }
              
              // Validate summary
              if (!summaryElem.value.trim()) {
                  summaryElem.nextElementSibling.textContent = 'Summary is required';
                  isValid = false;
              }
          }
          
          // Step 3 validation (Education section)
          if (stepNum == 3) {
              const eduSchools = document.querySelectorAll('.edu_school');
              let hasEducation = false;
              
              eduSchools.forEach(school => {
                  if (school.value.trim()) {
                      hasEducation = true;
                  }
              });
              
              if (!hasEducation) {
                  alert('Please add at least one education entry');
                  isValid = false;
              }
          }
          
          return isValid;
      }
  
      // Fetch values from repeated fields
      const fetchValues = (attrs, ...nodeLists) => {
          let elemsAttrsCount = nodeLists.length;
          let elemsDataCount = nodeLists[0].length;
          let tempDataArr = [];
      
          for(let i = 0; i < elemsDataCount; i++){
              let dataObj = {};
              for(let j = 0; j < elemsAttrsCount; j++){
                  dataObj[`${attrs[j]}`] = nodeLists[j][i].value;
              }
              tempDataArr.push(dataObj);
          }
      
          return tempDataArr;
      }
  
      // Get all user inputs
      const getUserInputs = () => {
          let achievementsTitleElem = document.querySelectorAll('.achieve_title'),
              achievementsDescriptionElem = document.querySelectorAll('.achieve_description');
          let expTitleElem = document.querySelectorAll('.exp_title'),
              expOrganizationElem = document.querySelectorAll('.exp_organization'),
              expLocationElem = document.querySelectorAll('.exp_location'),
              expStartDateElem = document.querySelectorAll('.exp_start_date'),
              expEndDateElem = document.querySelectorAll('.exp_end_date'),
              expDescriptionElem = document.querySelectorAll('.exp_description');
          let eduSchoolElem = document.querySelectorAll('.edu_school'),
              eduDegreeElem = document.querySelectorAll('.edu_degree'),
              eduCityElem = document.querySelectorAll('.edu_city'),
              eduStartDateElem = document.querySelectorAll('.edu_start_date'),
              eduGraduationDateElem = document.querySelectorAll('.edu_graduation_date'),
              eduDescriptionElem = document.querySelectorAll('.edu_description');
          let projTitleElem = document.querySelectorAll('.proj_title'),
              projLinkElem = document.querySelectorAll('.proj_link'),
              projDescriptionElem = document.querySelectorAll('.proj_description');
          let skillElem = document.querySelectorAll('.skill');
  
          return {
              firstname: firstnameElem.value,
              middlename: middlenameElem.value,
              lastname: lastnameElem.value,
              designation: designationElem.value,
              address: addressElem.value,
              email: emailElem.value,
              phoneno: phonenoElem.value,
              summary: summaryElem.value,
              achievements: fetchValues(['achieve_title', 'achieve_description'], achievementsTitleElem, achievementsDescriptionElem),
              experiences: fetchValues(['exp_title', 'exp_organization', 'exp_location', 'exp_start_date', 'exp_end_date', 'exp_description'], 
                             expTitleElem, expOrganizationElem, expLocationElem, expStartDateElem, expEndDateElem, expDescriptionElem),
              educations: fetchValues(['edu_school', 'edu_degree', 'edu_city', 'edu_start_date', 'edu_graduation_date', 'edu_description'], 
                            eduSchoolElem, eduDegreeElem, eduCityElem, eduStartDateElem, eduGraduationDateElem, eduDescriptionElem),
              projects: fetchValues(['proj_title', 'proj_link', 'proj_description'], projTitleElem, projLinkElem, projDescriptionElem),
              skills: fetchValues(['skill'], skillElem),
              theme: {
                  primary: getComputedStyle(document.documentElement).getPropertyValue('--primary-color').trim(),
                  secondary: getComputedStyle(document.documentElement).getPropertyValue('--secondary-color').trim()
              }
          }
      };
  
      // Format date for display
      function formatDate(dateString) {
          if (!dateString) return '';
          
          const date = new Date(dateString);
          return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
      }
  
      // ========== CHANGED FUNCTION: showListData ==========
      // Display list data in preview
      const showListData = (listData, listContainer) => {
          listContainer.innerHTML = "";
          
          if (!listData || listData.length === 0) {
              listContainer.innerHTML = '<div class="preview-item"><span>No information added</span></div>';
              return;
          }
          
          listData.forEach(listItem => {
              let itemElem = document.createElement('div');
              itemElem.classList.add('preview-item');
              
              // Special handling for experiences and education
              if (listContainer.id === 'experiences_dsp' || listContainer.id === 'educations_dsp') {
                  let title = listItem.exp_title || listItem.edu_school || '';
                  let subtitle = listItem.exp_organization || listItem.edu_degree || '';
                  let location = listItem.exp_location || listItem.edu_city || ''; // ADDED CITY FIELD
                  let dateRange = '';
                  
                  if (listItem.exp_start_date || listItem.exp_end_date) {
                      dateRange = `${formatDate(listItem.exp_start_date)} - ${formatDate(listItem.exp_end_date) || 'Present'}`;
                  } else if (listItem.edu_start_date || listItem.edu_graduation_date) {
                      dateRange = `${formatDate(listItem.edu_start_date)} - ${formatDate(listItem.edu_graduation_date) || 'Present'}`;
                  }
                  
                  let description = listItem.exp_description || listItem.edu_description || '';
                  
                  if (title) {
                      let titleElem = document.createElement('span');
                      titleElem.innerHTML = `<strong>${title}</strong>`;
                      itemElem.appendChild(titleElem);
                  }
                  
                  if (subtitle) {
                      let subtitleElem = document.createElement('span');
                      subtitleElem.innerHTML = subtitle;
                      subtitleElem.style.fontStyle = 'italic';
                      itemElem.appendChild(subtitleElem);
                  }
                  
                  // ADDED: Display city for education entries
                  if (location && listContainer.id === 'educations_dsp') {
                      let locationElem = document.createElement('span');
                      locationElem.innerHTML = location;
                      locationElem.style.display = 'block';
                      locationElem.style.color = 'var(--text-light)';
                      itemElem.appendChild(locationElem);
                  }
                  
                  if (dateRange) {
                      let dateElem = document.createElement('span');
                      dateElem.innerHTML = dateRange;
                      dateElem.style.color = 'var(--text-light)';
                      dateElem.style.fontSize = '13px';
                      itemElem.appendChild(dateElem);
                  }
                  
                  if (description) {
                      let descElem = document.createElement('span');
                      descElem.innerHTML = description.replace(/\n/g, '<br>');
                      descElem.style.marginTop = '8px';
                      descElem.style.display = 'block';
                      itemElem.appendChild(descElem);
                  }
              } 
              // Handling for achievements
              else if (listContainer.id === 'achievements_dsp') {
                  let title = listItem.achieve_title || '';
                  let description = listItem.achieve_description || '';
                  
                  if (title) {
                      let titleElem = document.createElement('span');
                      titleElem.innerHTML = `<strong>${title}</strong>`;
                      itemElem.appendChild(titleElem);
                  }
                  
                  if (description) {
                      let descElem = document.createElement('span');
                      descElem.innerHTML = description.replace(/\n/g, '<br>');
                      descElem.style.marginTop = '5px';
                      descElem.style.display = 'block';
                      itemElem.appendChild(descElem);
                  }
              }
              // Handling for projects
              else if (listContainer.id === 'projects_dsp') {
                  let title = listItem.proj_title || '';
                  let link = listItem.proj_link || '';
                  let description = listItem.proj_description || '';
                  
                  if (title) {
                      let titleElem = document.createElement('span');
                      titleElem.innerHTML = `<strong>${title}</strong>`;
                      itemElem.appendChild(titleElem);
                  }
                  
                  if (link) {
                      let linkElem = document.createElement('a');
                      linkElem.href = link;
                      linkElem.target = '_blank';
                      linkElem.innerHTML = link;
                      linkElem.style.display = 'block';
                      linkElem.style.margin = '5px 0';
                      linkElem.style.color = 'var(--secondary-color)';
                      itemElem.appendChild(linkElem);
                  }
                  
                  if (description) {
                      let descElem = document.createElement('span');
                      descElem.innerHTML = description.replace(/\n/g, '<br>');
                      descElem.style.display = 'block';
                      itemElem.appendChild(descElem);
                  }
              }
              // Handling for skills
              else if (listContainer.id === 'skills_dsp') {
                  let skill = listItem.skill || '';
                  
                  if (skill) {
                      let skillElem = document.createElement('span');
                      skillElem.classList.add('preview-item-val');
                      skillElem.innerHTML = skill.split(',').map(s => s.trim()).join(', ');
                      itemElem.appendChild(skillElem);
                  }
              }
              
              listContainer.appendChild(itemElem);
          });
      }
  
      // Preview uploaded image
      function previewImage() {
          const file = imageElem.files[0];
          if (file) {
              const reader = new FileReader();
              reader.onload = function(e) {
                  imageDsp.src = e.target.result;
                  generateCV();
              };
              reader.readAsDataURL(file);
          }
      }
  
      // Generate CV preview
      function generateCV() {
          // Get all user inputs
          let userInputs = getUserInputs();
          
          // Set personal information
          let fullName = '';
          if (userInputs.firstname) fullName += userInputs.firstname;
          if (userInputs.middlename) fullName += ' ' + userInputs.middlename;
          if (userInputs.lastname) fullName += ' ' + userInputs.lastname;
          nameDsp.textContent = fullName || 'Your Name';
          
          designationDsp.textContent = userInputs.designation || 'Your Profession';
          phonenoDsp.textContent = userInputs.phoneno || '+123 456 7890';
          emailDsp.textContent = userInputs.email || 'your@email.com';
          addressDsp.textContent = userInputs.address || 'Your Address';
          summaryDsp.textContent = userInputs.summary || 'Brief summary about yourself';
          
          // Set lists
          showListData(userInputs.achievements, achievementsDsp);
          showListData(userInputs.experiences, experiencesDsp);
          showListData(userInputs.educations, educationsDsp);
          showListData(userInputs.projects, projectsDsp);
          showListData(userInputs.skills, skillsDsp);
      }
  
      // Print CV
      function printCV() {
          // Validate form before printing
          if (!validateForm()) {
              alert('Please fill in all required fields correctly before downloading.');
              return;
          }
          
          // Generate CV one last time before printing
          generateCV();
          
          // Print the CV
          window.print();
      }
  
      // ========== CHANGED FUNCTION: saveCV ==========
      // Save CV data to localStorage
      function saveCV() {
          // Validate form before saving
          if (!validateForm()) {
              alert('Please fill in all required fields correctly before saving.');
              return;
          }
          
          // Get all user inputs
          let userInputs = getUserInputs();
          
          // Handle image separately
          if (imageElem.files[0]) {
              const reader = new FileReader();
              reader.onload = function(e) {
                  userInputs.imageData = e.target.result;
                  saveAllData(userInputs);
              };
              reader.readAsDataURL(imageElem.files[0]);
          } else {
              saveAllData(userInputs);
          }
      }
  
      // ========== NEW FUNCTION: saveAllData ==========
      // Helper function to save all data
      function saveAllData(userInputs) {
          try {
              localStorage.setItem('cvData', JSON.stringify(userInputs));
              showConfirmation('CV saved successfully!');
          } catch (e) {
              if (e.name === 'QuotaExceededError') {
                  // Handle storage full error
                  showConfirmation('Error: Storage is full. Could not save CV.');
              } else {
                  showConfirmation('Error saving CV: ' + e.message);
              }
          }
      }
  
      // ========== CHANGED FUNCTION: loadCV ==========
      // Load CV data from localStorage
      function loadCV() {
          const savedData = localStorage.getItem('cvData');
          if (savedData) {
              const userInputs = JSON.parse(savedData);
              
              // Set basic fields
              if (userInputs.firstname) firstnameElem.value = userInputs.firstname;
              if (userInputs.middlename) middlenameElem.value = userInputs.middlename;
              if (userInputs.lastname) lastnameElem.value = userInputs.lastname;
              if (userInputs.designation) designationElem.value = userInputs.designation;
              if (userInputs.address) addressElem.value = userInputs.address;
              if (userInputs.email) emailElem.value = userInputs.email;
              if (userInputs.phoneno) phonenoElem.value = userInputs.phoneno;
              if (userInputs.summary) summaryElem.value = userInputs.summary;
             
  
  
  
  
              
              // Set image if available
              if (userInputs.imageData) {
                  imageDsp.src = userInputs.imageData;
              }
              
              // Set theme if available
              if (userInputs.theme) {
                  document.documentElement.style.setProperty('--primary-color', userInputs.theme.primary);
                  document.documentElement.style.setProperty('--secondary-color', userInputs.theme.secondary);
                  
                  // Update active color option
                  $('.color-option').removeClass('active');
                  $(`.color-option[data-primary="${userInputs.theme.primary}"]`).addClass('active');
                  
                  // Update button colors
                  $('.btn-primary, .repeater-add-btn, .fab').css('background-color', userInputs.theme.secondary);
                  $('.btn-primary:hover, .repeater-add-btn:hover, .fab:hover').css('background-color', 'var(--hover)');
                  $('.btn-outline').css({
                      'border-color': userInputs.theme.secondary,
                      'color': userInputs.theme.secondary
                  });
                  $('.btn-outline:hover').css('background-color', 'rgba(' + hexToRgb(userInputs.theme.secondary) + ', 0.1)');
              }
              
              // Set repeater fields (education, experience, etc.)
              if (userInputs.educations && userInputs.educations.length > 0) {
                  $('[data-repeater-list="group-c"]').repeater('add', userInputs.educations);
              }
              
              if (userInputs.experiences && userInputs.experiences.length > 0) {
                  $('[data-repeater-list="group-b"]').repeater('add', userInputs.experiences);
              }
              
              if (userInputs.achievements && userInputs.achievements.length > 0) {
                  $('[data-repeater-list="group-a"]').repeater('add', userInputs.achievements);
              }
              
              if (userInputs.projects && userInputs.projects.length > 0) {
                  $('[data-repeater-list="group-d"]').repeater('add', userInputs.projects);
              }
              
              if (userInputs.skills && userInputs.skills.length > 0) {
                  $('[data-repeater-list="group-e"]').repeater('add', userInputs.skills);
              }
              
              generateCV();
          }
      }
  
      // Validate form inputs
      function validateForm() {
          let isValid = true;
          
          // Reset error messages
          document.querySelectorAll('.form-text').forEach(elem => {
              elem.textContent = '';
          });
          
          // Validate name fields
          if (!firstnameElem.value.trim()) {
              firstnameElem.nextElementSibling.textContent = 'First name is required';
              isValid = false;
          } else if (!strRegex.test(firstnameElem.value)) {
              firstnameElem.nextElementSibling.textContent = 'Only letters and spaces allowed';
              isValid = false;
          }
          
          if (middlenameElem.value && !strRegex.test(middlenameElem.value)) {
              middlenameElem.nextElementSibling.textContent = 'Only letters and spaces allowed';
              isValid = false;
          }
          
          if (!lastnameElem.value.trim()) {
              lastnameElem.nextElementSibling.textContent = 'Last name is required';
              isValid = false;
          } else if (!strRegex.test(lastnameElem.value)) {
              lastnameElem.nextElementSibling.textContent = 'Only letters and spaces allowed';
              isValid = false;
          }
          
          // Validate email
          if (!emailElem.value.trim()) {
              emailElem.nextElementSibling.textContent = 'Email is required';
              isValid = false;
          } else if (!emailRegex.test(emailElem.value)) {
              emailElem.nextElementSibling.textContent = 'Invalid email format';
              isValid = false;
          }
          
          // Validate phone
          if (!phonenoElem.value.trim()) {
              phonenoElem.nextElementSibling.textContent = 'Phone number is required';
              isValid = false;
          } else if (!phoneRegex.test(phonenoElem.value)) {
              phonenoElem.nextElementSibling.textContent = 'Invalid phone number';
              isValid = false;
          }
          
          // Validate designation
          if (!designationElem.value.trim()) {
              designationElem.nextElementSibling.textContent = 'Designation is required';
              isValid = false;
          }
          
          // Validate summary
          if (!summaryElem.value.trim()) {
              summaryElem.nextElementSibling.textContent = 'Summary is required';
              isValid = false;
          }
          
          return isValid;
      }
  
      // Initialize CV generation
      generateCV();


      
// Make sure key functions are globally accessible
window.printCV = printCV;
window.saveCV = saveCV;
window.generateCV = generateCV;
  
      // Show/hide floating action button based on scroll
      window.addEventListener('scroll', function() {
          const fab = document.querySelector('.fab');
          if (window.scrollY > 300) {
              fab.style.display = 'flex';
          } else {
              fab.style.display = 'none';
          }
      });
});