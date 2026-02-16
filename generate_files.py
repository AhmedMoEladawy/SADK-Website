#!/usr/bin/env python3
# Script to generate all HTML files for the Deutsch Klub website

import os

# Create directory structure
os.makedirs("pages/curriculum/g10/semester1", exist_ok=True)
os.makedirs("pages/curriculum/g10/semester2", exist_ok=True)
os.makedirs("pages/curriculum/g11/semester1", exist_ok=True)
os.makedirs("pages/curriculum/g11/semester2", exist_ok=True)

# Common navigation HTML
def get_nav(active_page="", base_path="../"):
    return f'''    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <img src="{base_path}images/Logo.png" alt="Deutsch Klub Logo" class="logo-img">
                <span class="logo-text">Deutsch Klub</span>
            </div>
            <ul class="nav-menu" id="navMenu">
                <li class="nav-item">
                    <a href="{base_path}index.html" class="nav-link{' active' if active_page == 'home' else ''}">Home</a>
                </li>
                <li class="nav-item">
                    <a href="{base_path}pages/about.html" class="nav-link{' active' if active_page == 'about' else ''}">About Team</a>
                </li>
                <li class="nav-item dropdown">
                    <a href="#" class="nav-link dropdown-toggle">Curriculum ▼</a>
                    <ul class="dropdown-menu">
                        <li class="dropdown-item">
                            <a href="#" class="dropdown-toggle-sub">G10 ▼</a>
                            <ul class="dropdown-submenu">
                                <li class="dropdown-item">
                                    <a href="#" class="dropdown-toggle-sub">Semester 1 ▼</a>
                                    <ul class="dropdown-submenu">
                                        <li><a href="{base_path}pages/curriculum/g10/semester1/lektionen.html">Lektionen</a></li>
                                        <li><a href="{base_path}pages/curriculum/g10/semester1/study-guide.html">Study Guide</a></li>
                                        <li><a href="{base_path}pages/curriculum/g10/semester1/deutsch-com.html">Deutsch.com Book</a></li>
                                        <li><a href="{base_path}pages/curriculum/g10/semester1/old-exams.html">Old Exams</a></li>
                                        <li><a href="{base_path}pages/curriculum/g10/semester1/study-materials.html">Study Materials</a></li>
                                    </ul>
                                </li>
                                <li class="dropdown-item">
                                    <a href="#" class="dropdown-toggle-sub">Semester 2 ▼</a>
                                    <ul class="dropdown-submenu">
                                        <li><a href="{base_path}pages/curriculum/g10/semester2/lektionen.html">Lektionen</a></li>
                                        <li><a href="{base_path}pages/curriculum/g10/semester2/study-guide.html">Study Guide</a></li>
                                        <li><a href="{base_path}pages/curriculum/g10/semester2/deutsch-com.html">Deutsch.com Book</a></li>
                                        <li><a href="{base_path}pages/curriculum/g10/semester2/old-exams.html">Old Exams</a></li>
                                        <li><a href="{base_path}pages/curriculum/g10/semester2/study-materials.html">Study Materials</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li class="dropdown-item">
                            <a href="#" class="dropdown-toggle-sub">G11 ▼</a>
                            <ul class="dropdown-submenu">
                                <li class="dropdown-item">
                                    <a href="#" class="dropdown-toggle-sub">Semester 1 ▼</a>
                                    <ul class="dropdown-submenu">
                                        <li><a href="{base_path}pages/curriculum/g11/semester1/lektionen.html">Lektionen</a></li>
                                        <li><a href="{base_path}pages/curriculum/g11/semester1/study-guide.html">Study Guide</a></li>
                                        <li><a href="{base_path}pages/curriculum/g11/semester1/deutsch-com.html">Deutsch.com Book</a></li>
                                        <li><a href="{base_path}pages/curriculum/g11/semester1/old-exams.html">Old Exams</a></li>
                                        <li><a href="{base_path}pages/curriculum/g11/semester1/study-materials.html">Study Materials</a></li>
                                    </ul>
                                </li>
                                <li class="dropdown-item">
                                    <a href="#" class="dropdown-toggle-sub">Semester 2 ▼</a>
                                    <ul class="dropdown-submenu">
                                        <li><a href="{base_path}pages/curriculum/g11/semester2/lektionen.html">Lektionen</a></li>
                                        <li><a href="{base_path}pages/curriculum/g11/semester2/study-guide.html">Study Guide</a></li>
                                        <li><a href="{base_path}pages/curriculum/g11/semester2/deutsch-com.html">Deutsch.com Book</a></li>
                                        <li><a href="{base_path}pages/curriculum/g11/semester2/old-exams.html">Old Exams</a></li>
                                        <li><a href="{base_path}pages/curriculum/g11/semester2/study-materials.html">Study Materials</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="nav-item">
                    <a href="{base_path}pages/test-banks.html" class="nav-link{' active' if active_page == 'test' else ''}">Test Banks</a>
                </li>
                <li class="nav-item">
                    <a href="{base_path}pages/resources.html" class="nav-link{' active' if active_page == 'resources' else ''}">Resources</a>
                </li>
            </ul>
            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>'''

def get_footer(base_path="../"):
    return f'''    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Deutsch Klub</h3>
                    <p>Empowering students to excel in German language learning</p>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="{base_path}index.html">Home</a></li>
                        <li><a href="{base_path}pages/about.html">About Team</a></li>
                        <li><a href="{base_path}pages/test-banks.html">Test Banks</a></li>
                        <li><a href="{base_path}pages/resources.html">Resources</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Contact</h4>
                    <p>For questions and support, reach out to the Highboard team</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Deutsch Klub - Deutsch Klub Platform. All rights reserved.</p>
            </div>
        </div>
    </footer>'''

# About page
about_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Team - Deutsch Klub</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/about.css">
</head>
<body>
{get_nav("about", "../")}

    <div class="page-header">
        <h1>About Our Team</h1>
        <p>Meet the Highboard members dedicated to your success in Deutsch</p>
    </div>

    <section class="page-content">
        <div class="container">
            <div class="content-container">
                <h2>Welcome to the Deutsch Klub</h2>
                <p>
                    Willkommen! The Deutsch Klub (Deutsch Klub) is a dedicated group of students and educators 
                    committed to helping you excel in German language learning. Our mission is to provide 
                    comprehensive resources, support, and guidance to ensure every student achieves excellent 
                    performance in Deutsch.
                </p>
                <p>
                    We believe that Lernen (learning) should be accessible, engaging, and effective. Through 
                    our platform, you'll find everything you need to succeed, from curriculum materials to 
                    interactive practice tests.
                </p>
            </div>

            <div class="mission-vision">
                <div class="mv-card">
                    <h3>Our Mission</h3>
                    <p>
                        To empower students with comprehensive German language resources and support, 
                        fostering excellence in Deutsch learning and ensuring every student reaches 
                        their full potential.
                    </p>
                </div>
                <div class="mv-card">
                    <h3>Our Vision</h3>
                    <p>
                        To be the leading platform for German language education, creating a community 
                        where students can thrive, learn effectively, and achieve outstanding results 
                        in their Deutsch studies.
                    </p>
                </div>
            </div>

            <div class="highboard-section">
                <h2 class="section-title">Meet the Highboard</h2>
                <div class="highboard-grid">
                    <div class="member-card">
                        <div class="member-avatar">
                            <div class="avatar-placeholder">👤</div>
                        </div>
                        <h3>Team Leader</h3>
                        <p class="member-role">Head of Deutsch Klub</p>
                        <p class="member-description">
                            Leading the team with passion and dedication to ensure all students 
                            have access to the best learning resources.
                        </p>
                    </div>
                    <div class="member-card">
                        <div class="member-avatar">
                            <div class="avatar-placeholder">👤</div>
                        </div>
                        <h3>Curriculum Coordinator</h3>
                        <p class="member-role">Content Manager</p>
                        <p class="member-description">
                            Organizing and maintaining all curriculum materials, ensuring everything 
                            is up-to-date and easily accessible.
                        </p>
                    </div>
                    <div class="member-card">
                        <div class="member-avatar">
                            <div class="avatar-placeholder">👤</div>
                        </div>
                        <h3>Test Bank Manager</h3>
                        <p class="member-role">Assessment Specialist</p>
                        <p class="member-description">
                            Creating and managing interactive test banks to help students practice 
                            and improve their understanding of Deutsch.
                        </p>
                    </div>
                    <div class="member-card">
                        <div class="member-avatar">
                            <div class="avatar-placeholder">👤</div>
                        </div>
                        <h3>Student Support</h3>
                        <p class="member-role">Learning Assistant</p>
                        <p class="member-description">
                            Providing guidance and support to students, answering questions, and 
                            helping with any challenges in learning Deutsch.
                        </p>
                    </div>
                    <div class="member-card">
                        <div class="member-avatar">
                            <div class="avatar-placeholder">👤</div>
                        </div>
                        <h3>Resource Developer</h3>
                        <p class="member-role">Content Creator</p>
                        <p class="member-description">
                            Developing new learning materials, study guides, and resources to 
                            enhance the learning experience for all students.
                        </p>
                    </div>
                    <div class="member-card">
                        <div class="member-avatar">
                            <div class="avatar-placeholder">👤</div>
                        </div>
                        <h3>Technical Lead</h3>
                        <p class="member-role">Platform Manager</p>
                        <p class="member-description">
                            Maintaining and improving the platform to ensure smooth access to 
                            all resources and features.
                        </p>
                    </div>
                </div>
            </div>

            <div class="cta-section">
                <h2>Ready to Start Learning?</h2>
                <p>Viel Erfolg! Begin your journey to excellence in Deutsch today.</p>
                <div class="cta-buttons">
                    <a href="test-banks.html" class="btn btn-primary">Practice Now</a>
                    <a href="../index.html" class="btn btn-secondary">Back to Home</a>
                </div>
            </div>
        </div>
    </section>

{get_footer("../")}

    <script src="../js/main.js"></script>
</body>
</html>'''

with open("pages/about.html", "w", encoding="utf-8") as f:
    f.write(about_html)

print("Created about.html")

# Test Banks page
test_banks_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Banks - Deutsch Klub</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/test-banks.css">
</head>
<body>
{get_nav("test", "../")}

    <div class="page-header">
        <h1>Interactive Test Banks</h1>
        <p>Practice with instant feedback - Viel Erfolg!</p>
    </div>

    <section class="page-content">
        <div class="container">
            <div class="test-intro">
                <p>
                    Welcome to our interactive test bank! Practice your Deutsch skills with multiple-choice 
                    questions and get instant feedback. Select your answer and see if you're correct immediately.
                </p>
                <div class="score-display" id="scoreDisplay">
                    <span>Score: <strong id="score">0</strong> / <strong id="total">0</strong></span>
                </div>
            </div>

            <div class="questions-container" id="questionsContainer">
                <!-- Questions will be dynamically loaded here -->
            </div>

            <div class="test-actions">
                <button class="btn btn-primary" id="checkAllBtn">Check All Answers</button>
                <button class="btn btn-secondary" id="resetBtn">Reset Test</button>
            </div>
        </div>
    </section>

{get_footer("../")}

    <script src="../js/main.js"></script>
    <script src="../js/test-banks.js"></script>
</body>
</html>'''

with open("pages/test-banks.html", "w", encoding="utf-8") as f:
    f.write(test_banks_html)

print("Created test-banks.html")

# Resources page
resources_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resources - Deutsch Klub</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
{get_nav("resources", "../")}

    <div class="page-header">
        <h1>Learning Resources</h1>
        <p>Additional materials to support your Deutsch learning journey</p>
    </div>

    <section class="page-content">
        <div class="container">
            <div class="content-container">
                <h2>Additional Resources</h2>
                <p>
                    Here you'll find supplementary resources to enhance your German language learning experience. 
                    These materials are designed to support your studies and help you achieve excellence in Deutsch.
                </p>
                <p>
                    More resources will be added regularly. Check back often for updates!
                </p>
            </div>

            <div class="content-container">
                <h3>Coming Soon</h3>
                <p>
                    We're continuously adding new resources to help you succeed. Stay tuned for:
                </p>
                <ul style="list-style: none; padding-left: 2rem;">
                    <li>📖 Additional reading materials</li>
                    <li>🎧 Audio resources for pronunciation</li>
                    <li>📝 Writing practice exercises</li>
                    <li>🎬 Video tutorials</li>
                    <li>📚 Recommended books and references</li>
                </ul>
            </div>
        </div>
    </section>

{get_footer("../")}

    <script src="../js/main.js"></script>
</body>
</html>'''

with open("pages/resources.html", "w", encoding="utf-8") as f:
    f.write(resources_html)

print("Created resources.html")

# Curriculum page template
def create_curriculum_page(grade, semester, page_type, page_title, base_path="../../"):
    page_names = {
        "lektionen": "Lektionen",
        "study-guide": "Study Guide",
        "deutsch-com": "Deutsch.com Book",
        "old-exams": "Old Exams",
        "study-materials": "Study Materials"
    }
    
    display_name = page_names.get(page_type, page_type)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{display_name} - G{grade} Semester {semester} - Deutsch Klub</title>
    <link rel="stylesheet" href="{base_path}css/style.css">
</head>
<body>
{get_nav("", base_path)}

    <div class="page-header">
        <h1>{display_name}</h1>
        <p>G{grade} - Semester {semester}</p>
    </div>

    <section class="page-content">
        <div class="container">
            <div class="content-container">
                <h2>{display_name} - G{grade} Semester {semester}</h2>
                <p>
                    This page contains all {display_name.lower()} materials for Grade {grade}, Semester {semester}.
                    Files will be uploaded and embedded here for easy access and download.
                </p>
                
                <!-- Future files will be embedded here -->
                <!-- Use iframe for preview and allow downloading -->
                <div style="margin-top: 2rem; padding: 2rem; background-color: var(--color-light-gray); border-radius: 10px; text-align: center;">
                    <p style="color: var(--color-gray); font-style: italic;">
                        Files will be available here soon. Check back later!
                    </p>
                    <p style="margin-top: 1rem; color: var(--color-gray);">
                        When files are added, they will be displayed with preview options and download functionality.
                    </p>
                </div>
            </div>
        </div>
    </section>

{get_footer(base_path)}

    <script src="{base_path}js/main.js"></script>
</body>
</html>'''
    
    return html

# Generate all curriculum pages
curriculum_pages = [
    ("10", "1", "lektionen"),
    ("10", "1", "study-guide"),
    ("10", "1", "deutsch-com"),
    ("10", "1", "old-exams"),
    ("10", "1", "study-materials"),
    ("10", "2", "lektionen"),
    ("10", "2", "study-guide"),
    ("10", "2", "deutsch-com"),
    ("10", "2", "old-exams"),
    ("10", "2", "study-materials"),
    ("11", "1", "lektionen"),
    ("11", "1", "study-guide"),
    ("11", "1", "deutsch-com"),
    ("11", "1", "old-exams"),
    ("11", "1", "study-materials"),
    ("11", "2", "lektionen"),
    ("11", "2", "study-guide"),
    ("11", "2", "deutsch-com"),
    ("11", "2", "old-exams"),
    ("11", "2", "study-materials"),
]

for grade, semester, page_type in curriculum_pages:
    file_path = f"pages/curriculum/g{grade}/semester{semester}/{page_type}.html"
    html_content = create_curriculum_page(grade, semester, page_type, page_type, "../../")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Created {file_path}")

print("\nAll files generated successfully!")
