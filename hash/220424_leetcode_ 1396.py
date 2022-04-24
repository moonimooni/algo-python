# https://leetcode.com/problems/design-underground-system/
class UndergroundSystem:

    def __init__(self):
        self.stationConnections = dict()  # 3-depth
        self.checkedInCustomers = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedInCustomers[id] = [stationName, t]
        if stationName not in self.stationConnections:
            self.stationConnections[stationName] = {}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startData = self.checkedInCustomers[id]
        startStation, startTime = startData[0], startData[1]
        travelTime = float(t - startTime)

        if stationName not in self.stationConnections[startStation]:
            self.stationConnections[startStation][stationName] = [travelTime]
        else:
            self.stationConnections[startStation][stationName].append(
                travelTime
            )

        del self.checkedInCustomers[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        timeData = self.stationConnections[startStation][endStation]
        return sum(timeData) / len(timeData)


undergroundSystem = UndergroundSystem()

x = ["checkIn", "checkOut", "getAverageTime", "checkIn", "checkOut", "getAverageTime",
     "checkIn", "getAverageTime", "checkIn", "getAverageTime", "getAverageTime", "checkOut"]
y = [
    [37043, "K2618O72", 29],
    [37043, "U1DTINDT", 39],
    ["K2618O72", "U1DTINDT"],
    [779975, "K2618O72", 112],
    [779975, "CN3K6CYM", 157],
    ["K2618O72", "U1DTINDT"],
    [706901, "K2618O72", 221],
    ["K2618O72", "CN3K6CYM"],
    [18036, "K2618O72", 258],
    ["K2618O72", "U1DTINDT"],
    ["K2618O72", "CN3K6CYM"],
    [18036, "U1DTINDT", 293]
]

for i in range(len(x)):
    print(x[i], y[i])
    callMethod = getattr(undergroundSystem, x[i])
    if len(y[i]) == 3:
        callMethod(y[i][0], y[i][1], y[i][2])
    else:
        print(callMethod(y[i][0], y[i][1]))
