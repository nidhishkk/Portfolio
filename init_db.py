import os
from app import create_app, db
from app.models import User, Profile, Project, Skill, Certification

app = create_app()

with app.app_context():
    db.create_all()

    # Create admin user if not exists
    admin_user = User.query.first()
    if not admin_user:
        admin = User(username='admin123@gmail.com', email='admin123@gmail.com')
        admin.set_password('admin123')
        db.session.add(admin)

    # Create default profile if not exists
    profile = Profile.query.first()
    if not profile:
        profile = Profile(
            full_name='Nidhish K K',
            professional_title='Information Technology Student | Aspiring Full Stack Developer',
            about_me='I am an aspiring Information Technology student with a strong interest in Full Stack Web Development, Python programming, and modern web technologies. I enjoy building practical software solutions that solve real-world problems and continuously improving my development skills through projects and learning.',
            email='nidhishkk@example.com',
            location='OMR, Chennai',
            github_url='https://github.com/nidhishkk',
        )
        db.session.add(profile)
        
    # Add skills
    if Skill.query.count() == 0:
        skills = [
            Skill(name='Python', category='Programming Languages', proficiency_percent=90),
            Skill(name='Java', category='Programming Languages', proficiency_percent=80),
            Skill(name='C', category='Programming Languages', proficiency_percent=75),
            Skill(name='JavaScript', category='Programming Languages', proficiency_percent=85),
            Skill(name='Flask', category='Frameworks', proficiency_percent=85),
            Skill(name='Bootstrap', category='Frameworks', proficiency_percent=90),
            Skill(name='MySQL', category='Databases', proficiency_percent=80),
            Skill(name='SQLite', category='Databases', proficiency_percent=85),
            Skill(name='Git', category='Tools', proficiency_percent=85),
            Skill(name='GitHub', category='Tools', proficiency_percent=90),
            Skill(name='VS Code', category='Tools', proficiency_percent=95),
            Skill(name='MySQL Workbench', category='Tools', proficiency_percent=80),
            Skill(name='Communication', category='Soft Skills', proficiency_percent=90),
            Skill(name='Teamwork', category='Soft Skills', proficiency_percent=95),
            Skill(name='Problem Solving', category='Soft Skills', proficiency_percent=85),
            Skill(name='Adaptability', category='Soft Skills', proficiency_percent=90)
        ]
        db.session.bulk_save_objects(skills)

    # Add projects
    if Project.query.count() == 0:
        projects = [
            Project(
                title='ResQ',
                short_description='A disaster-response information exchange platform.',
                full_description='A disaster-response information exchange platform that enables affected individuals, volunteers, and authorities to share critical information during emergency situations.',
                technologies='Python, Flask, MySQL, HTML, CSS, JavaScript'
            ),
            Project(
                title='Advanced Repo Analyst Tool',
                short_description='A repository analysis platform for GitHub.',
                full_description='A repository analysis platform that examines GitHub repositories and provides insights about repository structure, files, technologies used, and project contents.',
                github_link='https://github.com/nidhishkk/Advanced-Repo-Analyst-Tool',
                technologies='Python, Flask, HTML, CSS, JavaScript'
            )
        ]
        db.session.bulk_save_objects(projects)

    db.session.commit()
    print("Database initialized and default data created.")
