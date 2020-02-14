// словарь вопросов
var level = [{ // Level 0
	text: 'С помощью чего пассажиры попадают в самолет?',
	a: 'A. Рукава',
	b: 'B. Манжета',
	c: 'C. Трапа',
	d: 'D. Билета',
	win: 'D. Билета'
	},  // Level 1
	{
	text: 'В каком году началась Вторая Мировая война',
	a: 'A. 1941',
	b: 'B. 756',
	c: 'C. 1939',
	d: 'D. 1939 до н.э.',
	win: 'C. 1939'
	},
	{  // Level 2
	text: 'Какая бывает лопата?',
	a: 'A. совковая',
	b: 'B. граблевая',
	c: 'C. нормальная',
	d: 'D. мотыжная',
	win: 'A. совковая'
	},
	{ // Level 3
	text: 'Что меняет хозяйка, работающая с кухонным комбайном?',
	a: 'A. мировой порядок',
	b: 'B. насадки с ножами',
	c: 'C. напряжение в сети',
	d: 'D. количество пальцев',
	win: 'B. насадки с ножами'
	},  // Level 4
	{
	text: 'Какого героя нет в фильме "Джентельмены удачи"',
	a: 'A. Хмыря',
	b: 'B. Доцента',
	c: 'C. Косого',
	d: 'D. Доктора',
	win: 'D. Доктора'
	},
	{  // Level 5
	text: 'Как зовут поросёнка, героя популярного мультфильма?',
	a: 'A. Фунтик',
	b: 'B. Наф',
	c: 'C. Нуф',
	d: 'D. Ниф',
	win: 'A. Фунтик'
	},
	{  // Level 6
	text: 'Что вместо валенок купил пёс Шарик в мультфильме о Простоквашино?',
	a: 'A. Фигвам',
	b: 'B. Корову',
	c: 'C. Кеды',
	d: 'D. Валерьянку',
	win: 'C. Кеды'
	}

];

var levelGame = 0;  // уровень игры
var timerID = undefined;  // переменная setInterval - отображение счетчика времени
var timeOver = undefined; // переменная setTimeout - ограничение времени ответа
var secondChance = false;  	// активность "Второго шанса". False - не активно, True - активно
							// "Второй шанс" позволяет ошибиться, и не проиграть. 
							// Появляется на 3 и 5 уровне
// запуск игры при нажатии на кнопку .start
$('.start').click(function () {
	$(this).hide();
	$('.game_container').show();
	game()
});

// при нажатии на кнопку .second
$('.second').click(function () {
	// активируеться "Второй шанс"
	window.secondChance = true;
	// кнопка пропадает
	$('.second').hide();
});

// функция которая отображает в элементе .timer отсчет времени
function timer() {
	$('timer').html('01:00');
	var counter = 60;
	window.timerID = setInterval(function () {
		$('.timer').html('00:' + --counter);
		if (counter == 10) $('.timer').css('color', 'red')
		if (counter == 0) clearInterval(timerID);
	}, 1000);
}

function game(){
		$('#messege').html('');
		// включается обработчик для всех .ansver
		$('.ansver').on("click", isWinner);
		// удаление все классов, кроме .ansver
		$('.ansver').removeClass('ansver_win ansver_choice ansver_loss');
		// Заполнение конейнеров вопросом и вариантами ответа, соответствующего уровня
		$('.question').html(level[levelGame].text);
		$('#a').html(level[levelGame].a);
		$('#b').html(level[levelGame].b);
		$('#c').html(level[levelGame].c);
		$('#d').html(level[levelGame].d);
		// на уровне 3 и 5 появляется "Второй шанс"
		if (levelGame == 2 || levelGame == 4) $('.second').show();
		timer();
		// если в течении 60 секунт не активированн ни один ответ - проигрыш
		window.timeOver = setTimeout(timeLosses, 60000);
	
}

// проигрыш по истечению времени
function timeLosses() {
	$('#messege').html('Время вышло!');
	// отключается обработчик для всех .ansver
	$('.ansver').off("click");
	// .game_container скрываеться
	$('.game_container').hide();
	// отображаеться сообщение о проигрыше .losses
	$('.losses').show()
}

// функция проверки выбранного ответа
function isWinner() {
	// отключаются таймеры
	clearInterval(window.timerID);
	clearTimeout(window.timeOver);
	// отключается обработчик для всех .ansver
	$('.ansver').off("click");
	// выбранному элементу добавляется класс ansver_choice
	$(this).addClass('ansver_choice');
	// переменная choise содержит выбранный элемент .ansver
	let choise = $(this);
	setTimeout(function () {
		if (choise.text() == level[levelGame].win) {  
			// правильный выриант
			levelGame++; // увеличивается уровень
			$('#messege').html('Правильно!!'); // сообщение о правильном выборе
			choise.addClass('ansver_win'); // добавляеться класс ansver_win
			// следующий уровень 
			setTimeout(function () {
				if (levelGame <= 6) {
					levelApp(); // меняються маркеры суммы выйграша
					game(); 
				} else { // максимальный уровень - победа
					$('.game_container').hide(); // .game_container скрываеться
					$('.winner').show(); // сообщение о победе
				}
			}, 2000);
		} else if (window.secondChance) {
			// ответ не верный, но активный "Второй шанс"
			window.secondChance = false; // деактивация "Второй шанс"
			choise.addClass('ansver_loss'); // добавляеться класс ansver_loss
			// демонстрация правильного ответа
			$('.ansver').filter(function () {
				return $(this).text() == level[levelGame].win;
			}).addClass('ansver_win'); // добавляеться класс ansver_win
			$('#messege').html('Не правильно! Но Вам дан второй шанс');
			levelGame++;
			setTimeout(function () {
				if (levelGame <= 6) {
					levelApp();
					game();
				} else {
					$('.game_container').hide(); // .game_container скрываеться
					$('.winner').show(); // отображаеться сообщение о победе .winner
				}
			}, 2000);
		} else { // ответ не верный и не активный "Второй шанс"
			choise.addClass('ansver_loss'); // добавляеться класс ansver_loss
			// демонстрация правильного ответа
			$('.ansver').filter(function () {
				return $(this).text() == level[levelGame].win;
			}).addClass('ansver_win');
			$('#messege').html('Не правильно!!');
			setTimeout(function () {
				$('.game_container').hide();// .game_container скрываеться
				$('.losses').show()// отображаеться сообщение о проигрыше .losses
			}, 2000)
		}
	}, 1000)
}

function levelApp(){
	// к элементу, который был активным, добавляется класс level_win 
  	$('.level_active').addClass('level_win');
  	// к последнему элементу из списка элементов с классом .level_gane 
  	//, добавляется класс level_win
  	$('.level_gane').get(-1).className = 'level_active';
}




