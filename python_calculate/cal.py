print("Enter the first number ")
first = input()
print("Enter the Second number ")
sec = input()

print("Enter the operation")
op = input()

if op ==  "+":
    ans = float(first) + float(sec)
elif op == "-":
    ans = float(first) - float(sec)
elif op == "*":
    ans = float(first) * float(sec)
elif op == "/":
    ans = float(first) / float(sec)

print("the result is",ans)