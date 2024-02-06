// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

function groupAnagrams(strs){
    groups = {};
    allAnagrams = [];

    strs.forEach(word => {
        sortedWord = word.split("").sort().join("");

        if (sortedWord in groups){
            groups[sortedWord].push(word);
        }else{
            groups[sortedWord] = [word];
        };
    });

    Object.values(groups).forEach(val => allAnagrams.push(val));

    return allAnagrams;
};

// Test cases
strs = ["eat","tea","tan","ate","nat","bat"]
console.log(groupAnagrams(strs))

strs = [""]
console.log(groupAnagrams(strs))

strs = ["a"]
console.log(groupAnagrams(strs))
