from __future__ import annotations
from typing import List, Dict
from enum import Enum
from abc import ABC, abstractproperty, abstractmethod


class TransactionType(Enum):
    Deposit = 0
    Withdrawal = 1
    Transfer = 2


class Bank:
    def __init__(self, name: str):
        self.__name: str = name
        self.__customers: List[Customer] = []
        self.__atms: List[Atm] = []
    
    def add_customer(self, customer: Customer) -> bool:
        if (isinstance(customer, Customer)):
            self.__customers.append(customer)
            return True
        return False

    def add_atms(self, terminal: Atm) -> bool:
        if (isinstance(terminal, Atm)):
            self.__atms.append(terminal)
            return True
        return False
    
    def get_customers(self) -> List[Customer]:
        return self.__customers
    
    def get_atms(self) -> List[Atm]:
        return self.__atms
    
    def get_customer_by_citizen_id(self, citizen_id: str) -> Customer | None:
        for customer in self.__customers:
            if (customer.get_citizen_id() == citizen_id):
                return customer
        return None
    
    def get_customer_by_name(self, name: str) -> Customer | None:
        for customer in self.__customers:
            if (customer.get_name() == name):
                return customer
        return None
    
    def get_atm_by_id(self, id: str) -> Atm | None:
        for terminal in self.__atms:
            if (terminal.get_id() == id):
                return terminal
        return None
    
    def get_account_from_card_id(self, id: str) -> Account | None:
        for customer in self.__customers:
            for account in customer.get_accounts():
                if isinstance(account, AccountSavings):
                    card = account.get_card()
                    if isinstance(card, Card) and (card.get_id() == id):
                        return account
        return None
    
    def get_account_from_account_id(self, id: str) -> Account | None:
        for customer in self.__customers:
            for account in customer.get_accounts():
                if(account.get_id() == id):
                    return account
        return None
    

class Customer:
    def __init__(self, citizen_id: str, name: str) -> None:
        self.__citizen_id: str = citizen_id
        self.__name: str = name
        self.__accounts: List[Account] = []
    
    def add_account(self, account: Account) -> bool:
        if (isinstance(account, Account)):
            self.__accounts.append(account)
            return True
        return False
    
    def get_accounts(self) -> List[Account]:
        return self.__accounts

    def get_citizen_id(self) -> str:
        return self.__citizen_id
    
    def get_name(self) -> str:
        return self.__name


class Merchant(Customer):
    def __init__(self, citizen_id: str, name: str) -> None:
        super().__init__(citizen_id, name)
        self.__edcs: List[Edc] = []

    def add_edc(self, edc: Edc):
        if isinstance(edc, Edc):
            self.__edcs.append(edc)
    
    def get_edc_by_id(self, id: str) -> Edc | None:
        for edc in self.__edcs:
            if (edc.get_id() == id):
                return edc
        return None

    def get_edcs(self) -> List[Edc]:
        return self.__edcs
    
    def deduct(self, origin: Account, amount: int, destination: Account):
        if (isinstance(origin, Account)) and (isinstance(destination, Account)) and \
            (isinstance(amount, int)) and (amount > 0) and (amount <= origin.get_balance()):
                transaction = Transaction(TransactionType.Transfer, amount, destination)
                origin.make_transaction(transaction)
                # destination.make_transaction(transaction)
                return True

class Account(ABC):
    @property
    @abstractmethod
    def interest_rate(self) -> float:
        pass
    
    def __init__(self, customer: Customer, id: str) -> None:
        self.__customer: Customer = customer
        self.__id: str = id
        self.__balance: int = 0
        
        self.__transactions: List[Transaction] = []
        
    def __iter__(self):
        for transaction in self.__transactions:
            yield transaction
        
    def __add__(self, amount: int) -> bool:
        if (isinstance(amount, int)):
            self.make_transaction(Transaction(TransactionType.Deposit, amount, self))
            return True
        return False
    
    def __sub__(self, amount: int) -> bool:
        if (isinstance(amount, int)):
            self.make_transaction(Transaction(TransactionType.Withdrawal, amount, self))
            return True
        return False
        
    
    def __rshift__(self, tuple: tuple[int, Account]) -> bool:
        if (isinstance(tuple[0], int)) and (isinstance(tuple[1], Account)):
            self.make_transaction(Transaction(TransactionType.Transfer, tuple[0], tuple[1]))
            # tuple[1].make_transaction(Transaction(TransactionType.Transfer, tuple[0], tuple[1]))
            return True
        return False
    
    def get_id(self) -> str:
        return self.__id
    
    def get_balance(self) -> int:
        return self.__balance
    
    def get_transactions(self) -> List[Transaction]:
        return self.__transactions
    
    def make_transaction(self, transaction: Transaction) -> bool:
        if (isinstance(transaction, Transaction)):
            transaction_type = transaction.get_type()
            if (transaction_type == TransactionType.Deposit):
                self.__balance += transaction.get_amount()
            elif (transaction_type == TransactionType.Withdrawal):
                self.__balance -= transaction.get_amount()
            elif (transaction_type == TransactionType.Transfer):
                if (transaction.get_destination() == self):
                    transaction.set_incoming_transfer(True)
                    self.__balance += transaction.get_amount()
                else:
                    transaction.get_destination().make_transaction(Transaction(TransactionType.Transfer, transaction.get_amount(), transaction.get_destination()))
                    transaction.set_incoming_transfer(False)
                    self.__balance -= transaction.get_amount()
            self.__transactions.append(transaction)
            transaction.record_balance(self.__balance)
            return True
        return False


class AccountSavings(Account):
    def interest_rate(self):
        return 0.5
    
    def __init__(self, customer: Customer, id: str) -> None:
        super().__init__(customer, id)
        self.__card: Card | None = None
    
    def set_card(self, card: Card) -> bool:
        if (isinstance(card, Card)):
            self.__card = card
            return True
        return False
    
    def get_card(self) -> Card | None:
        return self.__card


class AccountFixedDeposit(Account):
    def interest_rate(self):
        return 2.5
    
    def __init__(self, customer: Customer, id: str) -> None:
        super().__init__(customer, id)


class Card(ABC):
    daily_transaction_limit: int = -1
    yearly_fee: int = -1
    
    def __init__(self, account: Account, id: str, pin: str) -> None:
        self.__account: Account = account
        self.__id: str = id
        self.__pin: str = pin
        self.__transaction_quota = self.daily_transaction_limit  # Fix: Remove parentheses
        
    def validate_pin(self, pin: str) -> bool:
        if (self.__pin == pin):
            return True
        return False
        
    def get_id(self) -> str:
        return self.__id
    
    def get_account(self) -> Account:
        return self.__account
    
    def adjust_quota(self, amount: int) -> bool:
        new_quota = self.__transaction_quota + amount
        if (new_quota >= 0):
            self.__transaction_quota = new_quota
            return True
        return False
    
    def reset_quota(self):
        self.__transaction_quota = self.daily_transaction_limit
        

class CardAtm(Card):
    daily_transaction_limit = 40000
    yearly_fee = 150


class CardDebit(CardAtm):
    daily_transaction_limit = 40000
    yearly_fee = 300


class Atm:
    session_limit_withdrawal = 20000
    session_limit_transfer = 100000
    
    def __init__(self, _bank: Bank, id: str, balance: int) -> None:
        self.__bank: Bank = _bank
        self.__id: str = id
        self._balance: int = balance
        
    def get_id(self):
        return self.__id
    
    # @staticmethod
    def authenticate(self, card: Card, pin: str):
        if card.validate_pin(pin):
            return card.get_account()
        return None

    # @staticmethod
    def deposit(self, account: Account, amount: int) -> bool:
        if (isinstance(account, AccountSavings)):
            card = account.get_card()
            if (isinstance(amount, int)) and (amount > 0) and \
                (isinstance(card, Card)) and (card.adjust_quota(amount)):
                    self._balance += amount
                    account.make_transaction(Transaction(TransactionType.Deposit, amount, account))
                    return True
        return False

    # @staticmethod
    def withdraw(self, account: Account, amount: int) -> bool:
        if (isinstance(account, AccountSavings)):
            card = account.get_card()
            if (isinstance(account, Account)) and (isinstance(amount, int)) and (amount > 0) and \
                (amount <= account.get_balance()) and (isinstance(card, Card)) and (card.adjust_quota(-amount)):
                    self._balance += amount
                    account.make_transaction(Transaction(TransactionType.Withdrawal, amount, account))
                    return True
        return False
        
    # @staticmethod
    def transfer(self, origin: Account, destination: Account, amount: int) -> bool:
        if (isinstance(origin, AccountSavings)):
            card = origin.get_card()
            if (isinstance(origin, Account)) and (isinstance(destination, Account)) and \
                (isinstance(amount, int)) and (amount > 0) and (amount <= origin.get_balance()) and \
                (isinstance(card, Card)) and (card.adjust_quota(-amount)):
                    transaction = Transaction(TransactionType.Transfer, amount, destination)
                    origin.make_transaction(transaction)
                    return True
        return False


class Edc:
    def __init__(self, _bank: Bank, id: str, balance: int) -> None:
        self.__bank: Bank = _bank
        self.__id: str = id
        self._balance: int = balance
        
    def get_id(self):
        return self.__id
        
    def deduct(self, card: CardDebit, amount: int, destination: Account):
        origin = card.get_account()
        if (isinstance(origin, Account)) and (isinstance(destination, Account)) and \
            (isinstance(amount, int)) and (amount > 0) and (amount <= origin.get_balance()) and \
            (isinstance(card, Card)) and (card.adjust_quota(-amount)):
                transaction = Transaction(TransactionType.Transfer, amount, destination)
                origin.make_transaction(transaction)
                return True


class Transaction:
    def __init__(self, type: TransactionType, amount: int, destination: Account) -> None:
        self.__type: TransactionType = type
        self.__amount: int = amount
        self.__destination: Account = destination
        self.__balance = -1
        self.__incoming_transfer: bool | None
        
    def __str__(self) -> str:
        # return f'D-ATM:1002-1000-2000'
        sign = ''
        if (self.__type == TransactionType.Deposit):
            sign = '+'
        elif (self.__type == TransactionType.Withdrawal):
            sign = '-'
        elif (self.__type == TransactionType.Transfer):
            if (self.__incoming_transfer):
                sign = '+'
            else:
                sign = '-'
                
        return f'{self.__type.name[0]} {sign}{self.__amount} => {self.__balance}'
    
    def record_balance(self, balance: int) -> bool:
        if (isinstance(balance, int)) and (balance >= 0):
            self.__balance = balance
            return True
        return False
    
    def set_incoming_transfer(self, incoming: bool) -> bool:
        if(isinstance(incoming, bool)):
            self.__incoming_transfer = incoming
            return True
        return False
    
    def is_incoming_transfer(self) -> bool | None:
        return self.__incoming_transfer
    
    def get_type(self) -> TransactionType:
        return self.__type
    
    def get_amount(self) -> int:
        return self.__amount
    
    def get_destination(self) -> Account:
        return self.__destination


##################################################################################

# กำหนด รูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, ประเภทบัญชี, หมายเลขบัญชี, จำนวนเงินในบัญชี, ประเภทบัตร, หมายเลขบัตร ]}
users_import_dict = {
    '1-1101-12345-12-0': ['Harry Potter', 'Savings', '1234567890', 20000, 'ATM', '12345'], 
    '1-1101-12345-13-0': ['Hermione Jean Granger', 'Saving', '0987654321', 1000, 'Debit', '12346'], 
    '1-1101-12345-13-0': ['Hermione Jean Granger', 'Fix Deposit', '0987654322', 1000, '', ''], 
    '9-0000-00000-01-0': ['KFC', 'Savings', '0000000321', 0, '', ''], 
    '9-0000-00000-02-0': ['Tops', 'Savings', '0000000322', 0, '', '']
    }

atm_import_dict = {'1001': 1000000, '1002': 200000}

seller_import_dict = {'210': "KFC",  '220': "Tops"}

terminal_edc_import_dict = {'2101': "KFC",  '2201': "Tops"}

scb = Bank('SCB')

# TODO 7.1 : สร้าง Instance ของธนาคาร และ สร้าง Instance ของ User, Account, บัตร
# TODO     : จากข้อมูลใน user รูปแบบการนำข้อมูลไปใช้สามารถใช้ได้โดยอิสระ
# TODO     : โดย Account แบ่งเป็น 2 subclass คือ Savings และ FixedDeposit
# TODO     : โดย บัตร แบ่งเป็น 2 subclass คือ ATM และ Debit

scb.add_customer(Customer('1-1101-12345-12-0', 'Harry Potter'))
scb.add_customer(Customer('1-1101-12345-13-0', 'Hermione Jean Granger'))
# scb.add_customer(Customer('9-0000-00000-01-0', 'KFC'))
# scb.add_customer(Customer('9-0000-00000-02-0', 'Tops'))
scb.add_customer(Merchant('9-0000-00000-01-0', 'KFC'))
scb.add_customer(Merchant('9-0000-00000-02-0', 'Tops'))

harry = scb.get_customer_by_citizen_id('1-1101-12345-12-0')
if isinstance(harry, Customer):
    harry_account = AccountSavings(harry, '1234567890')
    if isinstance(harry_account, AccountSavings):
        harry.add_account(harry_account)
        harry_account.make_transaction(Transaction(TransactionType.Deposit, 20000, harry_account))
        harry_account.set_card(CardAtm(harry_account, '12345', '1234'))

hermione = scb.get_customer_by_citizen_id('1-1101-12345-13-0')
if isinstance(hermione, Customer):
    hermione_account1 = AccountSavings(hermione, '0987654321')
    if isinstance(hermione_account1, AccountSavings):
        hermione.add_account(hermione_account1)
        hermione_account1.make_transaction(Transaction(TransactionType.Deposit, 2000, hermione_account1))
        hermione_account1.set_card(CardDebit(hermione_account1, '12346', '1234'))
        hermione_account2 = AccountFixedDeposit(hermione, '0987654322')
        hermione.add_account(hermione_account2)
        hermione_account2.make_transaction(Transaction(TransactionType.Deposit, 1000, hermione_account1))
        

kfc = scb.get_customer_by_citizen_id('9-0000-00000-01-0')
if isinstance(kfc, Customer):
    kfc.add_account(AccountSavings(kfc, '0000000321'))
    
tops = scb.get_customer_by_citizen_id('9-0000-00000-02-0')
if isinstance(tops, Customer):
    tops.add_account(AccountSavings(tops, '0000000322'))

# TODO 7.2 : สร้าง Instance ของเครื่อง ATM

scb.add_atms(Atm(scb, '1001', 1000000))
scb.add_atms(Atm(scb, '1002', 200000))

# TODO 7.3 : สร้าง Instance ของ Seller และใส่เครื่อง EDC ใน Seller 

kfc = scb.get_customer_by_citizen_id('9-0000-00000-01-0')
if isinstance(kfc, Merchant):
    kfc.add_edc(Edc(scb, '2101', 0))

tops = scb.get_customer_by_citizen_id('9-0000-00000-02-0')
if isinstance(tops, Merchant):
    tops.add_edc(Edc(scb, '2201', 0))

# TODO 7.4 : สร้าง method ฝาก โดยใช้ __add__ ถอน โดยใช้ __sub__ และ โอนโดยใช้ __rshift__
# TODO     : ทดสอบการ ฝาก ถอน โอน โดยใช้ + - >> กับบัญชีแต่ละประเภท

# TODO 7.5 : สร้าง method insert_card, deposit, withdraw และ transfer ที่ตู้ atm และเรียกผ่าน account อีกที
# TODO     : ทดสอบโอนเงินระหว่างบัญชีแต่ละประเภท

# TODO 7.6 : สร้าง method paid ที่เครื่อง EDC และเรียกผ่าน account อีกที

# TODO 7.7 : สร้าง method __iter__ ใน account สำหรับส่งคืน transaction เพื่อให้ใช้กับ for ได้ 

# Test case #1 : ทดสอบ การฝาก จากเครื่อง ATM โดยใช้บัตร ATM ของ harry
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method deposit จากเครื่อง ATM และเรียกใช้ + จาก account
# ผลที่คาดหวัง :
# Test Case #1
# Harry's ATM No :  12345
# Harry's Account No :  1234567890
# Success
# Harry account before deposit :  20000
# Deposit 1000
# Harry account after deposit :  21000

atm_machine = scb.get_atm_by_id('1001')
harry_account = scb.get_account_from_card_id('12345')
if isinstance(harry_account, AccountSavings) and isinstance(atm_machine, Atm):
    atm_card = harry_account.get_card()
    if (atm_card):
        print("Test Case #1")
        print("Harry's ATM No : ", atm_card.get_id())
        print("Harry's Account No : ", harry_account.get_id())
        print(atm_machine.authenticate(atm_card,  "1234"))
        print("Harry account before deposit : ", harry_account.get_balance())
        print("Deposit 1000")
        atm_machine.deposit(harry_account, 1000)
        print("Harry account after deposit : ", harry_account.get_balance())
        print("")

# Test case #2 : ทดสอบ การถอน จากเครื่อง ATM โดยใช้บัตร ATM ของ hermione
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 2 และบัตร atm ของ hermione
# และเรียกใช้ function หรือ method withdraw จากเครื่อง ATM และเรียกใช้ - จาก account
# ผลที่คาดหวัง :
# Test Case #2
# Hermione's ATM No :  12346
# Hermione's Account No :  0987654321
# Success
# Hermione account before withdraw :  2000
# withdraw 1000
# Hermione account after withdraw :  1000

atm_machine = scb.get_atm_by_id('1002')
hermione_account1 = scb.get_account_from_card_id('12346')
if isinstance(hermione_account1, AccountSavings) and isinstance(atm_machine, Atm):
    atm_card = hermione_account1.get_card()
    if (atm_card):
        print("Test Case #2")
        print("Hermione's ATM No : ", atm_card.get_id())
        print("Hermione's Account No : ", hermione_account1.get_id())
        print(atm_machine.authenticate(atm_card, "1234"))
        print("Hermione account before withdraw : ",hermione_account1.get_balance())
        print("withdraw 1000")
        atm_machine.withdraw(hermione_account1, 1000)
        print("Hermione account after withdraw : ",hermione_account1.get_balance())
        print("")


# Test case #3 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ที่เคาน์เตอร์
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง
# Test Case #3
# Harry's Account No :  1234567890
# Hermione's Account No :  0987654321
# Harry account before transfer :  21000
# Hermione account before transfer :  1000
# Harry account after transfer :  11000
# Hermione account after transfer :  11000

harry_account = scb.get_account_from_card_id('12345')
hermione_account1 = scb.get_account_from_card_id('12346')
if isinstance(hermione_account1, AccountSavings) and (harry_account):
    print("Test Case #3")
    print("Harry's Account No : ",harry_account.get_id())
    print("Hermione's Account No : ", hermione_account1.get_id())
    print("Harry account before transfer : ",harry_account.get_balance())
    print("Hermione account before transfer : ",hermione_account1.get_balance())
    # harry_account.transfer("0000", 10000, hermione_account1)
    harry_account.make_transaction(Transaction(TransactionType.Transfer, 10000, hermione_account1))
    print("Harry account after transfer : ",harry_account.get_balance())
    print("Hermione account after transfer : ",hermione_account1.get_balance())
    print("")

# Test case #4 : ทดสอบการชำระเงินจากเครื่องรูดบัตร ให้เรียกใช้ method paid จากเครื่องรูดบัตร
# โดยให้ hermione ชำระเงินไปยัง KFC จำนวน 500 บาท ผ่านบัตรของตัวเอง
# ผลที่คาดหวัง
# Hermione's Debit Card No :  12346
# Hermione's Account No :  0987654321
# Seller :  KFC
# KFC's Account No :  0000000321
# KFC account before paid :  0
# Hermione account before paid :  11000
# KFC account after paid :  500
# Hermione account after paid :  10500

hermione_account1 = scb.get_account_from_account_id('0987654321')
if isinstance(hermione_account1, AccountSavings):
    debit_card = hermione_account1.get_card()
    kfc_account = scb.get_account_from_account_id('0000000321')
    kfc = scb.get_customer_by_name('KFC')
    if isinstance(kfc, Merchant) and isinstance(debit_card, CardDebit) and (kfc_account):
        edc = kfc.get_edc_by_id('2101')
        print("Test Case #4")
        print("Hermione's Debit Card No : ", debit_card.get_id())
        print("Hermione's Account No : ",hermione_account1.get_id())
        print("Seller : ", kfc.get_name())
        print("KFC's Account No : ", kfc_account.get_id())
        print("KFC account before paid : ",kfc_account.get_balance())
        print("Hermione account before paid : ",hermione_account1.get_balance())
        if (edc):
            edc.deduct(debit_card, 500, kfc_account)
        print("KFC account after paid : ",kfc_account.get_balance())
        print("Hermione account after paid : ",hermione_account1.get_balance())
        print("")

# Test case #5 : ทดสอบการชำระเงินแบบอิเล็กทรอนิกส์ ให้เรียกใช้ method paid จาก kfc
# โดยให้ Hermione ชำระเงินไปยัง Tops จำนวน 500 บาท
# ผลที่คาดหวัง
# Test Case #5
# Hermione's Account No :  0987654321
# Tops's Account No :  0000000322
# Tops account before paid :  0
# Hermione account before paid :  10500
# Tops account after paid :  500
# Hermione account after paid :  10000

hermione_account1 = scb.get_account_from_account_id('0987654321')
if isinstance(hermione_account1, AccountSavings):
    debit_card = hermione_account1.get_card()
    tops_account = scb.get_account_from_account_id('0000000322')
    tops = scb.get_customer_by_name('Tops')
    if (hermione_account1) and (tops_account) and isinstance(tops, Merchant):
        print("Test Case #5")
        print("Hermione's Account No : ",hermione_account1.get_id())
        print("Tops's Account No : ", tops_account.get_id())
        print("Tops account before paid : ",tops_account.get_balance())
        print("Hermione account before paid : ",hermione_account1.get_balance())
        tops.deduct(hermione_account1,500,tops_account)
        print("Tops account after paid : ",tops_account.get_balance())
        print("Hermione account after paid : ",hermione_account1.get_balance())
        print("")


# Test case #6 : แสดง transaction ของ Hermione ทั้งหมด โดยใช้ for loop 

print("Test Case #6")
hermione = scb.get_customer_by_citizen_id('1-1101-12345-13-0')
# print(hermione)
if (hermione):
    # print(hermione.get_accounts())
    for account in hermione.get_accounts():
        print(f'Account ID: {account.get_id()}')
        for transaction in account:
            print(transaction)
        print('')


# # overload test


# # Test case #1 : ทดสอบ การฝาก จากเครื่อง ATM โดยใช้บัตร ATM ของ harry
# # ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# # และเรียกใช้ function หรือ method deposit จากเครื่อง ATM และเรียกใช้ + จาก account
# # ผลที่คาดหวัง :
# # Test Case #1
# # Harry's ATM No :  12345
# # Harry's Account No :  1234567890
# # Success
# # Harry account before deposit :  20000
# # Deposit 1000
# # Harry account after deposit :  21000

# atm_machine = scb.get_atm_by_id('1001')
# harry_account = scb.get_account_from_card_id('12345')
# if isinstance(harry_account, AccountSavings) and isinstance(atm_machine, TerminalAtm):
#     atm_card = harry_account.get_card()
#     if (atm_card):
#         print("Test Case #1")
#         print("Harry's ATM No : ", atm_card.get_id())
#         print("Harry's Account No : ", harry_account.get_id())
#         print(atm_machine.authenticate(atm_card,  "1234"))
#         print("Harry account before deposit : ", harry_account.get_balance())
#         print("Deposit 1000")
#         print(harry_account + 1000)
#         print("Harry account after deposit : ", harry_account.get_balance())
#         print("")

# # Test case #2 : ทดสอบ การถอน จากเครื่อง ATM โดยใช้บัตร ATM ของ hermione
# # ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 2 และบัตร atm ของ hermione
# # และเรียกใช้ function หรือ method withdraw จากเครื่อง ATM และเรียกใช้ - จาก account
# # ผลที่คาดหวัง :
# # Test Case #2
# # Hermione's ATM No :  12346
# # Hermione's Account No :  0987654321
# # Success
# # Hermione account before withdraw :  2000
# # withdraw 1000
# # Hermione account after withdraw :  1000

# atm_machine = scb.get_atm_by_id('1002')
# hermione_account1 = scb.get_account_from_card_id('12346')
# if isinstance(hermione_account1, AccountSavings) and isinstance(atm_machine, TerminalAtm):
#     atm_card = hermione_account1.get_card()
#     if (atm_card):
#         print("Test Case #2")
#         print("Hermione's ATM No : ", atm_card.get_id())
#         print("Hermione's Account No : ", hermione_account1.get_id())
#         print(atm_machine.authenticate(atm_card, "1234"))
#         print("Hermione account before withdraw : ",hermione_account1.get_balance())
#         print("withdraw 1000")
#         print(hermione_account1 - 1000)
#         print("Hermione account after withdraw : ",hermione_account1.get_balance())
#         print("")


# # Test case #3 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ที่เคาน์เตอร์
# # ให้เรียกใช้ method ที่ทำการโอนเงิน
# # ผลที่คาดหวัง
# # Test Case #3
# # Harry's Account No :  1234567890
# # Hermione's Account No :  0987654321
# # Harry account before transfer :  21000
# # Hermione account before transfer :  1000
# # Harry account after transfer :  11000
# # Hermione account after transfer :  11000

# harry_account = scb.get_account_from_card_id('12345')
# hermione_account1 = scb.get_account_from_card_id('12346')
# if isinstance(hermione_account1, AccountSavings) and (harry_account):
#     print("Test Case #3")
#     print("Harry's Account No : ",harry_account.get_id())
#     print("Hermione's Account No : ", hermione_account1.get_id())
#     print("Harry account before transfer : ",harry_account.get_balance())
#     print("Hermione account before transfer : ",hermione_account1.get_balance())
#     # harry_account.transfer("0000", 10000, hermione_account1)
#     # harry_account.make_transaction(Transaction(TransactionType.Transfer, 10000, hermione_account1))
#     print(harry_account >> (10000, hermione_account1))
#     print("Harry account after transfer : ",harry_account.get_balance())
#     print("Hermione account after transfer : ",hermione_account1.get_balance())
#     print("")

