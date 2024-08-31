# python 3.12.5

import string, random

class Pwgv:
    """
• Генерирует 
• Записывает
• Выводит (сгенерированный пароль(-и) внутри текстового файла)
• Проверяет (в процентном сотношениях от каждого сгенерирового пароля)
    """
    def __init__(self, len_pw: int=8, num_pw: int=1):
        self.__data = ''  # Объединения всех символов, чисел и букв ВЕРШНЕГО НИЖНЕГО регистра
        self.__nglp = []  # Новый сгенерированный список из паролей (New generated list of passwords)
        self.__num_pw = num_pw  # Количестов паролей в списке
        self.__len_pw = len_pw  # Количестов знаков в паролей


    def main(self):
        """Тут проверка каждого методов внутри main"""
        self.set_nglp(False, False)
        #self.points_nglp()
        #self.percent_nglp()
        print(self.get_nglp())
        #self.percentage_record()


    def set_nglp(self, pun: bool=True, dig: bool=True, upp: bool=True, low: bool=True) -> None:
        """генерирует новый пароль в список"""
        try:
            if self.__len_pw <= 7 or self.__len_pw >= 65:
                # если менше 7 или больше 65 у len_pw то выдает ошибку
                raise SystemExit('Enter a number between 8 and 64 for this parameter len_pw')
            elif self.__num_pw < 1 or self.__num_pw >= 65:
                # если менше 1 или больше 65 у num_pw то выдает ошибку
                raise SystemExit('Enter a number between 1 and 64 for this parameter num_pw')
            for ch in [low, upp, dig, pun]:
                # Проверка каждого аргументе если не является Логический тип
                if not isinstance(ch, bool):
                    raise SystemExit('Only logical type')
            
            # Тут выполняется выбор символов для надежного гинерацый
            if low:
                self.__data += string.ascii_lowercase  # будут сгенерированы ВЕРХНЕГО РЕГИСТРА
            if upp:
                self.__data += string.ascii_uppercase  # будут сгенерированы НИЖНИГО РЕГИСТРА
            if dig:
                self.__data += string.digits  # будут сгенерированы НАТУРАЛЬНЫХ ЧИСЕЛ
            if pun:
                self.__data += string.punctuation  # будут сгенерированы СПЕЦСИМВОЛОВ
            if not self.__data:
                raise SystemExit("No characters are selected for password generation")

            for i in range(self.__num_pw):
                self.__nglp.append("".join(random.sample(self.__data, self.__len_pw)))

        except TypeError:
            raise SystemExit('Incorrectly entered. Enter only the number')
    

    def get_nglp(self) -> list:
        """выводит результат нового сгенерированного пароля, баллов и проценты виде списка"""
        return self.__nglp
        
    
    def nglp_record(self) -> None:
        """записывает список пароля в текстовом документе"""
        if len(self.__nglp) == 0:
            raise SystemExit('You have not generated a password')
        
        with open('password.txt', 'w') as file:
            file.write('__NEW_PASSWORD__\n\n')
            for i in range(len(self.__nglp)):
                pw_txt = self.__nglp[i] + '\n'
                file.write(pw_txt)
            file.close()


    def points_record(self) -> None:
        """записывает список пароля и баллов в текстовом документе"""
        if len(self.__nglp[0]) != 2:
            raise SystemExit('NOT generated POINTS')
        
        with open('password.txt', 'w') as file:
            file.write('__NEW_PASSWORD_POINT__\n\n')
            for i in range(len(self.__nglp)):
                points_txt = self.__nglp[i][0] + f' {self.__nglp[i][1]}\n'
                file.write(points_txt)
            file.close()


    def percentage_record(self) -> None:
        """записывает список пароля, баллов и проценты в текстовом документе"""
        if len(self.__nglp[0]) != 3:
            raise SystemExit('NOT generated PERCENTAGE')
        
        with open('password.txt', 'w') as file:
            file.write('__NEW_PASSWORD_PERCENT__\n\n')
            for i in range(len(self.__nglp)):
                percent_txt = self.__nglp[i][0] + f' {self.__nglp[i][2]}%\n'
                file.write(percent_txt)
            file.close()


    def points_nglp(self) -> None:
        """проверяет пароль, выводит виде баллов и храниться вложенном списке"""
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


    def percent_nglp(self) -> None:
        """проверяет пароль, выводит виде баллов, процентах и храниться вложенном списке"""
        lpw = len(self.__nglp)
        for i in range(lpw):
            pc = int((self.__nglp[i][1] / len(self.__nglp[i][0])) * 100)  # Конверт в ПРОЦЕНТАХ
            self.__nglp[i].append(min(pc, 100))  # Добовляет новый элемент ПРОЦЕНТ в список с ПАРОЛЯМИ и БАЛЛАМИ


if __name__ == '__main__':
    new_pw = Pwgv()
    new_pw.main()
