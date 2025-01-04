class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        total = 0
        gas_station = 0

        for station in range(len(gas)):
            total = total + gas[station] - cost[station]

            if total < 0:
                total = 0
                gas_station = station + 1
        return gas_station