#from db.demo import session,nav
#for i in session.query(nav).all():
    #print(i.name)

from db.bs_nav import bs_nav
from db import get_session
DB_URI = f'mysql+pymysql://root:123456@192.168.113.1:3306/mine'
g = get_session(DB_URI)()
#for i in g.query(bs_nav).all():
    #print(i.name)

