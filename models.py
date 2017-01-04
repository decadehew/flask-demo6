from views import db

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    menu_items = db.relationship('MenuItem', backref='restaurants', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)

class MenuItem(db.Model):
    __tablename__ = 'menu_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.String)
    restaurant = db.relationship('Restaurant')
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __init__(self, name, description, price,restaurant ):
        self.name = name
        self.description = description
        self.price = price
        self.restaurant = restaurant
        


    def __repr__(self):
        return '<MenuItem {}>'.format(self.name)
