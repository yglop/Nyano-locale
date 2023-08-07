replay-loading = Загрузка ({ $cur }/{ $total })
replay-loading-reading = Чтение файлов
replay-loading-processing = Обработка файлов
replay-loading-spawning = Создание сущностей
replay-loading-initializing = Инициализация объектов
replay-loading-starting = Старт объектов
replay-loading-failed =
    Не удалось загрузить реплей:
    { $reason }
# Main Menu
replay-menu-subtext = Клиент реплеев
replay-menu-load = Загрузить выбранный реплей
replay-menu-select = Выбрать реплей
replay-menu-open = Открыть папку с реплеями
replay-menu-none = Реплеи не найдены.
# Main Menu Info Box
replay-info-title = Информация о реплее
replay-info-none-selected = Реплей не выбран
replay-info-invalid = [color=red]Выбран неверный реплей[/color]
replay-info-info =
    { "[" }color=gray]Selected:[/color]  { $name } ({ $file })
    { "[" }color=gray]Time:[/color]   { $time }
    { "[" }color=gray]Round ID:[/color]   { $roundId }
    { "[" }color=gray]Duration:[/color]   { $duration }
    { "[" }color=gray]ForkId:[/color]   { $forkId }
    { "[" }color=gray]Version:[/color]   { $version }
    { "[" }color=gray]Engine:[/color]   { $engVersion }
    { "[" }color=gray]Type Hash:[/color]   { $hash }
    { "[" }color=gray]Comp Hash:[/color]   { $compHash }
# Replay selection window
replay-menu-select-title = Выбрать реплей
# Replay related verbs
replay-verb-spectate = Наблюдать
# command
cmd-replay-spectate-help = replay_spectate [optional entity]
cmd-replay-spectate-desc = Attaches or detaches the local player to a given entity uid.
cmd-replay-spectate-hint = Optional EntityUid
