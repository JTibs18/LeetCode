// Write code that enhances all arrays such that you can call the array.groupBy(fn) method on any array and it will return a grouped version of the array.
// A grouped array is an object where each key is the output of fn(arr[i]) and each value is an array containing all items in the original array with that key.
// The provided callback fn will accept an item in the array and return a string key.
// The order of each value list should be the order the items appear in the array. Any order of keys is acceptable.
// Please solve it without lodash's _.groupBy function.

declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function(fn) {
    let groups: Record<string, any[]> = {};

    this.forEach(element => {
        let key = fn(element);

        key in groups ? groups[key].push(element) : groups[key] = [element];
    });

    return groups;
}

export {};

// Test cases
console.log([{"id":"1"}, {"id":"1"}, {"id":"2"}].groupBy(function(item) { return item.id}))

console.log([[1, 2, 3], [1, 3, 5], [1, 5, 9]].groupBy(function(list) {return String(list[0])}))

console.log([1, 2, 3, 4, 5, 6, 7, 8, 9, 10].groupBy(function(n) { return String(n > 5)}))