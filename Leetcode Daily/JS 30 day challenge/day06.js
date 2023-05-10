var reduce = function(nums, fn, init) {
    let x = init
    for(let i = 0; i < nums.length; i++){
        x = fn(x,nums[i])
    }

    return x
};