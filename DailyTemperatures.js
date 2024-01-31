// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

function dailyTemperatures(temperatures){
    output = Array(temperatures.length).fill(0);
    stack = [];

    for (i = 0; i < temperatures.length; i++){
        while (stack.length && stack[stack.length - 1][0] < temperatures[i]){
            [_, stackIndx] = stack.pop();
            output[stackIndx] = i - stackIndx;
        };

        stack.push([temperatures[i], i]);
    };

    return output;
};

// Test cases
temperatures = [73,74,75,71,69,72,76,73]
console.log(dailyTemperatures(temperatures))

temperatures = [30,40,50,60]
console.log(dailyTemperatures(temperatures))

temperatures = [30,60,90]
console.log(dailyTemperatures(temperatures))

