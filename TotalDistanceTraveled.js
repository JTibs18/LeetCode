// A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in liters and additionalTank representing the fuel present in the additional tank in liters.
// The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.
// Return the maximum distance which can be traveled.
// Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.

function distanceTraveled(mainTank, additionalTank){
    distance = 0;

    while (mainTank){
        if (mainTank < 5){
            distance += mainTank * 10;
            mainTank = 0;
        }else{
            distance += 50;
            if (additionalTank > 0){
                mainTank -= 4;
                additionalTank -= 1;
            }else{
                mainTank -= 5;
            };
        };
    };

    return distance;
};

// Test cases
mainTank = 5
additionalTank = 10
console.log(distanceTraveled(mainTank, additionalTank))

mainTank = 1
additionalTank = 2
console.log(distanceTraveled(mainTank, additionalTank))

mainTank = 9
additionalTank = 2
console.log(distanceTraveled(mainTank, additionalTank))
