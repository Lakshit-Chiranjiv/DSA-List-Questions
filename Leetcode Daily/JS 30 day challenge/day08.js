var once = function(fn) {
    c = 0;
    return function(...args){
        if(c > 0)
            return undefined
        c++
        return fn(...args)
    }
};