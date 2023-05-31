class UndergroundSystem:
    class Passenger:
        def __init__(self, id, stationName, time):
            self.id = id
            self.stationName = stationName
            self.time = time

    class Route:
        def __init__(self):
            self.total = 0
            self.count = 0

        def update(self, difference):
            self.count += 1
            self.total += difference

        def getAvg(self):
            return self.total / self.count

    def __init__(self):
        self.passengersArrivals = {}
        self.routeAverage = {}        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengersArrivals[id] = self.Passenger(id, stationName, t)        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        arrivePassenger = self.passengersArrivals[id]
        del self.passengersArrivals[id]

        difference = t - arrivePassenger.time
        key = arrivePassenger.stationName + ',' + stationName

        average = self.routeAverage.get(key, self.Route())
        average.update(difference)

        self.routeAverage[key] = average       

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + ',' + endStation
        return self.routeAverage[key].getAvg()


# intuion:
# 1. Have a passenger and route encapsulation with the required data.
# 2. For route, we also need methods to update the average and get the average.
# 3. Keep a dictionary of passengers and routes and update the passengers dictionary when they check in and check out.
# 4. When they check out, get the difference between the check in time and check out time and update the route average.
# 5. Return the average when asked for it.

# solution:
# 1. Create a passenger class with id, stationName and time and a constructor to initialize them.
# 2. Create a route class with total(total time) and count(number of passengers) and a constructor to initialize them. Also, create a method to update the total and count and a method to get the average.
# 3. Create a dictionary of passengers and routes and initialize it in the constructor.
# 4. When a passenger checks in, add the passenger to the dictionary with the id as the key and the passenger object as the value.
# 5. When a passenger checks out, get the passenger object from the dictionary using the id and delete the entry from the dictionary. Get the difference between the check in time and check out time and update the route average. If the route is not in the dictionary, create a new route object and add it to the dictionary. If the route is already in the dictionary, update the route average.
# 6. When asked for the average, get the route object from the dictionary and return the average.

# Time Complexity:
# 1. checkIn: O(1) as we are just adding the passenger to the dictionary.
# 2. checkOut: O(1) as we are just getting the passenger from the dictionary and updating the route average.
# 3. getAverageTime: O(1) as we are just getting the route object from the dictionary and returning the average.

# Space Complexity: O(P + R) where P is the number of passengers and R is the number of routes. We are storing the passengers and routes in the dictionary.