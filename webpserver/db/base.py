from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import Integer,String,Text,ForeignKey,DateTime,Float,Column,UniqueConstraint,Index
from sqlalchemy.orm import relationship,sessionmaker

TabBase = declarative_base()
