/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    if (!s) {
        return True
    }
    
    let left = 0;
    let right = s.length - 1;
    
    while (left < right) {
        if (!isAlphaNum(s[left])) {
            left += 1;
            continue;
        }
    
        if (!isAlphaNum(s[right])) {
            right -= 1;
            continue
        }

        if (s[left].toLowerCase() !== s[right].toLowerCase()) {
            return false;
        }
    
        left += 1;
        right -= 1;
    }
    
    return true

    
};

const isAlphaNum = (char) => {
    return (
        (char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57) ||
        (char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90) || 
        (char.charCodeAt(0) >= 97 && char.charCodeAt(0) <= 122)
        )
}