import string, random

class New_password:
    """
• Генерирует 
• Записывает
• Выводит (сгенерированный пароль(-и) внутри текстового файла)
• Проверяет (в процентном сотношениях от каждого сгенерирового пароля)
    """
    def __init__(self, len_pw: int=8, num_pw: int=1):
        __a = "qwertyuiopasdfghjklzxcvbnm"
        __b = "QWERTYUIOPASDFGHJKLZXCVBNM"
        __c = "0123456789"
        __d = "[]{}()*'/,_-!?"
        self.__data = __a + __b + __c + __d  # Объединения всех символов, чисел и букв ВЕРШНЕГО НИЖНЕГО регистра
        self.__nglp = []  # Новый сгенерированный список из паролей (New generated list of passwords)
        self.__num_pw = num_pw  # Количестов паролей в списке
        self.__len_pw = len_pw  # Количестов знаков в паролей


    def main(self):
        """Тут проверка каждого методов внутри main"""
        self.pw_gen()
        self.points_chpw()
        self.percent_pwgen()
        print(self.__nglp)
        self.percentage_record()


    def pw_gen(self) -> list:
        """Генерация пароля"""
        try:
            if self.__len_pw <= 7 or self.__len_pw >= 65:
                raise SystemExit('Enter a number between 8 and 64 for this parameter len_pw')
            elif self.__num_pw < 1 or self.__num_pw >= 65:
                raise SystemExit('Enter a number between 1 and 64 for this parameter num_pw')
            
            for i in range(self.__num_pw):
                self.__nglp.append("".join(random.sample(self.__data, self.__len_pw)))

            return self.__nglp
        except TypeError:
            raise SystemExit('Incorrectly entered. Enter only the number')
        
    
    def pw_record(self) -> None:
        """Запись в текстовый файл пароли"""
        if len(self.__nglp) == 0:
            raise SystemExit('You have not generated a password')
        
        with open('password.txt', 'w') as file:
            file.write('__NEW_PASSWORD__\n\n')
            for i in range(len(self.__nglp)):
                pw_txt = self.__nglp[i] + '\n'
                file.write(pw_txt)
            file.close()


    def points_record(self) -> None:
        """Запись в текстовый файл пароли и баллы(в каждого пароле)"""
        if len(self.__nglp[0]) != 2:
            raise SystemExit('NOT generated POINTS')
        
        with open('password.txt', 'w') as file:
            file.write('__NEW_PASSWORD_POINT__\n\n')
            for i in range(len(self.__nglp)):
                points_txt = self.__nglp[i][0] + f' {self.__nglp[i][1]}\n'
                file.write(points_txt)
            file.close()


    def percentage_record(self) -> None:
        """Запись в текстовый файл пароли и проценты(в каждого пароле)"""
        if len(self.__nglp[0]) != 3:
            raise SystemExit('NOT generated PERCENTAGE')
        
        with open('password.txt', 'w') as file:
            file.write('__NEW_PASSWORD_PERCENT__\n\n')
            for i in range(len(self.__nglp)):
                percent_txt = self.__nglp[i][0] + f' {self.__nglp[i][2]}%\n'
                file.write(percent_txt)
            file.close()


    def points_chpw(self) -> None:
        """Проверка пароля на надежность"""
        new_pwgen = self.__nglp
        self.__nglp = []
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
            self.__nglp.append([new_pwgen[i], count])


    def percent_pwgen(self) -> None:
        """Проверка в процентах"""
        lpw = len(self.__nglp)
        for i in range(lpw):
            pc = int((self.__nglp[i][1] / len(self.__nglp[i][0])) * 100)  # Конверт в ПРОЦЕНТАХ
            self.__nglp[i].append(min(pc, 100))  # Добовляет новый элемент ПРОЦЕНТ в список с ПАРОЛЯМИ и БАЛЛАМИ


if __name__ == '__main__':
    new_pw = New_password()
    new_pw.main()
