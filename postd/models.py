

from postd import db,login_manager
from flask_login import UserMixin

# ------------------- Login ----------------------
@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)

# ------------------- Main Login Web page----------------------

# export FLASK_APP=run.py



# -------------------Home Iformation----------------------
class Homein(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(80), nullable=False)
    infoimg=db.Column(db.String(100))
    show=db.Column(db.String(1))

    def __repr__(self):
        return '<Homein %r>' % self.info

# -------------------About Iformation----------------------

class Aboutin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aboutinfo1 = db.Column(db.String(160), nullable=False)
    aboutinfo2 = db.Column(db.String(160), nullable=False)
    disgen1 = db.Column(db.String(25),nullable=False)
    disgen1interest = db.Column(db.Integer,nullable=False)
    disgen2 = db.Column(db.String(25),nullable=False)
    disgen2interest = db.Column(db.Integer,nullable=False)
    disgen3 = db.Column(db.String(25),nullable=False)
    disgen3interest = db.Column(db.Integer,nullable=False)
    disgen4 = db.Column(db.String(25),nullable=False)
    disgen4interest = db.Column(db.Integer,nullable=False)
    disgen5 = db.Column(db.String(25),nullable=False)
    disgen5interest = db.Column(db.Integer,nullable=False)
    aboutinfoimg=db.Column(db.String(100))
    show=db.Column(db.String(1))
    

    def __repr__(self):
        return '<Aboutin %r>' % self.aboutinfo1


# -------------------MyProject Iformation----------------------
class Projectin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    protime = db.Column(db.String(25), nullable=False)
    protitle = db.Column(db.String(50), nullable=False)
    prosortcut = db.Column(db.String(80), nullable=False)
    projareya = db.Column(db.Text)
    cardTextadd=db.Column(db.String(210))
    projareya2 = db.Column(db.Text)
    projtitle = db.Column(db.String(100))
    listp = db.Column(db.String(70))
    listp1 = db.Column(db.String(70))
    listp2 = db.Column(db.String(70))
    listp3 = db.Column(db.String(70))
    listp4 = db.Column(db.String(70))
    listp5 = db.Column(db.String(70))
    listp6 = db.Column(db.String(70))
    listp7 = db.Column(db.String(70))
    projareya3 = db.Column(db.Text)
    proimg=db.Column(db.String(100))
    show=db.Column(db.String(10))

    def __repr__(self):
        return '<Projectin %r>' % self.protitle



# ------------------- Contact Iformation----------------------

class Contactin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fulname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    
    

    def __repr__(self):
        return '<Contactin %r>' % self.fulname

# ------------------- Login Web page ----------------------

class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login= db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    

    def __repr__(self):
        return '<Contactin %r>' % self.login

class Backgroundimg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    infoimg = db.Column(db.String(80), nullable=False)
    show=db.Column(db.String(1))
    
    def __repr__(self):
        return '<Homein %r>' % self.infoimg

