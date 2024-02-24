// Write a function createHelloWorld. It should return a new function that always returns "Hello World".

function createHelloWord(){
    return function(...args:any): string {
        return "Hello World";
    };
};

// Test cases
const f = createHelloWord()
console.log(f([]))
console.log(f({}, null, 42))
