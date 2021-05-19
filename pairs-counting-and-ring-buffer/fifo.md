# Очередь FIFO на списке

## Базовые операции

Инициализация:

```python
Q = []
```

PUSH (добавить элемент в очередь):

```python
Q.append(x)
```

POP (удалить элемент из начала очереди и возвратить его в качестве результата):

```python
x = Q.pop(0)
```

## Циклическая очередь длины M

Инициализация:

```python
Q = [int(input()) for i in range(M)]
top = 0 # вершина
```

PUSHPOP:

```python
# top - текущая вершина
y = Q[top]
Q[top] = x
top = (top + 1) % M
# top += 1
# if top == M:
#     top = 0
```

Удобство в цикле:

```python
for i in range(M):
    top = (top + 1) % M # top - то же самое, что и i % 3
```
