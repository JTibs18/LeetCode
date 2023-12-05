// Write a function argumentsLength that returns the count of arguments passed to it.

var argumentsLength = function(...args) {
    return args.length
};

// Test cases
console.log(argumentsLength(5))

console.log(argumentsLength({}, null, "3"))
