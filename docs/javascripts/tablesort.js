document$.subscribe(function() {
  var tables = document.querySelectorAll("article table:not([class])")
  tables.forEach(function(table) {
    if (table.closest(".no-sort")) return
    var body = table.tBodies[0]
    var original = body ? Array.prototype.slice.call(body.rows) : []
    new Tablesort(table)
    // Third click on the same header restores the original row order
    table.addEventListener("click", function(e) {
      var th = e.target.closest("th")
      if (!th || !table.contains(th) || th.getAttribute("aria-sort") !== "descending") return
      e.stopPropagation()
      th.removeAttribute("aria-sort")
      original.forEach(function(row) { body.appendChild(row) })
    }, true)
  })
})

