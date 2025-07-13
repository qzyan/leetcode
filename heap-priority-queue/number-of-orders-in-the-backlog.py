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
                while buys_maxheap and -buys_maxheap[0][0] >= price and qty:
                    buy_price, buy_qty = heapq.heappop(buys_maxheap)
                    buy_price = -buy_price
                    if buy_qty == qty:
                        qty = 0
                    elif buy_qty > qty:
                        heapq.heappush(buys_maxheap, (-buy_price, buy_qty - qty))
                        qty = 0
                    else:
                        qty -= buy_qty
            
                if qty:
                    heapq.heappush(sells_minheap, (price, qty))

            elif order_type == OrderType.BUY:
                while sells_minheap and sells_minheap[0][0] <= price and qty:
                    sell_price, sell_qty = heapq.heappop(sells_minheap)
                    if sell_qty == qty:
                        qty = 0
                    elif sell_qty > qty:
                        heapq.heappush(sells_minheap, (sell_price, sell_qty - qty))
                        qty = 0
                    else:
                        qty -= sell_qty

                if qty:
                    heapq.heappush(buys_maxheap, (-price, qty))

        res = 0
        for order in buys_maxheap:
            res += order[1] 
            res %= MOD

        for order in sells_minheap:
            res += order[1]
            res %= MOD

        return res

        