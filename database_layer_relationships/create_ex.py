from app import db, Customers, Products, Orders

db.create_all() # Creates all table classes defined

customer_1 = Customers(name = 'Kiran', email = 'kk@qa.com',)

phone1 = Products(name = 'OnePlus 6t', price = 399.99)

db.session.add(customer_1)
db.session.add(phone1)
db.session.commit()
