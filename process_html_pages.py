import re
import os

variations = [
    {"num": "1", "name": "Alpine Racing Velocity", "folder": "variation-1-racing-velocity"},
    {"num": "2", "name": "Atomic ProCenter B&W", "folder": "variation-2-atomic-pro"},
    {"num": "3", "name": "Van Deer Refined Alpine", "folder": "variation-3-vandeer-minimal"},
    {"num": "4", "name": "Glacier Freeride & Jump", "folder": "variation-4-glacier-freeride"},
    {"num": "5", "name": "Styrian Summit Heritage", "folder": "variation-5-summit-heritage"}
]

pages = [
    {"source": "5215.html", "target": "index.html", "is_home": True, "nav_key": ""},
    {"source": "news.html", "target": "news.html", "is_home": False, "nav_key": "news"},
    {"source": "veranstaltungen.html", "target": "veranstaltungen.html", "is_home": False, "nav_key": "veranstaltungen"},
    {"source": "athleten.html", "target": "athleten.html", "is_home": False, "nav_key": "athleten"},
    {"source": "sponsoren.html", "target": "sponsoren.html", "is_home": False, "nav_key": "sponsoren"},
    {"source": "verein.html", "target": "verein.html", "is_home": False, "nav_key": "verein"},
]

hero_banner_html = """
<div class="component header-image is-not-container-sized scgraz-hero-banner">
  <div class="hero-banner-inner">
    <div class="hero-backdrop"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content-wrapper">
      <div class="hero-content">
        <div class="hero-top-row">
          <span class="club-badge"><span class="badge-dot"></span> ASVÖ SKICLUB GRAZ · SEIT 1974</span>
          <div class="moto-box">

            <span class="moto-switcher" id="moto-switcher">
              <span class="moto-phrase active" data-phrase="Ride on">Ride on</span>
              <span class="moto-phrase" data-phrase="Race on">Race on</span>
            </span>
          </div>
        </div>
        <h1 class="hero-title">
          <span class="hero-title-main">LEIDENSCHAFT AUF SCHNEE</span>
          <span class="hero-title-sub">Rennsport, Freeride & Nachwuchsförderung im ASVÖ Skiclub Graz</span>
        </h1>
        <div class="hero-athlete-badge">
          <div class="athlete-badge-avatar">PP</div>
          <div class="athlete-badge-text">
            <span class="athlete-badge-name">Philipp Papst</span>
            <span class="athlete-badge-role">Ski Austria D-Trainer</span>
          </div>
          <span class="trainer-pill">Head Coach</span>
        </div>
        <div class="hero-actions">
          <a href="news.html" class="btn-hero btn-hero-primary">Aktuelles</a>
          <a href="veranstaltungen.html" class="btn-hero btn-hero-secondary">Veranstaltungen</a>
          <a href="verein.html" class="btn-hero btn-hero-outline">Der Verein</a>
        </div>
      </div>
    </div>
  </div>
</div>
"""

def make_switcher(v_current, page_filename):
    out = f"""
<div class="variation-nav-pill" id="variation-nav-pill">
  <button class="pill-toggle-btn" id="pill-toggle-btn" type="button" title="Zwischen Design-Varianten wechseln">
    <span class="pill-num-badge">V{v_current['num']}</span>
    <span>{v_current['name']}</span>
    <span>▾</span>
  </button>
  <div class="pill-dropdown-content">
    <div style="font-size:11px; color:#94a3b8; text-transform:uppercase; margin-bottom:8px; font-weight:700;">Design-Varianten</div>
"""
    for v in variations:
        active_cls = "active" if v['num'] == v_current['num'] else ""
        out += f'    <a href="../{v["folder"]}/{page_filename}" class="pill-option {active_cls}">{v["num"]}. {v["name"]}</a>\n'
    out += f"""    <a href="../index.html" class="pill-option pill-option-hub">⊞ Zur Varianten-Übersicht</a>
  </div>
</div>
"""
    return out

for v in variations:
    folder = v["folder"]
    print(f"=== Processing pages for {v['name']} in {folder} ===")
    for p in pages:
        with open(p["source"], "r", encoding="utf-8") as f:
            html = f.read()

        # 1. Clean out NREUM script
        html = re.sub(r'<script type=\"text/javascript\">window\.NREUM.*?</script>', '', html, flags=re.DOTALL)

        # 2. Replace CDN theme stylesheet with local platform.css and theme.css
        html = re.sub(
            r'<link rel=\"stylesheet\" href=\"https://assets\d?\.skizeit\.at/assets/themes/platform_theme_[^>]+>',
            '<link rel="stylesheet" href="css/platform.css" />\n    <link rel="stylesheet" href="css/theme.css" />',
            html
        )

        # 3. Clean and replace CDN scripts with local external scripts
        html = re.sub(r'<script src=\"https://assets\d?\.skizeit\.at/assets/vendor/htmx[^>]+></script>', '', html)
        html = re.sub(r'<script src=\"https://assets\d?\.skizeit\.at/assets/platform-[^>]+></script>', '', html)
        
        # Insert scripts right before </head>
        script_block = """
    <script src="js/htmx.js" defer></script>
    <script src="js/platform.js" defer></script>
    <script src="js/theme.js" defer></script>
"""
        html = html.replace('</head>', script_block + '</head>')

        # 4. Body tag update
        html = re.sub(
            r'<body class=\"platform standalone [^\"]*\"[^>]*>',
            '<body class="platform standalone has-bg-img platform-5215">',
            html
        )

        # 5. Navbar tag update
        html = re.sub(
            r'<nav class=\"navbar navbar-default navbar-fixed-top [^\"]*\">',
            '<nav class="navbar navbar-default navbar-fixed-top navbar-style-with-bgcolor">',
            html
        )

        # 6. Navbar logo update
        html = re.sub(
            r'<img src=\"https://fs-skizeit-production\.s3-eu-west-1\.amazonaws\.com/pictures/25198/11_club_logo_fit/[^/]+/SCGrazLogo\.png\"[^>]*/>',
            '<img src="images/logo.png" alt="ASVÖ Skiclub Graz Logo" />',
            html
        )

        # 7. Update internal links
        html = re.sub(r'href=\"/\"', 'href="index.html"', html)
        html = re.sub(r'href=\"/news\"', 'href="news.html"', html)
        html = re.sub(r'href=\"/veranstaltungen\"', 'href="veranstaltungen.html"', html)
        html = re.sub(r'href=\"/athleten\"', 'href="athleten.html"', html)
        html = re.sub(r'href=\"/sponsoren\"', 'href="sponsoren.html"', html)
        html = re.sub(r'href=\"/verein\"', 'href="verein.html"', html)

        # 8. Set active class on navbar link
        if p["nav_key"]:
            html = re.sub(
                rf'(<li class=\"component platform-page-link [^\"]*\" data-id=\"\d+\" data-seq=\"\d+\" data-title=\"[^\"]*\">(?:\s*<a class=\"link\" href=\"{p["nav_key"]}\.html\">))',
                r'<li class="component platform-page-link active" data-title="\1',
                html
            )
        elif p["is_home"]:
            pass # home

        # 9. Localize downloaded images
        # Replace URLs like https://fs-skizeit-production.s3.../<filename> with images/<filename>
        for img_name in os.listdir("downloaded_assets"):
            html = html.replace(f"https://fs-skizeit-production.s3.eu-west-1.amazonaws.com/pictures/{img_name}", f"images/{img_name}")
            html = re.sub(rf'https://fs-skizeit-production\.s3[^\"]*/{re.escape(img_name)}', f'images/{img_name}', html)

        # 10. Inject Hero Banner ONLY on Home page (index.html)
        if p["is_home"]:
            # Place banner inside <section class="page-teaser page-teaser-articles-list"> right before <div class="page-section-header
            target_pos = html.find('<section class="page-teaser page-teaser-articles-list">')
            if target_pos != -1:
                after_tag = target_pos + len('<section class="page-teaser page-teaser-articles-list">')
                html = html[:after_tag] + "\n" + hero_banner_html + "\n" + html[after_tag:]
            else:
                print(f"Warning: page-teaser not found in {p['source']}")

        # 11. Inject Variation Switcher Widget right before </body>
        switcher_code = make_switcher(v, p["target"])
        html = html.replace('</body>', switcher_code + '</body>')

        # Write output file
        target_path = os.path.join(folder, p["target"])
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  -> Generated {target_path} ({len(html)} bytes)")

print("\nAll 30 HTML pages generated successfully across the 5 variations!")
