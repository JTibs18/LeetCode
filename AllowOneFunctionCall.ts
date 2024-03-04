// Given a function fn, return a new function that is identical to the original function except that it ensures fn is called at most once.
//  The first time the returned function is called, it should return the same result as fn.
//  Every subsequent time it is called, it should return undefined.

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined

function once(fn: Function): OnceFn {
    let called = false; 
    
    return function (...args) {
        if (called){
            return undefined; 
        };

        called = true; 
        return fn(...args);
    };
}

// Test cases
var fn = (a: number, b: number, c: number) => (a + b + c);
const onceFn = once(fn); 
console.log(onceFn(1, 2, 3));
console.log(onceFn(2, 3, 6));

fn = (a: number, b: number, c: number) => (a * b * c);
const onceFn2 = once(fn);
console.log(onceFn2(5, 7, 4));
console.log(onceFn2(2, 3, 6));
console.log(onceFn2(4, 6, 8));
