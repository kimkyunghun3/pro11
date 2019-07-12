import sys
n = 9
heights = [int(input()) for _ in range(n)]
heights.sort()
sum_heights=sum(heights)
for i in range(n):
    for j in range(i+1, n):
        if sum_heights - heights[i]-heights[j] == 100:
            for k in range(n):
                if i!= k and j != k:
                    print(heights[k])
            sys.exit(0)
