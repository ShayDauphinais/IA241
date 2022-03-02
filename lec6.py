'''
lec 6
'''

demo_str = 'this is my string'
for str_item in demo_str:
    print(str_item)

demo_str = 'this is my string'
for word_item in demo_str.split():
    print(word_item)
    
for i in range(5):
    print(i)
    
for i in range(1,5):
    print(i)

for i in range(1,5,2):
    print(i)

num_list = [213, 321, 123, 312]
max_item = num_list[0]

for num in num_list:
    if max_item<=num:
        max_item=num
print(max_item)