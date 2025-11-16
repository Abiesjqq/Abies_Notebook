window.MathJax = {
  tex: {
    inlineMath: [
      ["$", "$"],
      ["\\(", "\\)"],
    ],
    displayMath: [
      ["$$", "$$"],
      ["\\[", "\\]"],
    ],
    processEscapes: true,
    processEnvironments: true,
    tags: "ams",
    packages: { '[+]': ['physics'] },   // ★ 加入 physics 包以支持 \bm
  },

  loader: {
    load: ['[tex]/physics'],             // ★ 加载 physics 包
  },

  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "math|arithmatex",
  },
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
