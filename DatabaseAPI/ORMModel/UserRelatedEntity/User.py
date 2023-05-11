
class User (db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=False, nullable=False)
    user_email = db.Column(db.String(100), unique=False, nullable=False)
    user_phone_number = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return f"Name : {self.user_id}, Age: {self.user_name}"