// Given an array of functions [f1, f2, f3, ..., fn], return a new function fn that is the function composition of the array of functions.
// The function composition of [f(x), g(x), h(x)] is fn(x) = f(g(h(x))).
// The function composition of an empty list of functions is the identity function f(x) = x.
// You may assume each function in the array accepts one integer as input and returns one integer as output.

type F = (x: number) => number;

function compose1(functions: F[]): F {
    return function(x) {
        if (!functions.length) return x;

        while (functions.length) x = functions.pop()!(x);

        return x;
    };
};

function compose(functions: F[]): F {
    return function(x) {
        if (!functions.length) return x;

        for (var i = functions.length - 1; i >= 0; i-= 1) x = functions[i](x);

        return x;
    };
};

// Test cases
var fn = compose([x => x + 1, x => x * x, x => 2 * x])
console.log(fn(4))

var fn = compose([x => 10 * x, x => 10 * x, x => 10 * x])
console.log(fn(1))

var fn = compose([])
console.log(fn(42))