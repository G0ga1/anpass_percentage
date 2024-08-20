import os, string, random

class New_password:
    """
• Генерирует 
• Записывает
• Выводит (сгенерированный пароль(-и) внутри текстового файла)
• Проверяет (в процентном сотношениях от каждого сгенерирового пароля)
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
        passwds = '\n'.join(self.pw_gen())
        self.pw_record()
        print(passwds, end='')

    def pw_gen(self):
        """Генерация пароля"""
        for i in range(self.num_pw):
            self.pwgen.append("".join(random.sample(self.data, self.len_pw)))
        
        return self.pwgen
    
    def pw_record(self):
        sh = os.path.join('password.txt', '*.srt')
        if sh:
            with open('password.txt', 'w') as file:
                file.write('__NEW_PASSWORD__\n\n')
                for p in range(len(self.pwgen)):
                    pw_txt = self.pwgen[p] + '\n'
                    file.write(pw_txt)
                file.close()

    def ch_password(self):
        """Проверка пароля на надежность"""
        pass

    def percent_pw_gen():
        """Проверка в процентах"""
        pass

if __name__ == '__main__':
    new_pw = New_password(num_pw=12, len_pw=12)
    new_pw.main()
else:
    print('Ой!!! Ошибка вышло!')