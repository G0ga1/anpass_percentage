import os, string, random

class New_password:
    """
• Генерирует 
• Записывает
• Выводит (сгенерированный пароль(-и) внутри текстового файла)
• Проверяет (в процентном сотношениях от каждого сгенерирового пароля)
    """
    def __init__(self, len_pw=8, num_pw=1):
        __a = "qwertyuiopasdfghjklzxcvbnm"
        __b = "QWERTYUIOPASDFGHJKLZXCVBNM"
        __c = "0123456789"
        __d = "[]{}()*'/,_-!?"
        self.__data = __a + __b + __c + __d  # Конкатенация
        self.nglp = []  # Новый сгенерированный список из паролей (New generated list of passwords)
        self.__num_pw = num_pw  # Количестов паролей
        self.__len_pw = len_pw  # Длина паролей (или количество знаков)


    def main(self):
        """Проверка методов в классе"""
        self.pw_gen()
        self.points_chpw()
        self.percent_pwgen()
        print(self.nglp)
        self.percentage_record()


    def pw_gen(self):
        """Генерация пароля"""
        for i in range(self.__num_pw):
            self.nglp.append("".join(random.sample(self.__data, self.__len_pw)))
        return self.nglp
        
    
    def pw_record(self):
        """Запись в текстовый файл пароли"""
        sh = os.path.join('password.txt', '*.srt')
        if sh:
            with open('password.txt', 'w') as file:
                file.write('__NEW_PASSWORD__\n\n')
                for i in range(len(self.nglp)):
                    pw_txt = self.nglp[i] + '\n'
                    file.write(pw_txt)
                file.close()


    def points_record(self):
        """Запись в текстовый файл пароли и баллы(в каждого пароле)"""
        sh = os.path.join('password.txt', '*.srt')
        if sh:
            with open('password.txt', 'w') as file:
                file.write('__NEW_PASSWORD_POINT__\n\n')
                for i in range(len(self.nglp)):
                    points_txt = self.nglp[i][0] + f' {self.nglp[i][1]}\n'
                    file.write(points_txt)
                file.close()


    def percentage_record(self):
        """Запись в текстовый файл пароли и проценты(в каждого пароле)"""
        sh = os.path.join('password.txt', '*.srt')
        if sh:
            with open('password.txt', 'w') as file:
                file.write('__NEW_PASSWORD_PERCENT__\n\n')
                for i in range(len(self.nglp)):
                    percent_txt = self.nglp[i][0] + f' {self.nglp[i][2]}%\n'
                    file.write(percent_txt)
                file.close()


    def points_chpw(self):
        """Проверка пароля на надежность"""
        new_pwgen = self.nglp
        self.nglp = []
        for i in range(len(new_pwgen)):
            count = 0  # Потчет очков на НАДЕЖНОСТЬ паролей
            upper_case = any([1 if i in string.ascii_uppercase else 0 for i in new_pwgen[i]])  # проверка на наличий ВЕРХНЕГО РЕГИСТРА в строки
            lower_case = any([1 if i in string.ascii_lowercase else 0 for i in new_pwgen[i]])  # проверка на наличий НИЖНИГО РЕГИСТРА в строк
            special = any([1 if i in string.punctuation else 0 for i in new_pwgen[i]])  # проверка на наличий СПЕЦСИМВОЛОВ в строке
            digits = any([1 if i in string.digits else 0 for i in new_pwgen[i]])  # проверка на наличий НАТУРАЛЬНЫХ ЧИСЕЛ в строке
            repeated = any([len(new_pwgen[i]) != len(set(new_pwgen[i]))]) #  Проверка на дубликат СИМВОЛОВ и СПЕСИАЛЬНЫХ СИМВОЛОВ в строке
            checking = sum([upper_case, lower_case, special, digits, repeated])  # Объединяет алгоритм проверок из списка

            # Подчет спиcка на надженость в баллах
            for num in range(1, checking+1):
                if checking > num:
                    count += 1

            # Проверка на длину
            total = len(new_pwgen[i])
            count += sum(1 for j in range(8, 65) if total > j)

            # Добовляет новый список паролей с БАЛЛАМИ
            self.nglp.append([new_pwgen[i], count])


    def percent_pwgen(self):
        """Проверка в процентах"""
        lpw = len(self.nglp)
        for i in range(lpw):
            pc = int((self.nglp[i][1] / len(self.nglp[i][0])) * 100)  # Конверт в ПРОЦЕНТАХ
            self.nglp[i].append(min(pc, 100))  # Добовляет новый элемент ПРОЦЕНТ в список с паролями и баллами


if __name__ == '__main__':
    new_pw = New_password(num_pw=12, len_pw=12)
    new_pw.main()
