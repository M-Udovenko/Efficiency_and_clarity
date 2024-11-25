from abc import ABC, abstractmethod
from typing import Dict
from models import Employee, Department, Company


class ReportVisitor(ABC):
    @abstractmethod
    def visit_employee(self, employee: Employee) -> Dict:
        pass

    @abstractmethod
    def visit_department(self, department: Department) -> Dict:
        pass

    @abstractmethod
    def visit_company(self, company: Company) -> Dict:
        pass


class SalaryReportVisitor(ReportVisitor):
    def visit_employee(self, employee: Employee) -> Dict:
        return {
            'position': employee.position,
            'salary': employee.salary
        }

    def visit_department(self, department: Department) -> Dict:
        salaries = [emp.accept(self) for emp in department.employees]
        total_salary = sum(s['salary'] for s in salaries)

        return {
            'department_name': department.name,
            'employees_salaries': salaries,
            'total_salary': total_salary,
            'average_salary': total_salary / len(salaries) if salaries else 0
        }

    def visit_company(self, company: Company) -> Dict:
        departments_data = [dept.accept(self) for dept in company.departments]
        total_company_salary = sum(d['total_salary'] for d in departments_data)
        total_employees = sum(len(d['employees_salaries']) for d in departments_data)

        return {
            'company_name': company.name,
            'departments': departments_data,
            'total_company_salary': total_company_salary,
            'average_company_salary': total_company_salary / total_employees if total_employees else 0
        }

