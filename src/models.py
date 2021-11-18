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
    facebook = db.Column(db.String(250), nullable=True)
    twitter = db.Column(db.String(250), nullable=True)
    instagram = db.Column(db.String(250), nullable=True)
    whatsapp = db.Column(db.String(250), nullable=True)
    img_profile = db.Column(db.String(200), nullable=True)
    services  = db.relationship('Services', backref='professor', uselist=True)

#Method to serialize object

    def serialize(self):
        return {
            "id":self.id,
            "email":self.email,
            "user_name":self.user_name,
            "dob":self.dob,
            "country": self.country,
            "secondary_email":self.secondary_email,
            "facebook":self.facebook,
            "twitter":self.twitter,
            "instagram":self.instagram,
            "whatsapp":self.whatsapp,
            "img_profile":self.img_profile,
            "services":[service.serialize() for service in self.services]  
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

#Method to update a Professor by id
    def update(self, user):
        if "user_name" in user:
            self.user_name = user["user_name"]
        if "email" in user:
            self.email = user["email"]
        if "dob" in user:
            self.dob = user["dob"]
        if "country" in user:
            self.country = user["country"]
        if "password" in user:
            self.password = user["password"]
        if "secondary_email" in user:
            self.secondary_email = user["secondary_email"]
        if "facebook" in user:
            self.facebook = user["facebook"]
        if "twitter" in user:
            self.twitter = user["twitter"]
        if "instagram" in user:
            self.instagram = user["instagram"]
        if "whatsapp" in user:
            self.whatsapp = user["whatsapp"]
        if "img_profile" in user:
            self.img_profile = user['img_profile']

        try:
            db.session.commit()
            return True
        except Exception as error:
            db.session.rollback()
            print(error)
            return False

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
    img_profile = db.Column(db.String(200), nullable=True)
    favorites  = db.relationship('Favorites', backref='student', uselist=True)
    

#Method to serialize object

    def serialize(self):
        return {
            "id":self.id,
            "email":self.email,
            "user_name":self.user_name,
            "dob":self.dob,
            "country":self.country,
            "img_profile":self.img_profile,
            "favorites":self.favorites
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

#Method to update a Student profile by id
    def update(self, user):
        if "user_name" in user:
            self.user_name = user["user_name"]
        if "email" in user:
            self.email = user["email"]
        if "dob" in user:
            self.dob = user["dob"]
        if "country" in user:
            self.country = user["country"]
        if "img_profile" in user:
            self.img_profile = user['img_profile']
        if "password" in user:
            self.password = user["password"]
        try:
            db.session.commit()
            return True
        except Exception as error:
            db.session.rollback()
            print(error)
            return False

#Method to delete a Professor

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
    image = db.Column(db.String(250))
    professor_id = db.Column(db.Integer,db.ForeignKey('professor.id'), nullable=False)
    # __table_args__ = (db.UniqueConstraint(
    #     'professor_id',
    #     'title',
    #     name='unique_svc_for_professor'
    # ),)
    def serialize(self):
        return{
            "id":self.id,
            "professor_id":self.professor_id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "schedule": self.schedule,
            "image": self.image
        }
    
    #Method to create service
    @classmethod
    def create(cls, svc):
        try:
            new_svc = cls(**svc)
            db.session.add(new_svc)
            db.session.commit()
            return new_svc
        except Exception as error:
            db.session.rollback()
            print(error)
            return None

    #Method to delete a Service

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
            return True
        except Exception as error:
            db.session.rollback()
            return False

    #Method to update a specific Professor
    def update(self, svc):
        if "title" in svc:
            self.title = svc["title"]
        if "description" in svc:
            self.description = svc["description"]
        if "price" in svc:
            self.price = svc["price"]
        if "schedule" in svc:
            self.schedule = svc["schedule"]
        if "image" in svc:
            self.image = svc["image"]

        try:
            db.session.commit()
            return True
        except Exception as error:
            db.session.rollback()
            print(error)
            return False
    
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
