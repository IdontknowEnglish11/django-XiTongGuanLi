
from cmdb import sql_main
from sqlalchemy.orm import  sessionmaker
Session_class=sessionmaker(bind=sql_main.engine)

Session=Session_class()

###创建
s2=sql_main.UserHost(ip="192.168.10.1",port="3306",user="tang6",password="asd1",business="web",Asset_group="web",Admin="admin")
s3=sql_main.UserHost(ip="192.168.10.2",port="3306",user="tang1",password="asd2",business="web",Asset_group="web",Admin="admin")
s4=sql_main.UserHost(ip="192.168.10.3",port="3306",user="tang2",password="asd3",business="web",Asset_group="web",Admin="admin")
s5=sql_main.UserHost(ip="192.168.10.4",port="3306",user="tang5",password="asd4",business="web",Asset_group="web",Admin="admin")
s6=sql_main.UserHost(ip="192.168.10.5",port="3306",user="tang4",password="asd5",business="web",Asset_group="web",Admin="admin")
s7=sql_main.UserHost(ip="192.168.10.6",port="3306",user="tang3",password="asd6",business="web",Asset_group="web",Admin="admin")
s8=sql_main.UserHost(ip="192.168.10.7",port="3306",user="tang7",password="asd7",business="web",Asset_group="web",Admin="admin")

s9=sql_main.AdminUser(user="admin",password="admin123")
Session.add_all([s2,s3,s4,s5,s6,s7,s8,s9],)

Session.commit()