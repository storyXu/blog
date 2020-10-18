import logging; logging.basicConfig(level=logging.INFO)

from aiohttp import web
import pymysql

host = '127.0.0.1'
user = 'root'
password = 'root'
port = 3306

mysql = pymysql.connect(host=host, user=user, password=password, port=port)

cursor = mysql.cursor()

sql = 'select * from awesome.blogs'

cursor.execute(sql)

results = cursor.fetchall()

print(results)

def handle(request):
  return web.Response(text='123')

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
  web.run_app(app)
