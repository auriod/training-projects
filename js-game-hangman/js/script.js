var counterImages = ['c1.png', 'c2.png', 'c3.png', 'c4.png', 'c5.png', 'c6.png', 'c7.png', 'c8.png', 'c9.png', 'c10.png'];
var counterGame = 0;

var words = ["булка","топка", "фазан", "забор", "мусор","демка", "сопло"];
var ind = Math.floor(Math.random() * words.length);
var word = words[ind];
var wordLength = word.length;

var startDiv = document.getElementById('start-game-div')
var buttonStart = document.getElementById('game-start-button');
buttonStart.addEventListener('click', startGame);

// создание контейнера с игрой
var parentElem = document.body;
var gameContainer = document.createElement('div');
gameContainer.className = 'game-container';
gameContainer.style.display = 'none';
parentElem.appendChild(gameContainer);

// контейнер с блоками букв
var wordsContainer = document.createElement('div');
wordsContainer.className = 'div-words';
gameContainer.appendChild(wordsContainer);

for (var i = 0; i < wordLength; i++){
	wordsContainer.innerHTML += '<div class="my-char">' + word[i] + "</div>";
}

// изображение-счетчик
var imageCounter = document.createElement('img');
imageCounter.className = 'img-counter';
imageCounter.src = 'img/' + counterImages[counterGame];
wordsContainer.appendChild(imageCounter);


var counterDiv = document.createElement('div');
counterDiv.className = 'div-counter';
counterDiv.innerHTML += counterGame + '/' + wordLength;
wordsContainer.appendChild(counterDiv);

var messegeDiv = document.createElement('div');
messegeDiv.className = 'div-messege';
gameContainer.appendChild(messegeDiv);

// блок ввода букв 
var inputDiv = document.createElement('div');
inputDiv.className = 'div-input';
gameContainer.appendChild(inputDiv);

inputDiv.innerHTML += '<label for="input-char">Ваша буква: </label>';
var inputChar = document.createElement('input');
inputChar.className = 'input-char';
inputChar.id = 'input-char';
inputChar.type = 'text';
inputChar.onkeypress = handler2;
inputChar.onclick = clearMessege;
inputDiv.appendChild(inputChar);

var divs = document.getElementsByClassName('my-char'); 


function startGame () {
	startDiv.style.display = 'none';
	gameContainer.style.display = 'block';	
}

function testCode(e){
	if (e.keyCode == 13) {
		alert(e.keyCode + ' ' + inputChar.value + ' ' + inputChar.value.length);
	}
	
}

function clearMessege() {
	messegeDiv.innerHTML = '';
}

// массив с введенными буквами
var charChoise = [];
// счетчик букв
var counterChar = 0;

function handler2(e) {
	var ch = inputChar.value;	
	if (e.keyCode == 13) {
		if (ch.length != 1){
			messegeDiv.innerHTML = 'Многовато букав!!';
		} else if (charChoise.includes(ch)) {
				messegeDiv.innerHTML = 'Повторяетесь, сударь.';
			} else if (Number(ch) === 1) {
				messegeDiv.innerHTML = 'Буквы! И ничего, кроме них.';
			} else {
				charChoise.push(ch);

				if (word.includes(ch)) {
					messegeDiv.innerHTML = 'Таки да!';
					for (var i = 0; i < divs.length; i++){
						if (ch == word[i]) {
							divs[i].style.color = 'black';
							counterChar++;
							counterDiv.innerHTML = counterChar + '/' + wordLength;
						}
					if(wordLength == counterChar) showViner();
				}
			
				} else {
					messegeDiv.innerHTML = 'А вот и не угадал!';
					counterGame++;
					imageCounter.src = 'img/' + counterImages[counterGame];
					if(counterGame == 9) showLoss();
				}	
			}	
	}
}

function showViner() {
		gameContainer.style.display = 'none';
		document.getElementById('viner').style.display = 'block';
	}

function showLoss() {
		gameContainer.style.display = 'none';
		document.getElementById('loss').style.display = 'block';
	}