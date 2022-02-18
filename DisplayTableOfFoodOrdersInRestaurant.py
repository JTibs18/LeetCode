# Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.
# Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

def displayTable(orders):
    foodItems = []
    itemCount = {}
    table = []

    for i in orders:
        if i[2] not in foodItems:
            foodItems.append(i[2])
            foodItems = sorted(foodItems)

    for i in orders:
        if int(i[1]) not in itemCount:
            itemCount[int(i[1])] = [0] * len(foodItems)

        arr = itemCount.get(int(i[1]))
        arr[foodItems.index(i[2])] += 1

    header = []
    header.append("Table")
    header.extend(foodItems)
    table.append(header)

    for key in sorted(itemCount):
        tableOrders = []
        tableOrders.append(str(key))
        tableOrders.extend(str(i) for i in itemCount.get(key))
        table.append(tableOrders)

    return table

#Test Cases
orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(displayTable(orders))

orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
print(displayTable(orders))

orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
print(displayTable(orders))
