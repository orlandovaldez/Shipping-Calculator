
weight = float(input("What is the weight of your package: "))
cost = 0.0
flat_charge = 0.0
#Ground Shipping
if weight <= 2:
  flat_rate = 20.00
  cost = (weight * 1.50)
  print("Cost of Ground Shipping is: $",cost)
elif weight > 2 and weight <= 6:
  flat_rate = 20.00
  cost = (weight * 3.00) + flat_rate
  print("Cost of Ground Shipping is: $",cost)
elif weight > 6 and weight <= 10:
  flat_rate = 20.00
  cost = (weight * 4.00) + flat_rate
  print("Cost of Ground Shipping is: $",cost)
else:
  flat_rate = 20.00
  cost = (weight * 4.75) + flat_rate
  print("Cost of Ground Shipping is: $",cost)
#Ground Shipping Premium
premium_shipping = 125.00
print("Cost of Ground Shipping Premium is: $",premium_shipping)
#Drone Shipping 
if weight <= 2:
  cost = (weight * 4.50)
  print("Cost of Drone Shipping is: $",cost)
elif weight >2 and weight <= 6:
  cost = (weight * 9.00)
  print("Cost of Drone Shipping is: $",cost)
elif weight >6 and weight <= 10:
  cost = (weight * 12.00)
  print("Cost of Drone Shipping is: $",cost)
else:
  cost = (weight * 14.25)
  print("Cost of Drone Shipping is: $",cost)
