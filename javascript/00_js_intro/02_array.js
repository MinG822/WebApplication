const nums = [1, 2, 3, 4]

console.log(nums[0])
console.log(nums[nums.length - 1])

console.log(nums.reverse())
console.log(nums)

nums.push(0)
console.log(nums)

nums.pop()
console.log(nums)

// unshift, shift, includes, indexOf
nums.unshift(5)
console.log(nums)

nums.shift()
console.log(nums)

console.log(nums.includes(0))
console.log(nums.includes(4))

console.log(nums.indexOf(1))

// 반복문 : for (let num of nums) {}

// nums 안의 요소 각각을 제곱하시오
let newNums = []

nums.forEach(function(num){ 
    newNums.push(num ** 2)
})

console.log(newNums)

const squaredNums = nums.map(num => num ** 2)
// map(lambda x:x**2, nums) -> python vers.

console.log(squaredNums)