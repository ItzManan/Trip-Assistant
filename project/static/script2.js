const to = document.querySelector('#to')
const from = document.querySelector('#from')
const btn = document.querySelector('.submit')
const loadingBox = document.querySelector('.loading-container')
const fields = document.querySelector('.fields')

let data = {}

zenscroll.setup(null, 0)

from.addEventListener('focus', () => {
    to.style.zIndex = -1
})

from.addEventListener('blur', () => {
    to.style.zIndex = 0
    to.focus()
})

btn.addEventListener('click', () => {
    loadingBox.style.zIndex = 3
    loadingBox.classList.remove('hide')
    fetch(window.location.href, {
        method: 'POST', // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        //document.body.style.overflow = visible
        loadingBox.style.opacity = 0
        setTimeout(() => loadingBox.style.display = 'none', 500)
        document.body.style.overflowY = 'visible'
        fields.style.zIndex = 0
        displayData(data)
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
        ${JSON.stringify(data)}
    `
    document.body.appendChild(bigdiv)
    /*window.scrollBy({
        top: window.innerHeight,
        behavior: 'smooth'
    })*/
    zenscroll.to(bigdiv)
}