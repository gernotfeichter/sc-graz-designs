import os

html_hub = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ASVÖ Skiclub Graz — 5 Design-Variationen Showcase</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #C8102E;
      --primary-hover: #A50D24;
      --navy: #0B172A;
      --slate: #1E293B;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --bg-page: #F8FAFC;
      --card-bg: #FFFFFF;
      --border: #E2E8F0;
      --shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.08), 0 4px 12px -2px rgba(0, 0, 0, 0.04);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg-page);
      color: var(--text-main);
      line-height: 1.6;
      padding-bottom: 80px;
    }

    /* Hero Header */
    .showcase-header {
      background: linear-gradient(135deg, #0B172A 0%, #1E293B 60%, #16263D 100%);
      color: #FFFFFF;
      padding: 60px 24px 50px 24px;
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid var(--primary);
    }

    .showcase-header::after {
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      width: 45%;
      background: url('variation-1-racing-velocity/images/banner.jpg') center right/cover no-repeat;
      opacity: 0.22;
      pointer-events: none;
      mask-image: linear-gradient(to right, transparent 0%, black 100%);
      -webkit-mask-image: linear-gradient(to right, transparent 0%, black 100%);
    }

    .header-container {
      max-width: 1280px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
    }

    .header-top {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
    }

    .header-logo {
      height: 64px;
      width: auto;
      filter: drop-shadow(0 4px 12px rgba(0,0,0,0.4));
    }

    .header-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(200, 16, 46, 0.2);
      border: 1px solid var(--primary);
      color: #FFFFFF;
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
    }

    .header-badge .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #22C55E;
      box-shadow: 0 0 10px #22C55E;
    }

    .header-title {
      font-family: 'Montserrat', sans-serif;
      font-size: clamp(32px, 4.5vw, 52px);
      font-weight: 900;
      letter-spacing: -0.5px;
      line-height: 1.15;
      margin-bottom: 14px;
    }

    .header-title span {
      color: var(--primary);
    }

    .header-desc {
      font-size: 18px;
      color: #CBD5E1;
      max-width: 800px;
      margin-bottom: 24px;
    }

    .header-stats {
      display: flex;
      flex-wrap: wrap;
      gap: 24px;
      margin-top: 20px;
      padding-top: 20px;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }

    .stat-item {
      display: flex;
      flex-direction: column;
    }

    .stat-num {
      font-family: 'Montserrat', sans-serif;
      font-size: 26px;
      font-weight: 800;
      color: #FFFFFF;
    }

    .stat-label {
      font-size: 12px;
      color: #94A3B8;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      font-weight: 600;
    }

    /* Main Container */
    .container {
      max-width: 1280px;
      margin: -30px auto 0 auto;
      padding: 0 24px;
      position: relative;
      z-index: 10;
    }

    /* Tab Controls */
    .tab-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      background: #FFFFFF;
      padding: 8px;
      border-radius: 14px;
      box-shadow: var(--shadow);
      margin-bottom: 35px;
      border: 1px solid var(--border);
    }

    .tab-btn {
      flex: 1;
      min-width: 180px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 14px 18px;
      border: none;
      background: transparent;
      color: var(--text-muted);
      font-family: 'Montserrat', sans-serif;
      font-weight: 700;
      font-size: 14px;
      border-radius: 10px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .tab-btn:hover {
      background: #F1F5F9;
      color: var(--text-main);
    }

    .tab-btn.active {
      background: var(--navy);
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(11, 23, 42, 0.25);
    }

    .tab-num {
      background: var(--primary);
      color: #FFFFFF;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 800;
    }

    /* Interactive Preview Section */
    .preview-card {
      background: var(--card-bg);
      border-radius: 16px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      overflow: hidden;
      margin-bottom: 40px;
    }

    .preview-toolbar {
      background: #0F172A;
      color: #FFFFFF;
      padding: 14px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
      border-bottom: 1px solid #334155;
    }

    .toolbar-info {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .toolbar-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 16px;
      font-weight: 700;
    }

    .toolbar-badge {
      background: var(--primary);
      color: #FFFFFF;
      padding: 3px 10px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
    }

    .toolbar-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .viewport-btn {
      background: #1E293B;
      color: #CBD5E1;
      border: 1px solid #334155;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .viewport-btn:hover, .viewport-btn.active {
      background: var(--primary);
      color: #FFFFFF;
      border-color: var(--primary);
    }

    .open-full-btn {
      background: #2563EB;
      color: #FFFFFF;
      padding: 6px 16px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: background 0.2s ease;
    }

    .open-full-btn:hover {
      background: #1D4ED8;
    }

    .preview-viewport-wrapper {
      background: #64748B;
      padding: 20px;
      display: flex;
      justify-content: center;
      transition: all 0.3s ease;
    }

    .preview-frame {
      width: 100%;
      height: 720px;
      border: none;
      background: #FFFFFF;
      border-radius: 8px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
      transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Grid of 5 Variations */
    .variations-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 30px;
      margin-bottom: 50px;
    }

    .variation-card {
      background: var(--card-bg);
      border-radius: 16px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }

    .variation-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.15);
    }

    .card-banner-img {
      position: relative;
      height: 180px;
      background-size: cover;
      background-position: center;
      border-bottom: 4px solid var(--primary);
    }

    .card-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      background: rgba(11, 23, 42, 0.88);
      color: #FFFFFF;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.5px;
      backdrop-filter: blur(8px);
    }

    .card-moto-pill {
      position: absolute;
      bottom: 12px;
      right: 14px;
      background: rgba(0, 0, 0, 0.7);
      color: #38BDF8;
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 700;
      backdrop-filter: blur(8px);
    }

    .card-body {
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .card-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 20px;
      font-weight: 800;
      margin-bottom: 6px;
      color: var(--navy);
    }

    .card-subtitle {
      font-size: 13px;
      font-weight: 600;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }

    .card-desc {
      font-size: 14px;
      color: #475569;
      margin-bottom: 20px;
      flex-grow: 1;
    }

    .palette-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 20px;
      padding: 10px 14px;
      background: #F8FAFC;
      border-radius: 10px;
      border: 1px solid #EDF2F7;
    }

    .palette-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-right: 4px;
    }

    .swatch {
      width: 24px;
      height: 24px;
      border-radius: 6px;
      border: 1px solid rgba(0, 0, 0, 0.15);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .card-sublinks {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 20px;
    }

    .subpage-chip {
      background: #F1F5F9;
      color: #475569;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.15s ease;
    }

    .subpage-chip:hover {
      background: var(--navy);
      color: #FFFFFF;
    }

    .card-actions {
      display: flex;
      gap: 10px;
    }

    .btn-card {
      flex: 1;
      padding: 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      text-align: center;
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .btn-card-primary {
      background: var(--navy);
      color: #FFFFFF;
    }

    .btn-card-primary:hover {
      background: var(--primary);
    }

    .btn-card-preview {
      background: #F1F5F9;
      color: var(--navy);
      border: 1px solid var(--border);
    }

    .btn-card-preview:hover {
      background: #E2E8F0;
    }

    /* Comparison Table */
    .section-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 26px;
      font-weight: 800;
      color: var(--navy);
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .table-container {
      background: #FFFFFF;
      border-radius: 16px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      overflow-x: auto;
      margin-bottom: 50px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 14px;
    }

    th {
      background: #0F172A;
      color: #FFFFFF;
      font-family: 'Montserrat', sans-serif;
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 16px 20px;
    }

    td {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      color: #334155;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:hover td {
      background: #F8FAFC;
    }

    .check-icon {
      color: #16A34A;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <!-- Showcase Header -->
  <header class="showcase-header">
    <div class="header-container">
      <div class="header-top">
        <img src="SCGrazLogo.png" alt="ASVÖ Skiclub Graz Logo" class="header-logo">
        <div class="header-badge">
          <span class="dot"></span> 5 Lokale Website-Varianten Bereit
        </div>
      </div>
      <h1 class="header-title">Design-Modernisierung <span>ASVÖ Skiclub Graz</span></h1>
      <p class="header-desc">
        Neugestaltung von <strong>https://5215.auf.ski/</strong> in 5 eigenständigen, lokalen Design-Varianten.
        Jede Variante verfügt über ein maßgeschneidertes, künstlerisches Banner (nur Startseite), fixes atmosphärisches Hintergrundbild (wie atomic.auf.ski),
        den animierten Vereinsmotto-Ticker <strong>„Ride on - Race on“</strong>, das Trainer-Abzeichen für <strong>Philipp Papst (Ski Austria D-Trainer)</strong>
        sowie saubere externe CSS- und JS-Architektur.
      </p>
      <div class="header-stats">
        <div class="stat-item">
          <span class="stat-num">5</span>
          <span class="stat-label">Lokale Ordner</span>
        </div>
        <div class="stat-item">
          <span class="stat-num">30</span>
          <span class="stat-label">Fertige HTML-Seiten</span>
        </div>
        <div class="stat-item">
          <span class="stat-num">100%</span>
          <span class="stat-label">Offline Nutzbar</span>
        </div>
        <div class="stat-item">
          <span class="stat-num">1974</span>
          <span class="stat-label">Gründungsjahr SC Graz</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="container">

    <!-- Tab Bar for Live Preview Switcher -->
    <div class="tab-bar">
      <button class="tab-btn active" onclick="switchPreview('variation-1-racing-velocity', this)">
        <span class="tab-num">1</span> Racing Velocity
      </button>
      <button class="tab-btn" onclick="switchPreview('variation-2-atomic-pro', this)">
        <span class="tab-num">2</span> Atomic Pro (B&W)
      </button>
      <button class="tab-btn" onclick="switchPreview('variation-3-vandeer-minimal', this)">
        <span class="tab-num">3</span> Van Deer Minimal
      </button>
      <button class="tab-btn" onclick="switchPreview('variation-4-glacier-freeride', this)">
        <span class="tab-num">4</span> Glacier Freeride
      </button>
      <button class="tab-btn" onclick="switchPreview('variation-5-summit-heritage', this)">
        <span class="tab-num">5</span> Summit Heritage
      </button>
    </div>

    <!-- Live Interactive Previewer -->
    <section class="preview-card">
      <div class="preview-toolbar">
        <div class="toolbar-info">
          <span class="toolbar-title" id="preview-title">Variante 1: Alpine Racing Velocity</span>
          <span class="toolbar-badge" id="preview-badge">Live Interaktiv</span>
        </div>
        <div class="toolbar-actions">
          <button class="viewport-btn active" onclick="setViewport('100%', this)">🖥 Desktop</button>
          <button class="viewport-btn" onclick="setViewport('768px', this)">📱 Tablet</button>
          <button class="viewport-btn" onclick="setViewport('390px', this)">📱 Mobile</button>
          <a href="variation-1-racing-velocity/index.html" id="open-full-link" target="_blank" class="open-full-btn">
            ↗ Vollbild öffnen
          </a>
        </div>
      </div>
      <div class="preview-viewport-wrapper">
        <iframe id="preview-frame" class="preview-frame" src="variation-1-racing-velocity/index.html"></iframe>
      </div>
    </section>

    <!-- 5 Variations Detailed Cards -->
    <h2 class="section-title">Übersicht aller 5 Design-Varianten</h2>
    <div class="variations-grid">

      <!-- Card 1 -->
      <article class="variation-card">
        <div class="card-banner-img" style="background-image: url('variation-1-racing-velocity/images/banner.jpg');">
          <span class="card-badge">Variante 1</span>
          <span class="card-moto-pill">Motto: Ride on ⟷ Race on</span>
        </div>
        <div class="card-body">
          <h3 class="card-title">Alpine Racing Velocity</h3>
          <div class="card-subtitle">World Cup Racing Dynamik & ASVÖ Rot</div>
          <p class="card-desc">
            Sportlich-dynamisches Skirenn-Design mit diagonaler Geschwindigkeits-Linienführung, tiefem Nachtblau und leuchtendem ASVÖ-Rot. Philipp Papst (Ski Austria D-Trainer) carvt kraftvoll durch die weiße Gischt.
          </p>
          <div class="palette-row">
            <span class="palette-label">Farben:</span>
            <div class="swatch" style="background:#CA1919;" title="ASVÖ Rot"></div>
            <div class="swatch" style="background:#0C1B33;" title="Racing Navy"></div>
            <div class="swatch" style="background:#4A90E2;" title="Alpinblau"></div>
            <div class="swatch" style="background:#FFFFFF;" title="Schnee-Weiß"></div>
          </div>
          <div class="card-sublinks">
            <a href="variation-1-racing-velocity/index.html" class="subpage-chip">Startseite</a>
            <a href="variation-1-racing-velocity/news.html" class="subpage-chip">News</a>
            <a href="variation-1-racing-velocity/veranstaltungen.html" class="subpage-chip">Termine</a>
            <a href="variation-1-racing-velocity/athleten.html" class="subpage-chip">Athleten</a>
            <a href="variation-1-racing-velocity/sponsoren.html" class="subpage-chip">Sponsoren</a>
            <a href="variation-1-racing-velocity/verein.html" class="subpage-chip">Verein</a>
          </div>
          <div class="card-actions">
            <a href="variation-1-racing-velocity/index.html" class="btn-card btn-card-primary">Website öffnen</a>
            <button onclick="switchPreview('variation-1-racing-velocity')" class="btn-card btn-card-preview">Vorschau</button>
          </div>
        </div>
      </article>

      <!-- Card 2 -->
      <article class="variation-card">
        <div class="card-banner-img" style="background-image: url('variation-2-atomic-pro/images/banner.jpg');">
          <span class="card-badge">Variante 2</span>
          <span class="card-moto-pill">Motto: Ride on ⟷ Race on</span>
        </div>
        <div class="card-body">
          <h3 class="card-title">Atomic ProCenter B&W</h3>
          <div class="card-subtitle">Inspiriert von atomic.auf.ski</div>
          <p class="card-desc">
            Dramatische Schwarz-Weiß-Actionfotografie mit hohem Kontrast, angelehnt an Manuel Fellers Atomic-Hintergrund. Fixes B&W-Slalom-Hintergrundbild mit Glasmorphismus-Inhaltskarten und markanten roten Renn-Akzenten.
          </p>
          <div class="palette-row">
            <span class="palette-label">Farben:</span>
            <div class="swatch" style="background:#E11D48;" title="Atomic Crimson"></div>
            <div class="swatch" style="background:#0B0E14;" title="Tiefschwarz"></div>
            <div class="swatch" style="background:#94A3B8;" title="Platingrau"></div>
            <div class="swatch" style="background:#FFFFFF;" title="Reines Weiß"></div>
          </div>
          <div class="card-sublinks">
            <a href="variation-2-atomic-pro/index.html" class="subpage-chip">Startseite</a>
            <a href="variation-2-atomic-pro/news.html" class="subpage-chip">News</a>
            <a href="variation-2-atomic-pro/veranstaltungen.html" class="subpage-chip">Termine</a>
            <a href="variation-2-atomic-pro/athleten.html" class="subpage-chip">Athleten</a>
            <a href="variation-2-atomic-pro/sponsoren.html" class="subpage-chip">Sponsoren</a>
            <a href="variation-2-atomic-pro/verein.html" class="subpage-chip">Verein</a>
          </div>
          <div class="card-actions">
            <a href="variation-2-atomic-pro/index.html" class="btn-card btn-card-primary">Website öffnen</a>
            <button onclick="switchPreview('variation-2-atomic-pro')" class="btn-card btn-card-preview">Vorschau</button>
          </div>
        </div>
      </article>

      <!-- Card 3 -->
      <article class="variation-card">
        <div class="card-banner-img" style="background-image: url('variation-3-vandeer-minimal/images/banner.jpg');">
          <span class="card-badge">Variante 3</span>
          <span class="card-moto-pill">Motto: Ride on ⟷ Race on</span>
        </div>
        <div class="card-body">
          <h3 class="card-title">Van Deer Refined Alpine</h3>
          <div class="card-subtitle">Inspiriert von vandeer-redbull-sports.auf.ski</div>
          <p class="card-desc">
            Edle alpine Schlichtheit: Nahtlos in die Bergkette übergehendes Panoramabild, dezente Schieferanthrazit-Menüleiste (navbar-style-with-bgcolor), serifenbetonte Typografie und dezentes Vereinswappen-Badge.
          </p>
          <div class="palette-row">
            <span class="palette-label">Farben:</span>
            <div class="swatch" style="background:#991B1B;" title="Rubinrot"></div>
            <div class="swatch" style="background:#1E252B;" title="Van Deer Schiefer"></div>
            <div class="swatch" style="background:#64748B;" title="Mattes Silber"></div>
            <div class="swatch" style="background:#F7F6F2;" title="Alabaster"></div>
          </div>
          <div class="card-sublinks">
            <a href="variation-3-vandeer-minimal/index.html" class="subpage-chip">Startseite</a>
            <a href="variation-3-vandeer-minimal/news.html" class="subpage-chip">News</a>
            <a href="variation-3-vandeer-minimal/veranstaltungen.html" class="subpage-chip">Termine</a>
            <a href="variation-3-vandeer-minimal/athleten.html" class="subpage-chip">Athleten</a>
            <a href="variation-3-vandeer-minimal/sponsoren.html" class="subpage-chip">Sponsoren</a>
            <a href="variation-3-vandeer-minimal/verein.html" class="subpage-chip">Verein</a>
          </div>
          <div class="card-actions">
            <a href="variation-3-vandeer-minimal/index.html" class="btn-card btn-card-primary">Website öffnen</a>
            <button onclick="switchPreview('variation-3-vandeer-minimal')" class="btn-card btn-card-preview">Vorschau</button>
          </div>
        </div>
      </article>

      <!-- Card 4 -->
      <article class="variation-card">
        <div class="card-banner-img" style="background-image: url('variation-4-glacier-freeride/images/banner.jpg');">
          <span class="card-badge">Variante 4</span>
          <span class="card-moto-pill">Motto: Ride on ⟷ Race on</span>
        </div>
        <div class="card-body">
          <h3 class="card-title">Glacier Freeride & Jump</h3>
          <div class="card-subtitle">Fokus auf Freeride & Jump (Ride on)</div>
          <p class="card-desc">
            Doppel-Action-Konzept: Der Freerider aus jump.jpg springt links majestätisch in den tiefblauen Himmel („Ride on“), während Philipp Papst rechts („Race on“) präzise carvt. Frisches Gletscher-Cyan und leuchtende Glow-Effekte.
          </p>
          <div class="palette-row">
            <span class="palette-label">Farben:</span>
            <div class="swatch" style="background:#00A3E0;" title="Gletscher-Cyan"></div>
            <div class="swatch" style="background:#081B38;" title="Gletschernacht"></div>
            <div class="swatch" style="background:#CA1919;" title="SCG Rot"></div>
            <div class="swatch" style="background:#F0F9FF;" title="Eisweiß"></div>
          </div>
          <div class="card-sublinks">
            <a href="variation-4-glacier-freeride/index.html" class="subpage-chip">Startseite</a>
            <a href="variation-4-glacier-freeride/news.html" class="subpage-chip">News</a>
            <a href="variation-4-glacier-freeride/veranstaltungen.html" class="subpage-chip">Termine</a>
            <a href="variation-4-glacier-freeride/athleten.html" class="subpage-chip">Athleten</a>
            <a href="variation-4-glacier-freeride/sponsoren.html" class="subpage-chip">Sponsoren</a>
            <a href="variation-4-glacier-freeride/verein.html" class="subpage-chip">Verein</a>
          </div>
          <div class="card-actions">
            <a href="variation-4-glacier-freeride/index.html" class="btn-card btn-card-primary">Website öffnen</a>
            <button onclick="switchPreview('variation-4-glacier-freeride')" class="btn-card btn-card-preview">Vorschau</button>
          </div>
        </div>
      </article>

      <!-- Card 5 -->
      <article class="variation-card">
        <div class="card-banner-img" style="background-image: url('variation-5-summit-heritage/images/banner.jpg');">
          <span class="card-badge">Variante 5</span>
          <span class="card-moto-pill">Motto: Ride on ⟷ Race on</span>
        </div>
        <div class="card-body">
          <h3 class="card-title">Styrian Summit Heritage</h3>
          <div class="card-subtitle">50+ Jahre Vereinstradition & Alpenglow</div>
          <p class="card-desc">
            Warme Abendsonne am Berggipfel mit goldenem Alpenglühen, das die Schneekristalle erleuchtet. Gedenk-Badge „50+ Jahre SC Graz (1974–2024)“, steirische Alpentradition und klassisches österreichisches Rot-Weiß-Rot.
          </p>
          <div class="palette-row">
            <span class="palette-label">Farben:</span>
            <div class="swatch" style="background:#C8102E;" title="Österreich Rot"></div>
            <div class="swatch" style="background:#D97706;" title="Alpenglow Gold"></div>
            <div class="swatch" style="background:#14221A;" title="Zirbentanne"></div>
            <div class="swatch" style="background:#FFFBEB;" title="Warmer Schnee"></div>
          </div>
          <div class="card-sublinks">
            <a href="variation-5-summit-heritage/index.html" class="subpage-chip">Startseite</a>
            <a href="variation-5-summit-heritage/news.html" class="subpage-chip">News</a>
            <a href="variation-5-summit-heritage/veranstaltungen.html" class="subpage-chip">Termine</a>
            <a href="variation-5-summit-heritage/athleten.html" class="subpage-chip">Athleten</a>
            <a href="variation-5-summit-heritage/sponsoren.html" class="subpage-chip">Sponsoren</a>
            <a href="variation-5-summit-heritage/verein.html" class="subpage-chip">Verein</a>
          </div>
          <div class="card-actions">
            <a href="variation-5-summit-heritage/index.html" class="btn-card btn-card-primary">Website öffnen</a>
            <button onclick="switchPreview('variation-5-summit-heritage')" class="btn-card btn-card-preview">Vorschau</button>
          </div>
        </div>
      </article>

    </div>

    <!-- Requirements Comparison Table -->
    <h2 class="section-title">Anforderungs-Matrix gemäß Briefing</h2>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Anforderung</th>
            <th>V1: Racing Velocity</th>
            <th>V2: Atomic Pro (B&W)</th>
            <th>V3: Van Deer Minimal</th>
            <th>V4: Glacier Freeride</th>
            <th>V5: Summit Heritage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>5 Lokale Ordner</strong></td>
            <td><span class="check-icon">✓</span> variation-1-...</td>
            <td><span class="check-icon">✓</span> variation-2-...</td>
            <td><span class="check-icon">✓</span> variation-3-...</td>
            <td><span class="check-icon">✓</span> variation-4-...</td>
            <td><span class="check-icon">✓</span> variation-5-...</td>
          </tr>
          <tr>
            <td><strong>Künstlerisches Banner</strong></td>
            <td><span class="check-icon">✓</span> Diagonale Renn-Linien</td>
            <td><span class="check-icon">✓</span> Reines S/W Drama</td>
            <td><span class="check-icon">✓</span> Berggipfel-Panorama</td>
            <td><span class="check-icon">✓</span> Jump & Carve Dual</td>
            <td><span class="check-icon">✓</span> Goldenes Alpenglühen</td>
          </tr>
          <tr>
            <td><strong>Banner NUR auf Hauptseite</strong></td>
            <td><span class="check-icon">✓</span> Exklusiv auf index.html</td>
            <td><span class="check-icon">✓</span> Exklusiv auf index.html</td>
            <td><span class="check-icon">✓</span> Exklusiv auf index.html</td>
            <td><span class="check-icon">✓</span> Exklusiv auf index.html</td>
            <td><span class="check-icon">✓</span> Exklusiv auf index.html</td>
          </tr>
          <tr>
            <td><strong>Philipp Papst Trainer-Badge</strong></td>
            <td><span class="check-icon">✓</span> Ski Austria D-Trainer</td>
            <td><span class="check-icon">✓</span> Ski Austria D-Trainer</td>
            <td><span class="check-icon">✓</span> Ski Austria D-Trainer</td>
            <td><span class="check-icon">✓</span> Ski Austria D-Trainer</td>
            <td><span class="check-icon">✓</span> Ski Austria D-Trainer</td>
          </tr>
          <tr>
            <td><strong>Motto „Ride on - Race on“</strong></td>
            <td><span class="check-icon">✓</span> Animierter Ticker (3.5s)</td>
            <td><span class="check-icon">✓</span> Animierter Ticker (3.5s)</td>
            <td><span class="check-icon">✓</span> Animierter Ticker (3.5s)</td>
            <td><span class="check-icon">✓</span> Animierter Ticker (3.5s)</td>
            <td><span class="check-icon">✓</span> Animierter Ticker (3.5s)</td>
          </tr>
          <tr>
            <td><strong>Farben passen zum Logo</strong></td>
            <td><span class="check-icon">✓</span> ASVÖ Rot & Racing Blau</td>
            <td><span class="check-icon">✓</span> Slalom Rot & Schiefer</td>
            <td><span class="check-icon">✓</span> Muted Rot & Alpin-Grau</td>
            <td><span class="check-icon">✓</span> Cyan, Blau & SCG Rot</td>
            <td><span class="check-icon">✓</span> Gold & Österreich Rot</td>
          </tr>
          <tr>
            <td><strong>CSS & JS extern ausgelagert</strong></td>
            <td><span class="check-icon">✓</span> css/theme.css & js/theme.js</td>
            <td><span class="check-icon">✓</span> css/theme.css & js/theme.js</td>
            <td><span class="check-icon">✓</span> css/theme.css & js/theme.js</td>
            <td><span class="check-icon">✓</span> css/theme.css & js/theme.js</td>
            <td><span class="check-icon">✓</span> css/theme.css & js/theme.js</td>
          </tr>
        </tbody>
      </table>
    </div>

  </main>

  <script>
    const variationMeta = {
      'variation-1-racing-velocity': { title: 'Variante 1: Alpine Racing Velocity', badge: 'World Cup Dynamik' },
      'variation-2-atomic-pro': { title: 'Variante 2: Atomic ProCenter B&W', badge: 'Monochrome High-Contrast' },
      'variation-3-vandeer-minimal': { title: 'Variante 3: Van Deer Refined Alpine', badge: 'Editorial Luxury' },
      'variation-4-glacier-freeride': { title: 'Variante 4: Glacier Freeride & Jump', badge: 'Big-Air Freeride' },
      'variation-5-summit-heritage': { title: 'Variante 5: Styrian Summit Heritage', badge: '50+ Jahre Tradition' }
    };

    function switchPreview(folder, tabElement) {
      const frame = document.getElementById('preview-frame');
      const title = document.getElementById('preview-title');
      const badge = document.getElementById('preview-badge');
      const openLink = document.getElementById('open-full-link');

      frame.src = folder + '/index.html';
      openLink.href = folder + '/index.html';

      if (variationMeta[folder]) {
        title.innerText = variationMeta[folder].title;
        badge.innerText = variationMeta[folder].badge;
      }

      if (tabElement) {
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        tabElement.classList.add('active');
      }
    }

    function setViewport(width, btnElement) {
      const frame = document.getElementById('preview-frame');
      frame.style.width = width;
      document.querySelectorAll('.viewport-btn').forEach(btn => btn.classList.remove('active'));
      btnElement.classList.add('active');
    }
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_hub)

print("Showcase index.html successfully generated!")
