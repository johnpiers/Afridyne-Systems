(function initializeMarkmap() {
    const transformer = new markmap.Transformer();
    const preloadScripts = transformer.plugins
        .flatMap((plugin) => plugin.config?.preloadScripts || [])
        .map((item) => transformer.resolveJS(item));
    const assets = transformer.getAssets();
    const loading = Promise.all([
        assets.styles && markmap.loadCSS(assets.styles),
        markmap.loadJS([...preloadScripts, ...assets.scripts]),
    ]);

    function parseData(content) {
        const { root, frontmatter } = transformer.transform(content);
        let options = markmap.deriveOptions(frontmatter?.markmap);
        options = Object.assign(
            {
                fitRatio: 0.85,
            },
            options
        );
        return { root, options };
    }

    function resetMarkmap(m, el) {
        if (!m.state.rect) return;
        const { x1, y1, x2, y2 } = m.state.rect;
        const height = (el.offsetWidth / (x2 - x1)) * (y2 - y1);
        el.style.height = height + "px";
        m.fit();
    }

    function waitForWidth(el, callback, attempts = 0, lastWidth = -1) {
        const width = el.offsetWidth;
        if ((width > 0 && width === lastWidth) || attempts > 60) {
            callback();
            return;
        }
        requestAnimationFrame(() => waitForWidth(el, callback, attempts + 1, width));
    }
    function decodeBase64(encoded) {
        const binary = atob(encoded);
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < bytes.length; i++) {
            bytes[i] = binary.charCodeAt(i);
        }
        return new TextDecoder().decode(bytes);
    }

    // --- Click-to-expand modal support ---
    let modalOverlay = null;
    let modalMarkmap = null;

    function ensureModalStyles() {
        if (document.getElementById("markmap-modal-styles")) return;
        const style = document.createElement("style");
        style.id = "markmap-modal-styles";
        style.textContent = `
.markmap-modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.75);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
}
.markmap-modal-box {
    position: relative;
    width: 92vw;
    height: 88vh;
    background: var(--md-default-bg-color, #fff);
    border-radius: 8px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    overflow: hidden;
}
.markmap-modal-box svg {
    width: 100%;
    height: 100%;
    display: block;
}
.markmap-modal-close {
    position: absolute;
    top: 8px;
    right: 12px;
    z-index: 2;
    background: transparent;
    border: none;
    font-size: 28px;
    line-height: 1;
    cursor: pointer;
    color: var(--md-default-fg-color, #333);
}
.mkdocs-markmap-expand-btn {
    position: absolute;
    top: 6px;
    right: 8px;
    z-index: 2;
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.55);
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 15px;
    line-height: 1;
    opacity: 0;
    transition: opacity 0.15s ease;
}
.mkdocs-markmap:hover .mkdocs-markmap-expand-btn,
.mkdocs-markmap-expand-btn:focus {
    opacity: 1;
}
`;
        document.head.appendChild(style);
    }

    function handleModalKeydown(e) {
        if (e.key === "Escape") closeMarkmapModal();
    }

    function closeMarkmapModal() {
        if (!modalOverlay) return;
        modalOverlay.remove();
        modalOverlay = null;
        modalMarkmap = null;
        document.body.style.overflow = "";
        document.removeEventListener("keydown", handleModalKeydown);
    }

    function openMarkmapModal(content) {
        ensureModalStyles();
        closeMarkmapModal();

        modalOverlay = document.createElement("div");
        modalOverlay.className = "markmap-modal-overlay";
        modalOverlay.addEventListener("click", (e) => {
            if (e.target === modalOverlay) closeMarkmapModal();
        });

        const box = document.createElement("div");
        box.className = "markmap-modal-box";

        const closeBtn = document.createElement("button");
        closeBtn.className = "markmap-modal-close";
        closeBtn.setAttribute("aria-label", "Close");
        closeBtn.textContent = "\u00d7";
        closeBtn.addEventListener("click", closeMarkmapModal);

        const svgEl = document.createElementNS("http://www.w3.org/2000/svg", "svg");

        box.appendChild(closeBtn);
        box.appendChild(svgEl);
        modalOverlay.appendChild(box);
        document.body.appendChild(modalOverlay);
        document.body.style.overflow = "hidden";
        document.addEventListener("keydown", handleModalKeydown);

        const { root, options } = parseData(content);
        const modalOptions = Object.assign({}, options, {
            zoom: true,
            pan: true,
        });
        modalMarkmap = markmap.Markmap.create(svgEl, modalOptions);
        modalMarkmap.setData(root);
        requestAnimationFrame(() => modalMarkmap.fit());
    }

    function renderMarkmap(el) {
        const dataEl = el.querySelector("markmap-data");
        if (!dataEl) return;
        let content = el.textContent;
        if (dataEl.getAttribute("encoding") === "base64") {
            content = decodeBase64(content);
        }
        el.innerHTML = "<svg>";
        svg = el.firstChild;
        const { root, options } = parseData(content);
        const inlineOptions = Object.assign({}, options, {
            zoom: false,
            pan: false,
        });
        const m = markmap.Markmap.create(svg, inlineOptions);
        m.setData(root);
        waitForWidth(el, () => resetMarkmap(m, el));
        ensureModalStyles();
        el.style.position = el.style.position || "relative";
        const expandBtn = document.createElement("button");
        expandBtn.className = "mkdocs-markmap-expand-btn";
        expandBtn.setAttribute("aria-label", "Expand diagram");
        expandBtn.setAttribute("title", "Expand diagram");
        expandBtn.textContent = "\u2922";
        expandBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            openMarkmapModal(content);
        });
        el.appendChild(expandBtn);
    }

    function updateMarkmaps(node) {
        for (const el of node.querySelectorAll(".mkdocs-markmap")) {
            renderMarkmap(el);
        }
    }

    loading.then(() => {
        const observer = new MutationObserver((mutationList) => {
            for (const mutation of mutationList) {
                if (mutation.type === "childList") {
                    for (const node of mutation.addedNodes) {
                        updateMarkmaps(node);
                    }
                }
            }
        });

        observer.observe(document.body, { childList: true });

        updateMarkmaps(document);
    });
})();