**Условия:**

Написать утилиту, для проверки SSL сертификата. Никаких ограничений по реализации нет. Но выбор алгоритма и его реализация влияет на решение о приглашении кандидата на второй этап.


**Входные данные:**

   Имеется текстовый файл. В каждой строке записано имя хоста

**варианты:**

    https://hostname
    https://hostname/
    https://hostname/blabl
    hostname/
    hostname/blabla 

**Выходные данные:**

На выход требуется создать файл output.csv формата:

    HostSSL_validityExpires