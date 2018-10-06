from cmdb import sql_main
from sqlalchemy.orm import sessionmaker
import re

Session_class=sessionmaker(bind=sql_main.engine)

Session=Session_class()


def AdminUser(u,p):
    user_obj=Session.query(sql_main.AdminUser).filter(sql_main.AdminUser.user==u,
                                                      sql_main.AdminUser.password ==p).first()

    return user_obj

def Userhost():
    host_obj=Session.query(sql_main.UserHost.id,sql_main.UserHost.ip,
                         sql_main.UserHost.user,sql_main.UserHost.password,
                         sql_main.UserHost.port,sql_main.UserHost.Asset_group,
                         sql_main.UserHost.business,sql_main.UserHost.Admin).all()
    return host_obj

def IsIP(str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False

def IsPort(number):
        if number >0 and number<65535:
            return True
        else:
            return False

def LenGth(password,business,Asset_group,Admin):
    if len(password)<10 and len(business)<10 and len(Asset_group) and len(Admin):
        return True
    else:
        return False



def AddUserHost(ip,port,user,password,business,Asset_group,Admin):
    ip2=IsIP(str(ip))
    port2=int(port)
    port3=IsPort(port2)
    if ip2:
        if port3:
            if LenGth(password,business,Asset_group,Admin):
                s8=sql_main.UserHost(ip=ip,port=port,user=user,password=password,business=business,Asset_group=Asset_group,Admin=Admin)
                Session.add_all([s8])
                Session.commit()
                return True
        return False
    return False


def sql_host(id):
    x=Session.query(sql_main.UserHost).filter(sql_main.UserHost.id==id).first()
    if x:
        return x

def deleter(id):
    x=Session.query(sql_main.UserHost).filter(sql_main.UserHost.id==id).first()
    Session.delete(x)
    Session.commit()