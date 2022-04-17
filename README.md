# Требования к окружению на машине хоста

* Для работы тестов на машине хоста должен быть поднят selenoid на порту "4444"

# Запуск тестов
1. OPENCART_PORT=8081 PHPADMIN_PORT=8888 LOCAL_IP=$(hostname -I | grep -o "^[0-9.]*") docker-compose build
2. OPENCART_PORT=8081 PHPADMIN_PORT=8888 LOCAL_IP=$(hostname -I | grep -o "^[0-9.]*") docker-compose up --abort-on-container-exit

где:
* OPENCART_PORT - свободный порт на машине хоста для поднятия OpenCart
* PHPADMIN_PORT - свободный порт на машине хоста для поднятия PhpMyAdmin

# Генерация отчетов Allure

* Результаты теста биндятся в каталог ./allure-results в каталоге запуска docker-compose.