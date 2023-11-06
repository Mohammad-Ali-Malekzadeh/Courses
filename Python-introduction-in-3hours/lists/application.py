colors = ['Green', 'Blue', 'Black', 'White', 'Red', 'Green']
sorted_colors = sorted(colors)
# colors[1:4] = ['Yellow', 'Gray', 'Orange'] #! access to part of list with [start : until]
# colors[:4] = ['Yellow', 'Gray', 'Orange'] #! start from zero index [:X] until X
# colors.extend(['Ali', 'Mahdi']) #! Add list to end of the Main list
# colors.append('new index') #! Add to end of list - (Just one index)
# colors.insert(1, 'inserted index') #! Add to list anywhere
# colors.remove('Green') #! Remove First 'Green'
# colors.clear() 
# colors.reverse() #! reverse all indexes whose result is similar Previous list but start from the end until the first index    
# colors.pop(-2) #! delete from end of the list
del colors


print(colors[-1]) #! When adding - to numbers, this means counting from the end of the list
print(colors)  
print(len(colors))
print(colors.count('Green')) #! count Green in list
