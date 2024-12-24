Здравствуйте, мой проект написан на Python, в качестве БД я использовал PostgreSQL. Для проверки приложения я использовал Postman

Мой проект заключается в разработке онлайн платформы торговой сети электроники

Все зависимости можно посмотреть в файле requirements.txt. Так же перед применением миграций занесите все данные в файл .env и создайте базу данных в PostgreSQL

Функционал приложения заключается в следующем:
  1. Я реализовал модели сети по продаже электроники:
    Завод;
    Розничная сеть;
    Индивидуальный предприниматель.
  Каждое звено сети ссылается только на одного поставщика оборудования (у завода нет поставщика).

  2. Каждое звено сети обладает следующими элементами:
    Название.
    Контакты(создал для этого отдельную модель):
      Email,
      Страна,
      Город,
      Улица,
      Номер дома.
    Продукты(создал для этого отдельную модель):
      Название,
      Модель,
      Дата выхода продукта на рынок.
    Поставщик (у завода отсутствует).
    Задолженность перед поставщиком в денежном выражении с точностью до копеек(у завода отсутствует).
    Время создания (заполняется автоматически при создании).

  3. Сделал вывод в админ-панели созданных объектов.
    На странице объекта сети добавил:
      Ссылку на «Поставщика»((у завода отсутствует);
      Фильтр по названию города;
      Admin action, очищающий задолженность перед поставщиком у выбранных объектов(у завода отсутствует).
     
  4. Используя DRF, создал контроллеры для всех моделей;
     Запретил обновление через API поля «Задолженность перед поставщиком»;
     Добавил возможность фильтрации объектов по определенной стране в ListView у каждой модели сети(для этого добавьте к запросу - ?country=страна).
     
  5. Настроил права доступа к API так, чтобы только активные сотрудники имели доступ к API.
