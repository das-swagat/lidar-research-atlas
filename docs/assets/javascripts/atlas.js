document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("table").forEach((table) => {
    table.setAttribute("data-atlas-table", "true");
  });
});
