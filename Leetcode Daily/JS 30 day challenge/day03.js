var createCounter = function(init) {
    x = init
    return {
        increment: () => {
            return ++init
        },
        decrement: () => {
            return --init
        },
        reset: () => {
            init = x
            return x
        }
    }
};