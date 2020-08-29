/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var temp = 0;
    for(i = 0; i < nums.length; i++) {
        if(nums[i] != val) {
            nums[temp] = nums[i];
            temp++;
        }
    }
    
    return temp;
};