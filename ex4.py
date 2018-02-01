# Variables and Names
cars = 100
spaceInACar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInACar
averagePassengersPerCar = passengers / carsDriven

print("There are", cars, "cars available.")  # Don't have to + things
print("There are only", drivers, "drivers available.")
print("There will be", carsNotDriven, "empty cars today.")
print("We can transport", carpoolCapacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", averagePassengersPerCar,
      "passengers in each car.")
