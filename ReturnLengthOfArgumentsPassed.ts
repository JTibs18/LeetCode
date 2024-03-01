// Write a function argumentsLength that returns the count of arguments passed to it.

type JSONValue = null | boolean | number | string |JSONValue[] | {[key: string]: JSONValue}

function argumentsLength(...args:JSONValue[]): number {
    return args.length
};

// Test cases
console.log(argumentsLength([5]))
console.log(argumentsLength({}, null, "3"))
