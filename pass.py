import os, string, random

class New_password:
    """
• Генерирует 
• Записывает
• Выводит (записаный пароль внутри файла)
• Проверяет (в процентном сотношениях от пороля)
    """
    def __init__(self, len_pw = 8, num_pw = 1):
        a = "qwertyuiopasdfghjklzxcvbnm"
        b = "QWERTYUIOPASDFGHJKLZXCVBNM"
        c = "0123456789"
        d = "[]{}()*'/,_-!?"
        self.data = a + b + c + d
        self.pwgen = []
        self.num_pw = num_pw
        self.len_pw = len_pw
