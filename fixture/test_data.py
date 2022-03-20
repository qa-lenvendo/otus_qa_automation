from faker import Faker
from random import choice, randrange


class TestData:
    __test__ = False

    def __init__(self):
        self.email = self.email_generator
        self.phone = self.phone_generator
        self.firstname = self.firstname_generator
        self.lastname = self.lastname_generator
        self.password = self.password_generator

    @property
    def password_generator(self):
        return Faker('ru_RU').password(special_chars=False)

    @property
    def email_generator(self):
        return Faker('ru_RU').email()

    @property
    def firstname_generator(self):
        return Faker('ru_RU').first_name()

    @property
    def lastname_generator(self):
        return Faker('ru_RU').last_name()

    @property
    def phone_generator(self):
        """
        Генерирует номера телефонов
        """
        mobile_code = [901, 930, 932, 933, 938, 939, 958, 966, 977, 980, 989, 993, 995, 996, 995, 901, 904, 908, 912,
                       923, 924, 930, 931, 932, 933, 934, 936, 938, 939, 958, 966, 967, 968, 969, 977, 980, 981, 982,
                       983, 984, 985, 986, 988, 989, 991, 992, 993, 994, 995, 996, 999, 901, 902, 912, 930, 939, 955,
                       958, 970, 971, 991, 992, 993, 900, 901, 902, 904, 908, 950, 951, 952, 953, 958, 969, 977, 991,
                       992, 993, 994, 995, 996, 999]
        return '+7' + choice([str(x) for x in mobile_code]) + str(randrange(1111111, 9999999))
