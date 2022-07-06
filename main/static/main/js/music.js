const audioCard = document.querySelectorAll('.track-card');
const audioSrc = document.querySelectorAll('.play-track');

const music = new Audio();

let masterPlay = document.getElementById('play');
let player = document.getElementById('player')

if (audioSrc.length == 0){
    player.hidden = true
} else {
    player.hidden = false
}

masterPlay.addEventListener("click", () => {
    if (music.paused || music.currentTime <= 0) {
        music.play();
        masterPlay.classList.remove('bi-play-circle');
        masterPlay.classList.add('bi-pause-circle');
    }
    else {
        music.pause();
        masterPlay.classList.add('bi-play-circle');
        masterPlay.classList.remove('bi-pause-circle');
    }
})

const makeAllPlays = () => {
    Array.from(document.getElementsByClassName('playlistTrack')).forEach((element)=>{
        element.classList.add('bi-play-circle-fill');
        element.classList.remove('bi-pause-circle-fill');
    })
}


let index = 0;
let img = document.getElementById('img-item');
let title = document.getElementById('title');
let subtitle = document.getElementById('subtitle');

Array.from(document.getElementsByClassName('playlistTrack')).forEach((element)=>{
    element.addEventListener('click', (e)=>{
        index = e.target.id;
        makeAllPlays();
        e.target.classList.remove('bi-play-circle-fill');
        e.target.classList.add('bi-pause-circle-fill');
        music.src = audioSrc[index].dataset.key;
        img.src = audioCard[index].childNodes[3].src;
        music.play();
        title.innerText = audioCard[index].childNodes[5].childNodes[1].textContent;
        subtitle.innerText = audioCard[index].childNodes[5].childNodes[3].textContent;
        masterPlay.classList.remove('bi-play-circle');
        masterPlay.classList.add('bi-pause-circle');
        music.addEventListener('ended', ()=>{
            masterPlay.classList.add('bi-play-circle');
            masterPlay.classList.remove('bi-pause-circle');
        })

    })
})

let currentStart = document.getElementById('CurrentStart')
let currentEnd = document.getElementById('CurrentEnd')
let seek = document.getElementById('seek')
let bar2 = document.getElementById('bar2')
let dot = document.getElementsByClassName('dot-bar')[0]

music.addEventListener('timeupdate', ()=>{
    let music_curr = music.currentTime;
    let music_dur = music.duration;

    let min = Math.floor(music_dur/60);
    let sec = Math.floor(music_dur%60);
    if(sec < 10) {
        sec = `0${sec}`
    }
    currentEnd.innerText = `${min}:${sec}`;

    let min1 = Math.floor(music_curr/60);
    let sec1 = Math.floor(music_curr%60);
    if(sec1 < 10) {
        sec1 = `0${sec1}`
    }
    currentStart.innerText = `${min1}:${sec1}`;

    let progressbar = parseInt((music.currentTime/music.duration)*100);
    seek.value = progressbar;
    let seekbar = seek.value;
    bar2.style.width = `${seekbar}%`;
    dot.style.left = `${seekbar}%`;
})

seek.addEventListener('change', ()=>{
    music.currentTime = seek.value * music.duration/100;
})

music.addEventListener('ended', ()=>{
    masterPlay.classList.remove('bi-play-circle');
    masterPlay.classList.add('bi-pause-circle');
})

let vol_icon = document.getElementById('vol-icon')
let vol = document.getElementById('vol')
let vol_dot = document.getElementById('vol-dot')
let vol_bar = document.getElementsByClassName('vol-bar')[0]

vol.addEventListener('change', ()=>{
    if (vol.value == 0) {
        vol_icon.classList.remove('bi-volume-down-fill');
        vol_icon.classList.add('bi-volume-mute-fill');
        vol_icon.classList.remove('bi-volume-up-fill');
    }
    if (vol.value > 0) {
        vol_icon.classList.add('bi-volume-down-fill');
        vol_icon.classList.remove('bi-volume-mute-fill');
        vol_icon.classList.remove('bi-volume-up-fill');
    }
    if (vol.value > 50) {
        vol_icon.classList.remove('bi-volume-down-fill');
        vol_icon.classList.remove('bi-volume-mute-fill');
        vol_icon.classList.add('bi-volume-up-fill');
    }

    let vol_a = vol.value;
    vol_bar.style.width = `${vol_a}%`;
    vol_dot.style.left = `${vol_a}%`;
    music.volume = vol_a/100;
})

let back = document.getElementById('prev');
let next = document.getElementById('next');

back.addEventListener('click', ()=>{
    index -= 1;
    if (index < 0) {
        index = Array.from(document.getElementsByClassName('track')).length - 1;
    }
    music.src = audioSrc[index].dataset.key;
    img.src = audioCard[index].childNodes[3].src;
    music.play();
    title.innerText = audioCard[index].childNodes[5].childNodes[1].textContent;
    subtitle.innerText = audioCard[index].childNodes[5].childNodes[3].textContent;
    makeAllPlays();
    document.getElementById(`${index}`).classList.remove('bi-play-circle-fill');
    document.getElementById(`${index}`).classList.add('bi-pause-circle-fill');
})


next.addEventListener('click', () => {
    index -= 0;
    index += 1;
    if (index > Array.from(document.getElementsByClassName('track')).length - 1) {
        index = 0
    }
    music.src = audioSrc[index].dataset.key;
    img.src = audioCard[index].childNodes[3].src;
    music.play();
    title.innerText = audioCard[index].childNodes[5].childNodes[1].textContent;
    subtitle.innerText = audioCard[index].childNodes[5].childNodes[3].textContent;
    makeAllPlays();
    document.getElementById(`${index}`).classList.remove('bi-play-circle-fill');
    document.getElementById(`${index}`).classList.add('bi-pause-circle-fill');
})
