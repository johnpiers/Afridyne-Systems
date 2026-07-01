window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true,
    packages: {'[+]': ['color']}
  },
  loader: {
    load: ['[tex]/color']
  },
  options: {
    ignoreHtmlClass: ".*",
    processHtmlClass: "arithmatex",
    menuOptions: {
      settings: {
        zoom: 'Click',
        zscale: '200%'
      }
    }
  }
};

document$.subscribe(() => { 
  MathJax.startup.output.clearCache()
  MathJax.typesetClear()
  MathJax.texReset()
  MathJax.typesetPromise()
})






