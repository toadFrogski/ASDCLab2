import json
import csv
from enum import Enum
from typing import Self


class Student():

    class Department(Enum):
        BUISNESS = 0
        EDUCATION = 1
        ENGINEERING = 2
        LAW = 3
        MEDICINE = 4
        IT = 5

    def __init__(self, id=None, name=None, department=None, birthday=None, admission=None) -> None:
        self.id = id
        self.name = name
        self.department = department
        self.birthday = birthday
        self.admission = admission

    def copy(self, student: Self) -> Self:
        self.id = student.id
        self.name = student.name
        self.department = student.department
        self.birthday = student.birthday
        self.admission = student.admission
        return self

    def __eq__(self, __o) -> bool:
        result = False
        for key in self.__dict__.keys():
            result = True if getattr(self, key) == __o else result
        return result

    def read(self, student: dict[str, str]) -> Self:
        for key, value in student.items():
            setattr(self, key, value) if hasattr(
                self, key) else setattr(self, key, None)
        return self

    def __str__(self):
        return f"id: {self.id}, 'name': {self.name}, 'department: {self.Department(self.department).name}, 'birthday': {self.birthday}, 'admission': {self.admission}"


class StudentSerializer:

    @staticmethod
    def serialize(file, format=None, options: dict[str, str] | None = {}):
        format = file.split('.')[-1] if format is None else format
        serializer = StudentSerializer.__get_serializer(format)
        return serializer(file, options)

    def __get_serializer(format):
        if format in ('json', 'JSON'):
            return StudentSerializer.__serialize_from_json
        elif format in ('csv', 'CSV'):
            return StudentSerializer.__serialize_from_csv
        else:
            raise ValueError(format)

    def __serialize_from_json(file, options):
        encoding = options['encoding'] if options.get('encoding') else 'utf-8'
        with open(file, 'r', encoding=encoding) as f:
            return json.loads(f.read())

    def __serialize_from_csv(file, options):
        encoding = options['encoding'] if options.get('encoding') else 'utf-8'
        delimeter = options['delimeter'] if options.get('delimeter') else ';'
        with open(file, 'r', encoding=encoding, newline='') as f:
            return [row for row in csv.DictReader(f, delimiter=delimeter)]
