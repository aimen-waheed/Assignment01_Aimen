# INSERTION SORT 

# List of stars with name and temperature
stars = [
    {"name": "Sirius", "temperature": 9940},
    {"name": "Betelgeuse", "temperature": 3500},
    {"name": "Proxima Centauri", "temperature": 3042},
    {"name": "Rigel", "temperature": 12100},
    {"name": "Aldebaran", "temperature": 4010},
    {"name": "Vega", "temperature": 9602}
]

# Insertion Sort function
def insertion_sort(stars):
    for i in range(1, len(stars)):
        key = stars[i]  # Current star to insert
        j = i - 1
        while j >= 0 and stars[j]["temperature"] > key["temperature"]:
            stars[j + 1] = stars[j]  # Shift larger elements to the right
            j -= 1
        stars[j + 1] = key  # Place the key in its correct position

# Sorting the stars
insertion_sort(stars)

# Printing sorted stars by temperature
print("⭐ Stars Sorted by Temperature:")
for star in stars:
    print(f"{star['name']} - {star['temperature']} K")
print("\n")



# MERGE SORT

# List of stars with name and brightness
stars = [
    {"name": "Sirius", "brightness": 25.4},
    {"name": "Betelgeuse", "brightness": 126000},
    {"name": "Proxima Centauri", "brightness": 0.0017},
    {"name": "Rigel", "brightness": 120000},
    {"name": "Aldebaran", "brightness": 518},
    {"name": "Vega", "brightness": 40}
]

# Merge Sort function
def merge_sort(stars):
    if len(stars) > 1:
        mid = len(stars) // 2  # Find the middle point
        left_half = stars[:mid]  # Left sublist
        right_half = stars[mid:]  # Right sublist

        merge_sort(left_half)  # Recursively sort left half
        merge_sort(right_half)  # Recursively sort right half

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i]["brightness"] < right_half[j]["brightness"]:
                stars[k] = left_half[i]
                i += 1
            else:
                stars[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            stars[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            stars[k] = right_half[j]
            j += 1
            k += 1

# Sorting the stars
merge_sort(stars)

# Printing sorted stars by brightness
print("💡 Stars Sorted by Brightness:")
for star in stars:
    print(f"{star['name']} - {star['brightness']} Solar Luminosities")
print("\n")



# HEAP SORT

# Define spectral type priority (higher index = higher priority)
spectral_order = {"O": 7, "B": 6, "A": 5, "F": 4, "G": 3, "K": 2, "M": 1}

# List of stars with name and spectral type
stars = [
    {"name": "Sirius", "type": "A"},
    {"name": "Betelgeuse", "type": "M"},
    {"name": "Proxima Centauri", "type": "M"},
    {"name": "Rigel", "type": "B"},
    {"name": "Aldebaran", "type": "K"},
    {"name": "Vega", "type": "A"},
    {"name": "Canopus", "type": "F"},
    {"name": "Polaris", "type": "F"},
    {"name": "Deneb", "type": "A"}
]

# Heapify function (for max heap)
def heapify(stars, n, i):
    largest = i  # Assume root is largest
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare left child
    if left < n and spectral_order[stars[left]["type"]] > spectral_order[stars[largest]["type"]]:
        largest = left

    # Compare right child
    if right < n and spectral_order[stars[right]["type"]] > spectral_order[stars[largest]["type"]]:
        largest = right

    # Swap and continue heapifying if root is not largest
    if largest != i:
        stars[i], stars[largest] = stars[largest], stars[i]
        heapify(stars, n, largest)

# Heap Sort function
def heap_sort(stars):
    n = len(stars)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(stars, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        stars[i], stars[0] = stars[0], stars[i]  # Swap
        heapify(stars, i, 0)

# Sorting the stars
heap_sort(stars)

# Printing sorted stars by spectral type (O -> M)
print("🌟 Stars Sorted by Spectral Type (Descending Order - O to M):")
for star in reversed(stars):  # Reverse list for correct descending order
    print(f"{star['name']} - {star['type']} type")
print("\n")



# QUICK SORT

# Define category priority (higher number = higher priority)
category_order = {
    "Hypergiant": 5,
    "Supergiant": 4,
    "Giant": 3,
    "Main Sequence": 2,
    "White Dwarf": 1
}

# List of stars with name and category
stars = [
    {"name": "Betelgeuse", "category": "Supergiant"},
    {"name": "Sirius", "category": "Main Sequence"},
    {"name": "Rigel", "category": "Supergiant"},
    {"name": "Proxima Centauri", "category": "Main Sequence"},
    {"name": "Aldebaran", "category": "Giant"},
    {"name": "Canopus", "category": "Supergiant"},
    {"name": "Polaris", "category": "Supergiant"},
    {"name": "Vega", "category": "Main Sequence"},
    {"name": "Deneb", "category": "Supergiant"},
    {"name": "Sirius B", "category": "White Dwarf"}
]

# Quick Sort Partition Function
def partition(arr, low, high):
    pivot = category_order[arr[high]["category"]]  # Choosing last element's category as pivot
    i = low - 1  # Pointer for greater element

    for j in range(low, high):
        if category_order[arr[j]["category"]] >= pivot:  # Sorting in descending order (Hypergiant -> White Dwarf)
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is greater than pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot
    return i + 1

# Quick Sort Function
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index
        quick_sort(arr, low, pi - 1)  # Sort left subarray
        quick_sort(arr, pi + 1, high)  # Sort right subarray

# Sorting the stars
quick_sort(stars, 0, len(stars) - 1)

# Printing sorted stars by category (Descending Order - Hypergiant to White Dwarf)
print("🌟 Stars Sorted by Category (Descending Order):")
for star in stars:
    print(f"{star['name']} - {star['category']}")
print("\n")



# ARRAY 

stars = ["Sirius", "Alpha Centauri", "Betelgeuse", "Polaris"]
# Inserting a new star "Andromeda" at index 2
stars.insert(2, "Andromeda")
print("After Insertion:", stars)

# Deleting "Betelgeuse" by value
stars.remove("Betelgeuse")
print("After Deletion by Value:", stars)

# Deleting the star at index 1 (Alpha Centauri)
del stars[1]
print("After Deletion by Index:", stars)

# Updating the star at index 0 ("Sirius") to "Sun"
stars[0] = "Sun"
print("After Updation:", stars)

# Merging with another list of stars
new_stars = ["Venus", "Mars", "Jupiter"]
stars.extend(new_stars)
print("After Merging:", stars)
print("\n")



# STACK

stars_stack = ["Sirius", "Alpha Centauri", "Betelgeuse", "Polaris"]
# Pushing a new star "Andromeda" onto the stack
stars_stack.append("Andromeda")
print("After Push:", stars_stack)

# Popping the top star (Andromeda) from the stack
popped_star = stars_stack.pop()
print("After Pop:", stars_stack)
print("Popped Star:", popped_star)

# Peeking the top element (Polaris)
top_star = stars_stack[-1]
print("Top Element (Peek):", top_star)

# Checking if the stack is empty
is_empty = len(stars_stack) == 0
print("Is Stack Empty?", is_empty)
print("\n")



# SIMPLE QUEUE

from collections import deque

# Simple Queue implementation
stars_queue = deque(["Sirius", "Alpha Centauri", "Betelgeuse", "Polaris"])

# Enqueue (Insert) operation
stars_queue.append("Andromeda")

# Dequeue (Remove) operation
removed_star = stars_queue.popleft()

print("Queue after Enqueue and Dequeue:", list(stars_queue))
print("Removed Star:", removed_star)
print("\n")



# CIRCULAR QUEUE

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, star):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full!")
            return
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = star

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
            return None
        star = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return star

# Circular Queue implementation
stars_circular_queue = CircularQueue(5)
stars_circular_queue.enqueue("Sirius")
stars_circular_queue.enqueue("Alpha Centauri")
stars_circular_queue.enqueue("Betelgeuse")
stars_circular_queue.enqueue("Polaris")
stars_circular_queue.enqueue("Andromeda")

# Dequeue operation
removed_star_circular = stars_circular_queue.dequeue()

print("Queue after Enqueue and Dequeue:", stars_circular_queue.queue)
print("Removed Star from Circular Queue:", removed_star_circular)
print("\n")



# PRIORITY QUEUE

import heapq

# Priority Queue using heapq
stars_priority_queue = []
heapq.heappush(stars_priority_queue, (1, "Sirius"))
heapq.heappush(stars_priority_queue, (4, "Alpha Centauri"))
heapq.heappush(stars_priority_queue, (2, "Betelgeuse"))
heapq.heappush(stars_priority_queue, (3, "Polaris"))

# Dequeue (Remove) operation based on priority
priority_removed_star = heapq.heappop(stars_priority_queue)

print("Priority Queue after Enqueue and Dequeue:", [star[1] for star in stars_priority_queue])
print("Removed Star from Priority Queue:", priority_removed_star[1])
print("\n")



# DEQUE

from collections import deque

# Deque implementation
stars_deque = deque(["Sirius", "Alpha Centauri", "Betelgeuse", "Polaris"])

# Adding an element to the front
stars_deque.appendleft("Andromeda")

# Removing an element from the rear
removed_deque_star = stars_deque.pop()

print("Deque after Add to Front and Remove from Rear:", list(stars_deque))
print("Removed Star from Deque:", removed_deque_star)
print("\n")



# HASH

# Creating a hash table (dictionary)
stars_hash_table = {
    "Sirius": "Brightest star in the sky",
    "Alpha Centauri": "Nearest star system to Earth",
    "Betelgeuse": "A red supergiant star in Orion",
    "Polaris": "The North Star"
}

# 1. **Insertion**: Adding a new star to the hash table
stars_hash_table["Andromeda"] = "A galaxy in the Andromeda constellation"

# 2. **Retrieval**: Retrieving the description of a star using its key
star_description = stars_hash_table.get("Polaris")

# 3. **Deletion**: Removing a star from the hash table
removed_star = stars_hash_table.pop("Betelgeuse", "Star not found")

# 4. **Check if a Star Exists**: Checking if a star is in the hash table
is_present = "Alpha Centauri" in stars_hash_table

print("Hash Table after Insertion:", stars_hash_table)
print("Description of Polaris:", star_description)
print("Removed Star:", removed_star)
print("Is Alpha Centauri present?", is_present)
print("\n")



# BINARY TREE

class Node:
    def __init__(self, star_name):
        self.star_name = star_name
        self.left = None
        self.right = None

# Create nodes for the stars
ancestor = Node("Ancestor")          # Root node
sirius = Node("Sirius")              # Left child of root
alpha_centauri = Node("Alpha Centauri")  # Right child of root

# Build the tree
ancestor.left = sirius
ancestor.right = alpha_centauri

# Simple tree display (Pre-order traversal)
def display_tree(node):
    if node:
        print(node.star_name)
        display_tree(node.left)
        display_tree(node.right)

# Display the tree
display_tree(ancestor)
