"""Static site generator for jonathandigiorgio.com.

Run:  python build.py
Writes index.html, projects/<slug>/index.html, 404.html and resized images in assets/img/.
Source images live in _src/. Content lives in content.py.
"""
import html
import os
import shutil

from PIL import Image

import content as C

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "_src")
OUT_IMG = os.path.join(ROOT, "assets", "img")
SITE = "https://www.jonathandigiorgio.com"

# --------------------------------------------------------------------------- images

_meta = {}


def process_images():
    os.makedirs(OUT_IMG, exist_ok=True)
    wanted = set()
    for key, spec in C.IMAGES.items():
        src = os.path.join(SRC, spec["src"])
        im = Image.open(src).convert("RGB")
        if spec.get("crop"):
            l, t, r, b = spec["crop"]
            W, H = im.size
            im = im.crop((int(l * W), int(t * H), int(r * W), int(b * H)))
        W, H = im.size
        widths = [w for w in spec.get("widths", (800, 1600)) if w < W]
        widths.append(min(W, max(spec.get("widths", (800, 1600)))))
        widths = sorted(set(widths))
        files = []
        for w in widths:
            name = f"{key}-{w}.webp"
            wanted.add(name)
            path = os.path.join(OUT_IMG, name)
            if not os.path.exists(path) or os.path.getmtime(path) < os.path.getmtime(src) or os.path.getmtime(path) < os.path.getmtime(os.path.join(ROOT, "content.py")):
                h = round(H * w / W)
                im.resize((w, h), Image.LANCZOS).save(path, "WEBP", quality=spec.get("q", 80), method=6)
            files.append((w, name))
        _meta[key] = {"w": W, "h": H, "files": files}
    for f in os.listdir(OUT_IMG):
        if f not in wanted:
            os.remove(os.path.join(OUT_IMG, f))


def img(key, alt, sizes="100vw", cls="", eager=False, prefix=""):
    m = _meta[key]
    srcset = ", ".join(f"{prefix}assets/img/{n} {w}w" for w, n in m["files"])
    default = m["files"][min(1, len(m["files"]) - 1)][1] if len(m["files"]) > 1 else m["files"][0][1]
    attrs = [
        f'src="{prefix}assets/img/{default}"',
        f'srcset="{srcset}"',
        f'sizes="{sizes}"',
        f'width="{m["w"]}" height="{m["h"]}"',
        f'alt="{html.escape(alt, quote=True)}"',
        'decoding="async"',
        'fetchpriority="high"' if eager else 'loading="lazy"',
    ]
    if cls:
        attrs.append(f'class="{cls}"')
    return f"<img {' '.join(attrs)}>"


def largest(key, prefix=""):
    return f"{prefix}assets/img/{_meta[key]['files'][-1][1]}"


def plate(key, alt, caption="", n=None, prefix="", sizes="(min-width: 1100px) 900px, 100vw", fill=False, zoom=True, cls=""):
    """A figure on a neutral plate. Small images are never stretched past native width."""
    m = _meta[key]
    inner = img(key, alt, sizes=sizes, prefix=prefix)
    style = "" if fill else f' style="--nat:{m["w"]}px"'
    if zoom:
        inner = f'<a class="zoom" href="{largest(key, prefix)}" data-caption="{html.escape(caption, quote=True)}" aria-label="Open full size: {html.escape(alt, quote=True)}">{inner}</a>'
    label = f'<span class="fig-n">FIG. {n}</span> ' if n else ""
    cap = f"<figcaption>{label}{caption}</figcaption>" if caption or n else ""
    klass = "plate" + (" fill" if fill else "") + (f" {cls}" if cls else "")
    return f'<figure class="{klass}"{style}>{inner}{cap}</figure>'


# --------------------------------------------------------------------------- layout

FONTS = "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Schibsted+Grotesk:wght@400;500;600&display=swap"


def head(title, desc, prefix, path, og_img):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<meta name="color-scheme" content="light dark">
<script>document.documentElement.classList.add("js")</script>
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:image" content="{SITE}/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="{prefix}favicon-32x32.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{prefix}assets/site.css?v={C.VERSION}">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ZJ9CX0GBKX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-ZJ9CX0GBKX');</script>
</head>
<body id="top">
<a class="skip" href="#main">Skip to content</a>
"""


def header(prefix, current=""):
    home = prefix or "./"
    def nav(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<header class="site-head">
  <div class="wrap head-row">
    <a class="wordmark" href="{home}">Jonathan Di Giorgio</a>
    <nav class="nav" aria-label="Main">
      {nav(home + "#work", "Work", "work")}
      {nav(home + "#projects", "Projects", "projects")}
      {nav(home + "#about", "About", "about")}
      <a class="nav-cta" href="{prefix}{C.RESUME}" target="_blank" rel="noopener">Résumé <span aria-hidden="true">↗</span></a>
    </nav>
  </div>
</header>
"""


def footer(prefix):
    return f"""<footer class="site-foot" id="contact">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <p class="foot-line">I'm looking for full-time robotics and mechanical design roles starting summer 2027.</p>
        <a class="foot-mail" href="mailto:{C.EMAIL}">{C.EMAIL}</a>
      </div>
      <ul class="foot-links">
        <li><a href="{C.LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="{prefix}{C.RESUME}" target="_blank" rel="noopener">Résumé (PDF)</a></li>
        <li><a href="{C.GITHUB}" target="_blank" rel="noopener">GitHub</a></li>
      </ul>
    </div>
    <div class="foot-base"><span>© 2026 Jonathan Di Giorgio</span><a href="#top">Back to top ↑</a></div>
  </div>
</footer>
<dialog class="lightbox" aria-label="Image viewer">
  <button class="lb-close" type="button">Close</button>
  <button class="lb-prev" type="button" aria-label="Previous image">←</button>
  <figure><img alt=""><figcaption></figcaption></figure>
  <button class="lb-next" type="button" aria-label="Next image">→</button>
</dialog>
<script src="{prefix}assets/site.js?v={C.VERSION}" defer></script>
</body>
</html>
"""


# --------------------------------------------------------------------------- home

def build_home():
    p = ""
    out = [head("Jonathan Di Giorgio · Mechanical engineer, robotics", C.SITE_DESC, p, "/", largest("hero"))]
    out.append(header(p))
    out.append('<main id="main">')

    # hero
    balloons = "".join(
        f'<a class="balloon" href="projects/axon-v2/#{b["href"]}" style="--x:{b["x"]}%;--y:{b["y"]}%" data-b="{i}" aria-label="{i}. {html.escape(b["label"])}"><span>{i}</span></a>'
        for i, b in enumerate(C.BALLOONS, 1)
    )
    legend = "".join(
        f'<li><a href="projects/axon-v2/#{b["href"]}" data-b="{i}"><span class="bn">{i}</span><span class="bl">{b["label"]}</span><span class="bs">{b["spec"]}</span></a></li>'
        for i, b in enumerate(C.BALLOONS, 1)
    )
    tb = "".join(f'<div class="tb-cell"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in C.TITLE_BLOCK)
    out.append(f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div class="hero-text">
        <h1>Jonathan Di Giorgio</h1>
        <p class="pitch">{C.PITCH}</p>
        <p class="hero-sub">{C.HERO_SUB}</p>
        <div class="hero-links">
          <a class="btn" href="{C.RESUME}" target="_blank" rel="noopener">Résumé (PDF)</a>
          <a class="btn ghost" href="mailto:{C.EMAIL}">Email me</a>
          <a class="text-link" href="{C.LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
        </div>
      </div>
      <dl class="title-block" aria-label="Summary">{tb}</dl>
    <figure class="hero-fig">
      <div class="hero-img">
        {img("hero", "Axon V2, a grey six-axis robot arm with a two-finger gripper, on a wooden ledge", sizes="(min-width: 1280px) 1200px, 100vw", eager=True)}
        {balloons}
      </div>
      <figcaption class="hero-cap">
        <div class="hero-cap-head"><span class="fig-n">FIG. 1</span> Axon V2, the 6-DOF arm I built. 3 kg payload, 690 mm reach, about 1 mm repeatability, $297 in parts. <a href="projects/axon-v2/">See how it's built</a></div>
        <ol class="legend">{legend}</ol>
      </figcaption>
    </figure>
    </div>
  </div>
</section>
""")

    # experience
    roles = []
    for r in C.ROLES:
        figs = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in r.get("figures", []))
        figs = f'<dl class="figures">{figs}</dl>' if figs else ""
        pts = "".join(f"<li>{x}</li>" for x in r["points"])
        link = f'<p class="role-link"><a href="{r["link"][0]}">{r["link"][1]}</a></p>' if r.get("link") else ""
        quote = ""
        if r.get("quote"):
            quote = f'<blockquote class="rec"><p>"{r["quote"][0]}"</p><cite>{r["quote"][1]}</cite></blockquote>'
        roles.append(f"""
      <article class="role">
        <div class="role-co">
          <h3>{r["company"]}</h3>
          <p class="role-when">{r["dates"]}<br>{r["place"]}</p>
        </div>
        <div class="role-body">
          <p class="role-title">{r["title"]}</p>
          <p class="role-lead">{r["lead"]}</p>
          {figs}
          <details class="role-more">
            <summary>What I did</summary>
            <ul class="ticks">{pts}</ul>
            {quote}
            <p class="tools">{r["tools"]}</p>
          </details>
          {link}
        </div>
      </article>""")
    teams = "".join(
        f'<li><span class="t-name">{t["name"]}</span><span class="t-role">{t["role"]}</span><span class="t-when">{t["dates"]}</span>'
        + (f'<a class="t-link" href="{t["href"]}">{t["link"]}</a>' if t.get("href") else f'<span class="t-note">{t["note"]}</span>')
        + "</li>"
        for t in C.TEAMS
    )
    out.append(f"""
<section class="section" id="work">
  <div class="wrap">
    <header class="sec-head">
      <h2>Work</h2>
      <p>{C.WORK_INTRO}</p>
    </header>
    <div class="roles">{"".join(roles)}
    </div>
    <div class="teams">
      <h3 class="sub-h">Student design teams</h3>
      <ul class="team-list">{teams}</ul>
    </div>
  </div>
</section>
""")

    # projects index
    rows, previews = [], []
    for i, pr in enumerate(C.PROJECTS, 1):
        cover = pr.get("index_cover", pr["cover"])
        thumb = img(cover, "", sizes="96px", cls="row-thumb") if cover else '<span class="row-thumb ph"></span>'
        rows.append(f"""
        <li><a class="row" href="projects/{pr["slug"]}/" data-i="{i - 1}">
          <span class="row-n">{i:02d}</span>
          {thumb}
          <span class="row-main"><span class="row-k">{pr["kind"]}</span><span class="row-t">{pr["title"]}</span><span class="row-d">{pr["short"]}</span></span>
          <span class="row-go" aria-hidden="true">→</span>
        </a></li>""")
        if cover:
            pv = img(cover, pr["cover_alt"], sizes="(min-width: 1100px) 560px, 50vw")
        else:
            pv = C.COLLAR_SVG
        fitcls = " contain" if pr.get("fit") == "contain" else ""
        previews.append(f'<figure class="pv{fitcls}{" on" if i == 1 else ""}" data-i="{i - 1}"><div class="pv-img">{pv}</div><figcaption><span class="fig-n">{i:02d}</span> {pr["fact"]}</figcaption></figure>')
    out.append(f"""
<section class="section" id="projects">
  <div class="wrap">
    <header class="sec-head">
      <h2>Projects</h2>
      <p>{C.PROJECTS_INTRO}</p>
    </header>
    <div class="index">
      <ol class="rows">{"".join(rows)}
      </ol>
      <div class="preview" aria-hidden="true">{"".join(previews)}</div>
    </div>
  </div>
</section>
""")

    # about
    awards = "".join(f"<li>{a}</li>" for a in C.AWARDS)
    certs = "".join(f"<li>{a}</li>" for a in C.CERTS)
    skills = "".join(f"<div><h4>{k}</h4><p>{v}</p></div>" for k, v in C.SKILLS)
    bio = "".join(f"<p>{x}</p>" for x in C.BIO)
    out.append(f"""
<section class="section" id="about">
  <div class="wrap">
    <header class="sec-head">
      <h2>About</h2>
    </header>
    <div class="about">
      <div class="bio">{bio}</div>
      <div class="edu">
        <h3>University of Waterloo</h3>
        <p class="edu-deg">BASc, Mechanical Engineering, Mechatronics option<br>Sept 2022 to April 2027</p>
        <p class="edu-avg"><span>96.0%</span> cumulative average</p>
        <h4>Awards</h4><ul class="plain">{awards}</ul>
        <h4>Certifications</h4><ul class="plain">{certs}</ul>
      </div>
    </div>
    <div class="skills">{skills}</div>
  </div>
</section>
""")
    out.append("</main>")
    out.append(footer(p))
    write("index.html", "".join(out))


# --------------------------------------------------------------------------- project pages

def build_project(i, pr):
    p = "../../"
    slug = pr["slug"]
    og = largest(pr["cover"]) if pr["cover"] else largest("hero")
    out = [head(f'{pr["title"]} · Jonathan Di Giorgio', pr["short"], p, f"/projects/{slug}/", og)]
    out.append(header(p, "projects"))
    meta = "".join(f'<div class="tb-cell"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in pr["meta"])
    figs = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in pr.get("figures", []))
    figs = f'<dl class="figures big">{figs}</dl>' if figs else ""
    if "hero_html" in pr:
        hero = pr["hero_html"]
    elif pr["cover"]:
        hero = plate(pr.get("hero", pr["cover"]), pr["cover_alt"], pr.get("hero_caption", ""), n=1, prefix=p, fill=pr.get("hero_fill", True), sizes="(min-width: 1280px) 1200px, 100vw")
    else:
        hero = ""
    body = pr["body"](lambda *a, **k: plate(*a, prefix=p, **k), p)
    links = "".join(f'<a href="{(p + h) if not h.startswith("http") else h}" target="_blank" rel="noopener">{t}</a>' for t, h in pr.get("links", []))
    links = f'<div class="ext">{links}</div>' if links else ""
    prev_p = C.PROJECTS[i - 1]
    next_p = C.PROJECTS[(i + 1) % len(C.PROJECTS)]
    out.append(f"""<main id="main" class="proj">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{p}#projects">← All projects</a><span>{i + 1:02d} of {len(C.PROJECTS):02d}</span></nav>
    <header class="proj-head">
      <p class="proj-kind">{pr["kind"]}</p>
      <h1>{pr["title"]}</h1>
      <p class="proj-lede">{pr["lede"]}</p>
    </header>
    <div class="proj-facts">
      <dl class="title-block compact">{meta}</dl>
      {figs}
    </div>
  </div>
  <div class="wrap proj-hero">{hero}</div>
  <div class="wrap proj-body">
    {body}
    {links}
  </div>
  <nav class="wrap pager" aria-label="More projects">
    <a href="{p}projects/{prev_p["slug"]}/"><span>Previous</span>{prev_p["title"]}</a>
    <a href="{p}projects/{next_p["slug"]}/" class="next"><span>Next</span>{next_p["title"]}</a>
  </nav>
</main>
""")
    out.append(footer(p))
    write(f"projects/{slug}/index.html", "".join(out))


def build_404():
    p = "/"
    out = [head("Page not found · Jonathan Di Giorgio", C.SITE_DESC, p, "/404", largest("hero"))]
    out.append(header(p))
    out.append(f"""<main id="main" class="proj"><div class="wrap nf">
<h1>That page doesn't exist.</h1>
<p>It may have moved when I rebuilt the site. <a href="/">Go to the home page</a> or <a href="/#projects">browse projects</a>.</p>
</div></main>""")
    out.append(footer(p))
    write("404.html", "".join(out))


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    process_images()
    C.bind(img=img, largest=largest)
    if os.path.isdir(os.path.join(ROOT, "projects")):
        shutil.rmtree(os.path.join(ROOT, "projects"))
    build_home()
    for i, pr in enumerate(C.PROJECTS):
        build_project(i, pr)
    build_404()
    urls = ["/"] + [f"/projects/{p['slug']}/" for p in C.PROJECTS]
    NL = "\n"
    locs = "".join(f"  <url><loc>{SITE}{u}</loc></url>{NL}" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>{NL}<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{NL}{locs}</urlset>{NL}')
    write("robots.txt", f"User-agent: *{NL}Allow: /{NL}Sitemap: {SITE}/sitemap.xml{NL}")
    print("built", 2 + len(C.PROJECTS), "pages,", sum(len(m["files"]) for m in _meta.values()), "images")
