import logging; logging.basicConfig(level=logging.INFO)

from aiohttp import web
import aiohttp_jinja2
import jinja2
import pymysql
import json

host = '127.0.0.1'
user = 'root'
password = 'root'
port = 3306

mysql = pymysql.connect(host=host, user=user, password=password, port=port)

routes = web.RouteTableDef()

@routes.get('/')
@aiohttp_jinja2.template('index.jinja2')
async def handleContent(request):
  sql = 'select * from awesome.blogs'
  cursor = mysql.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  content = []
  if not rows: 
    cursor.close()
    mysql.close()
    return
  else:
    for row in rows:
      content.append({
        "id": row[0],
        "username": row[2],
        "title": row[4],
        "content": row[6],
        "create_time": row[7]
      })
    return {'list': content}
  # return web.json_response(content)
  # return web.json_response(json.dumps({"code": 200, "list": content}, sort_keys=True, indent=4, separators=(',', ': '))) 

@routes.get('/article/:id')
@aiohttp_jinja2.template('article.jinja2')
def showArtlce(request):
  return web.json_response({'data': 123})

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./views'))
# app = Flask(__name__, template_folder='./views')
app.add_routes(routes)

if __name__ == '__main__':
  web.run_app(app)
  
