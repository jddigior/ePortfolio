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

## What this site does instead
- Type pairing chosen for the job: Newsreader (a text serif with optical sizes) for display, Schibsted Grotesk for UI and body, IBM Plex Mono only for figure numbers and specs
- Warm paper background, near-black ink, one oxide-orange accent used for callout balloons and links. No gradients.
- Engineering-drawing language where it carries information: numbered balloon callouts on the hero photo (like a BOM), a title block for the key facts, figures labelled FIG. 1, 2, 3
- Real photos and CAD from the work, shown on neutral plates at their native resolution so nothing gets stretched
- Square corners, hairline rules, no card shadows
- Interaction only where it helps: the project index previews each project's image, the Axon V2 explorer switches subsystems, images open full size
- Every project is two clicks from the home page (home, then project)
- Copy follows Profile/writing-style.md and was run through the humanizer checklist
