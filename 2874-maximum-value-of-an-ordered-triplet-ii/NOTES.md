result = 0
​
max_num = max_difference = 0
​
for num in nums:
​
result = max(result, max_difference * num)
​
max_difference = max(max_difference , max_num - num)
​
max_num = max(max_num , num)
​
return result