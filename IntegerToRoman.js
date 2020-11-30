/**
 * @param {number} num
 * @return {string}
 * 1 <= num <= 3999
 */
var intToRoman = function(num) {
  let symbols = [
    [1000, "M"],
    [ 900, "CM"],
    [ 500, "D"],
    [ 400, "CD"],
    [ 100, "C"],
    [  90, "XC"],
    [  50, "L"],
    [  40, "XL"],
    [  10, "X"],
    [   9, "IX"],
    [   5, "V"],
    [   4, "IV"],
    [   1, "I"],
  ]

  let roman = ""
  symbols.forEach((tuple) => {
    let [value, symbol] = tuple
    while (num >= value) {
      roman += symbol
      num -= value
    }
  })

  return roman
}

let tests = [
  { input: 3, output: "III" },
  { input: 4, output: "IV" },
  { input: 9, output: "IX" },
  { input: 58, output: "LVIII" },
  { input: 1994, output: "MCMXCIV" },
]

let output, result
tests.forEach((t) => {
  output = intToRoman(t.input)
  result = output === t.output

  console.log(result)

  if (result) return

  console.log(`input: ${t.input}, output: ${output}, expected: ${t.output}`)
})

