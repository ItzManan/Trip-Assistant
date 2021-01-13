const to = document.querySelector('#to')
const from = document.querySelector('#from')
const btn = document.querySelector('.submit')
const loadingBox = document.querySelector('.loading-container')
const fields = document.querySelector('.fields')
const dep = document.getElementById('dep')
const arr = document.getElementById('arr')
const tripContainer = document.querySelector('.trip-container')

console.log(`url('./bgs/${Math.ceil(Math.random()*9)}.jpg')`)

tripContainer.style.backgroundImage = `url('static/bgs/${Math.ceil(Math.random()*9)}.jpg')`

let data = {}

zenscroll.setup(null, 0)

from.addEventListener('focus', () => {
    to.style.zIndex = -1
})

from.addEventListener('blur', () => {
    to.style.zIndex = 0
    to.focus()
})

dep.onchange = function() {
    data.depDate = this.value
    dep.classList.remove('active')
    dep.classList.add('show')
}

arr.onchange = function() {
    data.arrDate = this.value
    arr.classList.remove('active')
    arr.classList.add('show')
}

btn.addEventListener('click', () => {
    loadingBox.classList.remove('hide')
    loadingBox.style.zIndex = 3

    console.log(data)
    
    fetch(window.location.href, {
        method: 'POST', // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        console.log(window.location.href)
        window.location = window.location.href+'trip'
        /*document.body.style.overflowY = 'visible'
        fields.style.zIndex = 0
        loadingBox.classList.add('hide')
        console.log('HELLO')
        console.log(data)
        displayData(data)*/
    })
})

var fromPlaces = places({
    appId: 'plUM8RE4VBHN',
    apiKey: '7406d0106ec36b896f3a32cb314c2921',
    container: from,
    style: false,
})

var toPlaces = places({
    appId: 'plUM8RE4VBHN',
    apiKey: '7406d0106ec36b896f3a32cb314c2921',
    container: to,
    style: false,
})

fromPlaces.on('change', (e) => {
    data.origin_city = e.suggestion.name
    data.origin = e.suggestion.latlng.lat + ', ' + e.suggestion.latlng.lng
    console.log(data)
})

toPlaces.on('change', (e) => {
    data.destination_city = e.suggestion.name
    data.destination = e.suggestion.latlng.lat + ', ' + e.suggestion.latlng.lng
    console.log(data)
})

function displayData(data) {
    bigdiv = document.createElement('div')
    bigdiv.classList.add('ok')
    bigdiv.style.overflowX = 'hidden'
    bigdiv.style.background = 'black'
    bigdiv.style.color = 'white'
    bigdiv.innerHTML = `<center>EPIC ULTRA PRO MAX DATA!!!!!!</center>
        <br>
        ${JSON.stringify(data[0])}
        <br>
        ${JSON.stringify(data[1])}
    `
    document.body.appendChild(bigdiv)
    /*window.scrollBy({
        top: window.innerHeight,
        behavior: 'smooth'
    })*/
    zenscroll.to(bigdiv)
}
