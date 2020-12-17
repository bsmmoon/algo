/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 *  return """indices""" of the two numbers
 *
 * Approach 1.
 * Create a hash
 * For each element,
 *   if target - element is in the hash, return them
 *   else add (element, indice) to the hash
 * O(nums) for both time and space
 *
 */
var twoSum = function(nums, target) {
  let hash = {}
  let wanted, num
  const length = nums.length
  for (let i = 0; i < length; i++) {
    num = nums[i]
    wanted = (target - num).toString()
    if (hash[wanted] !== undefined) return [i, hash[wanted]]
    hash[num] = i
  }
  return []
}

const tests = [{
  input: [[2, 7, 11, 15], 9],
  output: [0, 1]
}, {
  input: [[3, 2, 4], 6],
  output: [1, 2]
}, {
  input: [[3, 3], 6],
  output: [0, 1]
}]

const MAX_OUTPUT = 100
let output, timetaken
let result = true
tests.forEach((t, i) => {
  timetaken = Date.now()
  output = twoSum(...t.input)
  timetaken = Date.now() - timetaken

  result = JSON.stringify(output.sort()) === JSON.stringify(t.output.sort())

  console.log(result, timetaken)

  if (result) return

  console.log(`input: ${JSON.stringify(t.input).substring(0, MAX_OUTPUT)}\noutput: ${JSON.stringify(output).substring(0, MAX_OUTPUT)}\nexpected: ${JSON.stringify(t.output).substring(0, MAX_OUTPUT)}`)
})

