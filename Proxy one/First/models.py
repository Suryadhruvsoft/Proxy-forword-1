from First import db

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(50))
   city = db.Column(db.String(15)) 
   pin = db.Column(db.Integer)

   def __init__(self, name, city, pin):
      self.name = name
      self.city = city
      self.pin = pin
