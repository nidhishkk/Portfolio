from app import create_app, db
from app.models import User, Profile, Project, Skill, Certification, Message

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Profile': Profile,
        'Project': Project,
        'Skill': Skill,
        'Certification': Certification,
        'Message': Message
    }

if __name__ == '__main__':
    app.run(debug=True)
