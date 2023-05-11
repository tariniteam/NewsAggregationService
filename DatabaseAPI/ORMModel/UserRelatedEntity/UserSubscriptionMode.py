class UserSubscriptionMode(db.Model):
    subscription_mode_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    subscription_mode = db.Column(db.String(20), unique=False, nullable=False)
    is_subscription_mode_active = db.Column(db.Bit, unique=False, nullable=False)

    def __repr__(self):
        return f"Name : {self.user_id}, Age: {self.subscription_mode_id}"