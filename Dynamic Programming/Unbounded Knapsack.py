def knapsack(weight, profit, capacity, n):
    # Initialise the list to 0
    p = [0] * (capacity + 1)
    # Create a list to store the items that are added
    items = [[] for x in range(capacity+1)]

    for c in range(capacity+1):
        for i in range(0, n):
            # Check if the current weight is less than the capacity
            if(weight[i] <= c):
                # Check if including the current object would increase the profit
                if (p[c-weight[i]] + profit[i]) > p[c]:
                    # Update if it increases the profit
                    p[c] = p[c-weight[i]] + profit[i]
                    # Add the current item into the list which contains the previous items
                    # Check the items inside the reduced capacity after considering item i for the maximum profit
                    items[c] = items[c-weight[i]] + [i]
                    
    return p, items[capacity]

def main():

    max_profit = []
    objects = []

    choice = input("Enter your choice: ")

    if choice == 'a':
        weight = [4, 6, 8]
        profit = [7, 6, 9]
        capacity = 14
        n = len(weight)
    
    elif choice == 'b':
        weight = [5, 6, 8]
        profit = [7, 6, 9]
        capacity = 14
        n = len(weight)

    # Example in the notes to check functionality
    elif choice == 'c':
        weight = [1, 2, 3]
        profit = [1, 4, 6]
        capacity = 3
        n = len(weight)

    max_profit, objects = knapsack(weight, profit, capacity, n)     

    print("The maximum profit for each capacity:")
    for i in range(capacity+1):
        print(max_profit[i], end = ' ')
    print("\nThe maximum profit: \n" + str(max_profit[capacity]))
    print("The objects inside the knapsack:")
    for j in objects:
        print(j, end = ' ')      

if __name__ == "__main__":
    main()
     


