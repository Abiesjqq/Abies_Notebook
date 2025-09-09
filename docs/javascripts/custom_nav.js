// 自定义导航行为，确保点击二级导航栏时只展开下一级
document.addEventListener("DOMContentLoaded", function () {
  // 获取所有的二级导航项
  const secondLevelItems = document.querySelectorAll(
    ".md-nav__item--second-level > a"
  );

  secondLevelItems.forEach((item) => {
    item.addEventListener("click", function (event) {
      // 阻止默认的跳转行为
      event.preventDefault();

      // 获取当前点击的二级导航项的父元素
      const parentItem = item.closest(".md-nav__item--second-level");

      // 切换当前二级导航项下的三级导航项
      const thirdLevelItems = parentItem.querySelectorAll(
        ".md-nav__item--third-level"
      );
      thirdLevelItems.forEach((thirdItem) => {
        thirdItem.classList.toggle("md-nav__item--open");
      });
    });
  });
});
