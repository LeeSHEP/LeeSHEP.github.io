window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    tags: "ams", // auto-number \begin{equation}; use \label / \eqref
    macros: {
      // common physics macros — add more here
      dd: "\\mathrm{d}",
      ii: "\\mathrm{i}",
      tr: "\\operatorname{tr}",
      Tr: "\\operatorname{Tr}",
      bra: ["\\langle #1 |", 1],
      ket: ["| #1 \\rangle", 1],
      braket: ["\\langle #1 | #2 \\rangle", 2],
      slashed: ["{#1\\!\\!\\!/}", 1],
      order: ["\\mathcal{O}\\left(#1\\right)", 1],
      Lag: "\\mathcal{L}",
    },
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

// re-render math after instant page navigation
document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
