import random
from datetime import timedelta, date

from django.core.management.base import BaseCommand
from faker import Faker

from users.models import CustomUser
from employee.models import Department, Employee, Attendance, Performance

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with fake users, departments, employees, attendance, and performance data'

    def handle(self, *args, **kwargs):
        users = []
        for _ in range(60):
            user = CustomUser.objects.create_user(
                email=fake.unique.email(),
                password='password123',
                name=fake.name(),
                mobile=fake.unique.msisdn()[:13]
            )
            users.append(user)

        departments = []
        for _ in range(5):
            dept = Department.objects.create(
                name=fake.unique.job(),
                created_by=random.choice(users)
            )
            departments.append(dept)

        employee_users = random.sample(users, 50)
        employees = []

        for user in employee_users:
            emp = Employee.objects.create(
                user=user,
                department=random.choice(departments),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='-1d')
            )
            employees.append(emp)

        for employee in employees:
            for i in range(10):  # 10 days of attendance per employee
                Attendance.objects.create(
                    employee=employee,
                    date=date.today() - timedelta(days=i),
                    status=random.choice(['present', 'absent', 'late'])
                )

        for employee in employees:
            Performance.objects.create(
                employee=employee,
                rating=random.randint(1, 5),
                review_date=fake.date_between(start_date='-1y', end_date='today')
            )

