/* 控件位于正文之外；主题模拟不改变 README 源文件。 */
const themeButton = document.querySelector("#theme-toggle");
const widthButton = document.querySelector("#width-toggle");
const frame = document.querySelector("#preview-frame");
const sources = [...document.querySelectorAll("#readme-content picture source")].map(
  (source) => ({ source, media: source.getAttribute("media") || "" })
);

/** 输入深色标志，同步上游样式及 picture 主题选择；不改写图片 URL。 */
function setTheme(dark) {
  const theme = dark ? "dark" : "light";
  document.documentElement.dataset.theme = theme;
  document.querySelector("#markdown-theme").href = `demo/vendor/github-markdown-${theme}.css`;
  sources.forEach(({ source, media }) => {
    source.media = media
      .replace(/\(prefers-color-scheme:\s*dark\)/g, dark ? "all" : "not all")
      .replace(/\(prefers-color-scheme:\s*light\)/g, dark ? "not all" : "all");
  });
  themeButton.setAttribute("aria-pressed", String(dark));
  themeButton.textContent = dark ? "浅色预览" : "深色预览";
}
themeButton.addEventListener("click", () => setTheme(document.documentElement.dataset.theme !== "dark"));
widthButton.addEventListener("click", () => {
  const compact = frame.classList.toggle("compact");
  widthButton.setAttribute("aria-pressed", String(compact));
  widthButton.textContent = compact ? "桌面预览" : "窄屏预览";
});
setTheme(window.matchMedia("(prefers-color-scheme: dark)").matches);
