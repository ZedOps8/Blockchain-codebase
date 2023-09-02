import hashlib

# Define a class for a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class for the linked list
class HashLinkedList:
    def __init__(self):
        self.head = None

    # Add a new node to the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Calculate the hash code of a given data
    @staticmethod
    def calculate_hash(data):
        return hashlib.md5(data.encode()).hexdigest()

    # Display data and their hash codes
    def display(self):
        current = self.head
        while current:
            data = current.data
            hash_code = self.calculate_hash(data)
            print(f"{data}: {hash_code}")
            current = current.next

# Create a HashLinkedList and add data
hash_linked_list = HashLinkedList()
data_list = ["CSE", "CSIT", "CSEAIML", "CSEDS", "CS"]

for data in data_list:
    hash_linked_list.append(data)

# Display the data along with their hash
hash_linked_list.display()
