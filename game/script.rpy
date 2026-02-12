# Вы можете расположить сценарий своей игры в этом файле.

# Определениеперсонажей игры.
define arsen = Character('Арсен')
image arsenImage = "sprites/arsen.png"
image arsenImage shock= "sprites/arsenShock.png"

define batrihan = Character ('Батырхан')
image batrihanImage = "sprites/batrihan.png"

define boss = Character('Сергей Петрович')
image bossImage = "sprites/boss.png"
image bossImage aggre = "sprites/boss_aggre.png"
image bossImage sad = "sprites/boss_sad.png"

define luba = Character('Люба')
image lubaImage = "sprites/luba.png"

define victor = Character('Виктор')
image victorImage = "sprites/Victor.png"

define maxs = Character('Макс')
image maxsImage = "sprites/Max.png"

define sonya = Character('Соня')
image sonyaImage = "sprites/sonya.png"
image sonyaImage smile = "sprites/sonya_smile.png"

define oper = Character('Опер')
image operImage = "sprites/oper.png"
image operImage aggre = "sprites/oper.png"


define diana = Character('Диана')
image dianaImage = "sprites/diana.png"

image CoffeyShop = "backgrounds/coffeeShop.png"
image Shop = "backgrounds/shop.png"

image street = "backgrounds/street.png"
image roomArsen = "backgrounds/roomArsen.png"


image officeBackground = "backgrounds/office.png"
image officeBackground Work = "backgrounds/office_work.png"
image officeBackground It = "backgrounds/officeIT.png"
image officeBackground cabinet = "backgrounds/cabinet.png"
image officeBackground PC_boss = "backgrounds/PC_boss.png"
image officeBackground PC_boss_1 = "backgrounds/PC_boss_1.png"
image officeBackground PC_boss_2 = "backgrounds/PC_boss_2.png"
image officeBackground PC_boss_3 = "backgrounds/PC_boss_3.png"
image officeBackground door = "backgrounds/door.png"
image officeBackground doorPeregovor = "backgrounds/doorPeregovor.png"
image officeBackground office = "backgrounds/streetOffice.png"
image officeBackground cabinetVictor = "backgrounds/cabinetVictor.png"
image officeBackground entryOffice = "backgrounds/entryOffice.png"

image Oracle slide1 = "backgrounds/oracle/1.png"
image Oracle slide2 = "backgrounds/oracle/2.png"
image Oracle slide3 = "backgrounds/oracle/3.png"
image Oracle slide4 = "backgrounds/oracle/4.png"
image Oracle slide5 = "backgrounds/oracle/5.png"

image Chat = "backgrounds/chat.png"
image Plan = "backgrounds/plan.png"

define audio.phone = "sounds/phone.ogg"


#audio

default authority = 0
default communication = 0
default selfSufficiency = 0
default choiceTwoPart = False

# Игра начинается здесь:
label start:
    scene officeBackground office
    "Офис банка 'Финанс-Капитал'"

    scene officeBackground with fade
    "Интерьер открытого офиса банка 'Финанс-Капитал'. Стук клавиатур, гул разговоров. Атмосфера напряженная."


    scene officeBackground with fade
    show arsenImage at left with moveinleft:
        xzoom -1
    "Арсен, невыспавшийся и в помятой рубашке, пытается незаметно пробраться к своему столу."

    "Батырхан спокойно пьет кофе и, увидев Арсена, качает головой."

    show batrihanImage at right with moveinright
    batrihan "Не перестаешь удивлять, Арсен..."
    batrihan "Ты в курсе, который час? Босс сегодня с утра рычал, как раненый медведь."
    batrihan "Кофе ему не тот подали. Ты сейчас на его гнев нарвешься."

    arsen "Батырхан, не нагоняй."
    arsen "Я и сам прекрасно понимаю, что попаду под раздачу."
    arsen "Еще и не выспался, никак не могу привыкнуть к графику…"
    hide batrihanImage
    
    "Внезапно дверь в отдел с грохотом распахивается."
    show bossImage aggre at right with moveinright:
        xpos 0.9
        xanchor 1.2
    "На пороге Сергей Петрович, лицо багровое от гнева. "
    show lubaImage at right with moveinright
    
    "За ним, как тень, семенит Люба."
    
    boss "Ну что такое?! Кто вам сказал, что опаздывать на работу - в порядке вещей?!"
    boss "Дела у нас горят, дедлайны жмут, бизнес не дремлет! Кто, вы думаете, кредиты будет выдавать?"
    boss "Феи-кредиторши?"
    boss "ВАШИ БАБУШКИ?!"
    boss "Чтобы я больше не видел таких вольностей!"

    luba "Да-да, совершенно верно!"
    luba "Вы совсем забыли, где работаете?!"
    luba "Быстро за дело, нечего рот разевать!"

    boss "Ты тоже не зазнавайся, дорогуша."
    boss "Иди заполняй документики по вчерашним заявкам и принеси мне кофе."
    boss "На этот раз без своей пенистой бурды!"
    
    hide lubaImage with moveoutright
    
    "Люба, обиженно надув губы, уходит."
    hide bossImage with moveoutright
    "Сергей Петрович бросает гневный взгляд на Арсена и скрывается в своем кабинете."
    "Арсен тяжело вздыхает и падает на стул."

    scene black with dissolve
    centered "{size=36}Час спустя...{/size}" with dissolve
    
    scene officeBackground It
    "Арсен и Батырхан погружены в код."
    "На экранах — сложные формы для автоматической выдачи кредитов."

    show arsenImage at left with moveinleft:
        xzoom -1
    arsen "Боже, так спать хочу... Я даже энергетик не успел купить. Как работать-то?"
    
    show batrihanImage at right with moveinright
    batrihan "Ну, все, хватит ныть."
    batrihan "Давай, пиши свой модуль. Проверка скоринга ждет не дождется, когда ты свою магию применишь."
    
    "Они работают в тишине несколько минут. Слышен только стук клавиш и тихий смех сплетниц впереди."

    arsen "Вот же кому-то весело на работе…"
    batrihan "Не говори, даже завидно. Могли бы и поделиться новостями  с нами, посмеялись бы вместе."

    hide batrihanImage
    arsen "Черт, вообще не сосредоточиться. Надо что-то делать."
    
    menu: 
        "СБЕГАТЬ ЗА ЭНЕРГЕТИКОМ":
            jump goEnergy
        "СОСРЕДОТОЧИТЬСЯ НА РАБОТЕ":
            show screen add_authority
            pause 1.0
            hide screen add_authority
            jump goConcentrate
        "ПРОГУЛЯТЬСЯ ПО ОФИСУ":
            show screen add_communication
            pause 1.0
            hide screen add_communication
            jump goWalk
    

    return

label goEnergy:
    "Арсен решает, что без допинга он не выживет"
    "Крадясь, направляется к выходу."

    scene Shop with fade
    pause 1.0
    scene officeBackground with fade

    show arsenImage at left:
        xzoom -1

    "Из кабинета выходит Сергей Петрович с папкой в руках."
    show boss at right with moveinright
    "Его взгляд падает на Арсена, который только что вернулся и ставит на стол банку энергетика."
    
    boss "Арсен! А ну-ка ко мне!"
    "Арсен подходит, дрожа."
    scene officeBackground cabinet with dissolve
    show arsenImage at left:
        xzoom -1
    show bossImage aggre at right

    boss "Ты мне объяснишь, что это за утренний променад?"
    boss "Работать не хочешь?"
    boss "Запомни, пацан: за опоздания и самовольности — вычет. Не хочешь остаться безработным и вернуться обратно в свою деревню — работай усердно."
    boss "Ясно?"

    scene officeBackground It with fade
    "Арсен возвращается в ступоре"
    show arsenImage at right with moveinright 
    show batrihanImage at left with moveinleft:
        xzoom -1

    batrihan "Ладно, я схожу размяться."
    arsen "Не боишься натолкнуться на босса? До перерыва еще работать и работать."
    batrihan "Да я буквально на пару минут, просто пройдусь по этажу."

    scene black with dissolve
    scene officeBackground It with fade
    show batrihanImage at left with moveinleft:
        xzoom -1
    
    "Батырхан возвращается с задумчивым видом"
    batrihan "Слышал, босс с кем-то ругался... Про какой-то 'Омега-Холдинг' и упрощенную схему."
    batrihan "Пахнет жареным. Наш босс, похоже, шаманит с какими-то сомнительными конторами."
    
    jump endDay
    return

label goConcentrate:
    $ authority += 1
    hide arsenImage
    "Арсен стискивает зубы и углубляется в код, пытаясь не обращать внимания на усталость. Скучно, но безопасно. "
    
    show batrihanImage at left with moveinleft:
        xzoom -1

    batrihan "Ладно, я схожу размяться."
    arsen "Не боишься натолкнуться на босса? До перерыва еще работать и работать."
    batrihan "Да я буквально на пару минут, просто пройдусь по этажу."

    scene black with dissolve
    scene officeBackground It with fade
    show batrihanImage at left with moveinleft:
        xzoom -1
    
    "Батырхан возвращается с задумчивым видом"
    batrihan "Слышал, босс с кем-то ругался... Про какой-то 'Омега-Холдинг' и упрощенную схему."
    batrihan "Пахнет жареным. Наш босс, похоже, шаманит с какими-то сомнительными конторами."
    
    jump endDay
    return


label goWalk:
    $ communication += 1
    hide arsenImage with moveoutleft
    "Арсен встает и делает вид, что направляется к кулеру."
    scene officeBackground with dissolve
    "Проходя мимо кабинета Сергея Петровича, он замечает, что дверь приоткрыта. Слышатся взволнованные голоса."

    scene officeBackground cabinet with dissolve
    show bossImage at right

    boss "...Да, я понимаю, 'Омега-Холдинг' не самый чистый клиент, но комиссия-то какая!"
    boss "Проведите их по упрощенной схеме..."
    boss "Да, я знаю, что у них проблемы с отчетностью..."
    boss "Сделайте как для 'дружественных'! Главное — быстро и тихо."
    
    "Арсен замирает, сердце бешено колотится."
    "Он слышит, как босс кладет трубку и бормочет себе под нос."

    boss "Идиоты... Не понимают, что в наше время нужно уметь вертеться."

    hide bossImage
    scene officeBackground It with dissolve
    show arsenImage shock at right with moveinright
    "Арсен воозврашается за стол, его лицо бледное. Батырхан замечает это."
    show batrihanImage at left with moveinleft:
        xzoom -1
    batrihan "Чего ты такой помятый? Босс тебя видел?"
    
    arsen "Батырхан, ты не поверишь... Я только что подслушал разговор босса."

    "Арсен пересказывает услышанный разговор."

    arsen "Он какие-то сомнительные кредиты проводит через 'упрощенку'! 'Омега-Холдинг', проблемы с отчетностью..."
    
    batrihan "Вот это поворот..."
    batrihan "Так наш босс не только козлина, но и аферист."
    batrihan "Это серьезно, Арсен. Это информация."

    jump endDay
    return

label endDay:
    scene black with fade
    centered "КУРИЛКА, КОНЕЦ ДНЯ" with dissolve
    
    scene street with dissolve
    "Виктор и Макс, пьют кофе. Рядом стоят Соня с Дианой."
    "Арсен и Батырхан делятся своими подозрениями с коллегами."
    
    show victorImage at right with moveinright
    victor "Опять этот Петрович ведет свои темные игры. Я чувствую, это плохо кончится. Банку потом расхлебывать."

    show maxsImage at left with moveinleft:
        xzoom -1
    maxs "Да ладно, Витя, успокойся."
    maxs "В каждом офисе есть свой 'император Палпатин'. Главное — вовремя принести попкорн."

    hide victorImage with moveoutright
    hide maxsImage with moveoutleft

    show arsenImage at right with moveinright
    show batrihanImage at left with moveinleft:
        xzoom -1
    "Арсен и Батырхан переглядываются."
    "Они понимают, что подозрения возникло не только у них."

    batrihan "Ну что, новичок? Похоже, твой первый опыт работы превращается в настоящий детектив."
    batrihan "Решай, что будешь делать с этой информацией. Сидеть тихо и не высовываться — безопасно."
    batrihan "Но если копнуть... можно и подставить себя, и на босса нарваться, а можно и карьеру сделать. Выбор за тобой."

    scene black with fade
    "Становится ясно, что это только начало большой офисной интриги, где Арсену предстоит сделать выбор:"
    "Остаться в стороне или рискнуть, раскрыв махинации босса, что может привести к увольнению, аресту, повышению или жизни простого офисного сотрудника."
    jump chapter_two
    return


label chapter_two:
    scene black with fade
    centered "Глава 2. Новые подробности." with dissolve
    centered "Офис утро." with dissolve
    
    scene officeBackground with dissolve
    "Прошло полтора месяца. Арсен сдружился со всеми, влился в коллектив."
    "За прошедшее время выяснилось, что босс сотрудничает с компанией конкурентов “Омега-Холдинг”, передает им конфиденциальную информацию, что противоречит политике банка “Финанс-Капитал”."
    "Естественно, что это не пришлось по вкусу сотрудникам банка, которые узнали о фактическом предательстве босса."

    "Очередной рабочий день."
    show arsenImage at left with moveinleft:
        xzoom -1
    "Арсен наконец-то привык к ранним подъемам, теперь он опаздывал редко, но метко. Так случилось и в этот день."
    "Арсен аккуратно крался к своему рабочему месту, стараясь не наткнуться на начальство, чтобы не получить выговор."
    
    "Навстречу ему шли Соня и Диана."
    scene officeBackground It with dissolve
    show arsenImage at left with moveinleft:
        xzoom -1
    show sonyaImage at right with moveinright:
        xpos 0.9
        xanchor 1.5
    show dianaImage at right with moveinright
    
    sonya "Арсен, вот ты где! Тебе повезло, Сергей Петрович сегодня будет не в офисе."
    arsen "Вот это новости, я понимаю! Хоть бы так было каждый день. А Батырхан уже здесь?"
    diana "Он уехал с боссом. А, и еще Сергей Петрович оставил Виктора замещать его, это наш шанс разузнать побольше о его махинациях!"
    arsen "Супер, вот только…"
    
    menu: 
        "Схожу за кофе, а потом сразу приступим.":
            show screen add_communication
            pause 1.0
            hide screen add_communication

            show screen add_authority
            pause 1.0
            hide screen add_authority
            jump option1
        "Ты закончила пересчитывать графики платежей? Скоро срок сдачи":
            show screen add_selfSufficiency
            pause 1.0
            hide screen add_selfSufficiency

            show screen add_authority
            pause 1.0
            hide screen add_authority
            jump option2
        "Думаю, меня это не интересует. Разбирайтесь сами, я просто понаблюдаю со стороны.": 
            show screen add_selfSufficiency
            pause 1.0
            hide screen add_selfSufficiency
            jump option3
    return




label option1:
    $ communication += 1
    $ authority += 1
    scene CoffeyShop with fade
    pause 1.0
    scene officeBackground cabinet with fade

    show dianaImage at left with moveinleft:
        xalign 0.5
        xzoom -1
    show sonyaImage at left with moveinleft:
        xalign 0.3
        xzoom -1
    show arsenImage at left with moveinleft:
        xzoom -1
    show victorImage at right with moveinright

    
    "В кабинете босса"

    sonya "Ну что, ты уже начинал что-то искать?"
    victor "Нет, я ждал вас. С чего предлагаете начать?"
    arsen "С почты конечно же! Он даже оставил ее открытой."

    scene officeBackground PC_boss with fade
    "Герои заходят в почту босса и начинают искать что-то необычное."
    "Виктор сразу предлагает искать чаты с “Омега-Холдингом”, но ничего компрометирующего они не находят, поэтому решают читать все подряд."
    
    "Спустя 20 минут…"

    diana "Как так… неужели тут ничего? Или он все удалил? Быть такого не может…"
    arsen "Погодите, а это что? o1m_h@mail.ru звучит подозрительно. Это точно не официальный адрес “Омега-Холдинга”."

    scene officeBackground PC_boss_1
    "Виктор открывает диалог, все герои внимательно изучают содержимое переписки."
    "Находят в ней какой-то файл, отправленный Сергеем Петровичем, и открывают его."
    
    scene officeBackground PC_boss_2
    diana "Это же…"
    arsen "Да, похоже на данные клиентов. Но зачем они ему?"
    victor "Это неважно, в любом случае, запрещено сохранять данные клиентов и уж тем более отправлять кому-то." 
    
    scene officeBackground PC_boss
    "Виктор закрывает файл."
    
    arsen "Ох ты ж… вы видите?"

    scene officeBackground PC_boss
    "Арсен указывает на письмо босса, в котором тот рассказывает об акциях, которые “Финанс-Капитал” планирует приобрести в больших количествах."
    
    scene officeBackground PC_boss_3
    arsen "Это разве не… как там называется… инсайдерская информация? Такое ведь нельзя передавать кому-то?"
    victor "Да, это конфиденциально. Банк еще не опубликовал эту информацию, а она уже утекла явно не туда, куда надо…"
    victor "Об этом стоит сообщить как можно скорее."

    sonya "А нам точно ничего не будет, за то что мы влезли, куда не надо?"
    
    arsen "Я думаю, будет хуже, если это так и останется в тайне. Еще окажемся виноватыми."
    
    victor "Ладно, разберемся с этим чуть позже. Я вас позову, а сейчас идите, у меня еще остались дела."
    
    scene officeBackground It with fade
    "Арсен, Соня и Диана уходят из кабинета босса."

    show sonyaImage at left with moveinleft:
        xalign 0.3
        xzoom -1
    show dianaImage at right with moveinright
    show arsenImage at left with moveinleft:
        xzoom -1
    
    arsen "Теперь можно спокойно заняться рабочими делами."
    sonya "А, точно, ты прав."

    scene officeBackground Work with fade
    show sonyaImage at left with moveinleft:
        xalign 0.3
        xzoom -1
    show dianaImage at right with moveinright
    show arsenImage at left with moveinleft:
        xzoom -1
    "Соня смотрит на экран с легкой улыбкой. Арсен нервно постукивает ручкой по столу. Диана проверяет время на телефоне."
    
    diana "Ну что, коллеги, давайте по существу."
    diana "Арсен, ты ведь говорил, есть критическая проблема с отчетом для финансов. Что случилось?"

    arsen "Отчёт, который прекрасно работал на тестовых данных, вчера вечером, на полной выгрузке, выполнялся три часа и упал по таймауту."
    arsen "Я уже всё перепробовал!"
    arsen "Я переписал запрос, добавил ещё индексов... ничего не помогает."
    arsen "Кажется, Oracle просто ненавидит меня лично."

    sonya "Oracle никого не ненавидит, Арсен."
    sonya "Он просто машина, которая делает ровно то, что ты ей сказал. Покажи-ка план выполнения того, что ты 'уже перепробовал'."
    

    scene Oracle slide1

    sonya "Ага. Я так и думала. Смотри."
    
    scene Oracle slide2
    sonya "Вот здесь, вместо ожидаемого NESTED LOOPS, оптимизатор решил сделать HASH JOIN."
    sonya "А здесь — вместо быстрого поиска по индексу (INDEX RANGE SCAN) пошел полным сканированием большой таблицы (FULL TABLE SCAN). Это и есть наша проблема."
    
    arsen "Но почему?! У меня же есть индекс по transaction_date! Я его специально вчера создал. "
    arsen "Oracle должен быть умным, почему он его не использует?"

    sonya "'Должен' — ключевое слово."
    sonya "Оптимизатор — не ясновидящий. Он принимает решение на основе статистики."
    sonya "Когда ты вчера обновил данные, статистика по таблицам устарела. Оптимизатор думает, что таблица маленькая и выгоднее её просканировать целиком, хотя на деле там миллионы строк."

    diana "Поняла не всё, но основной посыл уловила."
    diana "Получается, база данных принимает плохие решения из-за недостатка информации? Как мы это исправляем?"

    sonya "Есть несколько путей."
    sonya "Первый и самый простой — собрать свежую статистику."
    sonya "Арсен, выполни в SQL Developer: EXEC DBMS_STATS.GATHER_TABLE_STATS('SH', 'SALES'); Замени SH и SALES на нашу схему и таблицу."

    "Арсен быстро печатает на своем ноутбуке."
    scene Oracle slide3
    arsen "Понял, делаю... Готово."

    sonya "А теперь запусти свой запрос с /*+ GATHER_PLAN_STATISTICS */ и покажи новый план."

    "Арсен выполняет команду"

    arsen "Он пошел по индексу! Запрос выполнился за 12 секунд! Это магия?"

    sonya "Нет, это администрирование. Но это не всегда срабатывает. Иногда сам запрос написан так, что он ставит оптимизатор в тупик."
    sonya "Например, у тебя здесь есть функция UPPER() на индексированном поле."

    sonya "Индекс по полю customer_name не работает, когда ты используешь UPPER(customer_name). Для этого нужно создать функциональный индекс."

    diana "Стоп. Давайте на моём языке."
    diana "Это значит, что проблема не всегда в 'злой' программе, а в том, как мы её используем?"
    diana "Типа, можно криво сформулировать задание даже самому умному сотруднику, и он выдаст плохой результат?"

    sonya "Идеальная аналогия, Диана. Арсен — это наш 'умный сотрудник' (разработчик), а я — его руководитель (DBA), который проверяет, правильно ли он понял задачу и не противоречат ли его инструкции друг другу."
    
    scene Oracle slide4
    
    arsen "Ладно, признаю, погорячился с 'проклятием'."
    arsen "Получается, моя работа — не просто написать запрос, который вернет правильные данные, а написать запрос, который Oracle сможет выполнить правильно."

    sonya "Именно. Иногда для этого нужно дать ему свежие данные (статистику), иногда — подсказать явно, с помощью хинтов, например /*+ INDEX(t_cust idx_cust_name) */"
    sonya "а иногда — перестроить сами 'инструкции', то есть структуру таблиц и индексов."
    
    scene officeBackground Work with fade

    show sonyaImage at left:
        xalign 0.3
        xzoom -1
    show dianaImage at right
    show arsenImage at left:
        xzoom -1
    
    diana "Отлично. Итоговая картина мне ясна. Арсен, твоя задача — вместе с Соней проанализировать все медленные запросы и применить этот... 'метод научного тыка' к оптимизатору."
    sonya "Метод системного анализа, Диан."

    diana "Пусть будет так. Срок — до конца недели. Движемся дальше?"
    jump part3
    return

label option2:
    $ selfSufficiency += 1
    $ authority += 1
    $ choiceTwoPart = True
    sonya "А, точно, ты прав. Давай сначала закончим с работой, остальное подождет."
    scene officeBackground Work with fade
    show sonyaImage at left with moveinleft:
        xalign 0.3
        xzoom -1
    show dianaImage at right with moveinright
    show arsenImage at left with moveinleft:
        xzoom -1
    "Соня смотрит на экран с легкой улыбкой. Арсен нервно постукивает ручкой по столу. Диана проверяет время на телефоне."
    
    diana "Ну что, коллеги, давайте по существу."
    diana "Арсен, ты ведь говорил, есть критическая проблема с отчетом для финансов. Что случилось?"

    arsen "Отчёт, который прекрасно работал на тестовых данных, вчера вечером, на полной выгрузке, выполнялся три часа и упал по таймауту."
    arsen "Я уже всё перепробовал!"
    arsen "Я переписал запрос, добавил ещё индексов... ничего не помогает."
    arsen "Кажется, Oracle просто ненавидит меня лично."

    sonya "Oracle никого не ненавидит, Арсен."
    sonya "Он просто машина, которая делает ровно то, что ты ей сказал. Покажи-ка план выполнения того, что ты 'уже перепробовал'."


    scene Oracle slide1

    sonya "Ага. Я так и думала. Смотри."
    
    scene Oracle slide2
    sonya "Вот здесь, вместо ожидаемого NESTED LOOPS, оптимизатор решил сделать HASH JOIN."
    sonya "А здесь — вместо быстрого поиска по индексу (INDEX RANGE SCAN) пошел полным сканированием большой таблицы (FULL TABLE SCAN). Это и есть наша проблема."
    
    arsen "Но почему?! У меня же есть индекс по transaction_date! Я его специально вчера создал. "
    arsen "Oracle должен быть умным, почему он его не использует?"

    sonya "'Должен' — ключевое слово."
    sonya "Оптимизатор — не ясновидящий. Он принимает решение на основе статистики."
    sonya "Когда ты вчера обновил данные, статистика по таблицам устарела. Оптимизатор думает, что таблица маленькая и выгоднее её просканировать целиком, хотя на деле там миллионы строк."

    diana "Поняла не всё, но основной посыл уловила."
    diana "Получается, база данных принимает плохие решения из-за недостатка информации? Как мы это исправляем?"

    sonya "Есть несколько путей."
    sonya "Первый и самый простой — собрать свежую статистику."
    sonya "Арсен, выполни в SQL Developer: EXEC DBMS_STATS.GATHER_TABLE_STATS('SH', 'SALES'); Замени SH и SALES на нашу схему и таблицу."

    "Арсен быстро печатает на своем ноутбуке."
    scene Oracle slide3
    arsen "Понял, делаю... Готово."

    sonya "А теперь запусти свой запрос с /*+ GATHER_PLAN_STATISTICS */ и покажи новый план."

    "Арсен выполняет команду"

    arsen "Он пошел по индексу! Запрос выполнился за 12 секунд! Это магия?"

    sonya "Нет, это администрирование. Но это не всегда срабатывает. Иногда сам запрос написан так, что он ставит оптимизатор в тупик."
    sonya "Например, у тебя здесь есть функция UPPER() на индексированном поле."

    sonya "Индекс по полю customer_name не работает, когда ты используешь UPPER(customer_name). Для этого нужно создать функциональный индекс."

    diana "Стоп. Давайте на моём языке."
    diana "Это значит, что проблема не всегда в 'злой' программе, а в том, как мы её используем?"
    diana "Типа, можно криво сформулировать задание даже самому умному сотруднику, и он выдаст плохой результат?"

    sonya "Идеальная аналогия, Диана. Арсен — это наш 'умный сотрудник' (разработчик), а я — его руководитель (DBA), который проверяет, правильно ли он понял задачу и не противоречат ли его инструкции друг другу."
    
    scene Oracle slide4
    
    arsen "Ладно, признаю, погорячился с 'проклятием'."
    arsen "Получается, моя работа — не просто написать запрос, который вернет правильные данные, а написать запрос, который Oracle сможет выполнить правильно."

    sonya "Именно. Иногда для этого нужно дать ему свежие данные (статистику), иногда — подсказать явно, с помощью хинтов, например /*+ INDEX(t_cust idx_cust_name) */"
    sonya "а иногда — перестроить сами 'инструкции', то есть структуру таблиц и индексов."
    
    scene officeBackground Work with fade

    show sonyaImage at left:
        xalign 0.3
        xzoom -1
    show dianaImage at right
    show arsenImage at left:
        xzoom -1
    
    diana "Отлично. Итоговая картина мне ясна. Арсен, твоя задача — вместе с Соней проанализировать все медленные запросы и применить этот... 'метод научного тыка' к оптимизатору."
    sonya "Метод системного анализа, Диан."

    diana "Пусть будет так. Срок — до конца недели. Движемся дальше?"
    arsen "Я бы сходил взять кофе, и заодно можно дойти до Виктора."
    
    scene CoffeyShop with fade
    pause 1.0
    scene officeBackground cabinet with fade

    show dianaImage at left with moveinleft:
        xalign 0.5
        xzoom -1
    show sonyaImage at left with moveinleft:
        xalign 0.3
        xzoom -1
    show arsenImage at left with moveinleft:
        xzoom -1
    show victorImage at right with moveinright

    
    "В кабинете босса"

    sonya "Ну что, ты уже начинал что-то искать?"
    victor "Нет, я ждал вас. С чего предлагаете начать?"
    arsen "С почты конечно же! Он даже оставил ее открытой."

    scene officeBackground PC_boss with fade
    "Герои заходят в почту босса и начинают искать что-то необычное."
    "Виктор сразу предлагает искать чаты с “Омега-Холдингом”, но ничего компрометирующего они не находят, поэтому решают читать все подряд."
    
    "Спустя 20 минут…"

    diana "Как так… неужели тут ничего? Или он все удалил? Быть такого не может…"
    arsen "Погодите, а это что? o1m_h@mail.ru звучит подозрительно. Это точно не официальный адрес “Омега-Холдинга”."

    scene officeBackground PC_boss_1
    "Виктор открывает диалог, все герои внимательно изучают содержимое переписки."
    "Находят в ней какой-то файл, отправленный Сергеем Петровичем, и открывают его."
    
    scene officeBackground PC_boss_2
    diana "Это же…"
    arsen "Да, похоже на данные клиентов. Но зачем они ему?"
    victor "Это неважно, в любом случае, запрещено сохранять данные клиентов и уж тем более отправлять кому-то." 
    
    scene officeBackground PC_boss
    "Виктор закрывает файл."
    
    arsen "Ох ты ж… вы видите?"

    scene officeBackground PC_boss
    "Арсен указывает на письмо босса, в котором тот рассказывает об акциях, которые “Финанс-Капитал” планирует приобрести в больших количествах."
    
    scene officeBackground PC_boss_3
    arsen "Это разве не… как там называется… инсайдерская информация? Такое ведь нельзя передавать кому-то?"
    victor "Да, это конфиденциально. Банк еще не опубликовал эту информацию, а она уже утекла явно не туда, куда надо…"
    victor "Об этом стоит сообщить как можно скорее."

    sonya "А нам точно ничего не будет, за то что мы влезли, куда не надо?"
    
    arsen "Я думаю, будет хуже, если это так и останется в тайне. Еще окажемся виноватыми."
    
    victor "Ладно, разберемся с этим чуть позже. Я вас позову, а сейчас идите, у меня еще остались дела."
    
    scene officeBackground It with fade
    "Арсен, Соня и Диана уходят из кабинета босса."
    jump part3
    return

label option3:
    $ selfSufficiency += 1
    "Арсен лишь пожимает плечами и молча возвращается к своему рабочему месту."
    "Соня с Дианой обмениваются красноречивыми взглядами, но не настаивают."

    sonya "Ну что ж, тогда идем вдвоем. "
    scene Oracle slide1
    
    "Арсен делает вид, что погружен в работу, но время от времени украдкой поглядывает в сторону кабинета начальства."
    "Выражение лица — смесь любопытства и отстранённого высокомерия."
    
    scene Chat
    
    "Арсен сидит за своим столом, уставленно смотрит на экран."
    "Набирает сообщение в общий рабочий чат, но потом стирает его."

    scene Oracle slide1
    "Вместо этого решает структурировать мысли в служебной записке или вслух для себя, как будто готовится к отчету."

    arsen "Ладно, проблемный отчёт."
    arsen "Вчера всё летало на тестовых данных, а на полной выгрузке — три часа и таймаут. Я уже всё перепробовал!"
    arsen "Переписал запрос, добавил кучу индексов... Oracle, ну почему ты меня ненавидишь?"

    "Делает глубокий вдох, вспоминая принцип: «Oracle — не человек, это машина, которая делает то, что я ей сказал». "
    scene plan
    "Открывает план выполнения того, что «уже перепробовал» — огромную схему на экране."

    arsen "Так... смотрю на план."
    arsen "Вместо ожидаемого NESTED LLOOPS здесь — HASH JOIN."
    arsen "А здесь, вместо быстрого INDEX RANGE SCAN по transaction_date — FULL TABLE SCAN по огромной таблице."
    arsen "Значит, проблема где-то здесь."
    arsen "Но почему?! Индекс же есть! Я его вчера создал специально."

    menu:
        "Проверить статистику":
            arsen "Статистика! Конечно."
            arsen "Я же вчера загрузил в таблицу миллионы новых строк. Оптимизатор не ясновидящий, он думает, что таблица по-прежнему маленькая, и решает, что сканировать её целиком выгоднее."
            arsen "Надо обновить статистику."
        "Поменять данные":
            scene Oracle slide1
            arsen "Опять не работает!"
            scene Oracle slide2
            "Арсен чешет затылок, затем внезапно хлопает себя по лбу."
            arsen "Статистика! Конечно."
            arsen "Я же вчера загрузил в таблицу миллионы новых строк. Оптимизатор не ясновидящий, он думает, что таблица по-прежнему маленькая, и решает, что сканировать её целиком выгоднее."
            arsen "Надо обновить статистику."
    scene Oracle slide2

    arsen "Готово"

    "Запускает запрос"

    arsen "О! Сработало! Запрос выполнился за... 12 секунд! Отлично."
    
    "Арсен изучает запрос более внимательно."
    
    arsen "Хм, но здесь есть еще один потенциальный тормоз — функция UPPER() на поле customer_name."
    arsen "Индекс по обычному полю для такого условия бесполезен. Нужно будет создать функциональный индекс UPPER(customer_name). Или переписать условие..."
    arsen "Получается, моя работа — не просто написать запрос, который вернет правильные данные, а написать его так, чтобы Oracle мог его выполнить эффективно."
    
    scene plan
    "Арсен делает пометки"
    scene Oracle slide2

    arsen "Итак, план действий: первый шаг — собрать свежую статистику по всем затронутым таблицам после больших изменений данных. "
    scene Oracle slide3
    arsen "Второе — проанализировать сам запрос: нет ли там конструкций, которые «ставят оптимизатор в тупик», вроде функций над индексированными полями."
    scene Oracle slide4
    arsen "Возможно, где-то понадобятся хинты, чтобы явно указать, какой индекс использовать, или даже небольшая перестройка логики."
    scene Oracle slide5
    
    arsen "Ура, все работает!"

    "Арсен откидывается на спинку кресла с облегчением."

    scene officeBackground Work with fade

    show arsenImage at left
    
    arsen "Так, метод «научного тыка» — это не про нас. Это метод системного анализа."
    arsen "Нужно проверить по этому алгоритму все медленные запросы. Цель — разобраться до конца недели."

    "Снова наклоняется к клавиатуре, чтобы приступить к следующему запросу, уже более уверенно."
    
    scene black with dissolve
    centered "{size=36}Спустя 20 минут...{/size}" with dissolve

    scene officeBackground door with fade

    "Из приоткрытой двери кабинета босса доносятся голоса..."

    diana "Как так… неужели тут ничего? Или он все удалил?"

    sonya "Погодите, а это что?"

    victor "Это серьёзное нарушение. Конфиденциальные данные клиентов и инсайд. Об этом нужно доложить."
    
    diana "А нам точно ничего не будет? Мы же влезли в чужую почту..."

    victor "Риск есть. Но больший риск — промолчать. Ладно, идите. Я буду разбираться. Позову, когда нужно."

    "Диана и Соня выходят из кабинета. Арсен тут же отводит взгляд на монитор, делая вид, что не подслушивал."
    
    scene officeBackground Work with fade
    show arsenImage at left:
        xzoom -1
    show sonyaImage at right with moveinright:
        xpos 0.9
        xanchor 1.5
    show dianaImage at right with moveinright

    sonya "Ну что, насмотрелся? Теперь можешь спать спокойно, пока мы тут все риски на себя берём. Идём работать."

    "Герои собираются у экрана. Обстановка слегка натянутая. Арсен чувствует себя немного не в своей тарелке, но старается сохранять холодную маску безразличия."

    diana "Ну что, коллеги, давайте по существу, несмотря ни на что. Арсен, какая у тебя была проблема?"

    arsen "Уже никакая, я разобрался сам, пока вы отходили."

    sonya "Вот и славно, тогда обращайся, если появятся еще вопросы."

    arsen "Ага.."
    jump part3
    return


label part3:
    scene black with dissolve
    centered "{size=36}Глава 3 исход{/size}" with dissolve
    scene officeBackground office with fade
    "Обстановка в офисе накалена до предела. Слухи о внутреннем расследовании ходят по всем этажам."
    "Сергей Петрович, почуяв неладное, стал еще более агрессивным и непредсказуемым"
    "Люба суетится вокруг него, как оса вокруг разоренного улья."

    scene officeBackground cabinet with fade
    
    show bossImage sad at right:
        xpos 0.9
        xanchor 1.2
    show lubaImage at right

    show victorImage at left with moveinleft:
        xalign 0.3
        xzoom -1
    show operImage at left with moveinleft:
        xzoom -1 
    "В пятницу, ближе к вечеру, в отдел входит группа людей в строгой деловой одежде в сопровождении Виктора и начальника службы безопасности банка. "
    "Их лица бесстрастны. В воздухе висит тишина, густая, как смог."

    victor "Сергей Петрович. Вас просят в переговорную комнату номер один."
    victor "Сейчас. Вместе с ноутбуком и служебными ключами доступа."

    "Сергей Петрович бледнеет, но пытается сохранить браваду."
    
    boss "Что за цирк? Я занят! У меня совещание!"

    oper "Совещание, Сергей Петрович, как раз и начинается."
    oper "По фактам нарушения корпоративной политики, разглашения коммерческой тайны и возможного сговора с конкурентами."
    oper "Прошу пройти. Без комментариев."

    "Взгляд Любы мечется между боссом и пришедшими."
    "Она хочет сделать шаг вперед, чтобы что-то сказать, но Виктор останавливает ее ледяным взглядом."
    
    victor "Любовь Сергеевна, вас тоже попросят остаться. Для дачи пояснений."

    scene officeBackground doorPeregovor with fade
    "За считанные минуты Сергей Петровича и его секретаршу уводят. Дверь переговорной закрывается."
    "В офисе воцаряется гробовая тишина, которую через секунду взрывает всеобщий вздох облегчения, переходящий в гул обсуждений."
    
    scene officeBackground with fade
    show maxsImage at left with moveinleft:
        xzoom -1
    maxs "Вот это поворот. Палпатина, можно сказать, арестовали прямо при войсках. Кто попкорн заказывал?"
    
    show batrihanImage at right with moveinright
    "Батырхан, только что вернувшийся с задания, смотрит на Арсена, Соню и Диану."
    batrihan "Это твоих рук дело, новичок? Пока меня не было, тут, я смотрю, целое дело «Омега» раскопали."
    hide maxsImage
    if communication == 2 or (authority == 2 and selfSufficiency == 0) or (authority == 2 and choiceTwoPart):
        jump investigation
    else:
        jump aside
    return


label investigation:
    show arsenImage at left with moveinleft:
        xzoom -1
    "Арсен кивает Батырхану. Соня и Диана смотрят на него с одобрением"

    hide batrihanImage
    
    show victorImage at right with moveinright
    "Виктор, выйдя из переговорной, направляется прямо к их группе."
    
    victor "Всем спасибо. Ваша бдительность и собранные данные были решающими."
    victor "Расследование будет передано в компетентные органы. "
    victor "Компания «Омега-Холдинг» уже получила официальный запрос. Руководство банка в курсе."

    "Он делает паузу, смотрит на собравшихся: Арсена, Батырхана, Соню, Диану, Макса."

    victor "Я не знаю, что будет с отделом. Нового начальника назначат, наверное."
    victor "Но я знаю одно: команда, которая может не только писать код, но и мыслить системно, видеть проблемы и действовать по совести — это бесценный актив."
    victor "Мне такие люди нужны всегда и везде."
    
    "Макс переглядывается с Батырханом."
    hide arsenImage
    show maxsImage at left with moveinleft:
        xzoom -1
    maxs "Витя, ты к чему это?"

    victor "К тому, что у меня есть предложение. Не для всех, только для тех, кому интересно."
    victor "У меня есть контакты, есть понимание рынка. Есть идея создать свою небольшую, но технологичную фирму. Не банк, а fintech-лабораторию."
    victor "Чистая разработка, честные проекты, адекватные задачи. Без «Палпатинов». Мы уже доказали, что можем решать сложные проблемы — и технические, и человеческие."
    victor "Что скажете?"
    
    hide maxsImage
    "Все замирают, глядя на Арсена. Он был тем, кто сделал первый шаг, кто не побоялся. Теперь его слово значимо"

    show arsenImage at left with moveinleft:
        xzoom -1
    arsen "Я… я только начинаю. Но начинать с такими людьми, с которыми прошли через такое… Да. Я — за. Это шанс сделать все «правильно» с самого начала."
    
    hide victorImage
    "Соня улыбается. Диана одобрительно кивает. Батырхан хлопает Арсена по плечу."
    show batrihanImage at right with moveinright
    batrihan "Смотри, новичок, а уже в основатели намылился. Ладно, я с вами. Надоело, здесь стены душат."
    
    hide arsenImage
    show maxsImage at left with moveinleft:
        xzoom -1
    maxs "О, стартап! Можно к вам? Я буду отвечать за… позитивный настрой и нетривиальные решения"

    hide batrihanImage
    show victorImage at right with moveinright
    victor "Добро пожаловать. Значит, решено. С понедельника начинаем строить планы. А пока… пока давайте просто выдохнем."
    victor "Эра террора закончилась."
    
    jump epilogue_3
    return

label aside:
    "Арсен пожимает плечами в ответ на вопрос Батырхана."
    show arsenImage at left with moveinleft:
        xzoom -1
    arsen "Не совсем. Они (кивок на Соню и Диану) копали. Я был сосредоточен на работе."
    hide batrihanImage
    
    show victorImage at right with moveinright
    "В его голосе звучит легкое сожаление и отстраненность."
    "Виктор, выйдя из переговорной, благодарно смотрит на Соню и Диану, кивает Максу и Батырхану. "
    "Его взгляд скользит по Арсену без особых эмоций — просто коллега."
    victor "Спасибо тем, кто не остался равнодушным. Благодаря вашим данным ситуация прояснилась. Отдел, конечно, ждут изменения."

    scene black with dissolve
    centered "{size=36}Позже, в курилке{/size}" with dissolve

    scene street 
    show batrihanImage at right with moveinright
    show arsenImage at left with moveinleft:
        xzoom -1
    batrihan "Виктор уходит. Создает свою контору. Звал Соню, Диану, Макса… меня звал."
    batrihan "Спрашивал и про тебя. Говорит: «Парень технарь толковый, проблему с Oracle в одиночку разгромил. Но командный ли? Рисковый ли? Не уверен»."
    batrihan "Решай, новичок. Останешься здесь ждать нового Палпатина… или попробуешь что-то свое?"
    batrihan "Но если «свое» — то уже в одиночку. Доверие в команде надо зарабатывать, а не наблюдать со стороны."

    "Перед Арсеном встает трудный, но четкий выбор."
    menu: 
        "ПОЙТИ СВОИМ ПУТЕМ":
            scene roomArsen
            "Арсен спустя месяц увольняется из банка. Он берет в долг у родителей, регистрирует ИП и берет первые заказы на фрилансе."
            "Тяжело. Очень тяжело. Но он сам отвечает за каждый свой код, за каждое решение. "
            "Через два года у него маленькая, но стабильная клиентская база."
            "Иногда он видит в новостях успехи «Нейрона» — компании его бывших коллег."
            "Он чувствует легкую горечь упущенной возможности, но гордится тем, что выстоял в одиночку."
            "Его офис — его квартира. Его команда — он и его кошка."
            "Он свободен."
            jump epilogue_2
        "ПРОСИТЬ ШАНС":
            scene officeBackground cabinetVictor with dissolve
            show victorImage at right
            "Арсен набирается смелости и заходит в кабинет к Виктору в последний день его работы."
            show arsenImage at left with moveinleft:
                xzoom -1
            arsen "Виктор, я знаю, я был не на вашей стороне, когда это было важно. Я думал, что быть вне игры — это безопасно и умно."
            arsen "Но я ошибался. Я хочу учиться работать в команде. Я умею решать сложные задачи и готов пахать. Дай мне шанс доказать это."
            "Виктор долго смотрит на него, оценивая."
            
            victor "Хорошо. Но с условием."
            victor "Ты не просто разработчик. Ты будешь на подхвате, на самых разных задачах. И твоего мнения «со стороны» теперь будет недостаточно."
            victor "Придется включаться полностью. Испытательный срок — три месяца. Согласен?"

            "Арсен облегченно кивает. Это не тот стремительный старт, о котором он мечтал, но это шанс."
            "Он встает в самый конец новой команды, и ему предстоит долгий путь, чтобы догнать тех, кто уже сработался и доверяет друг другу. Но он готов начать."
            jump epilogue_1
    return

label epilogue_1:
    scene black
    show text "{size=36}АРСЕН ПРОШЕЛ ИСПЫТАТЕЛЬНЫЙ СРОК.\nЕМУ ПОТРЕБОВАЛОСЬ ЕЩЕ ПОЛГОДА, ЧТОБЫ СТАТЬ\nПОЛНОПРАВНЫМ ЧЛЕНОМ КОМАНДЫ «НЕЙРОН».\nОН НАУЧИЛСЯ НЕ ТОЛЬКО ОПТИМИЗИРОВАТЬ ЗАПРОСЫ,\nНО И ДОВЕРЯТЬ ЛЮДЯМ.\nИХ ПЕРВАЯ ОБЩАЯ ПОБЕДА СТАЛА\nИ ЕГО ЛИЧНОЙ ПОБЕДОЙ НАД СОБОЙ.{/size}" at truecenter with fade
    pause 6.0
    hide text with dissolve
    jump team_credits
    return

label epilogue_2:
    scene black
    show text "{size=36}АРСЕН СТАЛ УСПЕШНЫМ SOLO-РАЗРАБОТЧИКОМ.\nЕГО ПРИНЦИП «СНАЧАЛА РАБОТА, ПОТОМ ДРАМА»\nСТАЛ ЕГО ДЕВИЗОМ.\nОН НИКОГДА НЕ РАБОТАЕТ ПО ПЯТНИЦАМ\nИ НЕ ПЬЕТ ЭНЕРГЕТИКИ.\nОН НАУЧИЛСЯ ДОВЕРЯТЬ СЕБЕ.{/size}" at truecenter with fade
    pause 6.0
    hide text with dissolve
    jump team_credits
    return

label epilogue_3:
    scene black
    show text "{size=36}АРСЕН И ЕГО КОЛЛЕГИ ОСНОВАЛИ СТАРТАП «НЕЙРОН».\nЧЕРЕЗ ГОД ОНИ ВЫИГРАЛИ ПЕРВЫЙ КРУПНЫЙ ТЕНДЕР,\nА ИХ ПРИЛОЖЕНИЕ ДЛЯ АНАЛИЗА ФИНАНСОВЫХ РИСКОВ\nСТАЛО ОТРАСЛЕВЫМ СТАНДАРТОМ.\nОНИ ПО-ПРЕЖНЕМУ СПОРЯТ ОБ ORACLE,\nНО ТЕПЕРЬ ЭТО ДЕЛАЕТСЯ ЗА ОБЩИМ СТОЛОМ\nВ ИХ СОБСТВЕННОМ ОФИСЕ.{/size}" at truecenter with fade
    pause 6.0
    hide text with dissolve
    jump team_credits
    return

label team_credits:
    scene black
    with fade
    
    play music "audio/menu_music.ogg" fadein 2.0
    
    show text "{size=60}{font=DejaVuSans-Bold.ttf}НАД ИГРОЙ РАБОТАЛИ{/font}{/size}" at truecenter:
        ypos 0.2
        alpha 0.0
        linear 1.5 alpha 1.0
        pause 1.0
        linear 1.5 alpha 0.0
    pause 3.0
    
    show text "{size=48}{color=#ff6b6b}Бадретдинова Диана{/color}\n{size=36}{color=#4ecdc4}ТИМЛИД{/color}{/size}" at truecenter:
        ypos 0.3
        alpha 0.0
        linear 1.5 alpha 1.0
        pause 1.5
        linear 1.5 alpha 0.0 ypos -0.5
    pause 4.5
    
    show text "{size=48}{color=#ffd166}Иванова Софья{/color}\n{size=36}{color=#4ecdc4}ДИЗАЙНЕР{/color}{/size}" at truecenter:
        ypos 0.3
        alpha 0.0
        linear 1.5 alpha 1.0
        pause 1.5
        linear 1.5 alpha 0.0 ypos -0.5
    pause 4.5
    
    show text "{size=48}{color=#06d6a0}Лукьянова Диана{/color}\n{size=36}{color=#4ecdc4}СЦЕНАРИСТ{/color}{/size}" at truecenter:
        ypos 0.3
        alpha 0.0
        linear 1.5 alpha 1.0
        pause 1.5
        linear 1.5 alpha 0.0 ypos -0.5
    pause 4.5
    
    show text "{size=48}{color=#118ab2}Хайранов Арсен{/color}\n{size=36}{color=#4ecdc4}ПРОГРАММИСТ{/color}{/size}" at truecenter:
        ypos 0.3
        alpha 0.0
        linear 1.5 alpha 1.0
        pause 1.5
        linear 1.5 alpha 0.0 ypos -0.5
    pause 4.5
    
    show text "{size=48}{color=#ef476f}Архипов Никита{/color}\n{size=36}{color=#4ecdc4}АНАЛИТИК{/color}{/size}" at truecenter:
        ypos 0.3
        alpha 0.0
        linear 1.5 alpha 1.0
        pause 1.5
        linear 1.5 alpha 0.0 ypos -0.5
    pause 4.5
    
    show text "{size=72}{font=DejaVuSans-Bold.ttf}{color=#ffd700}TEAM LUBA ОПД 1 курс{/color}{/font}{/size}" at truecenter:
        alpha 0.0
        linear 2.0 alpha 1.0
        pause 3.0
        linear 2.0 alpha 0.0
    pause 5.0
    
    stop music fadeout 3.0
    
    scene black with dissolve
    pause 1.0
    
    return



screen add_authority():
    frame:
        xalign 1.0
        yalign 0.0
        background "#222c"
        xpadding 15
        ypadding 10
        vbox:
            text "+ Авторитет"

screen add_communication():
    frame:
        xalign 1.0
        yalign 0.0
        background "#222c"
        xpadding 15
        ypadding 10
        vbox:
            text "+ Коммуникабельность"

screen add_selfSufficiency():
    frame:
        xalign 1.0
        yalign 0.0
        background "#222c"
        xpadding 15
        ypadding 10
        vbox:
            text "+ Самодостаточность"
