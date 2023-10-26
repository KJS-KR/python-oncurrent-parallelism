# Chapter02-02
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수


# 클래스 재 선언
class Car:
    # 클래스 설명 주석 __doc__ 메서드를 통해 확인
    """
    Car Class
    Author : Kim
    Date : 2023.10.10
    """

    # 클래스 변수 : 같은 클래스로 만들어진 모든 인스턴스가 공유하는 데이터
    #
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "repr : {} - {}".format(self._company, self._details)

    def detail_info(self):
        print("Current Id : {}".format(id(self)))
        print(
            "Car Detail Info : {} {}".format(self._company, self._details.get("price"))
        )

    def __del__(self):
        Car.car_count -= 1


# Self 의미
car1 = Car("Ferrari", {"color": "White", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

# ID 확인
print("-------- Check ID --------")
print(id(car1))
print(id(car2))
print(id(car3))
print()

print("car1 company = car2 company : ", car1._company == car2._company)
print("car1 object = car2 object : ", car1 is car2)
print()


# dir & __dict__ 확인
# dir : 해당 객체가 어떤 변수와 메소드(method)를 가지고 있는지 나열
print("-------- dir() --------")
print(dir(car1))
print(dir(car2))
print()

print("-------- __dict__ --------")
print(car1.__dict__)
print(car2.__dict__)
print()

# Doctring
print("-------- __doc__ --------")
print(Car.__doc__)
print()

# 실행
print("-------- detail_info() --------")
car1.detail_info()
car2.detail_info()
print()

# 에러
print("-------- Error --------")
# Car.detail_info()
# print()

# Car.detail_info()
print("-------- detail_info Other Way --------")
Car.detail_info(car1)
Car.detail_info(car2)
print()

# 비교
print("-------- __class__ --------")
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car3.__class__))
print(id(car1.__class__), id(car3.__class__))
print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장X)
print("-------- Instance Variable --------")
print(car1._company, car2._company)
print(car2._company, car3._company)
print()

# 클래스 변수
# 접근
print("-------- Class Variable --------")
print("car1 car_count : ", car1.car_count)
print("car2 car_count : ", car2.car_count)
print("Car Class car_count : ", Car.car_count)
print()

# 공유 확인
print("-------- Verify Class Variable Sharing --------")
print(Car.__dict__)
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print()

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
print("delete car2")
del car2
print()

# del Method 호출 후 변화
print("-------- after del Method call --------")
print("car1 car_count : ", car1.car_count)
print("Car class car_count : ", Car.car_count)
