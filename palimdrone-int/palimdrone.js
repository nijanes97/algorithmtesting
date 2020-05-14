/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0){
        return false
    }
    temp = x.toString()
    temp_reverse = ''
    for(i = 0; i < temp.length; i++){
        temp_reverse = temp[i] + temp_reverse
    }
    
    return temp_reverse === temp
};