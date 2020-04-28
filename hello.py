#this is a comment

#printing stuff
print('Hi abhi')
a = "first"
print(a)

#boolean value
print(1 > 2)

#list
#contains haterogenious data
list_a = [1,2,'three']
list_a[0] = 5

#for loop
for x in list_a:
    print(x)

#tuple
tuple_a = (1,2,"three")
print(tuple_a)

#Following not possible for tuple
#tuple_a[0] = 2

#Dict
dict_a = {
    'type': 'car',
    'name': 'merc'
}
print('type is '+ dict_a['type'])

#if else
if dict_a['type'] == 'car':
    print('yes')

#while loop
num = 2
while num > 0:
    print(num)
    num -= 1

#function
def myFunc():
    print('calling myFunc()')

myFunc()
