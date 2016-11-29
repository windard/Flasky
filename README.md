## Flasky

《Flask Web 开发：基于Python的 web 应用开发实战》示例，其实也是 Flask 的官方教程的一个完整示例，演示如何使用 Flask 完成一个真正的大型网站项目。

cent OS 7 上完整重现

```
sudo yum install python-pip
sudo yum install python-devel
sudo yum install zlib-devel
sudo yum install libjpeg-turbo-devel
sudo yum install mariadb-server mysql-devel mysql-common mysql-libs gcc
```

启动 MySQL，修改 MySQL 编码。

```
pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

```
python manage.py db init
python manage.py db upgrade
```

```
python manage.py shell

db.drop_all()
db.create_all()
Role.insert_roles()

```

```
nohup python manage.py runserver --host=0.0.0.0 --port=80 >flasky.log &
```

```
// 产生 count 个随机用户
User.generate_fake(count=100)
// 产生 count 篇随机文章
Post.generate_fake(count=100)
// 让已有的每一位用户关注自己
User.add_self_follows()
```

Windows 

```
set MAIL_USERNAME=XXX
set MAIL_PASSWORD=XXX
set FLASKY_ADMIN=XXX
set DEV_DATABASE_URL=XXX
```

Linux

```
export MAIL_USERNAME=XXX
export MAIL_PASSWORD=XXX
export FLASKY_ADMIN=XXX
export DEV_DATABASE_URL=XXX
```

Mark 一下
- 下次的站将所有的 `db.String()` 换成 `db.Unicode()` , 将所有的 `db.Text()` 换成 `db.UnicodeText`
- 下次的站用 `flask-avatar` 替代 `Gravtar`
- 在使用 `bleach` 的 `clean` 的时候，也要注意那个标签的顺序，这样才能够在解析的时候不会发生在解析 `li` 的时候把 `ul` 给解析没有的了问题。
- `Flask-Captcha` 可以使用 验证码，可惜只支持 Python 3.3+ ，使用 `wheezy.captcha` 替代
- 使用 `Flask-WhooshAlchemy` 来进行全文搜索
- HTTP 的基本认证方式是 `Authorization` 的 header ，参数是 `Basic base64(email:password)` 或者是 `token`
- HTTP 传送 json 格式的数据，需要发送请求头 `Content-Type: application/json`，然后数据段使用 json 格式书写
- 在 flask 下使用 SQLAlchemy 实现数据库关系继承，使用抽象的父类，即不在数据库中创建，然后分发出来两个子类，在数据库中创建表并使用，好像叫做混合继承（Concrete Table Inheritance）,这两个子类有部分相同的数据域也有部分不同的数据域，同时有相同的第三个表的外键。