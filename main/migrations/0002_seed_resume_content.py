from django.db import migrations


def seed_content(apps, schema_editor):
    Profile = apps.get_model("main", "PortfolioProfile")
    Skill = apps.get_model("main", "Skill")
    Experience = apps.get_model("main", "Experience")
    Project = apps.get_model("main", "Project")
    Education = apps.get_model("main", "Education")
    SocialLink = apps.get_model("main", "SocialLink")

    Profile.objects.get_or_create(
        name="Arshit Gondaliya",
        defaults={
            "title": "Software Engineer | Web Developer | Data Analytics",
            "description": "Enthusiastic and detail-oriented BCA graduate with strong knowledge of Python programming, SQL, Data Analytics, and Machine Learning. Experienced in developing real-world analytics projects, building predictive machine learning models, and creating data-driven solutions using Python.",
            "about_text": "I am a BCA graduate building a practical foundation across Python, SQL, data analytics, machine learning, and web development. My project work covers predictive models, interactive dashboards, operational analysis, and a Django-based e-commerce platform. I enjoy translating a real-world problem into a clear, useful technical solution.",
        },
    )
    skills = [
        ("Python", "programming", "fa-brands fa-python"), ("SQL", "programming", "fa-solid fa-database"), ("C", "programming", "fa-solid fa-code"), ("Java", "programming", "fa-brands fa-java"), ("PHP", "programming", "fa-brands fa-php"),
        ("Machine Learning", "data", "fa-solid fa-brain"), ("Data Analytics", "data", "fa-solid fa-chart-line"), ("Predictive Modeling", "data", "fa-solid fa-wand-magic-sparkles"), ("Exploratory Data Analysis", "data", "fa-solid fa-magnifying-glass-chart"), ("Pandas", "data", "fa-solid fa-table"), ("NumPy", "data", "fa-solid fa-square-root-variable"), ("Scikit-learn", "data", "fa-solid fa-flask"),
        ("HTML5", "web", "fa-brands fa-html5"), ("CSS3", "web", "fa-brands fa-css3-alt"), ("JavaScript", "web", "fa-brands fa-js"), ("Django", "web", "fa-solid fa-server"), ("MySQL", "web", "fa-solid fa-database"), ("SQLite", "web", "fa-solid fa-database"), ("Responsive Design", "web", "fa-solid fa-mobile-screen"),
        ("Excel", "tools", "fa-solid fa-file-excel"), ("MS Word", "tools", "fa-solid fa-file-word"), ("Git", "tools", "fa-brands fa-git-alt"), ("GitHub", "tools", "fa-brands fa-github"), ("VS Code", "tools", "fa-solid fa-code"), ("PyCharm", "tools", "fa-solid fa-laptop-code"),
    ]
    for index, (name, category, icon) in enumerate(skills):
        Skill.objects.get_or_create(name=name, defaults={"category": category, "icon": icon, "display_order": index})

    experiences = [
        ("Parth Enterprise, Amreli", "Web Development Intern", "3.5 Months", "Developed features for an e-commerce grocery platform, including cart and order systems. Translated business requirements into functional technical solutions.", "HTML, CSS, JavaScript, Django, MySQL/SQLite"),
        ("Unifide Menter", "Machine Learning & Data Analytics Intern", "3 Months", "Worked on real-world Machine Learning and Data Analytics projects. Performed data cleaning, preprocessing, and exploratory data analysis using Python.", "Python, Data Cleaning, Preprocessing, EDA"),
    ]
    for index, item in enumerate(experiences):
        Experience.objects.get_or_create(company=item[0], position=item[1], defaults={"duration": item[2], "description": item[3], "technologies": item[4], "display_order": index})

    projects = [
        ("Care Transition Efficiency & Placement Outcome Analytics", "Healthcare Analytics / Machine Learning", "Developed a Streamlit-based Healthcare Analytics dashboard to evaluate care transition efficiency, monitor backlog trends, visualize operational KPIs, and predict discharge outcomes using Machine Learning.", "Python, Pandas, NumPy, Streamlit, Plotly, Scikit-learn, Random Forest Regression"),
        ("Product Line Profitability & Margin Performance Analysis for Nassau Candy Distributor", "E-commerce Analytics / Business Analytics / Machine Learning", "Built an interactive Machine Learning dashboard to evaluate product profitability, margin risk, division performance, Pareto (80/20) analysis, and business KPIs, enabling data-driven decision-making through predictive analytics.", "Python, Pandas, NumPy, Streamlit, Plotly, Scikit-learn, Linear Regression"),
        ("Online Grocery Shop (Parth Enterprise)", "Web Development / E-commerce", "Built a wholesale e-commerce platform with product management and order processing capabilities.", "HTML, CSS, JavaScript, Python (Django), MySQL/SQLite"),
        ("Blood Collection & Supply Management System", "Academic Project", "Managed blood distribution logistics between banks and hospitals to ensure optimized supply chains.", "PHP, MySQL, HTML, CSS, JavaScript"),
    ]
    for index, item in enumerate(projects):
        Project.objects.get_or_create(title=item[0], defaults={"category": item[1], "description": item[2], "detailed_description": item[2], "technologies": item[3], "display_order": index, "featured": index < 3})

    education = [
        ("BCA (Computer Applications)", "Saurashtra University", "2023–2026", "6.35 CGPA"),
        ("Class 12 (HSC)", "Meghani High School (HSC)", "2023", "52%"),
        ("Class 10 (SSC)", "Meghani High School (SSC)", "2021", "49%"),
    ]
    for index, item in enumerate(education):
        Education.objects.get_or_create(degree=item[0], defaults={"institution": item[1], "year": item[2], "result": item[3], "display_order": index})

    socials = [("GitHub", "https://github.com/ArshitGondaliya", "fa-brands fa-github"), ("LinkedIn", "https://linkedin.com/in/arshit-gondaliya", "fa-brands fa-linkedin-in"), ("Email", "mailto:arshitgondaliya09@gmail.com", "fa-solid fa-envelope")]
    for index, (label, url, icon) in enumerate(socials):
        SocialLink.objects.get_or_create(label=label, defaults={"url": url, "icon": icon, "display_order": index})


def remove_content(apps, schema_editor):
    for model_name in ["SocialLink", "Education", "Project", "Experience", "Skill", "PortfolioProfile"]:
        apps.get_model("main", model_name).objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("main", "0001_initial")]
    operations = [migrations.RunPython(seed_content, remove_content)]
