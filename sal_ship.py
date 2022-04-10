'''this program takes the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.'''

weight = 4.8

#Ground Shipping
ground_flat = 20
if weight <= 2 :
  ground_cost = ground_flat + (1.5*weight)
elif weight <= 6:
  ground_cost = ground_flat + (3*weight)
elif weight <= 10:
  ground_cost = ground_flat + (4*weight)
elif weight > 10:
  ground_cost = ground_flat + (4.75 * weight)

print("Ground Shipping Cost: $", ground_cost)

premium_ground_shipping = 125.00

print("Premium Ground Shipping Cost: $", premium_ground_shipping)

#Drone Shipping
if weight <= 2 :
  drone_cost = (4.5*weight)
elif weight <= 6:
  drone_cost = (9*weight)
elif weight <= 10:
  drone_cost = (12*weight)
elif weight > 10:
  drone_cost = (14.25 * weight)

print("Drone Shipping Cost: $", drone_cost)
