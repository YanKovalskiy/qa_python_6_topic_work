from datetime import date, timedelta

ORDER_DATA_SET = (
    (('Иван', 'Иванов', 'ул. Космонавтов, д.4', 'ВДНХ', '89009001122',
      date.today() + timedelta(days=1), 'сутки', (True, False), 'Можно и серый')),
    (('Петр', 'Петров', 'ул. Новопесчаная, д.9', 'Сокол', '89009003344',
      date.today() + timedelta(days=3), 'четверо суток', (True, True), 'Не позднее 20:00')),
)
