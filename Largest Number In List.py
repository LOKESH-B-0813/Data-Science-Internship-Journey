numbers=[100,90,80,20,190,200]
if not numbers:
  print("The list is empty")
else:
  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
  print(largest)
