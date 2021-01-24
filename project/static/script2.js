const to = document.querySelector('#to')
const from = document.querySelector('#from')
const btn = document.querySelector('.submit')
const loadingBox = document.querySelector('.loading-container')
const fields = document.querySelector('.fields')
const dep = document.getElementById('dep')
const arr = document.getElementById('arr')
const tripContainer = document.querySelector('.trip-container')
const error = document.querySelector('.error')

tripContainer.style.backgroundImage = `url('static/bgs/${Math.ceil(Math.random()*9)}.jpg')`

let data = {}

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


    if (!('origin' in data && 'destination' in data)) {
        alert('Please enter the locations using the dropdown box.')
    } else if (!('depDate' in data && 'arrDate' in data)) {
        alert('Please enter valid dates.')
    } else if (Date.parse(data.depDate) > Date.parse(data.arrDate)) {
        alert('Return Date should be later than the departure date')
    } else {
        loadingBox.classList.remove('hide')
        loadingBox.style.zIndex = 3
        error.style.top = '-100%'
        console.log(data)
        tripContainer.style.filter = 'blur(5px)'
        btn.disabled = true
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
            if (data == 'ERROR') {
                fields.style.zIndex = 0
                error.style.top = 0
                loadingBox.classList.add('hide')
                tripContainer.style.filter = 'blur(0px)'
                btn.disabled = false
            } else {
                console.log(data)
                console.log(window.location.href)
                btn.disabled = false
                window.location = window.location.href+'trip'
                /*document.body.style.overflowY = 'visible'
                console.log('HELLO')
                console.log(data)
                displayData(data)*/
            }
         
        })
    }
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
    data.countryCode = e.suggestion.countryCode
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
