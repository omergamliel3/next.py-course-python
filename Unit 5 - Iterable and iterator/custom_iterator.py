class Employee:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def get_name(self):
        return self._name


class EmployeeManager:
    def __init__(self):
        self._employee_lst = []

    def add_employee(self, new_employee: Employee):
        self._employee_lst.append(new_employee)

    def get_employees(self):
        return self._employee_lst

    # implementing "Iterator Protocol"

    # create index and return self
    def __iter__(self):
        self.eml_index = -1
        return self

    # increment index by 1 and return
    # element at index from employee_lst
    def __next__(self):
        # raise StopIteration exception when reach the end of the list
        if self.eml_index >= len(self._employee_lst) - 1:
            raise StopIteration()

        self.eml_index += 1
        return self._employee_lst[self.eml_index].get_name()


def main():
    hr_manager = EmployeeManager()
    hr_manager.add_employee(Employee("Lia Levi", 30, 20000))
    hr_manager.add_employee(Employee("Yosef Cohen", 32, 4800))
    hr_manager.add_employee(Employee("Oded Haim", 47, 5100))

    # allow us to iterate employee list in hr_manager and
    # print the name directly
    for empl in hr_manager:
        print(f'Name: {empl}')

    # instead of traditionaly iteration
    for impl in hr_manager.get_employees():
        print(f'Name: {impl.get_name()}')


if __name__ == "__main__":
    main()
