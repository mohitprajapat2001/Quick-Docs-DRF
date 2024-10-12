from dataclasses import dataclass


@dataclass
class Test:
    name: str
    age: int

    def get_data(self):
        print(self.name, self.age)


Test(name="Mohit", age=22).get_data()
