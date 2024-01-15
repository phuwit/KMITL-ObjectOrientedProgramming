from __future__ import annotations
from typing import List, Dict
from enum import Enum
from datetime import datetime


class AccountType(Enum):
    Undefined = -1
    Savings = 0
    Current = 1


class CardType(Enum):
    Undefined = -1
    ATM = 0
    Debit = 1
    
    
class TransactionType(Enum):
    Deposit = 0
    Withdrawal = 1
    Transfer = 2


class Bank:
    def __init__(self) -> None:
        self.__customers: List[Customer] = []
        self.__atms: List[Atm] = []
    
    def add_customer(self, customer: Customer) -> bool:
        if (isinstance(customer, Customer)):
            self.__customers.append(customer)
            return True
        return False

    def add_atm(self, atm: Atm) -> bool:
        if (isinstance(atm, Atm)):
            self.__atms.append(atm)
            return True
        return False
    
    def get_customers(self) -> List[Customer]:
        return self.__customers
    
    def get_atms(self) -> List[Atm]:
        return self.__atms


class Customer:
    def __init__(self, id: str, name: str) -> None:
        self.__id: str = id
        self.__name: str = name
        self.__accounts: List[Account] = []
    
    def add_account(self, account: Account) -> bool:
        if (isinstance(account, Account)):
            self.__accounts.append(account)
            return True
        return False
    
    def get_accounts(self) -> List[Account]:
        return self.__accounts


class Account:
    def __init__(self, customer: Customer, id: str) -> None:
        self.__customer: Customer = customer
        self.__id: str = id
        self.__balance: int = 0
        self.__cards: List[Card] = []
        self.__transactions: List[Transaction] = []
    
    def add_card(self, card: Card) -> bool:
        if (isinstance(card, Card)):
            self.__cards.append(card)
            return True
        return False
    
    def get_id(self) -> str:
        return self.__id
    
    def get_balance(self) -> int:
        return self.__balance
    
    def get_cards(self) -> List[Card]:
        return self.__cards
    
    def get_transactions(self) -> List[Transaction]:
        return self.__transactions
    
    def transact(self, transaction: Transaction) -> bool:
        if (isinstance(transaction, Transaction)):
            self.__transactions.append(transaction)
            transaction_type = transaction.get_type()
            if (transaction_type == TransactionType.Deposit):
                self.__balance += transaction.get_amount()
            elif (transaction_type == TransactionType.Withdrawal):
                self.__balance -= transaction.get_amount()
            elif (isinstance(transaction, TransactionTransfer)):
                if (transaction.get_destination() == self):
                    transaction.set_incoming(True)
                    self.__balance += transaction.get_amount()
                else:
                    transaction.set_incoming(False)
                    self.__balance -= transaction.get_amount()
            transaction.record_balance(self.__balance)
            return True
        return False

class Card:
    type: CardType = CardType.Undefined
    card_per_account_limit: int = -1
    daily_transaction_limit: int = -1
    yearly_fee: int = -1
    
    def __init__(self, account: Account, id: int) -> None:
        self.__account: Account = account
        self.__id: int = id
        
    def get_id(self) -> int:
        return self.__id
        

class CardAtm(Card):
    type = CardType.ATM
    card_per_account_limit = 1
    daily_transaction_limit = 40000
    yearly_fee = 150
    
    
class Atm:
    def __init__(self, id: str, balance: int) -> None:
        self.__id: str = id
        self.__balance: int = balance
        self.__account: Account | None = None
        
    def get_id(self):
        return self.__id
        
    # TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
    # TODO     2) atm_card เป็นหมายเลขของ atm_card
    # TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
    # TODO     ควรเป็น method ของเครื่อง ATM

    # @staticmethod
    def authenticate(self, _bank: Bank, card_id: str):
        for customer in _bank.get_customers():
            for account in customer.get_accounts():
                for card in account.get_cards():
                    if (card.get_id() == card_id):
                        self.__account = account
                        return account
        return None

    # TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account 3) จำนวนเงิน
    # TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0

    # @staticmethod
    def deposit(self, account: Account, amount: int) -> bool:
        if (isinstance(account, Account)) and \
            (isinstance(amount, int)) and (amount > 0):
                self.__balance += amount
                account.transact(Transaction(TransactionType.Deposit, amount, datetime.now(), self))
                return True
        return False

    # TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account 3) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

    # @staticmethod
    def withdraw(self, account: Account, amount: int) -> bool:
        if (isinstance(account, Account)) and (isinstance(amount, int)) and (amount > 0) and (amount <= account.get_balance()):
                self.__balance -= amount
                account.transact(Transaction(TransactionType.Withdrawal, amount, datetime.now(), self))
                return True
        return False

    # TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
        
    # @staticmethod
    def transfer(self, origin: Account, destination: Account, amount: int) -> bool:
        if (isinstance(origin, Account)) and (isinstance(destination, Account)) and \
            (isinstance(amount, int)) and (amount > 0) and (amount <= origin.get_balance()):
                transaction = TransactionTransfer(TransactionType.Transfer, amount, datetime.now(), self, origin, destination)
                origin.transact(transaction)
                destination.transact(transaction)
                return True
        return False


class Transaction:
    def __init__(self, type: TransactionType, amount: int, timestamp: datetime, machine: Atm) -> None:
        self.__type: TransactionType = type
        self.__amount: int = amount
        self.__timestamp: datetime = timestamp
        self.__machine: Atm = machine
        self.__balance = -1
    
    def record_balance(self, balance: int) -> bool:
        if (isinstance(balance, int)) and (balance >= 0):
            self.__balance = balance
            return True
        return False
        
    def __str__(self) -> str:
        # return f'D-ATM:1002-1000-2000'
        if (isinstance(self, TransactionTransfer)):
            if (self.is_incoming()):
                sign = '+'
            else:
                sign = '-'
            return f'{self.__type.name[0]}-ATM:{self.__machine.get_id()}-{sign}{self.__amount}-{self.__balance}'
        else:    
            return f'{self.__type.name[0]}-ATM:{self.__machine.get_id()}-{self.__amount}-{self.__balance}'
    
    def get_type(self) -> TransactionType:
        return self.__type
    
    def get_amount(self) -> int:
        return self.__amount
        
        
class TransactionTransfer(Transaction):
    def __init__(self, type: TransactionType, amount: int, timestamp: datetime, machine: Atm, origin: Account, destination: Account) -> None:
        super().__init__(type, amount, timestamp, machine)
        self.__origin: Account = origin
        self.__destination: Account = destination
        self.__incoming: bool = False
        
    def set_incoming(self, incoming: bool):
        if (isinstance(incoming, bool)):
            self.__incoming = incoming
            return True
        return False

    def is_incoming(self):
        return self.__incoming
    
    def get_destination(self) -> Account:
        return self.__destination


# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user = {'1-1101-12345-12-0' : ['Harry Potter', '1234567890', 20000, '12345'],
        '1-1101-12345-13-0' : ['Hermione Jean Granger', '0987654321', 1000, '12346']}

atm = {'1001':1000000,'1002':200000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

def initialize_bank(userdata: Dict, atmdata: Dict[str, int]):
    _bank = Bank()
    
    for key, value in atmdata.items():
        atm = Atm(key, value)
        _bank.add_atm(atm)
        
    for key, value in userdata.items():
        customer = Customer(key, value[0])
        account = Account(customer, value[1])
        card_atm = CardAtm(account, value[3])
        
        account.transact(Transaction(TransactionType.Deposit, int(value[2]), datetime.now(), _bank.get_atms()[0]))
        account.add_card(card_atm)
        customer.add_account(account)
        _bank.add_customer(customer)
    
    return _bank

bank = initialize_bank(user, atm)

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM

bank.get_atms()[0].authenticate(bank, atm['1001'])

# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0

bank.get_atms()[0].authenticate(bank, atm['1001'])

#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี



#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี



harry_account0 = bank.get_customers()[0].get_accounts()[0]
hermione_account0 = bank.get_customers()[1].get_accounts()[0]

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

print('Test #1')
print('Expected :\n12345, 1234567890, Success')
print('Actual :')
test1_account = bank.get_atms()[0].authenticate(bank, '12345')
if test1_account is not None:
    print(test1_account.get_cards()[0].get_id(), test1_account.get_id(), 'Success' ,sep=', ')
else:
    print('Error')


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000

print('\n\nTest #2')
print('Expected :\n1000\n2000')
print('Actual :')
print(hermione_account0.get_balance())
print(bank.get_atms()[1].deposit(hermione_account0, 1000))
print(hermione_account0.get_balance())


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error

print('\n\nTest #3')
print('Expected :\nFalse')
print('Actual :')
# print(hermione_account0.get_balance())
print(bank.get_atms()[1].deposit(hermione_account0, -1))
# print(hermione_account0.get_balance())

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500

print('\n\nTest #4')
print('Expected :\n2000\n1500')
print('Actual :')
print(hermione_account0.get_balance())
print(bank.get_atms()[1].withdraw(hermione_account0, 500))
print(hermione_account0.get_balance())

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

print('\n\nTest #5')
print('Expected :\nFalse')
print('Actual :')
# print(hermione_account0.get_balance())
print(bank.get_atms()[1].withdraw(hermione_account0, 2000))
# print(hermione_account0.get_balance())

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500

print('\n\nTest #6')
print('Expected :\n20000\n1500\n10000\n11500')
print('Actual :')
print(harry_account0.get_balance())
print(hermione_account0.get_balance())
print(bank.get_atms()[1].transfer(harry_account0, hermione_account0, 10000))
print(harry_account0.get_balance())
print(hermione_account0.get_balance())

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500

print('\n\nTest #7')
print('Expected :\nD-ATM:1002-1000-2000\nW-ATM:1002-500-1500\nT-ATM:1002-+10000-11500')
print('Actual :')
for transaction in hermione_account0.get_transactions():
    print(transaction)
