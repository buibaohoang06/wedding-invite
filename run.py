from app import app
from models import db
import os

#For development env
if __name__ == "__main__":
    if os.path.exists('database.db') == False:
        with app.app_context():
            db.create_all()
    app.run(debug=True, host="0.0.0.0", port=80)