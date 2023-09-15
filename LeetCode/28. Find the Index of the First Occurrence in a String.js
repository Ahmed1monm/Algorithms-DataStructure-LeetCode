// Two pointers
var strStr = function(haystack, needle) {
    // if(typeof needle === 'string' && needle.length === 1) return  haystack.indexOf(needle);
    // if (haystack.startsWith(needle)) return 0;
    // if (haystack.endsWith(needle)) return haystack.lenght - needle.lenght;

    if(haystack.includes(needle)){
        return haystack.indexOf(needle)
        // let left = 0;
        // let reight = haystack.length -1;
        // let subString =haystack.substr(left, reight+1);
        // while(left <= reight){
        //     if(needle === subString) return left;
        //     if(needle[0] === haystack[left]){
        //         reight--;
        //     } else if(needle[-1] === haystack[reight]){
        //         left++
        //     }else{
        //         left++;
        //         reight--;
        //         subString =haystack.substr(left, reight)
        //     }
        // }
        
    } 
    return -1
};

const test = "mississippi";

console.log(strStr(test, 'issi'))

// function isSingleChar(input) {
//     return typeof input === 'string' && input.length === 1;
// }
// console.log(isSingleChar('c'))