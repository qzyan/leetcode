```py
class Solution:
def strStr(self, haystack: str, needle: str) -> int:
needle_len = len(needle)
haystack_len = len(haystack)
for i in range(0, haystack_len - needle_len + 1):
if haystack[i: i + needle_len] == needle:
return i
return -1
```
创建haystack\[i: i + needle_len], 占用额外空间，可以避免。通过另一层for循环
​
​
## Robin Karp
```
31^n % BASE = (31^(n-1) * 31) % BASE
fn(n) = (fn(n - 1) % BASE * 31) % BASE
```
​
​
​