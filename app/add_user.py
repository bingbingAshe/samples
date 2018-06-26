from app import db, models
import datetime
# db.create_all()
u = models.User(nickname='john', email='john@email.com')
db.session.add(u)
db.session.commit()
u1 = models.User(nickname='susan', email='susan@email.com')
db.session.add(u1)
db.session.commit()

print(models.User.query.all())
for u2 in models.User.query.all():
	print(u2.id, u2.nickname)
	
u3 = models.User.query.get(1)
p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u3)
db.session.add(p)
db.session.commit()



