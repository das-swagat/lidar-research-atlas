document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("table").forEach((table) => table.setAttribute("data-atlas-table", "true"));

  document.querySelectorAll("[data-atlas-filter]").forEach((input) => {
    const target = document.getElementById(input.dataset.atlasFilter);
    if (!target) return;
    const table = target.querySelector("table");
    if (!table) return;
    const rows = [...table.querySelectorAll("tbody tr")];
    const counter = document.createElement("span");
    counter.className = "atlas-filter-count";
    input.parentElement.appendChild(counter);

    const apply = () => {
      const query = input.value.trim().toLowerCase();
      let visible = 0;
      rows.forEach((row) => {
        const show = !query || row.textContent.toLowerCase().includes(query);
        row.hidden = !show;
        if (show) visible += 1;
      });
      counter.textContent = `${visible} of ${rows.length} shown`;
    };
    input.addEventListener("input", apply);
    apply();
  });
});
