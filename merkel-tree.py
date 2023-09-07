import hashlib

# here function to calculate the hash of data
def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# List of data elements (transactions)
data_list = ["Transaction1", "Transaction2", "Transaction3", "Transaction4"]

# Then here Calculating the hash for each data element and store them in a list
hashed_data_list = [calculate_hash(data) for data in data_list]

# leaf nodes of the Merkle tree
leaf_nodes = hashed_data_list

# Building the Merkle tree from the leaf nodes
while len(leaf_nodes) > 1:
    new_level = []
    # Pair adjacent nodes, hash them together, and store the result in the new level
    for i in range(0, len(leaf_nodes), 2):
        if i + 1 < len(leaf_nodes):
            combined_hash = calculate_hash(leaf_nodes[i] + leaf_nodes[i + 1])
            new_level.append(combined_hash)
        else:
            # If there's an odd number of nodes, hash the last node with itself
            combined_hash = calculate_hash(leaf_nodes[i] + leaf_nodes[i])
            new_level.append(combined_hash)
    leaf_nodes = new_level

# Step 4: The root hash (Merkle root) is the final remaining element in the tree
merkle_root = leaf_nodes[0]

# Print the Merkle root
print("Merkle Root:", merkle_root)
