class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        position, speed = map(list, zip(*sorted(zip(position, speed), reverse=True)))

        time = []
        for x, y in zip(position, speed):
            time.append( (target - x) / y )

        stack = []
        fleets = len(time)
        for i, t in enumerate(time):
            if len(stack) == 0 or t > stack[-1]:
                stack.append(t)

        return len(stack)