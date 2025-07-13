MOD = 10 ** 9 + 7

class OrderType:
    SELL = 1
    BUY = 0

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        if not orders:
            return 0

        buys_maxheap = []
        sells_minheap = []

        for order in orders:
            price, qty, order_type = order
            if order_type == OrderType.SELL:
                heapq.heappush(sells_minheap, (price, qty))

            if order_type == OrderType.BUY:
                heapq.heappush(buys_maxheap, (-price, qty))

            while buys_maxheap and sells_minheap and -buys_maxheap[0][0] >= sells_minheap[0][0]:
                buy_price, buy_qty = heapq.heappop(buys_maxheap)
                buy_price = -buy_price
                sell_price, sell_qty = heapq.heappop(sells_minheap)

                trade = min(sell_qty, buy_qty)

                if buy_qty - trade > 0:
                    heapq.heappush(buys_maxheap, (-buy_price, buy_qty - trade))
                
                if sell_qty - trade > 0:
                    heapq.heappush(sells_minheap, (sell_price, sell_qty - trade))

        
        res = 0
        for order in buys_maxheap:
            res += order[1] 
            res %= MOD

        for order in sells_minheap:
            res += order[1]
            res %= MOD

        return res

        