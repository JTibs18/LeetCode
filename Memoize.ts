// Given a function fn, return a memoized version of that function.
// A memoized function is a function that will never be called twice with the same inputs. Instead it will return a cached value.
// You can assume there are 3 possible input functions: sum, fib, and factorial.
//  sum accepts two integers a and b and returns a + b.
//  fib accepts a single integer n and returns 1 if n <= 1 or fib(n - 1) + fib(n - 2) otherwise.
//  factorial accepts a single integer n and returns 1 if n <= 1 or factorial(n - 1) * n otherwise.
 
type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    let memo = new Map();

    return function(...args){
        let key = String(args);

        if (!memo.has(key)){
            memo.set(key, fn(...args));
        };
        
        return memo.get(key);
    };
};

// Test cases
const sum = (a: number, b: number) => a + b;
const memoizedSum = memoize(sum);
console.log(memoizedSum(2, 2));
console.log(memoizedSum(2, 2));
console.log(memoizedSum(1, 2));

const factorial = (n: number): number => (n <= 1) ? 1 : (n * factorial(n-1));
const memoFactorial = memoize(factorial);
console.log(memoFactorial(2));
console.log(memoFactorial(3));
console.log(memoFactorial(2));
console.log(memoFactorial(3));

const fib = (n: number): number => (n <= 1) ? n : (fib(n - 1) + fib(n - 2));
const memoFib = memoize(fib);
console.log(fib(5));