from typing import Dict


class ReportFormatter:
    @staticmethod
    def format_report(report_data: Dict, level: int = 0) -> None:
        indent = "  " * level
        if 'company_name' in report_data:
            print(f"🏢 Отчет по компании: {report_data['company_name']}")
            print(f"💰 Общая сумма зарплат: {report_data['total_company_salary']:,.2f}")
            print(f"📊 Средняя зарплата: {report_data['average_company_salary']:,.2f}")
            print("\n📋 Данные по департаментам:")
            for dept in report_data['departments']:
                ReportFormatter.format_report(dept, level + 1)

        elif 'department_name' in report_data:
            print(f"\n{indent}🏫 Департамент: {report_data['department_name']}")
            print(f"{indent}💵 Общая сумма зарплат: {report_data['total_salary']:,.2f}")
            print(f"{indent}📈 Средняя зарплата: {report_data['average_salary']:,.2f}")
            print(f"{indent}👥 Сотрудники:")
            for emp in report_data['employees_salaries']:
                print(f"{indent}  👤 {emp['position']}: {emp['salary']:,.2f}")

