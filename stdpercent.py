if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    lst = student_marks[query_name]
    lambai = len(lst)
    total = 0
    for x in lst:
        total += x

    avg = total / lambai
    print('%.2f' % avg)