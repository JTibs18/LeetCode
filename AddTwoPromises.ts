// Given two promises promise1 and promise2, return a new promise. promise1 and promise2 will both resolve with a number. The returned promise should resolve with the sum of the two numbers.

type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    return await promise1 + await promise2 
}; 

// Test cases
addTwoPromises(Promise.resolve(2), Promise.resolve(5)).then(console.log)

addTwoPromises(Promise.resolve(10), Promise.resolve(-12)).then(console.log)
