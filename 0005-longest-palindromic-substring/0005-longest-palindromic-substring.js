/**
 * Best Solution
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (!s) {
        return false;
    }
    
    const is_pal = [];
    for (let i = 0; i < s.length; i++) {
        const row = []
        for (let j = 0; j < s.length; j++) {
            row.push(false)
        }
        is_pal.push(row)
    }
    
    for (let i = 0; i < s.length; i++) {
        is_pal[i][i] = true
    }
    
    for (let i = 1; i < s.length; i++) {
        is_pal[i][i - 1] = true
    }
    let start = 0
    let end = 0
    longest_len = 1
    for (let row_idx = s.length - 2; row_idx >=0; row_idx--) {
        for (let col_idx = row_idx + 1; col_idx < s.length; col_idx++) {
            is_pal[row_idx][col_idx] = is_pal[row_idx + 1][col_idx - 1] && s[row_idx] === s[col_idx]
            
            if (is_pal[row_idx][col_idx] && longest_len < col_idx - row_idx + 1) {
                start = row_idx
                end = col_idx 
                longest_len = end - start + 1
            }
        }
    }
    
    return s.slice(start, end + 1)
        

    
};
