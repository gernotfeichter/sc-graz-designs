import re
import os
import shutil

variations = [
    {
        "id": "variation-1-racing-velocity",
        "name": "Alpine Racing Velocity",
        "num": "1",
        "folder": "variation-1-racing-velocity",
        "subtitle": "High-Speed World Cup Racing Aesthetic",
        "tagline": "Dynamic ASVÖ Red & Midnight Navy with High-Speed Carving",
        "font_family": "'Montserrat', 'Inter', -apple-system, sans-serif",
        "font_import": "@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,600;0,700;0,800;0,900;1,700&family=Inter:wght@400;500;600;700&display=swap');",
        "primary_color": "#CA1919",
        "primary_hover": "#A81414",
        "secondary_color": "#0C1B33",
        "accent_color": "#4A90E2",
        "nav_bg": "rgba(12, 27, 51, 0.98)",
        "nav_text": "#FFFFFF",
        "hero_overlay": "linear-gradient(90deg, rgba(12,27,51,0.92) 0%, rgba(12,27,51,0.70) 45%, rgba(12,27,51,0.15) 75%, rgba(12,27,51,0) 100%)",
        "card_bg": "rgba(255, 255, 255, 0.96)",
        "card_border": "1px solid rgba(202, 25, 25, 0.15)",
        "card_shadow": "0 10px 30px rgba(12, 27, 51, 0.12)",
        "hero_accent_border": "4px solid #CA1919",
        "badge_bg": "rgba(202, 25, 25, 0.12)",
        "badge_border": "1px solid #CA1919",
        "badge_color": "#CA1919",
        "tag_color": "#4A90E2",
        "pulse_color": "#CA1919"
    },
    {
        "id": "variation-2-atomic-pro",
        "name": "Atomic ProCenter B&W",
        "num": "2",
        "folder": "variation-2-atomic-pro",
        "subtitle": "Dramatic High-Contrast Monochrome",
        "tagline": "Inspired by atomic.auf.ski — Pure Slalom Drama with Crimson Accents",
        "font_family": "'Oswald', 'Inter', -apple-system, sans-serif",
        "font_import": "@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');",
        "primary_color": "#E11D48",
        "primary_hover": "#BE123C",
        "secondary_color": "#0B0E14",
        "accent_color": "#94A3B8",
        "nav_bg": "rgba(11, 14, 20, 0.98)",
        "nav_text": "#F8FAFC",
        "hero_overlay": "linear-gradient(90deg, rgba(11,14,20,0.95) 0%, rgba(11,14,20,0.80) 45%, rgba(11,14,20,0.2) 80%, rgba(11,14,20,0) 100%)",
        "card_bg": "rgba(255, 255, 255, 0.94)",
        "card_border": "1px solid rgba(225, 29, 72, 0.2)",
        "card_shadow": "0 12px 36px rgba(0, 0, 0, 0.35)",
        "hero_accent_border": "4px solid #E11D48",
        "badge_bg": "rgba(225, 29, 72, 0.15)",
        "badge_border": "1px solid #E11D48",
        "badge_color": "#E11D48",
        "tag_color": "#F8FAFC",
        "pulse_color": "#E11D48"
    },
    {
        "id": "variation-3-vandeer-minimal",
        "name": "Van Deer Refined Alpine",
        "num": "3",
        "folder": "variation-3-vandeer-minimal",
        "subtitle": "Understated Minimalist Luxury",
        "tagline": "Inspired by vandeer-redbull-sports.auf.ski — Matte Slate, Muted Panorama & Editorial Typography",
        "font_family": "'Cinzel', 'Plus Jakarta Sans', -apple-system, sans-serif",
        "font_import": "@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');",
        "primary_color": "#991B1B",
        "primary_hover": "#7F1D1D",
        "secondary_color": "#1E252B",
        "accent_color": "#64748B",
        "nav_bg": "rgba(30, 37, 43, 0.98)",
        "nav_text": "#F7F6F2",
        "hero_overlay": "linear-gradient(90deg, rgba(30,37,43,0.94) 0%, rgba(30,37,43,0.72) 42%, rgba(30,37,43,0.15) 75%, rgba(30,37,43,0) 100%)",
        "card_bg": "rgba(255, 255, 255, 0.96)",
        "card_border": "1px solid #E2E8F0",
        "card_shadow": "0 6px 24px rgba(30, 37, 43, 0.06)",
        "hero_accent_border": "2px solid #991B1B",
        "badge_bg": "rgba(153, 27, 27, 0.08)",
        "badge_border": "1px solid #991B1B",
        "badge_color": "#991B1B",
        "tag_color": "#1E252B",
        "pulse_color": "#991B1B"
    },
    {
        "id": "variation-4-glacier-freeride",
        "name": "Glacier Freeride & Jump",
        "num": "4",
        "folder": "variation-4-glacier-freeride",
        "subtitle": "Aerial Freedom & Big-Air Powder",
        "tagline": "Dual Action — Skier Soaring High ('Ride on') + Philipp Papst Carving ('Race on')",
        "font_family": "'Outfit', -apple-system, sans-serif",
        "font_import": "@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');",
        "primary_color": "#00A3E0",
        "primary_hover": "#0284C7",
        "secondary_color": "#081B38",
        "accent_color": "#CA1919",
        "nav_bg": "rgba(8, 27, 56, 0.98)",
        "nav_text": "#F0F9FF",
        "hero_overlay": "linear-gradient(90deg, rgba(8,27,56,0.92) 0%, rgba(8,27,56,0.70) 45%, rgba(8,27,56,0.15) 80%, rgba(8,27,56,0) 100%)",
        "card_bg": "rgba(255, 255, 255, 0.96)",
        "card_border": "1px solid rgba(0, 163, 224, 0.25)",
        "card_shadow": "0 10px 32px rgba(8, 27, 56, 0.15)",
        "hero_accent_border": "3px solid #00A3E0",
        "badge_bg": "rgba(0, 163, 224, 0.15)",
        "badge_border": "1px solid #00A3E0",
        "badge_color": "#00A3E0",
        "tag_color": "#0284C7",
        "pulse_color": "#00A3E0"
    },
    {
        "id": "variation-5-summit-heritage",
        "name": "Styrian Summit Heritage",
        "num": "5",
        "folder": "variation-5-summit-heritage",
        "subtitle": "Alpenglow Sunset & 50+ Years Club Pride",
        "tagline": "Celebrating Since 1974 with Golden Alpine Sunset and Authentic Austrian Tradition",
        "font_family": "'Montserrat', 'Merriweather', -apple-system, sans-serif",
        "font_import": "@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&display=swap');",
        "primary_color": "#C8102E",
        "primary_hover": "#A50D24",
        "secondary_color": "#14221A",
        "accent_color": "#D97706",
        "nav_bg": "rgba(20, 34, 26, 0.98)",
        "nav_text": "#FFFBEB",
        "hero_overlay": "linear-gradient(90deg, rgba(20,34,26,0.94) 0%, rgba(20,34,26,0.72) 42%, rgba(20,34,26,0.15) 75%, rgba(20,34,26,0) 100%)",
        "card_bg": "rgba(255, 255, 255, 0.96)",
        "card_border": "1px solid rgba(217, 119, 6, 0.25)",
        "card_shadow": "0 10px 30px rgba(20, 34, 26, 0.12)",
        "hero_accent_border": "3px solid #D97706",
        "badge_bg": "rgba(217, 119, 6, 0.15)",
        "badge_border": "1px solid #D97706",
        "badge_color": "#D97706",
        "tag_color": "#C8102E",
        "pulse_color": "#D97706"
    }
]

# Generate CSS for each variation
for v in variations:
    css_content = f"""/* ==========================================================
 * ASVÖ Skiclub Graz - Design Variation {v['num']}: {v['name']}
 * {v['subtitle']}
 * Theme CSS: Externalized for performance, modularity & clarity
 * ========================================================== */

{v['font_import']}

:root {{
  --scg-primary: {v['primary_color']};
  --scg-primary-hover: {v['primary_hover']};
  --scg-secondary: {v['secondary_color']};
  --scg-accent: {v['accent_color']};
  --scg-nav-bg: {v['nav_bg']};
  --scg-nav-text: {v['nav_text']};
  --scg-card-bg: {v['card_bg']};
  --scg-card-border: {v['card_border']};
  --scg-card-shadow: {v['card_shadow']};
  --scg-font: {v['font_family']};
}}

/* Body & Background */
body.platform,
body.platform.standalone {{
  font-family: var(--scg-font) !important;
  color: #1e293b;
  background-image: url('../images/background.jpg') !important;
  background-attachment: fixed !important;
  background-size: cover !important;
  background-position: center !important;
  background-repeat: no-repeat !important;
  min-height: 100vh;
}}

/* Navbar Styling */
.navbar.navbar-style-with-bgcolor,
.navbar.navbar-default {{
  background-color: var(--scg-nav-bg) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-bottom: {v['hero_accent_border']} !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
  transition: all 0.3s ease;
}}

.navbar-default .navbar-header .navbar-img-wrapper img {{
  max-height: 52px;
  width: auto;
  filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.3));
  transition: transform 0.2s ease;
}}

.navbar-default .navbar-header .navbar-img-wrapper img:hover {{
  transform: scale(1.05);
}}

.navbar h1 a,
.navbar .navbar-nav .nav-label {{
  color: var(--scg-nav-text) !important;
  font-weight: 600;
  letter-spacing: 0.3px;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
}}

.navbar h1 {{
  font-size: 22px;
  margin-top: 15px;
  margin-bottom: 10px;
}}

.navbar-nav > li > a {{
  padding-top: 20px !important;
  padding-bottom: 20px !important;
  transition: color 0.2s ease, background-color 0.2s ease;
}}

.navbar-nav > li > a:hover,
.navbar-nav > li.active > a {{
  background-color: rgba(255, 255, 255, 0.1) !important;
  border-bottom: 3px solid var(--scg-primary);
}}

.navbar-nav > li.active > a .nav-label {{
  color: #FFFFFF !important;
}}

/* Hero Banner (Shown ONLY on main/home page) */
.component.header-image.scgraz-hero-banner {{
  position: relative;
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  margin-right: calc(-50vw + 50%);
  margin-top: -15px;
  margin-bottom: 45px;
  min-height: clamp(380px, 42vw, 540px);
  overflow: hidden;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
  display: block;
}}

.hero-banner-inner {{
  position: relative;
  width: 100%;
  min-height: clamp(380px, 42vw, 540px);
  display: flex;
  align-items: center;
}}

.hero-backdrop {{
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('../images/banner.jpg');
  background-size: cover;
  background-position: center right;
  z-index: 1;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}}

.scgraz-hero-banner:hover .hero-backdrop {{
  transform: scale(1.02);
}}

.hero-overlay {{
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: {v['hero_overlay']};
  z-index: 2;
}}

.hero-content-wrapper {{
  position: relative;
  z-index: 3;
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 40px 30px;
}}

.hero-content {{
  max-width: 680px;
}}

/* Club Badge & Motto Switcher */
.hero-top-row {{
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 18px;
}}

.club-badge {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border-radius: 9999px;
  background: {v['badge_bg']};
  border: {v['badge_border']};
  color: #FFFFFF;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  backdrop-filter: blur(8px);
}}

.badge-dot {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: {v['pulse_color']};
  box-shadow: 0 0 10px {v['pulse_color']};
  animation: pulse-dot 2s infinite;
}}

@keyframes pulse-dot {{
  0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(202, 25, 25, 0.7); }}
  70% {{ transform: scale(1); box-shadow: 0 0 0 8px rgba(202, 25, 25, 0); }}
  100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(202, 25, 25, 0); }}
}}

/* Motto Switcher: "Ride on - Race on" */
.moto-box {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(0, 0, 0, 0.45);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 5px 14px;
  border-radius: 9999px;
  backdrop-filter: blur(8px);
}}

.moto-label {{
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: rgba(255, 255, 255, 0.7);
  font-weight: 600;
}}

.moto-switcher {{
  position: relative;
  display: inline-block;
  min-width: 90px;
  height: 22px;
}}

.moto-phrase {{
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1), transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  font-size: 15px;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: 0.5px;
  white-space: nowrap;
}}

.moto-phrase.active {{
  opacity: 1;
  transform: translateY(0);
}}

.moto-phrase[data-phrase="Ride on"] {{
  color: #38BDF8;
  text-shadow: 0 0 12px rgba(56, 189, 248, 0.6);
}}

.moto-phrase[data-phrase="Race on"] {{
  color: #F87171;
  text-shadow: 0 0 12px rgba(248, 113, 113, 0.6);
}}

/* Hero Title */
.hero-title {{
  color: #FFFFFF;
  margin: 0 0 18px 0;
  line-height: 1.15;
}}

.hero-title-main {{
  display: block;
  font-size: clamp(28px, 4.2vw, 48px);
  font-weight: 900;
  letter-spacing: -0.5px;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}}

.hero-title-sub {{
  display: block;
  font-size: clamp(16px, 2vw, 22px);
  font-weight: 400;
  opacity: 0.92;
  margin-top: 8px;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}}

/* Philipp Papst Coach Badge */
.hero-athlete-badge {{
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: rgba(15, 23, 42, 0.75);
  border: 1px solid rgba(255, 255, 255, 0.25);
  padding: 8px 16px;
  border-radius: 12px;
  margin-bottom: 24px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
  transition: transform 0.2s ease, border-color 0.2s ease;
}}

.hero-athlete-badge:hover {{
  transform: translateY(-2px);
  border-color: var(--scg-primary);
}}

.athlete-badge-avatar {{
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--scg-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  font-weight: 800;
  font-size: 14px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}}

.athlete-badge-text {{
  display: flex;
  flex-direction: column;
}}

.athlete-badge-name {{
  color: #FFFFFF;
  font-weight: 700;
  font-size: 15px;
  letter-spacing: 0.3px;
}}

.athlete-badge-role {{
  color: {v['tag_color']};
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}}

.trainer-pill {{
  background: var(--scg-primary);
  color: #FFFFFF;
  font-size: 10px;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 9999px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}}

/* Hero Action Buttons */
.hero-actions {{
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}}

.btn-hero {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 22px;
  font-size: 14px;
  font-weight: 700;
  border-radius: 8px;
  text-decoration: none !important;
  transition: all 0.2s ease;
  letter-spacing: 0.3px;
}}

.btn-hero-primary {{
  background: var(--scg-primary);
  color: #FFFFFF !important;
  border: 1px solid var(--scg-primary);
  box-shadow: 0 4px 14px rgba(202, 25, 25, 0.4);
}}

.btn-hero-primary:hover {{
  background: var(--scg-primary-hover);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(202, 25, 25, 0.5);
}}

.btn-hero-secondary {{
  background: rgba(255, 255, 255, 0.15);
  color: #FFFFFF !important;
  border: 1px solid rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(8px);
}}

.btn-hero-secondary:hover {{
  background: rgba(255, 255, 255, 0.25);
  transform: translateY(-2px);
}}

.btn-hero-outline {{
  background: transparent;
  color: rgba(255, 255, 255, 0.85) !important;
  border: 1px solid rgba(255, 255, 255, 0.25);
}}

.btn-hero-outline:hover {{
  color: #FFFFFF !important;
  border-color: #FFFFFF;
}}

/* Cards & Content Sections */
.content-container {{
  padding: 20px 4vw 80px 4vw !important;
}}

.article-teaser,
.article-default,
.article-custom-articles-list,
.page-section-header,
.filter-container,
.entity-article {{
  background: var(--scg-card-bg) !important;
  border: var(--scg-card-border) !important;
  border-radius: 12px !important;
  box-shadow: var(--scg-card-shadow) !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}}

.article-teaser:hover {{
  transform: translateY(-4px);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.15) !important;
}}

.page-section-header h2 {{
  font-size: 26px;
  font-weight: 800;
  color: var(--scg-secondary);
  border-left: 5px solid var(--scg-primary);
  padding-left: 12px;
  margin: 0;
}}

.article-subject a {{
  color: var(--scg-secondary) !important;
  font-weight: 700;
  transition: color 0.2s ease;
}}

.article-subject a:hover {{
  color: var(--scg-primary) !important;
  text-decoration: none;
}}

.img-container img {{
  border-radius: 8px;
  max-width: 100%;
  height: auto;
}}

/* Floating Variation Navigator Switcher */
.variation-nav-pill {{
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 9999;
  background: rgba(15, 23, 42, 0.94);
  color: #FFFFFF;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 50px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  backdrop-filter: blur(12px);
  transition: all 0.3s ease;
}}

.variation-nav-pill.open {{
  border-radius: 16px;
}}

.pill-toggle-btn {{
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 18px;
  background: none;
  border: none;
  color: #FFFFFF;
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
}}

.pill-num-badge {{
  background: var(--scg-primary);
  color: #FFFFFF;
  padding: 2px 8px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 800;
}}

.pill-dropdown-content {{
  display: none;
  padding: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  min-width: 280px;
}}

.variation-nav-pill.open .pill-dropdown-content {{
  display: block;
}}

.pill-option {{
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none !important;
  font-size: 12px;
  font-weight: 500;
  border-radius: 8px;
  transition: background 0.2s ease, color 0.2s ease;
}}

.pill-option:hover {{
  background: rgba(255, 255, 255, 0.12);
  color: #FFFFFF;
}}

.pill-option.active {{
  background: var(--scg-primary);
  color: #FFFFFF;
  font-weight: 700;
}}

.pill-option-hub {{
  border-top: 1px dashed rgba(255, 255, 255, 0.2);
  margin-top: 6px;
  padding-top: 10px;
  color: #38BDF8 !important;
}}

/* Responsive tweaks */
@media (max-width: 768px) {{
  .component.header-image.scgraz-hero-banner {{
    min-height: 480px;
  }}
  .hero-content-wrapper {{
    padding: 30px 18px;
  }}
  .hero-actions {{
    flex-direction: column;
    align-items: stretch;
  }}
  .btn-hero {{
    width: 100%;
    text-align: center;
  }}
  .variation-nav-pill {{
    bottom: 15px;
    right: 15px;
  }}
}}
"""
    with open(f"{v['folder']}/css/theme.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    print(f"Generated CSS for {v['name']}")

    # Generate JS for each variation
    js_content = f"""/* ==========================================================
 * ASVÖ Skiclub Graz - Design Variation {v['num']}: {v['name']}
 * Theme JS: External script for motto ticker & UI interactions
 * ========================================================== */

document.addEventListener("DOMContentLoaded", function () {{
  // 1. Motto Switcher: Alternates between "Ride on" and "Race on" every 3.5s
  var switcher = document.getElementById("moto-switcher");
  if (switcher) {{
    var phrases = switcher.querySelectorAll(".moto-phrase");
    var currentIdx = 0;
    if (phrases.length > 1) {{
      setInterval(function () {{
        phrases[currentIdx].classList.remove("active");
        currentIdx = (currentIdx + 1) % phrases.length;
        phrases[currentIdx].classList.add("active");
      }}, 3500);
    }}
  }}

  // 2. Navbar Scroll Dynamic Blur
  var navbar = document.querySelector(".navbar");
  if (navbar) {{
    window.addEventListener("scroll", function () {{
      if (window.scrollY > 40) {{
        navbar.classList.add("navbar-scrolled");
      }} else {{
        navbar.classList.remove("navbar-scrolled");
      }}
    }});
  }}

  // 3. Floating Variation Navigator Dropdown Toggle
  var pill = document.getElementById("variation-nav-pill");
  var toggleBtn = document.getElementById("pill-toggle-btn");
  if (pill && toggleBtn) {{
    toggleBtn.addEventListener("click", function (e) {{
      e.stopPropagation();
      pill.classList.toggle("open");
    }});
    document.addEventListener("click", function (e) {{
      if (!pill.contains(e.target)) {{
        pill.classList.remove("open");
      }}
    }});
  }}

  // 4. Mobile Menu Hamburger Toggle Helper
  var mobileToggle = document.querySelector(".navbar-toggle");
  var mobileCollapse = document.getElementById("navbar-collapse");
  if (mobileToggle && mobileCollapse) {{
    mobileToggle.addEventListener("click", function () {{
      var isExpanded = mobileToggle.getAttribute("aria-expanded") === "true";
      mobileToggle.setAttribute("aria-expanded", !isExpanded);
      mobileCollapse.classList.toggle("in");
    }});
  }}
}});
"""
    with open(f"{v['folder']}/js/theme.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Generated JS for {v['name']}")

print("All CSS and JS files generated.")
