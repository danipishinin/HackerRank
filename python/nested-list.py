from operator import itemgetter

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # order to score and for name
    sorted_list = sorted(students, key=itemgetter(1, 0))
    
    # get the second lowest grade
    lowest_position = 0
    for i in range(0, len(sorted_list)):
        if sorted_list[i][1] > sorted_list[lowest_position][1]:
            lowest_position = i
            break

    # print people with second lowest grade
    for i in range(0, len(sorted_list)):
        if sorted_list[i][1] == sorted_list[lowest_position][1]:
            print(sorted_list[i][0])