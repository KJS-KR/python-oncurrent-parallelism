class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return "This Object - Company : {0}, Detail : {1}".format(
            self._company, self._details
        )

    # def __repr__(self):
    #     return "This Object - Company : {0}, Detail : {1}".format(
    #         self._company, self._details
    #     )


c = Car("car", "red")

print(c.__str__())
print(c.__repr__())

# 딕셔너리로 car1 객체 정보 출력
car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

print(car1.__dict__)

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 반복(__str__)
for x in car_list:
    print(repr(x))
    print(x)
