const tickets = document.querySelectorAll('.main-ticket')
const info = document.querySelectorAll('.info')

tickets.forEach((ticket, idx) => {
    if (idx % 2 == 1) {
        ticket.classList.add('ticket1')
    } else {
        ticket.classList.add('ticket')
    }
})

// info.forEach((infoEl, idx) => {
//     if (idx % 2 == 1) {
//         infoEl.classList.add('ticket1')
//     } else {
//         infoEl.classList.add('ticket')
//     }
// })