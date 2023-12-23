// Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
// Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

function isPathCrossing(path){
    curLocation = [0, 0]
    grid = [curLocation]

    for(i=0; i<path.length; i++){
        if (path[i] == "N"){
            curLocation = [curLocation[0], curLocation[1] + 1];
        }else if (path[i] == "S"){
            curLocation = [curLocation[0], curLocation[1] - 1]; 
        }else if (path[i] == "E"){
            curLocation = [curLocation[0] + 1, curLocation[1]];
        }else{
            curLocation = [curLocation[0] - 1, curLocation[1]];
        }

        if (JSON.stringify(grid).indexOf(JSON.stringify(curLocation)) != -1){
            return true;
        }else{
            grid.push(curLocation);
        }
    }
    return false 
};

// Test cases
path = "NES"
console.log(isPathCrossing(path))

path = "NESWW"
console.log(isPathCrossing(path))
