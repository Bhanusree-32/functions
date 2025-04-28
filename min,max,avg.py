def values(numbers):
return min(numbers),max(numbers),sum(numbers)/len(numbers)
min_val,max_val,avg=values([1,2,3,4,5])
print(f"min:{min_val},max:{max_val},average:{avg}")
