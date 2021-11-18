from DS.stack import Stack

l1 = Stack()
l1.printall()
for i in range(10):
    l1.push(i)

l1.printall()

print(l1.peek())
l1.printall()
l1.pop()
l1.pop()
l1.pop()
l1.pop()
print(l1.peek())
l1.printall()
