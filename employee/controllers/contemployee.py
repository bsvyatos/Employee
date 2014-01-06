import logging
import re
import sqlalchemy as sa
import urlparse


from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from employee.lib.base import BaseController, render
from webhelpers.html.tags import stylesheet_link
from sqlalchemy.sql import exists


from employee.model import meta, Person, Department
import employee.model as model

DB_URL = "sqlite:///test.sqlite"

engine = sa.create_engine(DB_URL)
model.init_model(engine)

meta.Base.metadata.create_all(bind=engine)

log = logging.getLogger(__name__)

# SQLAlchemy 0.4 and 0.5 syntax without Declarative
#meta.metadata.drop_all(bind=engine, checkfirst=True)
#meta.metadataa.create_all(bind=engine)

class ContemployeeController(BaseController):
        
    def __init__(self):
        context_clear()
       
    def index(self):
        redirect(url(controller="contemployee", action="home"))
        
    def render_edit(self):
        c.txttosend = ''
        for p in meta.Session.query(Department):
            c.txttosend += "<option value=" + p.depart + ">" + p.depart.upper() + "</option>"
        return render('/edit.mako')
    
    def newemployee(self):
        c.state = "Add"
        c.submit = "Save"
        return self.render_edit()
    
    def form(self):
        return render('/newemp.mako')
    
    def list(self):
        c.txttosend=''
        num = 1
        for p in meta.Session.query(Person):
            c.txttosend += '<tr>'
            dep = meta.Session.query(Department.depart).filter_by(id=p.depart_id).scalar()
            c.txttosend += '<td>' + str(num) + '</td>' + '<td>' + p.sname + '</td>' + '<td>' + p.name + '</td>' + '<td>' + p.email + '</td>' + '<td>' + p.birthday + '</td>' + '<td>' + str(p.wage) + '</td>' + '<td>' + dep.upper() + '</td>'
            r = str(p.id)
            c.txttosend += '<td><button class="btn btn-warning btn-xs" id="' + r + '" onClick="click_edit(this.id)"><span class="glyphicon glyphicon-wrench"></span></button></td>'
            c.txttosend += '<td><button class="btn btn-danger btn-xs" id="' + r + '" onClick="click_del(this.id)"><span class="glyphicon glyphicon-trash"></span></button></td></tr>'
            num += 1
            
        return render('/list.mako')
    
    def home(self):
        c.txttosend = ''
        for p in meta.Session.query(Department):
            c.txttosend += "<option value=" + p.depart + ">" + p.depart.upper() + "</option>"
        return render('/home.mako')
    
    def validate(self):
        context_clear()
        c.umail = request.params['umail']
        c.uname = request.params['uname']
        upass = request.params['upass']
        c.sname = request.params['sname']
        select = request.params['select']
        c.wage = request.params['wage']
        c.ubirth = request.params['birthday_day'] + '/' + request.params['birthday_month'] + '/' + request.params['birthday_year']
        c.depart = request.params['select']
        c.state = request.params['state']
        eid = False
        if c.state == "Edit":
            eid = request.params['iid']

        if(select == 'sd'):
            c.select_msg = 'Please select department'
            
        if(c.umail):
            if(not valid_email(c.umail)):
                c.umail_msg = 'The Email you entered seems to be invalid!'
            if eid and ifexists(c.umail, 0, eid):
                c.umail_msg = 'The Email you entered already exists!'
            if not eid and ifexists(c.umail, 0):
                c.umail_msg = 'The Email you entered already exists!'
        else:
            c.umail_msg = 'Please enter Email!'
            
        if(c.sname):
            if not valid_sname(c.sname):
                c.sname_msg = 'Incorrect name'
        else:
            c.sname_msg = 'Please enter the name'

        if(c.uname):
            if(not valid_name(c.uname)):
                c.uname_msg = 'This username is invalid!'
            if eid and ifexists(c.uname, 1, eid):                    
                c.uname_msg = 'Employee with this username already exists!'
            if not eid and ifexists(c.uname, 1):
                    c.uname_msg = 'Employee with this username already exists!'
        else:
            c.uname_msg = 'Please enter employees username'
            

        if(upass):
            if(not valid_pass(upass)):
                c.upass_msg = 'The password you entered seems to be invalid'
        else:
            c.upass_msg = 'Please enter the password'
            
            
        if(not (c.umail_msg or c.upass_msg or c.uname_msg or c.select_msg or c.sname_msg)):
            if(c.state == "Edit"):
                tmpname = findid(eid)
                user = meta.Session.query(Person).get((eid, tmpname.name))
            else:
                user = Person()
                user.id = newid()
            
            if ifdepart(select):
                depid = meta.Session.query(Department.id).filter_by(depart=select).scalar()
            else:
                depid = departid()
                ndepart = Department()
                ndepart.id = depid
                ndepart.depart = select
                meta.Session.add(ndepart)
                meta.Session.commit()
                
            user.sname = c.sname
            user.name = c.uname
            user.email = c.umail
            user.password = upass
            user.depart_id = depid
            user.birthday = str(request.params['birthday_day']) + '/' + str(request.params['birthday_month']) + '/' + str(request.params['birthday_year'])
            user.wage = request.params['wage']
            
            if(c.state == "Add"):
                meta.Session.add(user)
                
            meta.Session.commit()
            return render('/success.mako')
        
        c.submit = "Add"
        if(c.state == "Edit"):
            c.iid = eid
            c.submit = "Save"
        return self.render_edit()

    
    def edit(self):
        id = int(request.params['iid'])
        user = findid(id)
        if(request.params['del'] == 'yes'):
            user = meta.Session.query(Person).get((id, findid(id).name))
            meta.Session.delete(user)
            meta.Session.commit()
            redirect(url(controller='contemployee', action='list'))
        if not user:
            redirect(url(controller='contemployee', action='home'))
        
        
        c.depart = meta.Session.query(Department.depart).filter_by(id=user.depart_id).scalar()
        c.ubirth = user.birthday
        c.uname = user.name
        c.sname = user.sname
        c.umail = user.email
        c.wage = user.wage
        c.iid = int(request.params['iid'])
        c.state = "Edit"
        c.submit = "Save"
        return self.render_edit()
    
    def check(self):
        #c.txt = 'empty'
        #tmp = meta.Session.query(Department).filter(Department.id == 1).scalar()
        #if tmp:
        #    c.txt = tmp.depart
        #depid = 1
        #ndepart = Department()
        #ndepart.id = depid
        #ndepart.depart = 'IT'
        #meta.Session.add(ndepart)
        #meta.Session.commit()
        c.txt = ''
        for txtbuff in meta.Session.query(Department):
            c.txt += txtbuff.depart + ' | '
        #if not txtbuff:
        #    return render('/check.mako')
        #c.txt = meta.Session.query(exists().where(Person.name == 'bsakjdhbf')).scalar()
        return render('/check.mako')
        
    
def findid(id):
    user = meta.Session.query(Person).filter(Person.id == id).scalar()
    if user:
        return user
    return False

def context_clear():
    c.depart = ''
    c.ubirth = ''
    c.sname_msg = ''
    c.umail_msg = ''
    c.uname_msg = ''
    c.upass_msg = ''
    c.select_msg = ''
    c.sname = ''
    c.uname = ''
    c.umail = ''
    c.wage = ''
    c.iid = ''
    
def valid_email(umail):
    if re.search("^[\S]+@[\S]+\.[\S]+$", umail):
        return True
    return False
    
def valid_pass(upass):
    if re.search("^.{3,20}$", upass):
        return True
    return False

def valid_name(uname):
    if re.search("^[a-zA-Z0-9_-]{3,20}$", uname):
        return True
    return False

def valid_sname(sname):
    if re.search(r"(?i)^[a-z ,.'-]+$", sname):
        return True
    return False

def ifexists(ename, ifname, iid = 0):
    iid = int(iid)
    
    if ifname:
        if meta.Session.query(Person).filter(Person.name == ename, Person.id != iid).all():
            return True
    else:
        if meta.Session.query(Person).filter(Person.email == ename, Person.id != iid).all():
            return True
        
    return False
        
def ifdepart(dep):
    if meta.Session.query(Department).filter(Department.depart == dep).all():
        return True
    return False

def newid():
    var = 0
    try:
        for p in meta.Session.query(Person):
            var = p.id
    except BaseException:
        return var
    return var + 1

def departid():
    var = 0
    try:
        for p in meta.Session.query(Department):
            var = p.id
    except BaseException:
        return var
    return var + 1
    