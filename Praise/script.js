const navItems = document.querySelectorAll('.navItem');
const dropdowns = document.querySelectorAll('.dropdown');

navItems.forEach((navItem, i) => {
  const navText = navItem
  const dropdown = dropdowns[i];

  navItem.addEventListener('mouseenter', () => {
    navText.style.color = '#ffffff';
    dropdown.classList.add('show');
  });

  navItem.addEventListener('mouseleave', () => {
    navText.style.color = '#9f9f9f';
    dropdown.classList.remove('show');
  });

  dropdown.addEventListener('mouseenter', () => {
    navText.style.color = '#ffffff';
    dropdown.classList.add('show');
  });

  dropdown.addEventListener('mouseleave', () => {
    navText.style.color = '#9f9f9f';
    dropdown.classList.remove('show');
  });
});

document.getElementsByClassName("ham")[0].addEventListener("click", function() {
  document.getElementsByClassName("ham")[0].classList.toggle('active')
  document.getElementById('myn').classList.toggle('active')
  const header = document.querySelector('header');
  const allElements = document.body.children;

  for (let el of allElements) {
    if (el !== header) {
      el.classList.toggle('blur-all');
    } else {
      el.classList.toggle('no-blur');
    }
  }
});
