class Solution:
    def binaryToDecimal(self, binary: str) -> int:
        answer = 0
        for i, v in enumerate(binary):
            answer += (int(v) * (2**(len(binary)-1-i)))
        return answer

    def addBinary(self, a: str, b: str) -> str:
        sum_int = self.binaryToDecimal(a) + self.binaryToDecimal(b)
        return bin(sum_int)[2:]
