coverage = set()
input_num = input()
while input_num != 'end':
    input_num = input_num.split(',')
    a, b = min(int(input_num[0]), int(input_num[1])), max(int(input_num[0]), int(input_num[1]))
   # print(i for i in range(a,b))
    set_ab = set()
    for i in range(a, b +1):
        set_ab.add(i)
    coverage = coverage.union(set_ab)
    print("Покрытие объединенного интервала: {}".format(len(coverage))) 
    input_num = input()
