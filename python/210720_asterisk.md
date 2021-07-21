210720 

# Asterisk(*)

가변 인자

```python
#끼워넣기
a = ['h', 'i']

c= ['b', 'y', 'e']

print(a + c)
print([*a, 'w', *c])


[출력]
['h', 'i', 'b', 'y', 'e']
['h', 'i', 'w', 'b', 'y', 'e']
```



```python
#
listall = list(range(10))
lista = listall[:5]
listb = listall[5:]

print(listall)
print(lista)
print(listb)
new_list = [*listb, *lista]
print(new_list)


[출력]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9, 0, 1, 2, 3, 4]

```



```python
numbers = [1,2,3,4,5,6]
*a, = numbers
print(*a)

*a, b = numbers
print(*a, '///', b)

a, *b =numbers
print(a, '///', *b)

a, *b, c = numbers
print(a, '/', *b, '/', c)

a, b, *lista, c = numbers
print(a, '/', b, '/', *lista , '/', c)
```

```
1 2 3 4 5 6
1 2 3 4 5 /// 6
1 /// 2 3 4 5 6
1 / 2 3 4 5 / 6
1 / 2 / 3 4 5 / 6
```
