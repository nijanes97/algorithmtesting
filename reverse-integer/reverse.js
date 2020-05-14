/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    temp = x.toString()
    temp_reverse = ''
    for(i = 0; i < temp.length; i++){
        temp_reverse = temp[i] + temp_reverse
    }
    
    answer = parseInt(temp_reverse)
    
    if (answer > 0x7FFFFFFF) {
        return 0;
    }
    
    if(x < 0){
        return answer * -1
    }
    return answer
};