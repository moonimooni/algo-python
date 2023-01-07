/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  const charMap = new Map();

  for (const char of s) {
    if (charMap[char]) {
      charMap[char] += 1;
    } else {
      charMap[char] = 1;
    }
  }

  let isOddExists = 0;
  const vals = Object.values(charMap);

  const ret = vals.reduce((acc, val) => {
    if (val % 2 === 0) {
      return acc + val;
    } else {
      isOddExists = 1;
    }
    return acc + val - 1;
  }, 0);

  return ret + isOddExists;
};

console.log(longestPalindrome('bananas'));
