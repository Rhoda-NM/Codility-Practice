let choice1 = 10
let choice2 = 12
let largest = 0
function solution(nums){
    let total = 0
    let largest1 = Math.max(...nums);
    //console.log(largest1)
    let numStr1 = largest1.toString();
    let sum1 = numStr1.split('').reduce((acc, digit) => {
        return acc + parseInt(digit, 10);
        }, 0);
    //console.log(sum1)
    for(let i=0;i<nums.length; i++) {
        let num = nums[i]
        if (num == largest1){
            nums[i] = sum1
        }
    }
    //console.log(nums)
    let largest2 = Math.max(...nums);
    let numStr2 = largest2.toString();
    let sum2 = numStr2.split('').reduce((acc, digit) => {
        return acc + parseInt(digit, 10);
        }, 0);
    //console.log(sum2)
    for(let i=0;i<nums.length; i++) {
        let num = nums[i]
        if (num == largest2){
            nums[i] = sum2
        }
    }
    total = nums.reduce((acc, number) => {
        return acc + number
    })
    //console.log(total)
    return total

}
let result = solution([12,1])
console.log(result)
