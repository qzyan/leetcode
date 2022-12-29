class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return ''
        
        val_symbol_map = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        
        romans = []
        
        while num:
            if num >= 1000:
                unit = 1000
            elif 100 <= num < 1000:
                unit = 100
            elif 10 <= num < 100:
                unit = 10
            elif 1<= num < 10:
                unit = 1
            
            
            count = num // unit
            num -= count * unit
            if count == 4:
                romans.append(val_symbol_map[unit])
                romans.append(val_symbol_map[unit * 5])
            elif count == 9:
                romans.append(val_symbol_map[unit])
                romans.append(val_symbol_map[unit * 10])
            elif count < 4:
                for _ in range(count):
                    romans.append(val_symbol_map[unit])
            elif count < 9:
                romans.append(val_symbol_map[unit * 5])
                for _ in range(count - 5):
                    romans.append(val_symbol_map[unit]) 
        print(romans)
        return ''.join(romans)