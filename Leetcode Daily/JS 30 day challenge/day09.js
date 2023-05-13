function memoize(fn) {
    let obj = {}
    return function(...args) {
        const key = JSON.stringify(args)
        if(key in obj)
            return obj[key]
        obj[key] = fn(...args)
        return obj[key]
    }
}