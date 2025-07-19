M = 10 ** 9 + 7
class TradeType:
    BUY = 0
    SELL = 1
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        if not orders:
            return 0
        buy_max_heap = [] # [[-50, 5], [-40, 3], ....] get the highest buy order
        sell_min_heap = [] # [[30, 5], [60, 3], ....] get the lowest sell order
        for order in orders:
            p, qty, order_type = order
            if order_type == TradeType.BUY:
                heapq.heappush(buy_max_heap, (-p, qty))
            else:
                heapq.heappush(sell_min_heap, (p, qty))

            while buy_max_heap and sell_min_heap:
                buy_max_p = -buy_max_heap[0][0]
                sell_min_p = sell_min_heap[0][0]
                if buy_max_p < sell_min_p:
                    break
                
                b_price, b_qty = heapq.heappop(buy_max_heap)
                b_price = -b_price
                s_price, s_qty = heapq.heappop(sell_min_heap)

                deal_qty = min(b_qty, s_qty)

                if b_qty - deal_qty > 0:
                    heapq.heappush(buy_max_heap, (-b_price, b_qty - deal_qty))

                if s_qty - deal_qty > 0:
                    heapq.heappush(sell_min_heap, (s_price, s_qty - deal_qty))

        res = self.get_count(buy_max_heap) + self.get_count(sell_min_heap)
        return res % M
        
    def get_count(self, orders):
        result = 0
        for order in orders:
            _, qty = order
            result += qty
            result % M
        return result

    