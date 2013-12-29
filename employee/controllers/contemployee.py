import logging
import re
import sqlalchemy as sa
import urlparse


from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from employee.lib.base import BaseController, render
from webhelpers.html.tags import stylesheet_link
from sqlalchemy.sql import exists


from employee.model import meta, Person
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
        
    def newemployee(self):
        return render('/addemp.mako')
    
    def form(self):
        return render('/newemp.mako')
    
    def list(self):
        c.txttosend=''
        num = 1
        for p in meta.Session.query(Person):
            c.txttosend += '<tr>'
            c.txttosend += '<td>' + str(num) + '</td>' + '<td>' + p.sname + '</td>' + '<td>' + p.name + '</td>' + '<td>' + p.email + '</td>' + '<td>' + p.birthday + '</td>' + '<td>' + str(p.wage) + '</td>' + '<td>' + p.depart + '</td>'
            r = str(p.id)
            c.txttosend += '<td><button class="btn btn-warning btn-xs" id="' + r + '" onClick="click_edit(this.id)"><span class="glyphicon glyphicon-wrench"></span></button></td>'
            c.txttosend += '<td><button class="btn btn-danger btn-xs" id="' + r + '" onClick="click_del(this.id)"><span class="glyphicon glyphicon-trash"></span></button></td></tr>'
            num += 1
            
        return render('/list.mako')
    
    def home(self):
        return render('/home.mako')
    
    def validate(self):
        context_clear()
        c.umail = request.params['umail']
        c.uname = request.params['uname']
        upass = request.params['upass']
        c.sname = request.params['sname']
        select = request.params['select']
        c.wage = request.params['wage']
        c.ubirth = request.params['birthday']
        c.depart = request.params['select']
        ifedit = request.params['edit']
        eid = False
        if ifedit:
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
            if(request.params['edit']):
                tmpname = findid(eid)
                user = meta.Session.query(Person).get((eid, tmpname.name))
            else:
                user = Person()
                user.id = newid()

            user.sname = c.sname
            user.name = c.uname
            user.email = c.umail
            user.password = upass
            user.depart = select
            user.birthday = request.params['birthday']
            user.wage = request.params['wage']
            
            if(ifedit):
                meta.Session.commit()
                redirect(url(controller='contemployee', action='successedit'))
                
            meta.Session.add(user)
            meta.Session.commit()
            redirect(url(controller='contemployee', action='success'))
        
        if(ifedit):
            c.iid = eid
            return render('/edit.mako')
        return render('/addemp.mako')

    def success(self) :
        return render('/success.mako')
    
    def successedit(self):
        return render('/successedit.mako')
    
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
        c.depart = user.depart
        c.ubirth = user.birthday
        c.uname = user.name
        c.sname = user.sname
        c.umail = user.email
        c.wage = user.wage
        c.iid = int(request.params['iid'])
        return render('/edit.mako')
    
    def check(self):
        c.txt = 'empty'
        tmp = meta.Session.query(Person).filter(Person.id == 7).scalar()
        c.txt = tmp
        #for txtbuff in meta.Session.query(Person.id).all():
        #    c.txt += str(txtbuff) + ' | '
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
        
    

def newid():
    try:
        for p in meta.Session.query(Person):
            var = p.id
    except BaseException:
        return var
    return var + 1

    