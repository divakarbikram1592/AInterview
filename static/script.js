function setFontSize(size) {
  document.querySelector('.content').style.fontSize = size + 'px';
  console.log("current size: ", size);
}

function increaseFontSize() {
  const content = document.querySelector('.content');
  const style = window.getComputedStyle(content, null).getPropertyValue('font-size');
  const currentSize = parseFloat(style);
  setFontSize(currentSize + 1);
  console.log("increaseFontSize: ", currentSize);
}

function decreaseFontSize() {
  const content = document.querySelector('.content');
  const style = window.getComputedStyle(content, null).getPropertyValue('font-size');
  const currentSize = parseFloat(style);
  setFontSize(currentSize - 1);
  console.log("decreaseFontSize: ", currentSize);
}

let isNightMode = false;

function toggleNightMode() {
  const reader = document.querySelector('.reader');
  const buttons = document.querySelectorAll('button');
  if (isNightMode) {
    reader.classList.remove('night');
    buttons.forEach(button => button.classList.remove('night'));
    isNightMode = false;
  } else {
    reader.classList.add('night');
    buttons.forEach(button => button.classList.add('night'));
    isNightMode = true;
  }
}

function changeTheme(theme) {
  const reader = document.querySelector('.reader');
  reader.className = 'reader ' + theme; // Resets and applies new theme class
}

function changeFont(fontType) {
  const reader = document.querySelector('.reader');
  reader.className = 'reader ' + fontType; // Resets and applies new font class
}

// TEXT-TO-SPEECH
if (!('speechSynthesis' in window)) {
  alert('Your browser does not support text-to-speech functionality.');
}
const synth = window.speechSynthesis;

function speakText() {
  const text = document.querySelector('.content').textContent; // Adjust selector as needed
  if (synth.speaking) {
    console.error('Speech synthesis is already in progress.');
    return;
  }
  if (text !== '') {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.onend = function(event) {
      console.log('Speech synthesis finished.');
    };
    utterance.onerror = function(event) {
      console.error('Speech synthesis error:', event);
    };
    synth.speak(utterance);
  }
}

function stopSpeaking() {
  if (synth.speaking) {
    synth.cancel();
  }
}

function setVoiceSettings(voice, rate, pitch) {
  const utterance = new SpeechSynthesisUtterance(document.querySelector('.content').textContent);
  utterance.voice = synth.getVoices().find(v => v.name === voice);
  utterance.rate = rate; // Normal rate is 1
  utterance.pitch = pitch; // Normal pitch is 1
  synth.speak(utterance);
}

window.speechSynthesis.onvoiceschanged = function() {
  const voices = window.speechSynthesis.getVoices();
  console.log(voices); // You can use this to populate voice options in your UI
};

function populateVoiceList() {
  if(typeof speechSynthesis === 'undefined') {
    return;
  }

  var voices = speechSynthesis.getVoices();
  var voiceSelect = document.getElementById('voiceSelection');

  voices.forEach((voice, index) => {
    var option = document.createElement('option');
    option.textContent = voice.name + ' (' + voice.lang + ')';

    if (voice.default) {
      option.textContent += ' -- DEFAULT';
    }

    option.setAttribute('data-lang', voice.lang);
    option.setAttribute('data-name', voice.name);
    voiceSelect.appendChild(option);
  });
}

window.speechSynthesis.onvoiceschanged = populateVoiceList;


function updateVoice() {
  var voiceSelect = document.getElementById('voiceSelection');
  var selectedOption = voiceSelect.selectedOptions[0];
  var selectedVoice = speechSynthesis.getVoices().find(voice => voice.name === selectedOption.getAttribute('data-name'));

  speakText(selectedVoice); // Update the speakText function to accept a voice parameter
}

function speakText(selectedVoice) {
  var utterance = new SpeechSynthesisUtterance(document.querySelector('.content').textContent);
  utterance.voice = selectedVoice;

  speechSynthesis.cancel(); // Cancel any ongoing speech
  speechSynthesis.speak(utterance);
}

function populateLanguageList() {
  if (typeof speechSynthesis === 'undefined') {
    return;
  }

  var voices = speechSynthesis.getVoices();
  var languageSet = new Set(voices.map(voice => voice.lang));
  var languageSelect = document.getElementById('languageSelection');

  languageSet.forEach(lang => {
    var option = document.createElement('option');
    option.textContent = lang;
    option.value = lang;
    languageSelect.appendChild(option);
  });
}


function filterVoicesByLanguage() {
  // var selectedLanguage = document.getElementById('languageSelection').value;
  var selectedLanguage = "hi-IN"
  var voices = speechSynthesis.getVoices();
  var voiceSelect = document.getElementById('voiceSelection');

  voiceSelect.innerHTML = ''; // Clear existing options

  voices.forEach(voice => {
    if (voice.lang === selectedLanguage) {
      var option = document.createElement('option');
      option.textContent = voice.name + ' (' + voice.lang + ')';
      option.setAttribute('data-name', voice.name);
      voiceSelect.appendChild(option);
    }
  });
}

window.speechSynthesis.onvoiceschanged = function() {
  populateLanguageList();
  populateVoiceList();
};


// Initialize with a default font size
setFontSize(18);
