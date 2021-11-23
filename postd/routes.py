from flask import Flask,redirect,render_template,request,url_for,session
import flask_login
from werkzeug.utils import secure_filename
from . models import Homein,Aboutin,Projectin,Contactin,Admin,Backgroundimg
from postd import app,db,os ,bcrypt,login_manager
from flask_login import login_user,login_required,logout_user
from postd.forms import ContactFrom,Adminlogin





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Main Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@app.route('/',methods=['GET','POST'])
def main():
    form=ContactFrom()
    print(form.errors)
    if form.validate_on_submit():
        contact=Contactin(
            fulname=form.fulname.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('main'))
# ---------------Background Img Iformasion --------------------- 
    backgroundimgall=Backgroundimg.query.all()
    for backgroundimg in backgroundimgall:
        if backgroundimg.show=="1":
            backimg=Backgroundimg.query.get_or_404(backgroundimg.id)

# ---------------Home Iformasion --------------------- 
    homeinfoall=Homein.query.all()
    for info_home in homeinfoall:
        if info_home.show=="1":
            homeinfo=Homein.query.get_or_404(info_home.id)
    
# ---------------About Iformasion ---------------------
    
    aboutinfoall=Aboutin.query.all()
    for info_about in aboutinfoall:
        if info_about.show=="1":
            aboutinfo=Aboutin.query.get_or_404(info_about.id)
            
# ----------------MyProject Iformasion -----------------
    proje = Projectin.query.all()
    proje =proje[::-1]
    prostatic=[]
    shadowbox=[]
    a=0;
    for infora in proje:
        if infora.show=="1":    
            a+=1
            if a>4 :
                shadowbox.append(infora)
            else:
                prostatic.append(infora)  
             
    return render_template('maxwill.html',projec=shadowbox,homeinfo=homeinfo,prostatic=prostatic,aboutinfo=aboutinfo,form=form,backimg=backimg)






# ----------------Project Web page (Main Single Web page) -----------------

@app.route('/project/<int:id>', methods=['GET','POST'])
def project(id):
    procejt=Projectin.query.get_or_404(id)
    bacgroundimall=Backgroundimg.query.all()
    hinfolen=len(bacgroundimall)-1
    backimg=bacgroundimall[hinfolen]
    return render_template('will-project.html',procejt=procejt,backimg=backimg)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Main End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Login Web page Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@app.route('/admin',methods=['GET','POST'])
def login():
    form=Adminlogin()
    if form.validate_on_submit():

        user=Admin.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('adminmain'))


        return redirect(url_for('login'))

    return render_template('admin/login.html',adminlog=form)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Login Web page End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Admin Panel  Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel Login Start <<<<<<<<<<<<<<<<<<<<<<<

# ----------------Admin Panel Login Add Web page ----------------------

@app.route("/admin/loginadd",methods=['GET','POST'])
@login_required
def loginadd():
    
    form=Adminlogin()
    if form.validate_on_submit():
        user_row_password=form.password.data
        pas_hash=bcrypt.generate_password_hash(user_row_password).decode('utf-8')
        
        user=Admin(
            login=form.login.data,      
            password=pas_hash
        )
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('adminmain'))

    return render_template('admin/admincreatelog.html',form=form)

# ----------------Admin Panel Login Delete Web page ----------------------

@app.route('/admin/login-delete/<int:id>', methods=['GET','POST'])
@login_required
def logindelete(id):
    user = Admin.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('adminmain'))
# ----------------Admin Panel Login Out Web page ----------------------
@app.route("/admin/main/logout")
@login_required
def logout():

    logout_user()
    return redirect(url_for('login'))


# >>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel Login End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<






# >>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel Main Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ---------------------Admin Panel Main Web page ------------------------

@app.route('/admin/main/',methods=['GET','POST'])
@login_required
def adminmain():
    admin=Admin().query.all()
    admin=admin[::-1]
    contact=Contactin.query.all()
    contact=contact[::-1]
    home=Homein.query.all()
    home=home[::-1]
    project=Projectin.query.all()
    project=project[::-1]
    about=Aboutin.query.all()
    about=about[::-1]
    backimgAll=Backgroundimg().query.all()
    backimg=backimgAll[::-1]
    if request.method=='POST':
        if "show" in request.form:
            show_id=int(request.form.get('show'))
            for show_other in backimgAll:
                if show_other.id==show_id:
                    show_other.show="1"
                else:
                    show_other.show="0"
            
            db.session.add(show_other)
        
        if "show_home" in request.form:
            show_home_id=int(request.form.get('show_home'))
            for info_home in home:
                if info_home.id==show_home_id:
                    info_home.show="1"
                else:
                    info_home.show="0"
            db.session.add(info_home)
        
        if  "show_about" in request.form:
            show_about_id=int(request.form.get("show_about"))
           
            for info_about in about:
                if info_about.id==show_about_id:
                    info_about.show="1"
                else:
                    info_about.show="0"
            db.session.add(info_about)

        if "show_project" in request.form:
            show_project_id=int(request.form.get('show_project'))
            show_project=Projectin.query.get_or_404(show_project_id)
            show_project.show="1"
            db.session.add(show_project)
        
        if "unshow_project" in request.form:
            unshow_project_id=int(request.form.get('unshow_project'))
            unshow_project=Projectin.query.get_or_404(unshow_project_id)
            unshow_project.show="0"
            db.session.add(unshow_project)


        # show_about_id=int(request.form.get(""))
        db.session.commit()
        return redirect(url_for('adminmain'))

    return render_template('admin/adminmain.html',contact=contact,home=home,about=about,project=project,admin=admin,backimg=backimg)


    

# ---------------------Admin Panel Contact Delete Web page -------------------
@app.route('/admin/Contact-delete/<int:id>', methods=['GET','POST'])
@login_required
def concactdelete(id):
    contact = Contactin.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('adminmain'))

# >>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel Main End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<




# >>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel Home Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ----------------Admin Panel Home Web page ----------------------
@app.route('/admin/home',methods=['GET','POST'])
@login_required
def adminhome():
    if request.method=='POST':
        file = request.files['file']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        homeinfo=Homein(
            info=request.form.get('HomeTitleText'),
            infoimg=filename
        )
        
        db.session.add(homeinfo)
        db.session.commit()
        return redirect(url_for('adminmain'))
    
    return render_template('admin/adminpanelhome.html')

# ----------------Admin Panel Home Delete Web page ----------------------------
@app.route('/admin/home-delete/<int:id>', methods=['GET','POST'])
@login_required
def homedelete(id):
    home = Homein.query.get_or_404(id)
    db.session.delete(home)
    db.session.commit()
    return redirect(url_for('adminmain'))

# ---------------------Admin Panel Home Edit Web page ----------------------
@app.route('/admin/home/edit/<int:id>', methods=['GET','POST'])
@login_required
def edithome(id):
    home = Homein.query.get_or_404(id)
    if request.method == 'POST':
       file = request.files['file']
       print(file)
       filename = secure_filename(file.filename)
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       home.info = request.form.get('HomeTitleText')
       home.infoimg = filename
       db.session.commit()
       return redirect(url_for("adminmain"))
    return render_template('admin/edithome.html',homes=home)


# ----------------Admin Panel Bacgroundimg Web page ----------------------
@app.route('/admin/bacgroundimg',methods=['GET','POST'])
@login_required
def bacgroundimg():
    if request.method=='POST':
        file = request.files['file']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        bacgroundim=Backgroundimg(
            infoimg=filename
        )
        
        db.session.add(bacgroundim)
        db.session.commit()
        return redirect(url_for('adminmain'))
    
    return render_template('admin/adminbacground.html')

# ---------------------Admin Panel Project Delete Web page -------------------
@app.route('/admin/backgroundimg-delete/<int:id>', methods=['GET','POST'])
@login_required
def backgoundelete(id):
    proje = Backgroundimg.query.get_or_404(id)
    db.session.delete(proje)
    db.session.commit()
    return redirect(url_for('adminmain'))

# >>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel Home End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# >>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel MyProject Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ---------------------Admin Panel MyProject Web page ----------------
@app.route('/admin/pro',methods=['GET','POST'])
@login_required
def adminpro():
    if request.method=='POST':
        file = request.files['pfile']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        proinfo=Projectin(
            protime=request.form.get('cardTime'),
            protitle=request.form.get('cardTitle'),
            prosortcut=request.form.get('cardText'),
            projareya = request.form.get('projareya'),
            cardTextadd=request.form.get('cardTextadd'),
            projareya2 = request.form.get('projareya2'),
            projtitle = request.form.get('projtitle'),
            listp =request.form.get('listp'),
            listp1 =request.form.get('listp1'),
            listp2 =request.form.get('listp2'),
            listp3 =request.form.get('listp3'),
            listp4 =request.form.get('listp4'),
            listp5 =request.form.get('listp5'),
            listp6 =request.form.get('listp6'),
            listp7 =request.form.get('listp7'),
            projareya3 = request.form.get('projareya3'),
            proimg=filename
        )
        db.session.add(proinfo)
        db.session.commit()
        return redirect(url_for('adminmain'))
    
    return render_template('admin/adminpanelpro.html')



# ---------------------Admin Panel Project Delete Web page -------------------
@app.route('/admin/Project-delete/<int:id>', methods=['GET','POST'])
@login_required
def projectdelete(id):
    proje = Projectin.query.get_or_404(id)
    db.session.delete(proje)
    db.session.commit()
    return redirect(url_for('adminmain'))

# -----------------------Admin Panel MyProject Edit Web page --------------------
@app.route('/admin/pro/edit/<int:id>', methods=['GET','POST'])
@login_required
def editpro(id):
    proce=Projectin.query.get_or_404(id)
    if request.method=='POST':
        file = request.files['pfile']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        proce.protime=request.form.get('cardTime')
        proce.protitle=request.form.get('cardTitle')
        proce.prosortcut=request.form.get('cardText')
        proce.projareya = request.form.get('projareya')
        proce.cardTextadd=request.form.get('cardTextadd')
        proce.projareya2 = request.form.get('projareya2')
        proce.projtitle = request.form.get('projtitle')
        proce.listp =request.form.get('listp')
        proce.listp1 =request.form.get('listp1')
        proce.listp2 =request.form.get('listp2')
        proce.listp3 =request.form.get('listp3')
        proce.listp4 =request.form.get('listp4')
        proce.listp5 =request.form.get('listp5')
        proce.listp6 =request.form.get('listp6')
        proce.listp7 =request.form.get('listp7')
        proce.projareya3 = request.form.get('projareya3')
        proce.proimg=filename
        db.session.commit()
        return redirect(url_for("adminmain"))
    
    return render_template('admin/editpro.html',proce=proce)

# >>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel MyProject End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    




# >>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel About Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ---------------------Admin Panel About Web page ---------------

@app.route('/admin/about',methods=['GET','POST'])
@login_required
def adminabout():
    if request.method=='POST':
        file = request.files['afile']
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        aboutinfo=Aboutin(
            aboutinfo1=request.form.get('info1'),
            aboutinfo2=request.form.get('info2'),
            disgen1=request.form.get('disgen1'),
            disgen1interest=request.form.get('disgen1interest'),
            disgen2=request.form.get('disgen2'),
            disgen2interest=request.form.get('disgen2interest'),
            disgen3=request.form.get('disgen3'),
            disgen3interest=request.form.get('disgen3interest'),
            disgen4=request.form.get('disgen4'),
            disgen4interest=request.form.get('disgen4interest'),
            disgen5=request.form.get('disgen5'),
            disgen5interest=request.form.get('disgen5interest'),
            aboutinfoimg=filename
        )
        db.session.add(aboutinfo)
        db.session.commit()
        return redirect(url_for('adminmain'))
    
    return render_template('admin/admipanelabout.html')


# ----------------Admin Panel About Delete Web page ----------------------------
@app.route('/admin/about-delete/<int:id>', methods=['GET','POST'])
@login_required
def aboutdelete(id):
    home = Aboutin.query.get_or_404(id)
    db.session.delete(home)
    db.session.commit()
    return redirect(url_for('adminmain'))

# -----------------------Admin Panel About Edit Web page ----------------------
@app.route('/admin/about/edit/<int:id>', methods=['GET','POST'])
@login_required
def editabout(id):
    aboute=Aboutin.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files.get('afile')
        print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        aboute.aboutinfo1=request.form.get('info1')
        aboute.aboutinfo2=request.form.get('info2')
        aboute.disgen1=request.form.get('disgen1')
        aboute.disgen1interest=request.form.get('disgen1interest')
        aboute.disgen2=request.form.get('disgen2')
        aboute.disgen2interest=request.form.get('disgen2interest')
        aboute.disgen3=request.form.get('disgen3')
        aboute.disgen3interest=request.form.get('disgen3interest')
        aboute.disgen4=request.form.get('disgen4')
        aboute.disgen4interest=request.form.get('disgen4interest')
        aboute.disgen5=request.form.get('disgen5')
        aboute.disgen5interest=request.form.get('disgen5interest')
        aboute.aboutinfoimg=filename
        db.session.commit()
        return redirect(url_for("adminmain"))
    return render_template('admin/editabout.html',aboute=aboute)



# >>>>>>>>>>>>>>>>>>>>>>>>> Admin Panel About End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

