from app import create_app
from app.models import db, User

app = create_app()
with app.app_context():
    db.create_all()
    # Create a test user if not exists
    if not User.query.filter_by(username='testuser').first():
        user = User(username='testuser')
        user.set_password('testpass')
        db.session.add(user)
        db.session.commit()
        print("Test user created: username='testuser', password='testpass'")
    else:
        print("Test user already exists.")
