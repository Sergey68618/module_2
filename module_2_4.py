my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
counter = 0
while counter < len(my_list):
    num = my_list[counter]
    counter +=1     #counter = counter + 1
    if num == 0:
        continue
    elif num < 0:
        break
    else:
        print(num)