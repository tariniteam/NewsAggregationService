class UserSubscribeTo(db.Model):
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    category_id = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"Name : {self.user_id}, Age: {self.category_id}"