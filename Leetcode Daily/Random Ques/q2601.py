class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(n):
            if n <= 1 :
                return False

            for i in range(2, n):
                if n % i == 0:
                    return False

            return True
        primes = []
        for i in range(2, 1001):
            if isPrime(i):
                primes.append(i)
                
        arr = [-1,-1,-1]
        for i in range(3,1001):
            j = 0
            while j < len(primes) and primes[j] < i:
                j += 1
            
            if j >= len(primes):
                arr.append(len(primes)-1)
                
            arr.append(j-1)
            
        
        mx = -1

        n = len(nums)
        prev = 0

        for i in range(n):
            if arr[nums[i]] == -1:
                if nums[i] <= prev:
                    return False
                prev = nums[i]
                continue
                
            if (nums[i] - primes[arr[nums[i]]]) <= prev:
                x = arr[nums[i]]

                while x >= 0 and (nums[i] - primes[x]) <= prev:
                    x -= 1
                
                if x < 0:
                    if nums[i] <= prev:
                        return False
                    else:
                        prev = nums[i]
                        continue
                nums[i] -= primes[x]
                
            else:
                nums[i] -= primes[arr[nums[i]]]
                
            if nums[i] <= prev:
                return False
            
            prev = nums[i]
                
            
        return True