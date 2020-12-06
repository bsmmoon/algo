
const bench = fn => {
  let start = Date.now()
  fn()
  return Date.now() - start
}

const testObjectKey = ((key, size) => {
  let timetaken = bench(() => {
    let obj = {}
    let arr = []
    for (let i = 0; i < Math.pow(size, 2); i++) {
//      obj[key] += 1
//      obj[key] = 1
//      key.toString()
      obj[key.toString()] += 1
//      arr[key] += 1
    }
  })
  console.log(`${key}: ${timetaken}ms`)
})

const SIZE = 2500
const tests = [
  "string",
  -1 * (Math.pow(2, 53)),
  -1 * (Math.pow(2, 53)) + 1,
  -1 * (Math.pow(2, 0)),
  0,
  Math.pow(2, 10) - 1,
  Math.pow(2, 10),
  Math.pow(2, 32) - 2,
  Math.pow(2, 32) - 1,
  Math.pow(2, 53) - 1,
  Math.pow(2, 53),
]
tests.forEach(test => testObjectKey(test, SIZE))

