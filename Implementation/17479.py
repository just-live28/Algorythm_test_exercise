import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
menu = {}
service = set()
for _ in range(a):
    name, price = input().rstrip().split()
    menu[name] = (0, int(price))
for _ in range(b):
    name, price = input().rstrip().split()
    menu[name] = (1, int(price))
for _ in range(c):
    service.add(input().rstrip())

n = int(input())
service_count = 0
normal_total = 0
special_total = 0
for _ in range(n):
    name = input().rstrip()

    if name in service:
        service_count += 1
        continue

    menu_type, menu_price = menu[name]
    if menu_type == 0:
        normal_total += menu_price
    elif menu_type == 1:
        special_total += menu_price

is_okay = True
if service_count > 1:
    is_okay = False
elif service_count == 1 and normal_total + special_total < 50000:
    is_okay = False
elif special_total > 0 and normal_total < 20000:
    is_okay = False

if is_okay:
    print('Okay')
else:
    print('No')