/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const hashMap = new Map() 
    for (let i = 0; i < nums.length; i++) {
        if (!hashMap.has(nums[i])) {
            hashMap.set(nums[i], [i])
            continue
        }
        const arr = hashMap.get(nums[i])
        arr.push(i)
    }
    
    for (let i = 0; i < nums.length; i++) {
        const a = target - nums[i]
        if (!hashMap.has(a)) {
           continue
        }
        
        const indexes = hashMap.get(a)
            for (let index of indexes) {
                if (index !== i) return [i, index]
            }
    }
};