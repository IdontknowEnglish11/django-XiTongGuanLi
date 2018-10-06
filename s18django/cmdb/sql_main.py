import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,VARCHAR
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:123@192.168.222.131/tang",
                       encoding='utf-8')# echo=True)

Base = declarative_base()#生成orm基类

class UserHost(Base):
    __tablename__='user_host'    #表名
    id = Column(Integer, primary_key=True)  # id
    ip = Column(VARCHAR(255), nullable=False)  # ip
    port = Column(VARCHAR(255), nullable=False)  # post
    user = Column(VARCHAR(255), nullable=False)  # 用户
    password = Column(VARCHAR(255), nullable=False)  # 密码
    business = Column(VARCHAR(255), nullable=False)  # 业务线
    Asset_group = Column(VARCHAR(255), nullable=False)  # 资产组
    Admin = Column(VARCHAR(255), nullable=False)  # 管理员




class AdminUser(Base):
    __tablename__ = 'admin_user'
    id = Column(Integer, primary_key=True)  # id
    user = Column(String(32), nullable=False)  # 用户名
    password = Column(String(32), nullable=False)  # 密码

    def __repr__(self):
        return "<%s name:%s>" % (self.id, self.user)


Base.metadata.create_all(engine)