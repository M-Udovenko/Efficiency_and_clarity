from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


class Visitable(ABC):
    @abstractmethod
    def accept(self, visitor: ReportVisitor) -> dict:
        pass


class Employee(Visitable):
    def __init__(self, position: str, salary: float):
        self.position = position
        self.salary = salary

    def accept(self, visitor: ReportVisitor) -> dict:
        return visitor.visit_employee(self)


class Department(Visitable):
    def __init__(self, name: str, employees: List[Employee]):
        self.name = name
        self.employees = employees

    def accept(self, visitor: ReportVisitor) -> dict:
        return visitor.visit_department(self)


class Company(Visitable):
    def __init__(self, name: str, departments: List[Department]):
        self.name = name
        self.departments = departments

    def accept(self, visitor: ReportVisitor) -> dict:
        return visitor.visit_company(self)

