from app import db, Countries, Cities
db.create_all() # Creates all table classes defined

UK = Countries(name = 'United Kingdom') #Add example to countries table
db.session.add(UK)
db.session.commit()

# Here we reference the country that london belongs to useing 'country', this is what we named the backref variable in db.relationship()
ldn = Cities(name='London', country = UK)
mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())

db.session.add(ldn)
db.session.add(mcr)
db.session.commit()
