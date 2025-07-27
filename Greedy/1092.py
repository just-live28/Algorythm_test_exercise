n = int(input())
crains = list(map(int, input().split()))
crains.sort(reverse=True)
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

if boxes[0] > crains[0]:
    print(-1)
else:
    time = 0
    while boxes:
        idx = 0
        for crain in crains:
            while idx < len(boxes):
                if crain >= boxes[idx]:
                    del boxes[idx]
                    break
                idx += 1
        time += 1

    print(time)