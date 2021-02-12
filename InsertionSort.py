#Insertion Sort
'''
    - Start with index 1 and compare it with element to its left
    - With each pass it stores the index key value in temp
    - Copy all the values (on the left) greater than key to their next index
    - In the right place of the list (when condition fails)
    - Insert the temp with each pass

    - It is similar to arranging a pack of card in hand
'''

def insertionsort(lists):
    
    for keyIndex in range(1, len(lists)):

        # Saving the key before inserting it
        key = lists[keyIndex]
        compareIndex = keyIndex-1
    
        while(compareIndex >= 0 and lists[compareIndex] > key):

            lists[compareIndex+1] = lists[compareIndex]
            compareIndex -= 1

        # Inserting the temp key value.
        lists[compareIndex+1] = key

if __name__ == "__main__":
    
    lists = list(map(int, input().split()))
    insertionsort(lists)
    print(lists)
