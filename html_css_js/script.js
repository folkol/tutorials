const navList = document.querySelector('nav ul');
const headers = document.querySelectorAll('h2');

headers.forEach(header => {
    const li = document.createElement('li');
    const id = header.id;
    const text = header.innerHTML;
    li.innerHTML = `<a href="#${id}">${text}</a>`;
    navList.appendChild(li);
});
