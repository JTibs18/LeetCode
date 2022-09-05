// Given the array restaurants where  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]. You have to filter the restaurants using three filters.
// The veganFriendly filter will be either true (meaning you should only include restaurants with veganFriendlyi set to true) or false (meaning you can include any restaurant). In addition, you have the filters maxPrice and maxDistance which are the maximum value for price and distance of restaurants you should consider respectively.
// Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest. For restaurants with the same rating, order them by id from highest to lowest. For simplicity veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.

function ratingCompare(aRating, bRating){
  if (aRating === bRating){
    return false;
  }else{
    return bRating - aRating;
  }
};

//First Attempt
function filterRestaurants1(restaurants, veganFriendly, maxPrice, maxDistance){
  var validRestaurants = [];
  for (i = 0; i < restaurants.length; i++ ){
    if (veganFriendly === 0 || veganFriendly === restaurants[i][2]){
      if (restaurants[i][3] <= maxPrice && restaurants[i][4] <= maxDistance){
        validRestaurants.push(restaurants[i]);
      }
    }
  }
  validRestaurants.sort((a, b) => ratingCompare(a[1], b[1]) || b[0] - a[0]);
  return validRestaurants.map(function(i) {
    return i[0];
  });
};

//Second Attempt (Runs faster than First Attempt but same memory)
function filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance){
  const veganFriendlyRestaurants = restaurants.filter(restaurant => restaurant[2] === veganFriendly || veganFriendly === 0);
  const restaurantsInPriceRange = veganFriendlyRestaurants.filter(restaurant => restaurant[3] <= maxPrice);
  const validRestaurants = restaurantsInPriceRange.filter(restaurant => restaurant[4] <= maxDistance);

  validRestaurants.sort((a, b) => ratingCompare(a[1], b[1]) || b[0] - a[0]);
  return validRestaurants.map(function(i) {
    return i[0];
  });
};

// Test cases
restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]];
veganFriendly = 1;
maxPrice = 50;
maxDistance = 10;
console.log(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance));

restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]];
veganFriendly = 0;
maxPrice = 50;
maxDistance = 10;
console.log(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance));

restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]];
veganFriendly = 0;
maxPrice = 30;
maxDistance = 3;
console.log(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance));
