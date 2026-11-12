/* ==========================================================
 * ASVÖ Skiclub Graz - Design Variation 1: Alpine Racing Velocity
 * Theme JS: External script for motto ticker & UI interactions
 * ========================================================== */

document.addEventListener("DOMContentLoaded", function () {
  // 1. Motto Switcher: Alternates between "Ride on" and "Race on" every 3.5s
  var switcher = document.getElementById("moto-switcher");
  if (switcher) {
    var phrases = switcher.querySelectorAll(".moto-phrase");
    var currentIdx = 0;
    if (phrases.length > 1) {
      setInterval(function () {
        phrases[currentIdx].classList.remove("active");
        currentIdx = (currentIdx + 1) % phrases.length;
        phrases[currentIdx].classList.add("active");
      }, 3500);
    }
  }

  // 2. Navbar Scroll Dynamic Blur
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

  // 3. Floating Variation Navigator Dropdown Toggle
  var pill = document.getElementById("variation-nav-pill");
  var toggleBtn = document.getElementById("pill-toggle-btn");
  if (pill && toggleBtn) {
    toggleBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      pill.classList.toggle("open");
    });
    document.addEventListener("click", function (e) {
      if (!pill.contains(e.target)) {
        pill.classList.remove("open");
      }
    });
  }

  // 4. Mobile Menu Hamburger Toggle Helper
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
