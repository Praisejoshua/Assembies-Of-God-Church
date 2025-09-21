document.addEventListener("DOMContentLoaded", () => {
  const ham = document.querySelector(".ham");
  const nav = document.getElementById("myn");
  const header = document.querySelector("header");
  const allElements = document.body.children;

  // Hamburger toggle with blur effect
  ham.addEventListener("click", () => {
    ham.classList.toggle("active");
    nav.classList.toggle("active");

    for (let el of allElements) {
      if (el !== header) {
        el.classList.toggle("blur-all");
      } else {
        el.classList.toggle("no-blur");
      }
    }
  });

  // Close menu when clicking a link (for mobile)
  document.querySelectorAll("#myn a").forEach(link => {
    link.addEventListener("click", () => {
      ham.classList.remove("active");
      nav.classList.remove("active");

      for (let el of allElements) {
        el.classList.remove("blur-all");
        el.classList.remove("no-blur");
      }
    });
  });
});
