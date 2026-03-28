extra_javascript:
  - some_plain_javascript.js       # <script src="some_plain_javascript.js"></script>
        # New behavior in MkDocs 1.5:
  - implicitly_as_module.mjs       # <script src="implicitly_as_module.mjs" type="module"></script>
        # Config keys only supported since MkDocs 1.5:
  - path: explicitly_as_module.mjs # <script src="explicitly_as_module.mjs" type="module"></script>
    type: module
  - path: deferred_plain.js        # <script src="deferred_plain.js" defer></script>
    defer: true
  - path: scripts/async_module.mjs # <script src="scripts/async_module.mjs" type="module" async></script>
    type: module
    async: true
