mail-recipient-mismatch = Имя или должность получателя не совпадают.
mail-invalid-access = Имя и должность получателя совпадают, не подходящий уровень допуска.
mail-locked = Электронный замок активен. Разблокируйте с помощью вашей ID карты.
mail-desc-far = Посылка. С такого расстояния вы не можете разобрать, кому она предназначена.
mail-desc-close = Посылка предназначенная для { CAPITALIZE($name) }, { $job }.
mail-desc-fragile = Имеется наклейка [color=red]Внимание! Хрупкое![/color].
mail-desc-priority = На электроном замке горит надпись [color=yellow]Высокий приоритет![/color]. Надо бы поторопиться с доставкой!
mail-desc-priority-inactive = На электронном замке не горит надпись [color=#886600]Высокий приоритет![/color].
mail-unlocked = Электронный замок разблокирован.
mail-unlocked-by-emag = Электронный замок *жужжит*.
mail-unlocked-reward = Электронный замок разблокирован. { $bounty } космобаксов начислено на счет отдела снабжения.
mail-penalty-lock = ЭЛЕКТРОННЫЙ ЗАМОК СЛОМАН. ОТДЕЛУ СНАБЖЕНИЯ БЫЛ ВЫСТАВЛЕН ШТРАФ В РАЗМЕРЕ { $credits } КОСМОБАКСОВ.
mail-penalty-fragile = НАРУШЕНА ЦЕЛОСТНОСТЬ ПОСЫЛКИ. ОТДЕЛУ СНАБЖЕНИЯ БЫЛ ВЫСТАВЛЕН ШТРАФ В РАЗМЕРЕ { $credits } КОСМОБАКСОВ.
mail-penalty-expired = СРОК ДОСТАВКИ НАРУШЕН. CARGO ОТДЕЛУ СНАБЖЕНИЯ БЫЛ ВЫСТАВЛЕН ШТРАФ В РАЗМЕРЕ { $credits } КОСМОБАКСОВ.
command-mailto-description = Queue a parcel to be delivered to an entity. Example usage: `mailto 1234 5678 false false`. The target container's contents will be transferred to an actual mail parcel.
command-mailto-help = Usage: { $command } <recipient entityUid> <container entityUid> [is-fragile: true or false] [is-priority: true or false]
command-mailto-no-mailreceiver = Target recipient entity does not have a { $requiredComponent }.
command-mailto-no-blankmail = The { $blankMail } prototype doesn't exist. Something is very wrong. Contact a programmer.
command-mailto-bogus-mail = { $blankMail } did not have { $requiredMailComponent }. Something is very wrong. Contact a programmer.
command-mailto-invalid-container = Target container entity does not have a { $requiredContainer } container.
command-mailto-unable-to-receive = Target recipient entity was unable to be setup for receiving mail. ID may be missing.
command-mailto-no-teleporter-found = Target recipient entity was unable to be matched to any station's mail teleporter. Recipient may be off-station.
command-mailto-success = Success! Mail parcel has been queued for next teleport in { $timeToTeleport } seconds.
command-mailnow = Force all mail teleporters to deliver another round of mail as soon as possible. This will not bypass the undelivered mail limit.
command-mailnow-help = Usage: { $command }
command-mailnow-success = Success! All mail teleporters will be delivering another round of mail soon.
mail-item-name-unaddressed = посылка
mail-item-name-addressed = посылка ({ $recipient })
