def pair_sum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        jumlah_sekarang = arr[left] + arr[right]

        if jumlah_sekarang == target:
            return [left, right]
        elif jumlah_sekarang < target:
            left += 1
        else:
            right -= 1

    return None

print(pair_sum([1, 2, 3, 4, 6], 6))  # [1, 3]
print(pair_sum([2, 5, 9, 11], 11))   # [0, 2]
print(pair_sum([1, 3, 5, 7], 12))    # [2, 3]
print(pair_sum([1, 4, 6, 8], 10))    # [1, 2]
print(pair_sum([1, 5, 6, 7], 6))     # [0, 1]