// # https://leetcode.com/problems/design-underground-system/
class UndergroundSystem {
  constructor() {
    this.stationConnections = {};
    this.checkedInCustomers = {};
  }

  checkIn(id, stationName, t) {
    this.checkedInCustomers[id] = [stationName, t];

    if (!this.stationConnections[stationName]) {
      this.stationConnections[stationName] = {};
    }
  }

  checkOut(id, stationName, t) {
    const startData = this.checkedInCustomers[id];
    const startStation = startData[0];
    const startTime = startData[1];
    const travelTime = t - startTime;

    const startOfConnection = this.stationConnections[startStation];

    if (!startOfConnection[stationName]) {
      startOfConnection[stationName] = [travelTime];
    } else {
      startOfConnection[stationName].push(travelTime);
    }

    delete this.checkedInCustomers[id];
  }

  getAverageTime(startStation, endStation) {
    const timeData = this.stationConnections[startStation][endStation];
    const sum = timeData.reduce((a, b) => a + b, 0);
    return sum / timeData.length;
  }
}

const x = [
  'checkIn',
  'checkOut',
  'getAverageTime',
  'checkIn',
  'checkOut',
  'getAverageTime',
  'checkIn',
  'getAverageTime',
  'checkIn',
  'getAverageTime',
  'getAverageTime',
  'checkOut',
];
const y = [
  [37043, 'K2618O72', 29],
  [37043, 'U1DTINDT', 39],
  ['K2618O72', 'U1DTINDT'],
  [779975, 'K2618O72', 112],
  [779975, 'CN3K6CYM', 157],
  ['K2618O72', 'U1DTINDT'],
  [706901, 'K2618O72', 221],
  ['K2618O72', 'CN3K6CYM'],
  [18036, 'K2618O72', 258],
  ['K2618O72', 'U1DTINDT'],
  ['K2618O72', 'CN3K6CYM'],
  [18036, 'U1DTINDT', 293],
];

const undergroundSystem = new UndergroundSystem();
for (let i = 0; i < x.length - 1; i++) {
  if (y[i].length === 3) {
    undergroundSystem[x[i]](y[i][0], y[i][1], y[i][2]);
  } else {
    console.log(undergroundSystem[x[i]](y[i][0], y[i][1]));
  }
}
