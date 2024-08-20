import os, string, random

class New_password:
    """
• Генерирует 
• Записывает
• Выводит (записаный пароль внутри файла)
• Проверяет (в процентном сотношениях от пороля)
    """
    def __init__(self, len_pw=8, num_pw=1):
        a = "qwertyuiopasdfghjklzxcvbnm"
        b = "QWERTYUIOPASDFGHJKLZXCVBNM"
        c = "0123456789"
        d = "[]{}()*'/,_-!?"
        self.data = a + b + c + d  # Конкатенация
        self.pwgen = []  # Список паролей
        self.num_pw = num_pw  # Количестов паролей
        self.len_pw = len_pw  # Длина паролей (или количество знаков)

    def main(self):
        """Проверка методов в классе"""
        for newpw in self.pw_gen():
            print(newpw)

    def pw_gen(self):
        """Генерация пароля"""
        for i in range(self.num_pw):
            self.pwgen.append("".join(random.sample(self.data, self.len_pw)))
        
        return self.pwgen
    
    def pw_record(self):
        """Запись паролей в текстовый файл"""
        pass

if __name__ == '__main__':
    new_pw = New_password(num_pw=5)
    new_pw.main()
else:
    print('Ой!!! Ошибка вышло!')