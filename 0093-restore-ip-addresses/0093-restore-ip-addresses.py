class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ip = []
        ips = []
        self.backtrack(ip, ips, 0, s)
        return ips
    
    def backtrack(self, ip, ips, start_idx, s):
        # ip will have more than 4 ints, return
        if len(ip) > 4:
            return
        
        # ip has exact 4 ints and all chars have been used
        if len(ip) == 4 and start_idx == len(s):
            ips.append('.'.join(ip))
            return
        
        for i in range(1, 4):
            end_idx = start_idx + i
            if end_idx > len(s):
                break
                
            number = int(s[start_idx:end_idx])
            if number > 255:
                continue
            # 00, 000, 023 -> 0, 0, 23 do not meet req
            if len(str(number)) != end_idx - start_idx:
                continue
            
            
            ip.append(str(number))
            self.backtrack(ip, ips, end_idx, s)
            ip.pop()
            
    