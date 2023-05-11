

class ScrapperDump(db.Model):	
    dump_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), unique=False, nullable=False)
    headline = db.Column(db.String(20), unique=False, nullable=False)
    url = db.Column(db.Integer, nullable=False)
    scrapping_time = db.Column(db.Time, unique=False, nullable=False)

    def __repr__(self):
    return f"Name : {self.first_name}, Age: {self.age}"