#!/usr/bin/env python
class TestHandler(self):

    def write_form(self, username="", uerror="", perror="", verror="", merror="", mail=""):
        self.response.out.write(form % {"username":escape_html(username),
                                        "uerror":uerror,
                                        "perror":perror,
                                        "verror":verror,
                                        "merror":merror,
                                        "mail":escape_html(mail)})
    
    def get(self):
        self.write_form()
    def post(self):
        username = re.search("^[a-zA-Z0-9_-]{3,20}$", self.request.get("username"))
        password = re.search("^.{3,20}$", self.request.get("password"))
        vpassword = self.request.get("verify")
        pass1 = self.request.get("password")
        flag = True
        if self.request.get("email"):
            email = re.search("^[\S]+@[\S]+\.[\S]+$", self.request.get("email"))
            if email:
                emailf = True
            else:
                emailf = False
        else:
            flag = False
            email = ''
            emailf = True
            
        if not (username and password and vpassword and emailf and vpassword == pass1):
            uerror = ''
            perror = ''
            verror = ''
            merror = ''
            if not username:
                uerror = "That's not a valid username."
            if not password:
                perror = "That wasn't a valid password."
            elif pass1 != vpassword:
                verror = "Your passwords didn't match."
            if flag:
                if not email:
                    merror = "That's not a valid email."
            username = self.request.get("username")
            email = self.request.get("email")
            self.write_form(username, uerror, perror, verror, merror, email)
        else:
            self.redirect("/welcome?username=%s" % self.request.get("username"))

