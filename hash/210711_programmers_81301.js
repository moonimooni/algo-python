// https://programmers.co.kr/learn/courses/30/lessons/81301
// 숫자 문자열과 영단어
// hash로 풀이 가능

function solution(s) {
  const dict = {
    zero: "0",
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
  };

  let numString = "";
  let answer = "";

  for (char of s) {
    if (Object.values(dict).includes(char)) {
      answer += char;
    } else {
      numString += char;
      if (numString in dict) {
        answer += dict[numString];
        numString = "";
      }
    }
  }
  return Number(answer);
}

console.log(solution("onetwothreefourfive"));