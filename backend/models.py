from config import db
from datetime import date

class Closet(db.Model):
     __tablename__ = "Skincare Closet"

     id = db.Column(db.Integer, primary_key = True)
     brand = db.Column(db.String(50), unique = False, nullable = False)
     item_name = db.Column(db.String(100), unique = False, nullable = False)
     category = db.Column(db.String(30), unique = False, nullable = False)
     date_added = db.Column(db.Datetime, default = date)

     def to_json(self):
          return {
               "id": self.id,
               "brand": self.brand,
               "itemName": self.item_name,
               "category": self.category,
               "dateAdded": self.date_added
          }
     
