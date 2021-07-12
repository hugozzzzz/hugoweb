from fastapi import FastAPI,Form
from pydantic import BaseModel
import uvicorn
import os
from fastapi.staticfiles import StaticFiles
import base64
from webapp import g,bs_nav
class Item(BaseModel):
    id:int = None
    name:str = None
    description:str = None
    url:str = None
    collection:int = None
    path:str = None
    logobase:str = None
app = FastAPI()
app.mount('/static',StaticFiles(directory='./static'),name='static')
@app.get('/')
def root():
    return 'Hello! I am Hugo!'
#导航收藏
@app.post('/collectNav')
def collectNav(item:Item):
    try:
        item_dict = item.dict()
        col = g.query(bs_nav).filter(bs_nav.id == item_dict['id']).first().collection+1
        info = {'collection':col}        
        g.query(bs_nav).filter(bs_nav.id == item_dict['id']).update(info)
        g.commit()
        return True
    except Exception as e:
        return False
#删除导航信息
@app.post('/delNav')
def delNav(item:Item):
    try:
        item_dict = item.dict()
        g.query(bs_nav).filter(bs_nav.id == item_dict['id']).delete()
        g.commit()
        return {"result":True,"msg":'删除成功'}
    except Exception as e:
        return {"result":False,"msg":e}
#修改导航信息
@app.post('/editNav')
def editNav(item:Item):
    try:
        item_dict = item.dict()
        id = item_dict['id']
        name = item_dict['name']
        description = item_dict['description']
        url = item_dict['url']
        logobase = item_dict['logobase']
        if logobase == '':
            path = f'static/image/vue.png'  
        else:
            spbase = logobase.split(',')[1]
            logo_info = base64.b64decode(spbase)
            with open(f'static/image/{name}.png','wb') as p:
                p.write(logo_info)  
            path = f'static/image/{name}.png'  
        info = {'name':name,'description':description,'url':url,'path':path}
        g.query(bs_nav).filter(bs_nav.id == id).update(info)
        g.commit()
        return True
    except Exception as e:
        return False
#获取单条导航信息
@app.post('/getNavInfo')
def getNavInfo(item:Item):
    try:
        item_dict = item.dict()
        id = item_dict['id'] 
        info = g.query(bs_nav).filter(bs_nav.id == id).first()
        return info
    except Exception as e:
        return False
# 上传导航信息
@app.post('/upload')
def upload(item:Item):
    try:
        item_dict = item.dict()
        name = item_dict['name']
        description = item_dict['description']
        url = item_dict['url']
        logobase = item_dict['logobase']
        if logobase == '':
            path = f'static/image/vue.png'  
        else:
            spbase = logobase.split(',')[1]
            logo_info = base64.b64decode(spbase)
            with open(f'static/image/{name}.png','wb') as p:
                p.write(logo_info)  
            path = f'static/image/{name}.png'  
        info = bs_nav(name = name, description = description, url = url, path = path, collection = 0)  
        g.add(info)
        g.commit()
        return True
    except Exception as e:
        return False
# 获取导航标签信息    
@app.post('/getNavList')
def getNavList():
    try:
        navList = []
        for i in g.query(bs_nav).all():
            info = {}
            info['id'] = i.id
            info['name'] = i.name
            info['description'] = i.description
            info['url'] = i.url
            info['path'] = i.path
            info['collection'] = i.collection
            navList.append(info)
        return navList
    except Exception as e:
        return False

if __name__ == "__main__":
    moudle = "{}:app".format(os.path.splitext(os.path.basename(__file__))[0])
    #uvicorn.run(moudle,host="172.16.42.49",port=1996,reload=True)
    uvicorn.run(moudle,host="192.168.113.1",port=1996,reload=True)