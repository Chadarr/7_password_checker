# Утилита проверки сложности пароля

Утилита для проверки сложности пароля. Проверяется наличие цифр, букв нижнего и верхнего регистра, спецсимволов.

### Как установить

Python3 должен быть уже установлен. 
Затем установите зависимости из файла requirements.
```
pip3 install -r requirements.txt
```

### Как запустить
Скрипт запускается из консоли.
```shell
foo@bar ~ % python3 main.py
```

### Как использовать
После запуска введите пароль, который хотите проверить. При вводе, сам пароль динамически проверяется на сложность, а в консоли символы заменяются на *.
```
Введите пароль: ******
Рейтинг пароля: 6
```
Для выхода из утилиты, нажмите CTRL+C

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
