const to = document.querySelector('#to')
const from = document.querySelector('#from')
const btn = document.querySelector('.submit')
const loadingBox = document.querySelector('.loading-container')
const fields = document.querySelector('.fields')
const dep = document.getElementById('dep')
const arr = document.getElementById('arr')

/*const bgs = {'1': ['https://images.unsplash.com/photo-1537346439163-eafb59bdc400?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=968&q=80', 'https://images.unsplash.com/photo-1537346439163-eafb59bdc400?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=968&q=80', 'https://images.unsplash.com/photo-1537346439163-eafb59bdc400?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=968&q=80'], 
2: ['https://images.unsplash.com/photo-1539511977266-f0b884a7ee39?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTV8fHxlbnwwfHx8&auto=format&fit=crop&w=500&q=60']}*/

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
        document.body.style.overflowY = 'visible'
        fields.style.zIndex = 0
        loadingBox.classList.add('hide')
        console.log(data)
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
        ${JSON.stringify(data[0])}
        <br>
        ${JSON.stringify(data[1])}
        `
}