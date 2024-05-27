function solution(arr) {
    let letterPos = null;
    let matchingArr = [0,0,0];
    for(let i=0; i<arr.length; i++){
        let str = arr[i] //"abc"
        for(let l=0; l<str.length; l++){// a b c
            for (let x=0; x<arr.length; x++){
                if(x !== i){ // "bca"
                    let secondStr = arr[x]
                    if(str[l] === secondStr[l]){
                        letterPos = l;
                        matchingArr[1] = x;
                        matchingArr[0] = i;
                        matchingArr[2] = letterPos;
                        console.log(`${str} and ${secondStr} have a matching letter at pos ${letterPos}`)
                        break
                    }
                }   
            }   
        }
        break
    }
    if(matchingArr == [0,0,0]){
        return []
    }
    else{
        return matchingArr;
    }
}

let ex1 = ["abc", "bca", "dbe"]
let ex2 = ["zzzz", "ferz", "asgd"]
console.log(solution(ex2));