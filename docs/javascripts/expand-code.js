document.addEventListener("DOMContentLoaded", function () {
  // Target the raw pre element blocks residing inside your content tab tracks
  const preElements = document.querySelectorAll(".md-typeset .tabbed-content .tabbed-block div.highlight > pre");

  preElements.forEach((preEl) => {
    // Read the true line length directly from text nodes
    const lineCount = preEl.textContent.split('\n').length;

    // Only apply layout truncation changes if it passes your 22-line ceiling
    if (lineCount > 22) {
      const highlightBox = preEl.parentElement;
      if (!highlightBox) return;

      // 1. Calculate exactly how many lines are hidden below the 22-line cut
      const remainingLines = lineCount - 22;

      // 2. Create a safe structural layout container box
      const wrapper = document.createElement("div");
      wrapper.className = "js-code-fade-wrapper";

      // 3. Put the wrapper in place and nest the pre tag directly within it
      preEl.parentNode.insertBefore(wrapper, preEl);
      wrapper.appendChild(preEl);

      // 4. Generate your exact pill layout tracking button
      const btn = document.createElement("button");
      btn.innerHTML = `Expand remaining ${remainingLines} lines`;
      
      // Layout structure remains hardcoded
      btn.style.display = "block";
      btn.style.margin = "20px auto 10px auto";
      btn.style.borderRadius = "20px";
      btn.style.padding = "6px 24px";
      btn.style.fontSize = "0.85rem";
      btn.style.cursor = "pointer";
      btn.style.outline = "none";
      btn.style.transition = "all 0.2s ease";

      // DYNAMIC VARIABLES FOR THE INITIAL STATE: Works on both light and dark mode backgrounds!
      btn.style.backgroundColor = "var(--md-code-bg-color)";
      btn.style.color = "var(--md-typeset-color)";
      btn.style.border = "1px solid var(--md-typeset-color)";
      btn.style.opacity = "0.6"; /* Mimics your original subtle/subdued layout style look */

      // 5. Active Hover Effect: Lights up cyan exclusively when the mouse covers it
      btn.addEventListener("mouseover", function() {
        btn.style.color = "#00bcd4";                           /* Cyan text */
        btn.style.border = "1px solid #00bcd4";                 /* Cyan border */
        btn.style.backgroundColor = "rgba(0, 188, 212, 0.08)";  /* Gentle cyan glow */
        btn.style.opacity = "1";                                /* Full brightness on hover */
      });

      // Mouse leaves button: Instantly snaps back to standard mode variables
      btn.addEventListener("mouseout", function() {
        if (!wrapper.classList.contains("is-expanded")) {
          btn.style.backgroundColor = "var(--md-code-bg-color)";
          btn.style.color = "var(--md-typeset-color)";
          btn.style.border = "1px solid var(--md-typeset-color)";
          btn.style.opacity = "0.6";
        } else {
          // Subtle look for the "Collapse" button when active
          btn.style.backgroundColor = "transparent";
          btn.style.color = "var(--md-typeset-color)";
          btn.style.border = "1px solid var(--md-typeset-color)";
          btn.style.opacity = "0.4";
        }
      });

      // Insert button right outside the master highlight container track
      highlightBox.parentNode.insertBefore(btn, highlightBox.nextSibling);

      // 6. Click event mechanics
      btn.addEventListener("click", function () {
        if (!wrapper.classList.contains("is-expanded")) {
          // EXPAND LAYOUT
          wrapper.classList.add("is-expanded");
          btn.innerHTML = "Collapse";
          btn.style.backgroundColor = "transparent";
          btn.style.color = "var(--md-typeset-color)";
          btn.style.border = "1px solid var(--md-typeset-color)";
          btn.style.opacity = "0.4";
        } else {
          // COLLAPSE LAYOUT
          wrapper.classList.remove("is-expanded");
          btn.innerHTML = `Expand remaining ${remainingLines} lines`;
          btn.style.backgroundColor = "var(--md-code-bg-color)";
          btn.style.color = "var(--md-typeset-color)";
          btn.style.border = "1px solid var(--md-typeset-color)";
          btn.style.opacity = "0.6";
          highlightBox.scrollIntoView({ behavior: "smooth", block: "nearest" });
        }
      });
    }
  });
});

