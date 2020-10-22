import logging; logging.basicConfig(level=logging.INFO)

from aiohttp import web
import pymysql
import json

host = '127.0.0.1'
user = 'root'
password = 'root'
port = 3306

mysql = pymysql.connect(host=host, user=user, password=password, port=port)

routes = web.RouteTableDef()

@routes.get('/')
def index(request):
  return web.Response(text="欢迎来到小楠子的博客")

@routes.get('/getContent')
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
  return web.json_response(content)
  # return web.json_response(json.dumps({"code": 200, "list": content}, sort_keys=True, indent=4, separators=(',', ': '))) 


app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':

  web.run_app(app)
  
