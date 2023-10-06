def muncul_sekali(angka):
    angka_count = {} 
    
    for digit in angka:
        if digit in angka_count:
            angka_count[digit] += 1
        else:
            angka_count[digit] = 1
    
    muncul_sekali_list = []
    for digit, count in angka_count.items():
        if count == 1:
            muncul_sekali_list.append(int(digit))

    return muncul_sekali_list

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]