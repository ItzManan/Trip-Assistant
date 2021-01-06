var origin = document.getElementById('origin')
var destination = document.getElementById('destination')

console.log("MAI HU YAHA PE!")
var placesAutocomplete1 = places({
    appId: 'plUM8RE4VBHN',
    apiKey: '7406d0106ec36b896f3a32cb314c2921',
    container: document.querySelector('#input-map1')
})
placesAutocomplete1.on('change', (e) => origin.value = `${e.suggestion.latlng.lat}, ${e.suggestion.latlng.lng}`)

var placesAutocomplete2 = places({
    appId: 'plUM8RE4VBHN',
    apiKey: '7406d0106ec36b896f3a32cb314c2921',
    container: document.querySelector('#input-map2')
})
placesAutocomplete2.on('change', (e) => destination.value = `${e.suggestion.latlng.lat}, ${e.suggestion.latlng.lng}`)