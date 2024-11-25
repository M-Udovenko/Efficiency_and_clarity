from models import Employee, Department, Company
from visitors import SalaryReportVisitor
from report_formatter import ReportFormatter


def create_sample_company() -> Company:

    developers = [
        Employee("Senior Developer", 150000),
        Employee("Middle Developer", 100000),
        Employee("Junior Developer", 70000)
    ]

    marketing = [
        Employee("Marketing Director", 130000),
        Employee("Marketing Manager", 90000),
        Employee("Marketing Specialist", 60000)
    ]

    dev_department = Department("Development", developers)
    marketing_department = Department("Marketing", marketing)

    return Company("Tech Stars", [dev_department, marketing_department])


def main():
    company = create_sample_company()

    salary_visitor = SalaryReportVisitor()

    print("=" * 50)
    print("📊 ОБЩИЙ ОТЧЕТ ПО КОМПАНИИ")
    print("=" * 50)
    company_report = company.accept(salary_visitor)
    ReportFormatter.format_report(company_report)

    print("\n" + "=" * 50)
    print("📊 ОТЧЕТ ПО ДЕПАРТАМЕНТУ РАЗРАБОТКИ")
    print("=" * 50)
    dev_department_report = company.departments[0].accept(salary_visitor)
    ReportFormatter.format_report(dev_department_report)


if __name__ == "__main__":
    main()