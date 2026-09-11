from employee import Employee
import pytest

@pytest.fixture
def default_employee():
    employee = Employee('Chris', 'Slusher', 166000)
    return employee

def test_give_default_raise(default_employee):
    default_employee.give_raise()

    assert default_employee.annual_salary == 171000

def test_give_custom_raise(default_employee):
    default_employee.give_raise(4000)

    assert default_employee.annual_salary == 170000