/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
  let str = s.split("");
  let removed = false;
  while (str) {
      for (let i=0; i<str.length-1; i++) {
          if (str[i] === str[i+1]) {
              str.splice(i,2);
              removed = true;
              break;
          } else {
              removed = false;
          }
      }
      if (str.length <= 1 || removed === false) {
          return str.join("");
      }
  }
};