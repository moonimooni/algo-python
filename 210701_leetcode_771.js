/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
  const jewelsArr = jewels.split("");
  const stonesArr = stones.split("");
  let answer = 0;
  jewelsArr.forEach((jewel) => {
    const found = stonesArr.filter((stone) => stone === jewel);
    answer += found.length;
  });
  return answer;
};
