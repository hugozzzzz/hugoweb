from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
from fastapi.staticfiles import StaticFiles
import base64
from webapp import g,bs_nav
class Item(BaseModel):
    name:str
    description:str
    url:str
    logobase:str
app = FastAPI()
app.mount('/static',StaticFiles(directory='./static'),name='static')
@app.get('/')
def root():
    return 'Hello! I am Hugo!'
#删除导航信息
@app.post('/delNav/{navId}')
# 上传导航信息
@app.post('/upload')
def upload(item:Item):
    try:
        item_dict = item.dict()
        name = item_dict['name']
        description = item_dict['description']
        url = item_dict['url']
        logobase = item_dict['logobase']
        spbase = logobase.split(',')[1]
        logo_info = base64.b64decode(spbase)
        with open(f'static/image/{name}.png','wb') as p:
            p.write(logo_info)  
        path = f'static/image/{name}.png'  
        info = bs_nav(name = name, description = description, url = url, path = path)  
        g.add(info)
        g.commit()
        return True
    except Exception as e:
        return e
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
            navList.append(info)
        return navList
    except Exception as e:
        return e

if __name__ == "__main__":
    moudle = "{}:app".format(os.path.splitext(os.path.basename(__file__))[0])
    #uvicorn.run(moudle,host="172.16.42.49",port=1996,reload=True)
    uvicorn.run(moudle,host="192.168.113.1",port=1996,reload=True)
