class OrderedStream:

    def __init__(self, n: int):
        self.vals = [""] * n
        self.last_unreturned_idx = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.vals[idKey] = value
        if idKey > self.last_unreturned_idx:
            return []

        results = []
        while idKey < len(self.vals) and self.vals[idKey] != "":
            results.append(self.vals[idKey])
            idKey += 1

        self.last_unreturned_idx = idKey
        return results
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)