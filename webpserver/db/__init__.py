from .bs_nav import bs_nav
from .base import TabBase,sessionmaker
from sqlalchemy import create_engine
#�������ݿ�
def init_db(connect_str:str,drop:bool) -> sessionmaker:
    engine = create_engine(connect_str)
    if drop:
        TabBase.metadata.drop_all(engine)
    TabBase.metadata.create_all(engine)
    return sessionmaker(bind=engine)
#�������ݿ�
def get_session(connect_str:str) -> sessionmaker:
    engine = create_engine(connect_str)
    return sessionmaker(bind=engine)