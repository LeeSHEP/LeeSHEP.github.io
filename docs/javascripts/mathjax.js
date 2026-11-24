window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    tags: "ams", // \begin{equation} 에 자동 번호, \label / \eqref 사용 가능
    macros: {
      // 자주 쓰는 물리 매크로 — 필요하면 여기에 추가
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

// 페이지 이동(instant navigation) 시에도 수식 다시 렌더링
document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
