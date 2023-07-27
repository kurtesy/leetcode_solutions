class UndergroundSystem:

    def __init__(self):
        self._in = {}
        self.out = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName in self._in:
            self._in[stationName][id] = t
        else:
            self._in[stationName] = {}
            self._in[stationName][id] = t
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if stationName in self.out:
            self.out[stationName][id] = t
        else:
            self.out[stationName] = {}
            self.out[stationName][id] = t
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        print(self._in, self.out)
        start = self._in[startStation]
        end = self.out[endStation]
        ids = [*start.keys()] + [*end.keys()]
        total_time = 0
        passenger_cnt = 0
        for _id in ids:
            if _id in start and _id in end:
                passenger_cnt += 1
                total_time += end[_id] - start[_id]
        return total_time/passenger_cnt





# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)