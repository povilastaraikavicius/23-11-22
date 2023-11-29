# Create class that woud repesent weather. This class takes several parameters (wind speed (km/hour) and temperature(F))
# This class should be able to return weather conditions:
# 1) Weather temperature in K , C , F
# 2) Wind speed in m/s , km/h , miles/h
# 3) Weather conditions : good (wind speed < 5m/s,  temp > 0C < 25 C) ,nommal (wind speed < 10m/s,
# temp > -15C < 28 C), bad (wind speed > 10m/s,  temp < -15C or > 30 C) , savere (wind speed > 15m/s,  temp < -25C or > 40 C)
# Use inheritance, private/protected methods/attributes if needed.


# class Weather:
#     def __init__(self, wind_speed_kmh: float, temperature_f: float) -> None:
#         self.wind_speed_kmh = wind_speed_kmh
#         self.temperature_f = temperature_f

#     def get_temperature(self, temperature_F: str) -> float:
#         if temperature_F == "C":
#             return (self.temperature_f - 32) * 5 / 9
#         elif temperature_F == "K":
#             return (self.temperature_f - 32) * 5 / 9 + 273.15
#         else:
#             return self.temperature_f

#     def get_wind_speed(self, wind: str) -> float:
#         if wind == "m/s":
#             return self.wind_speed_kmh * 1000 / 3600
#         elif wind == "miles/h":
#             return self.wind_speed_kmh / 1.60934
#         else:
#             return self.wind_speed_kmh

#     def weather_conditions(self):
#         wind_speed = self.get_wind_speed("m/s")
#         temperature = self.get_temperature("C")

#         if wind_speed < 5 and 0 < temperature < 25:
#             return "Good"
#         elif wind_speed < 10 and -15 < temperature < 28:
#             return "Normal"
#         elif wind_speed > 15 and temperature < -25 and temperature > 40:
#             return "Severe"
#         else:
#             return "Bad"


# class Weather2(Weather):
#     def __init__(self, wind_speed_kmh, temperature_f):
#         super().__init__(wind_speed_kmh=wind_speed_kmh, temperature_f=temperature_f)


# weather = Weather2(20, 50)

# print("Temperature:", weather.get_temperature("C"))
# print("Wind speed:", weather.get_wind_speed("m/s"))
# print("Weather conditions:", weather.weather_conditions())


# class Weather:
#     def __init__(self, wind_speed_kmh: float, temperature_f: float) -> None:
#         self.wind_speed_kmh = wind_speed_kmh
#         self.temperature_f = temperature_f

#     def get_temperature_C(self) -> float:
#         return (self.temperature_f - 32) * 5 / 9

#     def get_temperature_K(self) -> float:
#         return (self.temperature_f - 32) * 5 / 9 + 273.15

#     def get_wind_speed_meter(self) -> float:
#         return self.wind_speed_kmh * 1000 / 3600

#     def get_wind_speed_miles(self) -> float:
#         return self.wind_speed_kmh / 1.60934

#     def weather_conditions(self):
#         wind_speed = self.get_wind_speed_meter()
#         temperature = self.get_temperature_C()

#         if wind_speed < 5 and 0 < temperature < 25:
#             return "Good"
#         elif wind_speed < 10 and -15 < temperature < 28:
#             return "Normal"
#         elif wind_speed > 15 and temperature < -25 and temperature > 40:
#             return "Severe"
#         else:
#             return "Bad"


# class Weather2(Weather):
#     def __init__(self, wind_speed_kmh, temperature_f):
#         super().__init__(wind_speed_kmh=wind_speed_kmh, temperature_f=temperature_f)


# weather = Weather2(20, 50)

# print("Temperature:", weather.get_temperature_C())
# print("Wind speed:", weather.get_wind_speed_meter())
# print("Weather conditions:", weather.weather_conditions())


# task Nr2

# Basic Banking System Challenge

#  Define a class called Account with the following attributes and methods:
#  - Attributes: account_number, account_holder, balance
#  - Methods: display_account_info() - prints information about the account

#  Create two subclasses, SavingsAccount and CheckingAccount, that inherit from Account.
#  Each subclass should have its own unique method, for example, earn_interest() for SavingsAccount
#  and deduct_fees() for CheckingAccount.


# class Account:
#     def __init__(
#         self, account_number: float, account_holder: str, balance: float
#     ) -> None:
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def display_account_info(self):
#         return f"{self.account_holder} account number is {self.account_number} and balance is {self.balance}"


# class SavingsAccount(Account):
#     def __init__(
#         self, account_number: float, account_holder: str, balance: float
#     ) -> None:
#         super().__init__(
#             account_number=account_number,
#             account_holder=account_holder,
#             balance=balance,
#         )

#     def earn_interest(self, interest_rate: float) -> None:
#         interest = self.balance * (interest_rate / 100)
#         self.balance += interest


# user_info = SavingsAccount(
#     account_number=25684, account_holder="Povilas", balance=20000
# )
# user_info.earn_interest(20)
# print(user_info.display_account_info())


class Account:
    def __init__(
        self, account_number: int, account_holder: str, balance: float
    ) -> None:
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def display_account_info(self) -> str:
        return f"Account number: {self.account_number}\nAccount holder: {self.account_holder}\nBalance: {self.balance}"


class SavingsAccount(Account):
    def __init__(
        self, account_number: int, account_holder: str, balance: float, interest: float
    ) -> None:
        super().__init__(account_number, account_holder, balance)
        self.interest = interest

    def earn_interest(self, interest_rate: float) -> None:
        interest_earned = self.balance * (interest_rate / 100)
        self.balance += interest_earned


class CheckingAccount(Account):
    def __init__(
        self,
        account_number: int,
        account_holder: str,
        balance: float,
        deduct_fee: float,
    ) -> None:
        super().__init__(account_number, account_holder, balance)
        self.deduct_fee = deduct_fee

    def deduct_fees(self) -> None:
        self.balance -= self.deduct_fee


account_jonas = SavingsAccount(
    account_number=1241, account_holder="Jonas Jonaitis", balance=50, interest=50
)
account_jonas.earn_interest(interest_rate=10)
print(account_jonas.display_account_info())

account_matas = CheckingAccount(
    account_number=1941, account_holder="Matas Mataitis", balance=70, deduct_fee=35
)
account_matas.deduct_fees()
print(account_matas.display_account_info())
