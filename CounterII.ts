// Write a function createCounter. It should accept an initial integer init. It should return an object with three functions.
// The three functions are:
//  increment() increases the current value by 1 and then returns it.
//  decrement() reduces the current value by 1 and then returns it.
//  reset() sets the current value to init and then returns it.
 
type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
};

function createCounterII(init: number): Counter {
    var curVal = init 
    return {
        increment: () => {
            curVal += 1;
            return curVal;
        }, 
        decrement: () => {
            curVal -= 1;
            return curVal;
        },
        reset: () => {
            curVal = init; 
            return curVal;
        }
    };
};

// Test cases
const c1 = createCounterII(5)
console.log(c1.increment())
console.log(c1.reset())
console.log(c1.decrement())

const c = createCounterII(0)
console.log(c.increment())
console.log(c.increment())
console.log(c.decrement())
console.log(c.reset())
console.log(c.reset())
