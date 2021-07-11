from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
DB_URI = f'mysql+pymysql://root:123456@192.168.113.1:3306/mine'

engine = create_engine(DB_URI)
Base = declarative_base()  # SQLORM基类
class nav(Base):
    __tablename__  = 'nav'
    id = Column(Integer,primary_key = True, autoincrement = True)
    name = (Column(String(256)))
    description = (Column(String(256)))
    url = (Column(String(256)))
    path = (Column(String(256)))
#Base.metadata.create_all()  # 将模型映射到数据库中
session = sessionmaker(engine)()  # 构建session对象