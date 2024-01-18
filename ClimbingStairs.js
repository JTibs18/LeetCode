// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

function climbStairs(n){
    previousWays = [0, 1, 2];
    iter = n - 2;

    while (iter > 0) {
        previousWays.push(previousWays[previousWays.length - 1] + previousWays[previousWays.length - 2]);
        iter -= 1;
    };

    return previousWays[n];
}

// Test cases
n = 1
console.log(climbStairs(n))

n = 2
console.log(climbStairs(n))

n = 3
console.log(climbStairs(n))
