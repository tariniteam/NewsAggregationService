

class Category (db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), unique=False, nullable=False)
    is_category_active = db.Column(db.Bit, unique=False, nullable=False)

    def __repr__(self):
    return f"Name : {self.category_id}, Age: {self.category_name}"