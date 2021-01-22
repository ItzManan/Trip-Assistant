const tickets = document.querySelectorAll('.main-ticket')
const info = document.querySelectorAll('.info')
const prices = document.querySelectorAll('.price')


fx.base = 'USD'
fx.rates = {
    "EUR": 0.82,
    "USD": 1,
    "INR": 73.08,
}

prices.forEach(price => {
    price.addEventListener('click', () => {
        priceValue = price.innerHTML.slice(7, -3)
        currency = price.innerHTML.slice(-3)
        switch(currency) {
            case 'EUR':
                price.innerHTML = `Price: ${fx(priceValue).from(currency).to('USD').toFixed(2).toLocaleString()}USD`
                break
            case 'USD':
                price.innerHTML = `Price: ${fx(priceValue).from(currency).to('INR').toFixed(2)}INR`
                break
            case 'INR':
                price.innerHTML = `Price: ${fx(priceValue).from(currency).to('EUR').toFixed(2)}EUR`
                break
            default:
                break
        }
    })
})

tickets.forEach((ticket, idx) => {
    if (idx % 2 == 1) {
        ticket.classList.add('ticket1')
    } else {
        ticket.classList.add('ticket')
    }
})

<<<<<<< Updated upstream
=======
info.forEach((infoEl, idx) => {
    if (idx % 2 == 1) {
        infoEl.classList.add('ticket1')
    } else {
        infoEl.classList.add('ticket')
    }
})
>>>>>>> Stashed changes

