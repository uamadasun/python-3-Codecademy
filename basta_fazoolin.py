class Menu:
  #Menu class with 4 parameters: type of meal(brunch, dinner, early bird, etc.), 
  #list of items in the menu, and when the type of meal is offered
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def calculate_bill(self, purchased_items):
    '''
    Calculates how much the bill is based on a list of purchased items.
    Input - list of purchased items
    output - total price of meal
    '''
    count = 0
    total_price = 0
    while count < len(purchased_items):
      price = self.items[purchased_items[count]]
      total_price += price
      count+= 1
    return total_price

  def __repr__(self):
    '''
    prints a string telling customer which menu they are 
    looking at and what time the restaurant offers the menu.
    '''
    return("You are looking at the {n} menu. This menu is available from {s} to {e}.".format(n = self.name, s= self.start_time, e = self.end_time))

class Franchise:
  '''
  Franchise class that takes an address and menu for the franchise
  '''

  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return "The address of this franchise is {a}.".format(a=self.address)
  
  def available_menus(self, time):
    '''
    lets customers know what menus are available at the time they want to dine.
    input - time they customer arrives at the restaurant
    output - menus that are available for the customer at that time
    '''
    available_menu = []
    for menu in self.menus:
      start = menu.start_time
      end = menu.end_time
      if start <= time and end >= time:
        available_menu.append(menu.name)
    count = 0
    while count < len(available_menu):
      return ("The {} menu/s is/are available.".format(' & '.join(available_menu)))

class Business:
  #creating a new business class that takes the business' name and list of franchises under the business
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#creating brunch instance of the menu class
brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 1100, 1600)

#creating early bird instance of the menu class
early_bird = Menu("Early Bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 1500, 1800)

#creating dinner instance of the menu class
dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 1700, 2300)

#creating kids meal instance of the menu class
kids = Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 1100, 2100)

# print(brunch)
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#creating new instances of the Franchise class with the address of the Franchises and a list of menus available at each restaurant
flagship_store = Franchise("1232 West End Road",[brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# print(new_installment.available_menus(1700))

# creating new instance of the Business class with the restaurant name and its franchises in a list
business_one = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#creating a new menu instance of the menu class
arepas_menu = Menu("Take a' Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])

business_two = Business("Take a' Arepa", arepas_place)
