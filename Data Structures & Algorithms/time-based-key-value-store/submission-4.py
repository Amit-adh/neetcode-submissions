class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.keys.get(key)

        if not vals:
            return ""

        n = len(vals)

        left = 0
        right = len(vals) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if vals[mid][0] == timestamp:
                return self.keys.get(key)[mid][1]
            elif vals[mid][0] > timestamp:
                    right = mid - 1
            else:
                left = mid + 1

        if right and timestamp < vals[0][0]:
            return ""
        return vals[right][1] or ""


