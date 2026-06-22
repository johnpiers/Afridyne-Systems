window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*", // Clears out the trailing pipe bug for optimal speed
    processHtmlClass: "arithmatex",
    
    // Sets your preferred user interface defaults for everyone sitewide
    menuOptions: {
      settings: {
        zoom: 'Click',     // Locks left-mouse click as the zoom trigger
        zscale: '200%'     // Maintains your current zoom scale
      }
    }
  }
};

// CRITICAL FOR MATERIALX / MKDOCS: Handles fast dynamic page switching
document$.subscribe(() => { 
  MathJax.startup.output.clearCache()
  MathJax.typesetClear()
  MathJax.texReset()
  MathJax.typesetPromise()
})






