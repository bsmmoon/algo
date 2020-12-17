/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  return [0, 1]
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

  result = JSON.stringify(output) === JSON.stringify(t.output)

  console.log(result, timetaken)

  if (result) return

  console.log(`input: ${JSON.stringify(t.input).substring(0, MAX_OUTPUT)}\noutput: ${JSON.stringify(output).substring(0, MAX_OUTPUT)}\nexpected: ${JSON.stringify(t.output).substring(0, MAX_OUTPUT)}`)
})

