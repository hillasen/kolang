import {출력하기,질문하기} from "base_function.js";

function 피보나치(숫자){
if(숫자==0){
출력하기("0")
return 0
}
if(숫자==1){
출력하기("1")
return 1
}
return 피보나치(숫자-1)+피보나치(숫자-2)
}

var 번호=질문하기("피보나치를알아볼번호")
출력하기(피보나치(번호))
