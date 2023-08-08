cmd-ban-invalid-minutes = ${ minutes } не является допустимым количеством минут!
cmd-ban-invalid-severity = ${ severity } недопустимая тяжесть!
cmd-ban-invalid-arguments = Недопустимое количество аргументов
cmd-ban-hint-severity = [тяжесть]
cmd-banpanel-desc = Открывает панель бана
cmd-banpanel-help = Использование: banpanel [никнейм или ID пользователя]
cmd-banpanel-server = Это не может быть использовано в консоли сервера
cmd-banpanel-player-err = Указанный игрок не найден
ban-panel-title = Панель бана
ban-panel-player = Игрок
ban-panel-ip = IP
ban-panel-hwid = HWID
ban-panel-reason = Причина
ban-panel-last-conn = Использовать IP и HWID с последнего подключения?
ban-panel-submit = Забанить
ban-panel-confirm = Вы уверены?
ban-panel-tabs-basic = Основн инфо
ban-panel-tabs-reason = Причина
ban-panel-tabs-players = Список игрков
ban-panel-tabs-role = Инфо о запрете роли
ban-panel-no-data = Для бана необходимо указать пользователя, IP или HWID.
ban-panel-invalid-ip = Не удалось разобрать IP-адрес. Пожалуйста, попробуйте еще раз
ban-panel-select = Выберите тип
ban-panel-server = Бан
ban-panel-role = Бан роли
ban-panel-minutes = Минут
ban-panel-hours = Часов
ban-panel-days = Дней
ban-panel-weeks = Недель
ban-panel-months = Месяцев
ban-panel-years = Лет
ban-panel-permanent = Навсегда
ban-panel-ip-hwid-tooltip = Оставьте пустым и установите флажок ниже, чтобы использовать данные с последнего подключения
ban-panel-severity = Тяжесть:
# Ban string
server-ban-string = { $admin } выдал бан { $severity } тяжести, который истекает { $expires } для [{ $name }, { $ip }, { $hwid }], по причине: { $reason }
server-ban-string-never = никогда