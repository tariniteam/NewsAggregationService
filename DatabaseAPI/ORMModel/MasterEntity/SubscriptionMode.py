
class SubscriptionMode (db.Model):
    SubscriptionMode_id = db.Column(db.Integer, primary_key=True)
    SubscriptionMode = db.Column(db.String(20), unique=False, nullable=False)
    is_SubscriptionMode_active = db.Column(db.Bit, unique=False, nullable=False)

    def __repr__(self):
        return f"Name : {self.SubscriptionMode_id}, Age: {self.SubscriptionMode}"