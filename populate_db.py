import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from main.models import Project, SkillCategory, Skill, Experience

def populate():
    # 1. Projects
    projects_data = [
        {
            "title": "AgricConnect",
            "impact": "Connecting Farmers to Markets",
            "description": "A digital platform connecting farmers, marketers, and service providers. Features include real-time market access and supply chain coordination.",
            "stack": "Python, MySQL, Flask",
            "github_url": "https://github.com/haruna-ibrahim/agric-connect"
        },
        {
            "title": "Crop Diagnostic System",
            "impact": "AI-Driven Disease Identification",
            "description": "Designed and developed a system that identifies crop diseases from images. Implemented backend logic and MySQL logging.",
            "stack": "Python, MySQL, AI, Flask",
            "github_url": "https://github.com/haruna-ibrahim/crop-diagnosis"
        }
    ]
    for p in projects_data:
        Project.objects.get_or_create(title=p["title"], defaults=p)

    # 2. Skills
    skills_map = {
        "Backend": ["Python", "Flask / Django", "RESTful APIs", "MySQL", "Database Design"],
        "Frontend": ["HTML5", "CSS3 / Tailwind", "JavaScript (ES6+)", "Responsive Design"],
        "Tools & Dev": ["Git & GitHub", "VS Code", "Postman", "Linux / Bash"],
        "Future Mastery": ["Flutter", "Dart", "Cloud (AWS/GCP)", "Docker"]
    }
    for cat_name, skill_names in skills_map.items():
        cat, _ = SkillCategory.objects.get_or_create(name=cat_name)
        for s_name in skill_names:
            Skill.objects.get_or_create(category=cat, name=s_name)

    # 3. Experience
    exp_data = [
        {
            "title": "Final Year Project",
            "duration": "2024",
            "impact": "AI-Driven Crop Diagnostic System",
            "description": "Designed and developed a system that identifies crop diseases from images. Implemented the backend logic and integrated a MySQL database for logging disease outbreaks."
        },
        {
            "title": "Freelance Project",
            "duration": "2023 - Present",
            "impact": "Inventory System for Abuja Retailer",
            "description": "Built a custom inventory management tool using Python and MySQL. Enabled real-time stock tracking and automated low-stock alerts."
        }
    ]
    for e in exp_data:
        Experience.objects.get_or_create(title=e["title"], impact=e["impact"], defaults=e)

    print("Database successfully populated with data from original portfolio!")

if __name__ == '__main__':
    populate()
