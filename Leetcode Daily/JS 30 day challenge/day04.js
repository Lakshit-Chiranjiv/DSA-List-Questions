var map = function(arr, fn) {
    let ans = new Array(arr.length).fill(0);
    for(let i = 0; i < arr.length; i++){
        ans[i] = fn(arr[i],i)
    }

    return ans
};