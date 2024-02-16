// Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

function findLeastNumOfUniqueInts(arr, k){
    distinctNumCount = {};
    
    for (i of arr){
        if (i in distinctNumCount){
            distinctNumCount[i] += 1;
        }else{
            distinctNumCount[i] = 1;
        };
    };

    sortedNums = Object.values(distinctNumCount).sort((x, y) => x - y);

    leastNumCount = sortedNums.length;
    
    for (x of sortedNums){
        k -= x;
        leastNumCount -= 1;
        
        if (k == 0){
            break;
        }else if (k < 0){
            leastNumCount += 1;
            break;
        };
    };

    return leastNumCount;
}; 


// Test cases
arr = [5, 5, 4]
k = 1
console.log(findLeastNumOfUniqueInts(arr, k))

arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
console.log(findLeastNumOfUniqueInts(arr, k))
