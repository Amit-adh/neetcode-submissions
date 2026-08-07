class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for token in tokens:
            if token in "+-/*":
                a = ans.pop()
                b = ans.pop()

                if token == "+":
                    ans.append(a+b)
                elif token == "-":
                    ans.append(b-a)
                elif token == "*":
                    ans.append(a*b)
                else:
                    ans.append(int(b/a))
            else:
                ans.append(int(token))

        return ans[0]