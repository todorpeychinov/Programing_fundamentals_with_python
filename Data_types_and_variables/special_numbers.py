number = int(input())

for i in range(1, number + 1):
     temp_list = list(str(i))
     temp_sum = 0
     for j in range(len(temp_list)):
         temp_sum += int(temp_list[j])

     if temp_sum == 5 or temp_sum == 7 or temp_sum == 11:
         print(f"{i} -> True")
     else:
         print(f"{i} -> False")



