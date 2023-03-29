// A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
// Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
// Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.
// Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

function maxSatisfaction(satisfaction) {
    satisfaction = satisfaction.sort((a, b) => b - a)
    timeC = 0 
    
    satisfaction.forEach((value, indx) => {
        if (timeC < timeC + value + satisfaction.slice(0, indx).reduce((a, b) => a + b, 0)) {
            timeC = timeC + value + satisfaction.slice(0, indx).reduce((a, b) => a + b, 0); 
        } else {
            return timeC;
        }
    });

    return timeC 
}

// Test cases 
satisfaction = [-1,-8,0,5,-9]
console.log(maxSatisfaction(satisfaction))

satisfaction = [4,3,2]
console.log(maxSatisfaction(satisfaction))

satisfaction = [-1,-4,-5]
console.log(maxSatisfaction(satisfaction))