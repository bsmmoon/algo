
const bench = fn => {
  let start = Date.now()
  fn()
  return Date.now() - start
}

const testObjectKey = ((key, size) => {
  let obj = {}
  let arr = []

  let timetaken = bench(() => { 
    for (let i = 0; i < Math.pow(size, 2); i++) {
      key = key.toString()
      obj[key] += 1
    }
  })
  console.log(`${key}: ${timetaken}ms`)
})

const SIZE = 2500
const tests = [
  {},

  "string",

  -1 * (Math.pow(2, 53)), // BigInteger
  -1 * (Math.pow(2, 53) - 1), // MIN Number
  
  -1 * (Math.pow(2, 0)),
  0,
  
  Math.pow(2, 10) - 1,
  Math.pow(2, 10),
  
  9999999,
  10000000,
  
  Math.pow(2, 32) - 2,
  Math.pow(2, 32) - 1,
  
  Math.pow(2, 53) - 1, // MAX Number
  Math.pow(2, 53), // BigInteger
]
tests.forEach(test => testObjectKey(test, SIZE))

