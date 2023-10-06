def join_array_remove_duplicate(arrayA, arrayB):
    # your code here
    array_gabungan = arrayA + arrayB
    
    nilai_unik = set()
    hasil_array = []
    
    for nilai in array_gabungan:
        if nilai not in nilai_unik:
            nilai_unik.add(nilai)
            hasil_array.append(nilai)
    
    return hasil_array


if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
