BASE = 13
N = 101

def rolling_hash():
    string = "banana"
    hash_size = 3
    hashes = []

    i = hash_size
    strlen = len(string)
    while i <= strlen:
        hash = 0
        for j in range(i - hash_size, i):
            hash = ((hash * BASE) + ord(string[j])) % N
        hashes.append(hash)
        i += 1

    print(hashes)


rolling_hash()
