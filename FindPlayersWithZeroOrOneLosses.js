// You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
// Return a list answer of size 2 where:
//  answer[0] is a list of all players that have not lost any matches.
//  answer[1] is a list of all players that have lost exactly one match.
// The values in the two lists should be returned in increasing order.
// Note:
//  You should only consider the players that have played at least one match.
//  The testcases will be generated such that no two matches will have the same outcome.

function findWinners(matches){
    lostMatches = {}
    losses = [[], []]

    matches.forEach((game) => {
        if (!(game[0] in lostMatches)){
            lostMatches[game[0]] = 0
        }

        if (game[1] in lostMatches){
            lostMatches[game[1]] += 1
        } else {
            lostMatches[game[1]] = 1
        }
    })

    for ([key, value] of Object.entries(lostMatches)){
        if (value == 0){
            losses[0].push(key)
        }
        else if (value == 1){
            losses[1].push(key)
        }
    }
    
    return losses
}

// Test cases
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
console.log(findWinners(matches))

matches = [[2,3],[1,3],[5,4],[6,4]]
console.log(findWinners(matches))
