/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    var temp = s.split(" ").filter(el => {
        return el != '';
    });
    console.log(temp);
    var temp_ans = '';
    
    for(var i = temp.length; i > 0; i--) {
        temp_ans += temp[i-1] + " ";
    }
    
    return temp_ans.trim();
};