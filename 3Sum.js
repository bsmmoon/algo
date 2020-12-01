/**
 * @param {number[]} nums
 * @return {number[][]}
 * 0 <= nums.length <= 3000
 * -10^5 <= nums[i] <= 10^5
 */
var threeSum = function(nums) {
  return
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
  }
]

let output, result
tests.forEach((t) => {
  output = threeSum(t.input)
  result = output === t.output

  console.log(result)

  if (result) return

  console.log(`input: ${t.input}\noutput: ${output}\nexpected: ${t.output}`)
})

