from .base import TabBase,relationship,Integer,String,Text,ForeignKey,DateTime,Float,Column,UniqueConstraint,Index,ForeignKey
#数据库表模型
class bs_nav(TabBase):
    __tablename__ = 'nav'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(100))
    description = Column(String(100))
    url = Column(String(100))
    path = Column(String(100))