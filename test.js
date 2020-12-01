let obj = {}
let key = 1
obj[key] = "value"
console.log(obj[key])
console.log(obj[key.toString()])

const strGenerator = (length) => Math.random().toString(36).substring(0, length)


console.log(strGenerator(1))
console.log(strGenerator(2))
console.log(strGenerator(3))
console.log(strGenerator(4))
console.log(strGenerator(5))

