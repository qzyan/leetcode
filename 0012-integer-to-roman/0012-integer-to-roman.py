class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return ''
        
        val_symbols = [
            (1, 'I'),
            (4, 'IV'),
            (5, 'V'),
            (9, 'IX'),
            (10, 'X'),
            (40, 'XL'),
            (50, 'L'),
            (90, 'XC'),
            (100, 'C'),
            (400, 'CD'),
            (500, 'D'),
            (900, 'CM'),
            (1000, 'M')
        ]
        val_symbols.sort(reverse=True)
        print()
        
        romans = []
        
        for unit, symbol in val_symbols:
            count = num // unit
            romans.append(symbol * count)
            num = num % unit
            if num == 0:
                break
                
        return ''.join(romans)