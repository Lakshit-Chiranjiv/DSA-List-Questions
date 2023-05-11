var compose = function(functions) {
	return function(x) {
        if(! functions) return x

        functions.reverse()
        prev = x
        functions.forEach(z => {
            prev = z(prev)
        })

        return prev
    }
};