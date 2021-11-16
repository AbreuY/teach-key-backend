from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_name = db.Column(db.String(80), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name
            # do not serialize the password, its a security breach
        }

#Class Professor

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    user_name = db.Column(db.String(100), unique=True)
    dob = db.Column(db.String(100))
    country = db.Column(db.String(100))
    password = db.Column(db.String(100))
    secondary_email = db.Column(db.String(100), unique=True, nullable=True)
    contact_methods = db.Column(db.String(100), nullable=True)

#Method to serialize object

    def serialize(self):
        return {
            "id":self.id,
            "user_name":self.user_name
        }

#Method to create a new Professor

    @classmethod
    def create(cls, bubulala):
        try:
            new_user = cls(**bubulala)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as error:
            db.session.rollback()
            print(error)
            return None

#Method to delete a Professor

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
            return True
        except Exception as error:
            db.session.rollback()
            return False


#Class Student

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    user_name = db.Column(db.String(100), unique=True)
    dob = db.Column(db.String(100))
    password = db.Column(db.String(100))
    country = db.Column(db.String(100))
    favorites  = db.relationship('Favorites', backref='student', uselist=True)
    

#Method to serialize object

    def serialize(self):
        return {
            "id":self.id,
            "user_name":self.user_name
        }

#Method to create a new Student

    @classmethod
    def create(cls, bubulala):
        try:
            new_user = cls(**bubulala)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as error:
            db.session.rollback()
            print(error)
            return None

#Method to delete a Student

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
            return True
        except Exception as error:
            db.session.rollback()
            return False



#Class Services

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.String(300))
    price = db.Column(db.Integer)
    schedule = db.Column(db.Integer)
    image = db.Column(db.String(100))

    def serialize(self):
        return{
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "schedule": self.schedule,
            "image": self.image
        }

#Class Favorites

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'), nullable=False)
    url = db.Column(db.String(100))
    name = db.Column(db.String(100))
    __table_args__ = (db.UniqueConstraint(
        'student_id',
        'url',
        name='unique_fav_for_user'
    ),)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "url": self.url,
            "id": self.id,
            "favName": self.name
        }

