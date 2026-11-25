# Design notes

## What makes a site read as AI-built (researched 2026-11-24)

Sources: 925 Studios ("AI slop fonts and gradients", "AI slop web design guide"), Utsubo ("The built-with-AI tell"), MindStudio and Aura ("avoid vibe-coded landing pages"), the Laith0003 ux-skill "Anti AI slop ban list", Built In ("AI makes bad design look good enough"), plus Wikipedia's "Signs of AI writing" for copy.

Visual tells
- Inter (or another system grotesk) for everything, with no deliberate type pairing
- Purple to blue gradients, gradient text, and gradient blobs or mesh backgrounds as wallpaper
- Glassmorphism cards (frosted blur, translucent white borders) and soft drop-shadow cards everywhere
- The stock SaaS skeleton: centered hero, three rounded feature cards in a row, logo strip, testimonial carousel, CTA band
- Oversized pill "eyebrow" labels above every heading that add no information
- Emoji or icon bullets, sparkle icons, a green "available for work" pulsing dot
- Hover effects on everything (tilt, glow, lift) that do nothing useful
- Dark mode with neon accents as the default "tech" look
- Skill bars and percentage meters ("Python 85%")
- Huge rounded corners on everything, identical radius and spacing on every element
- Stock or generated imagery instead of the person's own work
- Animated counters and scroll-triggered fade-ins on every block

Copy tells
- Generic hero lines ("Hi, I'm X, a passionate engineer who loves solving problems")
- Contrasts that add weight but no fact ("not just X, but Y"), one-line closers, forced groups of three
- Inflated words (seamless, robust, cutting-edge, passionate, leverage, showcase, delve)
- Bold labels with colons on every list item, em dashes everywhere
- Services sections and claims nobody can check

## What this site does instead ("from the bench", redesigned 2026-11-24 with the frontend-design plugin)
- Palette taken from Axon V2 itself: graphite `#22252A` ink, bench white `#F3F4F2`, arm grey `#6F737A`, bearing blue `#9EC3DB` (the arm's pale-blue caps; used only on interactive things), birch `#D8B98A` (the ledge in the hero photo). Dark mode keeps the same roles.
- One family, Archivo, using its width axis: wide and heavy for headings (like part numbers stamped into a casting), normal width for reading, semi-condensed for small labels. Tabular figures for numbers instead of a monospace face. No all-caps labels.
- The hero photo is the one bold element: it opens the page, and a birch band starts at the photo's ledge and carries the legend, so the arm sits on the page. Numbered balloons stay because they map to real subsystems.
- Work is a timeline (dates, a rail with a node per role, stats always visible). Project index numbering, FIG. labels and appended arrows were removed, since the content isn't a sequence.
- Real photos and CAD from the work, shown on neutral plates at their native resolution so nothing gets stretched
- Small 3–4 px radii, few rules, no shadows
- Interaction only where it helps: the project index previews each project's image, the Axon V2 explorer switches subsystems, images open full size
- Every project is two clicks from the home page (home, then project)
- Copy follows Profile/writing-style.md and was run through the humanizer checklist
