# CRANIUM BONES (INSERTION SORT)

# Dictionary with bones in random order
bones_count = {
    "frontal": 1,
    "temporal": 2,
    "sphenoid": 1,
    "parietal": 2,
    "ethmoid": 1,
    "occipital": 1
}

# Function to arrange bones by their count
def arrange_bones_by_count(bones_count):
    # Sort the dictionary items by their count in descending order
    sorted_bones = sorted(bones_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_bones

# Arrange the bones
arranged_bones = arrange_bones_by_count(bones_count)

# Display the arrangement
print("Bones arranged by count (descending order):")
for bone, count in arranged_bones:
    print(f"{bone.capitalize()} Bone: {count}")
print("\n")




# FACIAL BONES (MERGE SORT)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the first half
        merge_sort(right_half)  # Recursively sort the second half

        # Merge the two halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in the left or right half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# List of bones with their counts (1 for single, 2 for paired)
bones_count = [
    ("mandible", 1),
    ("maxilla", 2),
    ("vomer", 1),
    ("zygomatic", 2),
    ("lacrimal", 2),
    ("nasal", 2),
    ("inferior concha", 2),
    ("palatine", 2)
]

# Apply merge sort based on bone count
merge_sort(bones_count)

# Display the sorted list based on their count
print("Bones sorted by number of bones (ascending order):")
for bone, count in bones_count:
    print(f"{bone.capitalize()} Bone: {count}")
print("\n")




# HEAP SORT (FORELIMBS)

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left][1] > arr[largest][1]:
        largest = left

    # Check if right child exists and is greater than largest
    if right < n and arr[right][1] > arr[largest][1]:
        largest = right

    # If largest is not root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

# Heap sort function
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the last element
        heapify(arr, i, 0)  # Heapify the root element

# List of bones with their position value (Humerus = 1, Radius = 2, etc.)
bones_position = [
    ("metacarpals", 5),
    ("radius", 2),
    ("ulna", 3),
    ("humerus", 1),
    ("carpals", 4),
    ("phalanges", 6)
]

# Apply heap sort to sort bones based on their position
heap_sort(bones_position)

# Display the sorted list
print("Bones sorted by position in the body:")
for bone, position in bones_position:
    print(f"{bone.capitalize()} (Position: {position})")
print("\n")




# QUICK SORT (HIND LIMBS)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0][1]  # The position of the first bone
    left = [x for x in arr[1:] if x[1] <= pivot]
    right = [x for x in arr[1:] if x[1] > pivot]
    return quick_sort(left) + [arr[0]] + quick_sort(right)

# List of bones in random order with their position directly specified
bones_input = [
    ("metatarsals", 5),
    ("fibula", 3),
    ("femur", 1),
    ("tarsals", 4),
    ("tibia", 2),
    ("feet phalanges", 6)
]

# Apply Quick Sort to sort bones based on their position
sorted_bones = quick_sort(bones_input)

# Display the sorted bones
print("Bones sorted by position in the body:")
for bone, position in sorted_bones:
    print(f"{bone.capitalize()} (Position: {position})")
print("\n")




# EAR AND NECK BONE (ARRAY INSERTION)

def insert_bone(bones_list, bone):
    bones_list.append(bone)
    print(f"'{bone.capitalize()}' has been inserted.")
    return bones_list

# Initial list of bones
bones = ["incus", "malleus", "stapes"]

# Insert a new bone
new_bone = "hyoid"
bones = insert_bone(bones, new_bone)

# Display the updated list
print("Updated list of bones:", bones)
print("\n")




# ARRAY DELETION

def delete_bone(bones_list, bone):
    if bone in bones_list:
        bones_list.remove(bone)
        print(f"'{bone.capitalize()}' has been deleted.")
    else:
        print(f"'{bone.capitalize()}' not found in the list.")
    return bones_list

# Initial list of bones
bones = ["incus", "malleus", "stapes", "hyoid"]

# Delete a bone
bone_to_delete = "hyoid"
bones = delete_bone(bones, bone_to_delete)

# Display the updated list
print("Updated list of bones:", bones)
print("\n")




# SEARCHING IN ARRAY

def search_bone(bones_list, bone):
    if bone in bones_list:
        print(f"'{bone.capitalize()}' found in the list.")
    else:
        print(f"'{bone.capitalize()}' not found in the list.")

# Initial list of bones
bones = ["incus", "malleus", "stapes", "hyoid"]

# Search for a bone
search_bone(bones, "malleus")
search_bone(bones, "hyoid")
search_bone(bones, "clavicle")
print("\n")




# MERGE TWO ARRAYS

# Arrays (lists) of bones
array1 = ["malleus", "incus"]
array2 = ["stapes", "hyoid"]

# Merge the two arrays
merged_array = array1 + array2

# Display the merged array
print("Merged array of bones:", merged_array)
print("\n")




# VERTEBRAES (STACK)

# Stack class to represent the vertebrae
class VertebraeStack:
    def __init__(self):
        self.stack = []

    # Function to push a vertebra onto the stack
    def push(self, vertebra):
        self.stack.append(vertebra)
        print(f"'{vertebra.capitalize()}' vertebra added to the stack.")

    # Function to pop a vertebra from the stack
    def pop(self):
        if len(self.stack) > 0:
            removed_vertebra = self.stack.pop()
            print(f"'{removed_vertebra.capitalize()}' vertebra removed from the stack.")
        else:
            print("No vertebrae in the stack to remove.")

    # Function to display the current stack of vertebrae
    def display_stack(self):
        print("\nCurrent stack of vertebrae (top to bottom):")
        for vertebra in reversed(self.stack):
            print(vertebra.capitalize())

    # Function to arrange vertebrae in the correct order
    def arrange_stack(self):
        # Correct order of vertebrae
        correct_order = ["cervical", "thoracic", "lumbar", "sacral", "coccyx"]
        
        # Sort the stack according to the correct order
        self.stack = sorted(self.stack, key=lambda vertebra: correct_order.index(vertebra))
        print("\nVertebrae arranged in correct order:")

# Initialize the stack for vertebrae
vertebrae_stack = VertebraeStack()

# Insert vertebrae in random order
vertebrae_stack.push("thoracic")
vertebrae_stack.push("lumbar")
vertebrae_stack.push("sacral")
vertebrae_stack.push("coccyx")
vertebrae_stack.push("cervical")

# Display the current stack in random order
vertebrae_stack.display_stack()

# Pop a vertebra from the stack
vertebrae_stack.pop()

# Display the stack after popping a vertebra
vertebrae_stack.display_stack()

# Arrange vertebrae in correct order
vertebrae_stack.arrange_stack()

# Display the stack after arranging in correct order
vertebrae_stack.display_stack()
print("\n")




# PECTORAL GIRDLE (SIMPLE QUEUE)

from queue import Queue

# Create a simple queue
simple_queue = Queue()

# Enqueue bones
simple_queue.put("ventral coracoid")
simple_queue.put("scapula")
simple_queue.put("clavicle")

# Display the queue (before dequeuing)
print("Simple Queue (FIFO) - Before Dequeue:")
while not simple_queue.empty():
    print(simple_queue.get())  # Dequeue the elements one by one
print("\n")




# CIRCULAR QUEUE
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
            return
        elif self.front == -1:  # If queue is empty
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"'{item}' added to circular queue.")

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
            return
        i = self.front
        print("Circular Queue (from front to rear):")
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# Create a circular queue
circular_queue = CircularQueue(5)

# Enqueue bones
circular_queue.enqueue("ventral coracoid")
circular_queue.enqueue("scapula")
circular_queue.enqueue("clavicle")

# Display the queue (after enqueueing)
circular_queue.display()
print("\n")




# PELVIC GIRDLE (PRIORTY QUEUE)

from queue import PriorityQueue

# Create a priority queue
priority_queue = PriorityQueue()

# Enqueue bones with priority (lower number means higher priority)
priority_queue.put((1, "ilium"))  # Highest priority
priority_queue.put((2, "ischium"))
priority_queue.put((3, "pubis"))  # Lowest priority

# Display the queue (before dequeuing)
print("Priority Queue (Highest priority first):")
while not priority_queue.empty():
    priority, bone = priority_queue.get()
    print(f"{bone} with priority {priority}")
print("\n")



 
# DEQUE

from collections import deque

# Create a deque
bone_deque = deque()

# Add bones to the deque (front and rear)
bone_deque.append("ilium")  # Add to the rear
bone_deque.appendleft("ischium")  # Add to the front
bone_deque.append("pubis")  # Add to the rear

# Display the deque
print("Deque (elements added to front and rear):")
print(bone_deque)

# Remove an element from the front and rear
removed_from_front = bone_deque.popleft()
removed_from_rear = bone_deque.pop()

print(f"Removed from front: {removed_from_front}")
print(f"Removed from rear: {removed_from_rear}")

# Display the updated deque
print("Updated deque:")
print(bone_deque)
print("\n")




# RIBS (HASH)

# Dictionary to store rib information
ribs = {
    1: "True rib",
    2: "True rib",
    3: "True rib",
    4: "True rib",
    5: "True rib",
    6: "True rib",
    7: "True rib",
    8: "False rib",
    9: "False rib",
    10: "False rib",
    11: "Floating rib",
    12: "Floating rib"
}

# Function to display information about a rib
def get_rib_info(rib_number):
    # Using hash (dictionary) to retrieve information
    if rib_number in ribs:
        print(f"Rib {rib_number}: {ribs[rib_number]}")
    else:
        print("Invalid rib number! Please enter a number between 1 and 12.")

# Taking user input for rib number
rib_number = int(input("Enter rib number (1 to 12): "))

# Display the information about the rib
get_rib_info(rib_number)
print("\n")



# CONNECTIVE TISSUES (TREE)
class TreeNode:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.left = None  # Left child
        self.right = None  # Right child

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}{self.name}: {self.description if self.description else ''}")
        if self.left:
            self.left.display(level + 1)
        if self.right:
            self.right.display(level + 1)


# Creating the root node (Connective Tissue)
connective_tissue = TreeNode("Connective Tissue")

# Creating child nodes (Bone and Cartilage)
bone = TreeNode("Bone (Osseous Tissue)", "Hard and rigid connective tissue")
cartilage = TreeNode("Cartilage", "Flexible connective tissue")

# Assigning Bone and Cartilage as children of Connective Tissue
connective_tissue.left = bone
connective_tissue.right = cartilage

# Displaying the tree structure
connective_tissue.display()
print("\n")


