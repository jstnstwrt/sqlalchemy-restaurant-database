from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

myFirstRestaurant = Restaurant( name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

cheesepizza = MenuItem( name = "Cheese Pizza", description = "Made with all natural ingredients"
				, course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()

# firstResult = session.query(Restaurant).first()
# print firstResult.name

items =  session.query(Restaurant).all()
for item in items:
	print item.name