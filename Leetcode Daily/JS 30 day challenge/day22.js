/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    const res = []

    const helper = (arr,dep) => {
        for (const val of arr){
            if (typeof val === 'object' && dep<n){
                helper(val, dep+1)
            }
            else{
                res.push(val)
            }
        }
        return res
    }
    return helper(arr,0)
};