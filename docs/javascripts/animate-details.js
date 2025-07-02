document.addEventListener("DOMContentLoaded", () => {
    const detailsElements = document.querySelectorAll("details");

    detailsElements.forEach((detail) => {
        detail.addEventListener("toggle", () => {
            if (detail.open) {
                // 找到第一个非 summary 的元素添加动画
                const children = Array.from(detail.children);
                const content = children.find(
                    (el) => el.tagName.toLowerCase() !== "summary"
                );
                if (content) {
                    content.style.animation = "none";
                    void content.offsetWidth; // 强制触发重绘，重置动画
                    content.style.animation = "fadeSlideIn 0.4s ease-out";
                }
            }
        });
    });
});

