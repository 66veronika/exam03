# Write a function that rotates an array to the right by k positions,
# rotating right by k means the last k elements move to the front.

def twist_sequence(arr: list[int], k: int) -> list[int]:
    split = len(arr) - k
    return arr[split:] + arr[:split]


print(twist_sequence([1, 2, 3, 4, 5], 2))
