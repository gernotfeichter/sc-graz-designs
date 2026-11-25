/* ==========================================================
 * ASVÖ Skiclub Graz - Design Variation 4: Glacier Freeride & Jump
 * Theme JS: External script for UI interactions
 * ========================================================== */

document.addEventListener("DOMContentLoaded", function () {
  // 1. Navbar Scroll Dynamic Blur
  var navbar = document.querySelector(".navbar");
  if (navbar) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 40) {
        navbar.classList.add("navbar-scrolled");
      } else {
        navbar.classList.remove("navbar-scrolled");
      }
    });
  }

  // 2. Mobile Menu Hamburger Toggle Helper
  var mobileToggle = document.querySelector(".navbar-toggle");
  var mobileCollapse = document.getElementById("navbar-collapse");
  if (mobileToggle && mobileCollapse) {
    mobileToggle.addEventListener("click", function () {
      var isExpanded = mobileToggle.getAttribute("aria-expanded") === "true";
      mobileToggle.setAttribute("aria-expanded", !isExpanded);
      mobileCollapse.classList.toggle("in");
    });
  }
});
