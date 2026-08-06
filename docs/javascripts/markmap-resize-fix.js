// Markmap sometimes measures its container's size before admonitions (and
// other elements with their own layout/padding) have finished settling,
// resulting in a transform of "translate(NaN,NaN)" and a blank diagram.
//
// markmap-view recalculates its layout on the browser's "resize" event, so
// firing one manually shortly after load nudges it to redo that math once
// the real page layout has settled.
window.addEventListener("load", function () {
  setTimeout(function () {
    window.dispatchEvent(new Event("resize"));
  }, 1200);
});
