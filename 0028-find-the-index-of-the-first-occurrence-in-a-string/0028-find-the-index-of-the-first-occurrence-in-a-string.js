/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (!needle) {
        return 0
    }

    for (let i = 0; i < haystack.length - needle.length + 1; i++) {
        let isFound = true
        for (let j = 0; j < needle.length; j++) {
            if (haystack[i + j] != needle[j]) {
                isFound = false
                break
            }
        }
        if (isFound) {
            return i
        }
    }
    
    return -1
};