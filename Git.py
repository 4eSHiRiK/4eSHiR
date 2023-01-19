git --version #Проверяет версию Гита
cd #Меняет директорию
ls #Список папок
clear # очищает историю запросов
git help - a #Список стандарт программм гита (ПРОБЕЛ ЧТОБЫ ПРОДОЛЖИТЬ СПИСОК )
                                              Q - выход
git command --help #Cправка по конкретной программе
git init #Инициализация гита (1 раз в начале проекта)
git commit #Создание слепка файла
hash #40 символов хранящих инфу про комит
git config --list --global/--local/--system #конфиг гита списком
git add #добавляет файл в гит
git status #Информация о файлах
git diff #Разница между файлами до совершения commit
git commit -am ""   #Создание commit
git commit --amend #Изменение имени commit   [insert - изменяем название комита - ESC - ctrl+c - :wq -> save
                                                                                                 :qa! -> not save
git log -p -2 #журнал комитов -разнциа между комитами -кол-во послед комитов (q-выход из журнала)
git diff hash_1_comit..hash_2_commit - #разница между комитами
git show commit #что было сделано в комите
git checkout commit #переключиться на версию файлов при этом комите НЕЛЬЗЯ ОТРЫВАТЬ ГОЛОВУ!
git checkout commit путь к файлу #переключиться на версию файла! при этом комите
git reset --hard commit #безвозвратно откатывает файлы до этого комита(можно и вперед)
git branch #Список веток
git branch имя ветки #создание новой ветки
git checkout <branch> #Переключчение на ветку
git merge <branch> # склеиваем <branch > в master
git remote -v #список удаленных репозиториев
git remote add origin <link на репозиторий> #добавить локальный репозиторий в удаленный (shift+insert)