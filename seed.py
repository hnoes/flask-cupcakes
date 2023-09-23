from app import app, db
from models import Cupcake

# Initialize the Flask app context
with app.app_context():
    # Create the database tables
    db.create_all()

    # Create Cupcake objects
    c1 = Cupcake(flavor="Chocolate", size="Large", rating=4.5)
    c2 = Cupcake(flavor="Vanilla", size="Medium", rating=3.8)

    # Add Cupcake objects to the session and commit them to the database
    db.session.add_all([c1, c2])
    db.session.commit()
