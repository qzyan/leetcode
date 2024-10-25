/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */

const HASHSIZE = 10 ** 6
const MAGICNUM = 31
    
var strStr = function(haystack, needle) {
    if (!needle) {
        return 0
    }
    
    if (haystack.length < needle.length) {
        return -1
    }
    
    const needleHashVal = getHashValue(needle)
    let hayStackHashVal = getHashValue(haystack.substring(0, needle.length))
    let power = 1
    for (let i = 0; i < needle.length; i++) {
        power = (power * MAGICNUM) % HASHSIZE
    }
    
    for (let i = 0; i < haystack.length - needle.length + 1; i++) {
        console.log(needleHashVal, hayStackHashVal)
        if (hayStackHashVal === needleHashVal) {
            if (compare(haystack, needle, i)) {
                return i
            }
        }
        
        hayStackHashVal = (hayStackHashVal * MAGICNUM + haystack.charCodeAt(i + needle.length)) % HASHSIZE
        hayStackHashVal = hayStackHashVal - (haystack.charCodeAt(i) * power) % HASHSIZE
        
        if (hayStackHashVal < 0) {
            hayStackHashVal += HASHSIZE
        }
    }
    
    return -1
    
};


const getHashValue = (s) => {
    let val = 0
    for (let i = 0; i < s.length; i++) {
        val = (val * MAGICNUM + s.charCodeAt(i)) % HASHSIZE
    }
    
    return val
}

const compare = (haystack, needle, start_idx) => {
    for (let i = 0; i < needle.length; i++) {
        if (haystack[start_idx + i] !== needle[i]) {
            return false
        }
    }
    
    return true
}