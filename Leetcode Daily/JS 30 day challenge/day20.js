/**
 * @param {object} obj1
 * @param {object} obj2
 * @return {object}
 */
function objDiff(obj1, obj2) {
    const isObject = (obj) => (obj != null && typeof obj === 'object')

    if (!isObject(obj1) && !isObject(obj2))
        return obj1 === obj2 ? {} : [obj1, obj2]

    if (!isObject(obj1) || !isObject(obj2))
        return [obj1, obj2]

    if (Array.isArray(obj1) !== Array.isArray(obj2))
        return [obj1, obj2]

    let diff = {}

    for (const key in obj1){
        if (obj2.hasOwnProperty(key)){
            const res = objDiff(obj1[key],obj2[key])
            if (Object.keys(res).length > 0)
                diff[key] = res
        }
    }

    return diff
};