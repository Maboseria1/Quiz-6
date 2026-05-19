from typing import List

class Solution:
    def findCheapestPrice(
        self, 
        n: int, 
        flights: List[List[int]], 
        src: int, 
        dst: int, 
        k: int
    ) -> int:
        
        # Infinity means we do not know how to reach that city yet
        INF = float("inf")

        # prices[i] = cheapest cost to reach city i
        prices = [INF] * n

        # Cost to reach the starting city is 0
        prices[src] = 0

        # We can take at most k + 1 flights
        # Example: k = 1 stop means src -> middle -> dst, which is 2 flights
        for i in range(k + 1):

            # Make a copy so this round only uses results from the previous round
            # This prevents using too many flights in one iteration
            temp = prices.copy()

            # Try every flight and see if it gives a cheaper price
            for from_city, to_city, price in flights:

                # If we cannot reach from_city yet, skip it
                if prices[from_city] == INF:
                    continue

                # New possible cost to reach to_city
                new_cost = prices[from_city] + price

                # If this route is cheaper, update temp
                if new_cost < temp[to_city]:
                    temp[to_city] = new_cost

            # Move to the next round
            prices = temp

        # If destination is still infinity, there is no valid route
        if prices[dst] == INF:
            return -1

        # Otherwise return the cheapest price
        return prices[dst]
