from functools import reduce
from src.classes.student import Student, StudentSerializer
from src.services.algsorts import Sort


def lab2():

    students = [Student().read(student) for student in StudentSerializer.serialize('./data/students.json')]
    shell = Sort.shell(students.copy(), 'name')
    print(f"Shell sort\tswp:\t{shell[1]}\tcmp:\t{shell[2]}\tBest:O(n*log(n))\tWorst:O(n^2)")
    quick = Sort.quickSort(students.copy(), 'name')
    print(f"Quick sort\tswp:\t{quick[1]}\tcmp:\t{quick[2]}\tBest:O(n*log(n))\tWorst:O(n^2)")
    merge = Sort.mergeSort(students.copy(), 'name')
    print(f"Quick sort\tswp:\t{merge[1]}\tcmp:\t{merge[2]}\tBest:O(n*log(n))\tWorst:O(n*log(n))")
