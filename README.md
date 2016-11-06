## Flasky

《Flask Web 开发：基于Python的 web 应用开发实战》示例，其实也是 Flask 的官方教程的一个完整示例，演示如何使用 Flask 完成一个真正的大型网站项目。

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
// 产生 count 个随机用户
User.generate_fake(count=100)
// 产生 count 篇随机文章
Post.generate_fake(count=100)
// 让已有的每一位用户关注自己
User.add_self_follows()
```