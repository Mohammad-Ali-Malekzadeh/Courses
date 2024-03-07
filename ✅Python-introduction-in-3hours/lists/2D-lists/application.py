queb_list = [
    [2, 1, 3],
    [4, 8, 2],
    [3, 5, 4]
]

# print(queb_list[0][1])

for queb in queb_list:
    result = 1
    for dimesion in queb:
        result = result * dimesion
    
    print(result)