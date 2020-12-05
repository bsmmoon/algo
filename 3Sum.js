/**
  return tuple
 * @param {number[]} nums
 * @return {number[][]}
 * 0 <= nums.length <= 3000
 * -10^5 <= nums[i] <= 10^5
 *  Approach 1:
 *    Brute Force: O(N^3)
 *  Approach 2:
 *    Sort, pick 2 and search matching number
 *    O(NlogN) + O(N^2 * logN) = O(N^2logN)
 */
var threeSum = function(nums) {
  if (nums.length < 3) return []

  nums = nums.sort((a, b) => a - b)

  let result = new Set()
  let sum, has, tuple
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      sum = nums[i] + nums[j]

      if (sum > 0) continue
      
      has = bsearch(nums.slice(j + 1), sum * -1)

      if (!has) continue

      tuple = [nums[i], nums[j], sum * -1]

      result.add(JSON.stringify(tuple))
    }
  }

  return [...result].map(e => JSON.parse(e))
}

let bsearch = (arr, value) => {
  if (arr.length === 0) return false
  
  let index = Math.floor(arr.length / 2)
  
  if (arr[index] === value) return true
  
  let from, to

  if (arr[index] > value) {
    from = 0
    to = index
  } else {
    from = index + 1
    to = arr.length
  }
  return bsearch(arr.slice(from, to), value)
}

let tests = [
  {
    input: [-1, 0, 1, 2, -1, -4],
    output: [[-1, -1, 2], [-1, 0, 1]]
  },
  {
    input: [],
    output: []
  },
  {
    input: [0],
    output: []
  },
  {
    input: [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49],
    output: [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]
  }, 
]

let output, result

result = true
tests.forEach((t) => {
  output = threeSum(t.input)

  result = JSON.stringify(output) === JSON.stringify(t.output)

  console.log(result)

  if (result) return

  console.log(`input: ${t.input}\noutput: ${JSON.stringify(output)}\nexpected: ${JSON.stringify(t.output)}`)
})

