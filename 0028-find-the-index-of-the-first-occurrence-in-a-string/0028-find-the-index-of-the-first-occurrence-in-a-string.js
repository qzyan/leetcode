/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    for (let left = 0; left < haystack.length - needle.length + 1; left++) {
        if (haystack.slice(left, left + needle.length) === needle) {
            return left;
        }
    }
    
    return -1
};