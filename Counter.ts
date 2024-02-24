// Given an integer n, return a counter function. This counter function initially returns n and then returns 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).

function createCounter(n: number): () => number {
    return function (){
        n = n + 1;
        return n - 1;
    };
};

// Test cases
const counter = createCounter(10);
console.log(counter());
console.log(counter());
console.log(counter());

const c2 = createCounter(-2);
console.log(c2());
console.log(c2());
console.log(c2());
console.log(c2());
console.log(c2());
