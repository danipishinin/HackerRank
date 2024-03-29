if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student_selected = student_marks.get(query_name)
    avarege = 0
    for i in range(len(student_selected)): 
        avarege += student_selected[i]
    avarege /= 3
    print("{:.2f}".format(avarege))