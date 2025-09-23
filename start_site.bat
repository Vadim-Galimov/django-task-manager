
@echo off
echo Запуск Django сайта...

REM Проверяем, что мы в правильной папке
if not exist "manage.py" (
    echo Ошибка: Файл manage.py не найден!
    echo Перехожу в папку проекта...
    cd /d "D:\github\django-task-manager"
)

REM Проверяем виртуальное окружение
if not exist "venv\Scripts\activate.bat" (
    echo Ошибка: Виртуальное окружение не найдено!
    pause
    exit
)

REM Активируем виртуальное окружение
call venv\Scripts\activate

REM Запускаем сервер
echo Сервер запускается...
python manage.py runserver

pause