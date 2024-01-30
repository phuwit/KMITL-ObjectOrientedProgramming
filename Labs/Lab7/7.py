from __future__ import annotations
from typing import List, Dict
from enum import Enum
from datetime import datetime
from abc import ABC, abstractproperty, abstractmethod


class AccountType(Enum):
    Undefined = -1
    Savings = 0
    Current = 1
    FixedDeposit = 1


class CardType(Enum):
    Undefined = -1
    ATM = 0
    Debit = 1

    
class TransactionType(Enum):
    Deposit = 0
    Withdrawal = 1
    Transfer = 2


class TerminalType(Enum):
    Undefined  = -1
    ATM = 0
    EDC = 1


class Bank:
    def __init__(self,name):
        self.__customers: List[Customer] = []
        self.__terminals: List[Terminal] = []
        self.__name=name
        self.__user_list = []
        self.__card_list = []
        self.__atm_list = []
        self.__seller_list = []
    
    def add_customer(self, customer: Customer) -> bool:
        if (isinstance(customer, Customer)):
            self.__customers.append(customer)
            return True
        return False

    def add_atm(self, atm: Terminal) -> bool:
        if (isinstance(atm, Terminal)):
            self.__terminals.append(atm)
            return True
        return False
    
    def get_customers(self) -> List[Customer]:
        return self.__customers
    
    def get_terminals(self) -> List[Terminal]:
        return self.__terminals

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

class Account(ABC):
    @property
    @abstractmethod
    def type(self) -> AccountType:
        pass
    
    @property
    @abstractmethod
    def interest_rate(self) -> float:
        pass
    
    def __init__(self, customer: Customer, id: str) -> None:
        self.__customer: Customer = customer
        self.__id: str = id
        self.__balance: int = 0
        self.__card: Card | None = None
        self.__transactions: List[Transaction] = []
    
    def set_card(self, card: Card) -> bool:
        if (isinstance(card, Card)):
            self.__card = card
            return True
        return False
    
    def get_id(self) -> str:
        return self.__id
    
    def get_balance(self) -> int:
        return self.__balance
    
    def get_card(self) -> Card | None:
        return self.__card
    
    def get_transactions(self) -> List[Transaction]:
        return self.__transactions
    
    def make_transaction(self, transaction: Transaction) -> bool:
        if (isinstance(transaction, Transaction)):
            self.__transactions.append(transaction)
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
                    transaction.set_incoming_transfer(False)
                    self.__balance -= transaction.get_amount()
            transaction.record_balance(self.__balance)
            return True
        return False


class AccountSavings(Account):
    def interest_rate(self):
        return 0.5
    
    def type(self):
        return AccountType.Savings
    

    def __init__(self, customer: Customer, id: str) -> None:
        super().__init__(customer, id)


class AccountFixedDeposit(Account):
    def interest_rate(self):
        return 2.5
    
    def type(self):
        return AccountType.Savings
    
    
    def __init__(self, customer: Customer, id: str) -> None:
        super().__init__(customer, id)
    

class Merchant:
    def __init__(self, id: str, name: str):
        self.__id: str = id
        self.__name: str = name
        self.__edcs: List[TerminalEdc] = []
    

class Card(ABC):
    @property
    @abstractmethod
    def type(self) -> AccountType:
        pass
    
    @property
    @abstractmethod
    def daily_transaction_limit(self) -> int:
        pass
    
    @property
    @abstractmethod
    def yearly_fee(self) -> int:
        pass
    
    def __init__(self, account: Account, id: str, pin: str) -> None:
        self.__account: Account = account
        self.__id: str = id
        self.__pin: str = pin
        self.__transaction_quota = self.daily_transaction_limit
        
    def get_id(self) -> str:
        return self.__id
    
    def get_account(self) -> Account:
        return self.__account
    
    def adjust_quota(self, amount: int) -> bool:
        if (self.__transaction_quota + amount >= 0):
            self.__transaction_quota += amount
            return True
        return False
    
    def reset_quota(self):
        self.__transaction_quota = self.daily_transaction_limit
        

class CardAtm(Card):
    def type(self):
        return CardType.ATM
    
    def daily_transaction_limit(self):
        return 40000
    
    def yearly_fee(self):
        return 150
    
    
class CardDebit(Card):
    def type(self):
        return CardType.Debit
    
    def daily_transaction_limit(self):
        return 40000
    
    def yearly_fee(self):
        return 150


class Terminal:
    type: TerminalType = TerminalType.Undefined
    
    def __init__(self, _bank: Bank, id: str, balance: int) -> None:
        self.__bank: Bank = _bank
        self.__id: str = id
        self._balance: int = balance
        
    def __find_card_from_id(self, card_id: str) -> Card | None:
        for customer in self.__bank.get_customers():
            for account in customer.get_accounts():
                card = account.get_card()
                if (isinstance(card, Card)) and (card.get_id() == card_id):
                    return account.get_card()
        return None
    
    def get_id(self):
        return self.__id

    # TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
    # TODO     2) atm_card เป็นหมายเลขของ atm_card
    # TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
    # TODO     ควรเป็น method ของเครื่อง ATM

    # @staticmethod
    def get_account(self, card_id: str):
        card = self.__find_card_from_id(card_id)
        if (card is not None) and (card.get_id() == card_id):
            return card.get_account()
        return None 


class TerminalAtm(Terminal):
    type = TerminalType.ATM

    # TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account 3) จำนวนเงิน
    # TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0

    # @staticmethod
    def deposit(self, account: Account, amount: int) -> bool:
        card = account.get_card()
        if (isinstance(account, Account)) and (isinstance(amount, int)) and (amount > 0) and \
            (isinstance(card, Card)) and (card.adjust_quota(amount)):
                self._balance += amount
                account.make_transaction(Transaction(TransactionType.Deposit, amount, datetime.now(), account, self))
                return True
        return False

    # TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account 3) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

    # @staticmethod
    def withdraw(self, account: Account, amount: int) -> bool:
        card = account.get_card()
        if (isinstance(account, Account)) and (isinstance(amount, int)) and (amount > 0) and \
            (amount <= account.get_balance()) and (isinstance(card, Card)) and (card.adjust_quota(-amount)):
                self._balance += amount
                account.make_transaction(Transaction(TransactionType.Withdrawal, amount, datetime.now(), account, self))
                return True
        return False

    # TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
        
    # @staticmethod
    def transfer(self, origin: Account, destination: Account, amount: int) -> bool:
        card = origin.get_card()
        if (isinstance(origin, Account)) and (isinstance(destination, Account)) and \
            (isinstance(amount, int)) and (amount > 0) and (amount <= origin.get_balance()) and \
            (isinstance(card, Card)) and (card.adjust_quota(-amount)):
                transaction = Transaction(TransactionType.Transfer, amount, datetime.now(), destination, self)
                origin.make_transaction(transaction)
                destination.make_transaction(transaction)
                return True
        return False


class TerminalEdc(Terminal):
    type = TerminalType.EDC
    
    def __init__(self, _bank: Bank, id: str, balance: int) -> None:
        super().__init__(_bank, id, balance)


class Transaction:
    def __init__(self, type: TransactionType, amount: int, timestamp: datetime, destination: Account, machine: Terminal) -> None:
        self.__type: TransactionType = type
        self.__amount: int = amount
        self.__timestamp: datetime = timestamp
        self.__destination: Account = destination
        self.__machine: Terminal = machine
        self.__balance = -1
        self.__incoming_transfer: bool | None
        
    def __str__(self) -> str:
        # return f'D-ATM:1002-1000-2000'
        sign = ''
        if (self.__type == TransactionType.Transfer):
            if (self.__incoming_transfer):
                sign = '+'
            else:
                sign = '-'
                
        return f'{self.__type.name[0]}-{self.__machine.type.name}:{self.__machine.get_id()}-{sign}{self.__amount}-{self.__balance}'
    
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
user ={'1-1101-12345-12-0':['Harry Potter','Savings','1234567890',20000,'ATM','12345'],
       '1-1101-12345-13-0':['Hermione Jean Granger','Saving','0987654321',1000,'Debit','12346'],
       '1-1101-12345-13-0':['Hermione Jean Granger','Fix Deposit','0987654322',1000,'',''],
       '9-0000-00000-01-0':['KFC','Savings','0000000321',0,'',''],
       '9-0000-00000-02-0':['Tops','Savings','0000000322',0,'','']}

atm ={'1001':1000000,'1002':200000}

seller_dic = {'210':"KFC", '220':"Tops"}

EDC = {'2101':"KFC", '2201':"Tops"}

# TODO 1 : สร้าง Instance ของธนาคาร และ สร้าง Instance ของ User, Account, บัตร
# TODO   : จากข้อมูลใน user รูปแบบการนำข้อมูลไปใช้สามารถใช้ได้โดยอิสระ
# TODO   : โดย Account แบ่งเป็น 2 subclass คือ Savings และ FixedDeposit
# TODO   : โดย บัตร แบ่งเป็น 2 subclass คือ ATM และ Debit

scb = Bank('SCB')
scb.add_user(User('1-1101-12345-12-0','Harry Potter'))
scb.add_user(User('1-1101-12345-13-0','Hermione Jean Granger'))
scb.add_user(User('9-0000-00000-01-0','KFC'))
scb.add_user(User('9-0000-00000-02-0','Tops'))
harry = scb.search_user_from_id('1-1101-12345-12-0')
harry.add_account(SavingAccount('1234567890', harry, 20000))
harry_account = harry.search_account('1234567890')
harry_account.add_card(ATM_Card('12345', harry, '1234'))
hermione = scb.search_user_from_id('1-1101-12345-12-0')
hermione.add_account(SavingAccount('0987654321',hermione,2000))
hermione_account1 = hermione.search_account('0987654321')
hermione_account1.add_card(Debit_Card('12346',hermione_account1,'1234'))
hermione.add_account(FixDepositAccount('0987654322',hermione,1000))
kfc = scb.search_user_from_id('9-0000-00000-01-0')
kfc.add_account(SavingAccount('0000000321', kfc, 0))
tops = scb.search_user_from_id('9-0000-00000-02-0')
tops.add_account(SavingAccount('0000000322', tops, 0))

# TODO 2 : สร้าง Instance ของเครื่อง ATM

scb.add_atm_machine(ATM_machine('1001',1000000))
scb.add_atm_machine(ATM_machine('1002',200000))

# TODO 3 : สร้าง Instance ของ Seller และใส่เครื่อง EDC ใน Seller 

temp = Merchant('210','KFC')
temp.add_edc(EDC_machine('2101',temp))
scb.add_seller(temp)
temp = Merchant('220',"Tops")
temp.add_edc(EDC_machine('2201',temp))
scb.add_seller(temp)

# TODO 4 : สร้าง method ฝาก โดยใช้ __add__ ถอน โดยใช้ __sub__ และ โอนโดยใช้ __rshift__
# TODO   : ทดสอบการ ฝาก ถอน โอน โดยใช้ + - >> กับบัญชีแต่ละประเภท

# TODO 5 : สร้าง method insert_card, deposit, withdraw และ transfer ที่ตู้ atm และเรียกผ่าน account อีกที
# TODO   : ทดสอบโอนเงินระหว่างบัญชีแต่ละประเภท

# TODO 6 : สร้าง method paid ที่เครื่อง EDC และเรียกผ่าน account อีกที

# TODO 7 : สร้าง method __iter__ ใน account สำหรับส่งคืน transaction เพื่อให้ใช้กับ for ได้ 

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

atm_machine = scb.search_atm_machine('1001')
harry_account = scb.search_account_from_card('12345')
atm_card = harry_account.get_card()
print("Test Case #1")
print("Harry's ATM No : ",atm_card.card_no)
print("Harry's Account No : ",harry_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Harry account before deposit : ",harry_account.amount)
print("Deposit 1000")
atm_machine.deposit(harry_account,1000)
print("Harry account after deposit : ",harry_account.amount)
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

atm_machine = scb.search_atm_machine('1002')
hermione_account = scb.search_account_from_card('12346')
atm_card = hermione_account.get_card()
print("Test Case #2")
print("Hermione's ATM No : ", atm_card.card_no)
print("Hermione's Account No : ", hermione_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Hermione account before withdraw : ",hermione_account.amount)
print("withdraw 1000")
atm_machine.withdraw(hermione_account,1000)
print("Hermione account after withdraw : ",hermione_account.amount)
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

harry_account = scb.search_account_from_card('12345')
hermione_account = scb.search_account_from_card('12346')
print("Test Case #3")
print("Harry's Account No : ",harry_account.account_no)
print("Hermione's Account No : ", hermione_account.account_no)
print("Harry account before transfer : ",harry_account.amount)
print("Hermione account before transfer : ",hermione_account.amount)
harry_account.transfer("0000", 10000, hermione_account)
print("Harry account after transfer : ",harry_account.amount)
print("Hermione account after transfer : ",hermione_account.amount)
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

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
kfc_account = scb.search_account_from_account_no('0000000321')
kfc = scb.search_seller('KFC')
edc = kfc.search_edc_from_no('2101')

print("Test Case #4")
print("Hermione's Debit Card No : ", debit_card.card_no)
print("Hermione's Account No : ",hermione_account.account_no)
print("Seller : ", kfc.name)
print("KFC's Account No : ", kfc_account.account_no)
print("KFC account before paid : ",kfc_account.amount)
print("Hermione account before paid : ",hermione_account.amount)
edc.paid(debit_card, 500, kfc_account)
print("KFC account after paid : ",kfc_account.amount)
print("Hermione account after paid : ",hermione_account.amount)
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

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
tops_account = scb.search_account_from_account_no('0000000322')
tops = scb.search_seller('Tops')
print("Test Case #5")
print("Hermione's Account No : ",hermione_account.account_no)
print("Tops's Account No : ", tops_account.account_no)
print("Tops account before paid : ",tops_account.amount)
print("Hermione account before paid : ",hermione_account.amount)
tops.paid(hermione_account,500,tops_account)
print("Tops account after paid : ",tops_account.amount)
print("Hermione account after paid : ",hermione_account.amount)
print("")


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด โดยใช้ for loop 


