const obj1 = {num: 3};
const obj2 = {num: 3};
let num = 3;
function fn (object1Arg, object2Arg, numberArg) {
    object1Arg = {num: 5};
    object2Arg.num = 5;
    numberArg = 5;
}

fn(obj1, obj2, num);

// > 3
console.log(obj1.num);
// > 5
console.log(obj2.num);
// > 3
console.log(num);