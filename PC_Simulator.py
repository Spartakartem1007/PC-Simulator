k = 0
t = 100
y = 500
u = 2000
i = 30000
o = 200000
print("Select a language/Выберите язык")
a = input('Eng=2/Рус=1:')
if a == '1':
    input('Добро пожаловать в Эпоху Рассвета.Воздух пахнет пылью от системного блока и озоном. За окном – начало нового тысячелетия, а здесь, в сети – абсолютная свобода. Ты сидишь в кресле перед огромным ЭЛТ-монитором. Это твоя капитанская рубка.Твои инструменты: мышь, клавиатура, острый ум и безграничное любопытство. Твой капитал – время и клики. Начни с малого: кликай и добывай монеты. Прокачивай свой ПК и получай еще больше монет. Цель твоя - купить новую квартиру. Удачи. Для запуска работы  нажмите Enter')
    print('Доступные покупки: 1.+128 мб. ОЗУ;2. +1 гб к памяти диска; 3. + 10 пользователей к сайту. 4. Дополнительный системный блок 5. Новая квартира. Покупка с вашего баланса происходит автоматически. Для открытия магазина пропишите команду menu. ')
    while True:
        b =input("Пополнение баланса ")
        k += 1
        print('Ваш баланс:',k)
        if b == 'menu':
           print('1. - 100 монет. + 1 за нажатие. 2. - 500 монет. + 5 к нажатию. 3. - 2000 монет. + 20 к нажатию. 4. - 30000 монет. + 100 к нажатию. 5. - 200000 монет')
        if k >= t:
            k += 2
        if k >= y:
            k += 5
        if k >= u:
            k += 20
        if k >= i:
            k += 100
        if k >= o :
            print("Спустя сутки вам пришло письмо. Поздравляем! Теперь вы живете в новой квартире! Продолжение следует...")
            break
if a == '2':
    input("Welcome to the Dawn of the Age. The air smells of dust from the system unit and ozone. Outside the window is the beginning of a new millennium, and here, on the network, there is absolute freedom. You are sitting in a chair in front of a huge CRT monitor. This is your captain's cabin. Your tools are a mouse, a keyboard, a sharp mind, and boundless curiosity. Your capital is time and clicks. Start small: click and get coins. Upgrade your PC and get even more coins. Your goal is to buy a new apartment. Good luck. Press Enter to start")
    print('Available purchases: 1. +128 MB of RAM; 2. +1 GB of disk memory; 3. +10 users for the website. 4. Additional system unit; 5. New apartment. Purchases are automatically deducted from your balance. To open the store, enter the menu command. ')
    while True:
        b = input("Adding funds to your balance ")
        k += 1
        print('Your balance:', k)
        if b == 'menu':
            print('1. - 100 coins. + 1 per click. 2. - 500 coins. + 5 per click. 3. - 2000 coins. + 20 per click. 4. - 30000 coins. + 100 per click. 5. - 200000 coins')
        if k >= t:
            k += 2
        if k >= y:
            k += 5
        if k >= u:
            k += 20
        if k >= i:
            k += 100
        if k >= o:
            print("A day later, you received an email. Congratulations! You now live in a new apartment! The story continues...")
            break
