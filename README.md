## Пульт охраны банка

web-страница с таблицей содержащей информацию об активных картах доступа работников 
и посещениях хранилища владельцами этих карт.

### Установка

Python3 должен быть уже установлен.  
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```commandline
pip install -r requirements.txt
```

Должен быть создан `.env` файл содержащий переменные:
* SECRET_KEY=''
* ENGINE=''
* HOST=''
* PORT='' - int
* NAME=''
* USER=''
* PASSWORD=''
* DEBUG='' - bool

### Использование
Запускаем и переходим по ссылке
```commandline
python manage.py runserver 127.0.0.1:8000
```
'Starting development server at (тут ссылка)'

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).