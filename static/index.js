const themeBtn = document.getElementById("themeBtn");
const root = document.documentElement;

const savedTheme = localStorage.getItem("theme") || "dark";
root.setAttribute("data-theme", savedTheme);

themeBtn.addEventListener("click", () => {
  const current = root.getAttribute("data-theme");
  const next = current === "dark" ? "light" : "dark";
  root.setAttribute("data-theme", next);
  localStorage.setItem("theme", next);
});

document.getElementById("year").textContent = new Date().getFullYear();
