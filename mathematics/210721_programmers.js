// https://programmers.co.kr/learn/courses/30/lessons/12911

// 문제 설명
// 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

// 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
// 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
// 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
// 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

// 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

// 제한 사항
// n은 1,000,000 이하의 자연수 입니다.

// 입출력 예
// n	result
// 78	83
// 15	23

function decToBin(n) {
  let binaryNum = "";
  while (n > 1) {
    binaryNum = String(n % 2) + binaryNum;
    n = Math.floor(n / 2);
  }
  binaryNum = String(n) + binaryNum;
  return binaryNum;
}

// 👇🏻 당연하지만 시간 초과 코드

function lessEfficientSolution(n) {
  const binaryNum = decToBin(n);
  console.log(n, binaryNum);
  const oneCount = binaryNum.match(/1/g || []).length;

  let nextNum = n;
  while (true) {
    nextNum++;
    const nextNumBin = decToBin(nextNum);
    const oneCountOfNextNum = nextNumBin.match(/1/g || []).length;
    if (oneCountOfNextNum === oneCount) {
      break;
    }
  }
  return nextNum;
}

// 다른 방안.. 하지만 테스트케이스 일부 통과 못함.

function solution(n) {
  const binaryNum = decToBin(n);
  const oneCount = binaryNum.match(/1/g || []).length;
  const zeroCount = binaryNum.length - oneCount;

  let answer = binaryNum.split("");
  let leftOnes = oneCount;
  let leftZeroes = zeroCount;
  let idxSwitched = false;

  let i;
  for (i = 0; i < answer.length - 1; i++) {
    if (answer[i] === "1") {
      leftOnes--;
    }

    if (answer[i] === "0") {
      leftZeroes--;
    }

    if (answer[i] === "0" && answer[i + 1] === "1") {
      answer[i] = "1";
      answer[i + 1] = "0";
      idxSwitched = true;
      leftOnes--;

      const tail = makeTail(leftZeroes, leftOnes);
      answer = answer.slice(0, i + 2).concat(tail);
      break;
    }
  }
  if (!idxSwitched) {
    const tail = makeTail(zeroCount, oneCount-1);
    answer = ["1", "0"].concat(tail);
  }
  return binToDec(answer.join(""));
}

function binToDec(n) {
  n = String(n);
  let answer = 0;
  for (let i = 0; i < n.length; i++) {
    answer += Number(n[i]) * (2 ** (n.length - 1 - i));
  }
  return answer;
}

function makeTail(zeroCount, oneCount) {
  let zeroes;
  let ones;

  if (zeroCount === 0) {
    zeroes = [];
  } else {
    zeroes = new Array(zeroCount).fill("0");
  }

  if (oneCount === 0) {
    ones = [];
  } else {
    ones = new Array(oneCount).fill("1");
  }

  const tail = zeroes.concat(ones);
  return tail;
}

console.log(solution(15));
