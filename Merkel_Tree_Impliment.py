import hashlib

# Function to calculate the SHA-256 hash of a string
def calculate_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# List of transactions
transactions = [
    "Dear UPI user A/C X8420 debited by 80.0 on date 24JUL23 time 10.084 am trf to Maa Tarini Varie Refno 320913455297",
    "Dear UPI user A/C X8420 debited by 100.0 on date 25JUL23 time 9.03 am trf to PRASANT KUMAR DA Refno 324450623256",
    "Dear UPI user A/C X8420 debited by 175.0 on date 26JUL23 time 4.54 pm trf to MANISH MEHER Refno 361095582975",
    "Dear UPI user A/C X8420 debited by 10.0 on date 27JUL23 time 10.084 am trf to SIBANI SAHOO Refno 320913457554",
    "Dear UPI user A/C X8420 debited by 170.0 on date 02SEP23 time 6.03 am trf to KHISOR MISHRA Refno 324450623324",
    "Dear UPI user A/C X8420 debited by 17.0 on date 03SEP23 time 11.54 pm trf to PUJA RAO Refno 361095582431",
    "Dear UPI user A/C X8420 debited by 17.0 on date 04SEP23 time 1.54 pm trf to ASHIS ROY Refno 361095582221"
]

# Function to build the Merkle tree
def build_merkle_tree(transactions):
    if len(transactions) % 2 != 0:
        transactions.append(transactions[-1])  # Duplicate the last transaction if odd number
    
    hashes = [calculate_hash(txn) for txn in transactions]
    
    while len(hashes) > 1:
        next_level = []
        for i in range(0, len(hashes), 2):
            combined_hash = hashes[i] + hashes[i+1]
            next_level.append(calculate_hash(combined_hash))
        hashes = next_level
    
    return hashes[0]

# Build the Merkle tree
merkle_root = build_merkle_tree(transactions)
print(f"Merkle Root: {merkle_root}")
