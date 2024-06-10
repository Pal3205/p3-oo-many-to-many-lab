class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.__class__.members.append(self)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self.__title = value


class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.__class__.members.append(self)
        self.__contracts = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self.__name = value

    def contracts(self):
        return self.__contracts

    def books(self):
        return [contract.book for contract in self.__contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.__contracts.append(contract)
        return contract

    def total_royalties(self):
        total = sum(contract.royalties for contract in self.__contracts)
        return total


class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.members.append(self)


    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.members if contract.date == date]

