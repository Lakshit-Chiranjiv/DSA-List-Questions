var throttle = function(fn, t) {
    let isThrottled = false
    let nextArgs = null

      const helper = () => {
          if (nextArgs){
              fn(...nextArgs)
              isThrottled = true
              nextArgs = null
              setTimeout(helper,t)
          }
          else{
              isThrottled = false
          }
      }
  return function(...args) {
      if (isThrottled){
          nextArgs = args
      }
      else{
          fn(...args)
          isThrottled = true
          setTimeout(helper, t)
      }
  }
};