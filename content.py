"""All site copy and image definitions. Facts come from ../Experience and ../Projects."""

VERSION = "20261124b"
EMAIL = "jonathan.digiorgio04@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/j-digiorgio/"
GITHUB = "https://github.com/jddigior"
RESUME = "assets/docs/Jonathan_DiGiorgio_Resume.pdf"

SITE_DESC = ("Jonathan Di Giorgio is a mechanical engineer who designs robots and automation. "
             "Internships at Neuralink, Tesla and Pratt & Whitney Canada. University of Waterloo, graduating April 2027.")

_img = _largest = None


def bind(img, largest):
    global _img, _largest
    _img, _largest = img, largest


# --------------------------------------------------------------------------- images
# key: src file in _src, optional crop (l, t, r, b as fractions), widths
IMAGES = {
    "hero": {"src": "axon-v2_web_main-photo.webp", "widths": (700, 1100, 1377), "q": 78},
    "axon-labelled": {"src": "axon-v2_web_6dof-labelled.webp", "widths": (800, 1500)},
    "axon-base": {"src": "axon-v2_web_rotating-base.webp", "widths": (800, 1500)},
    "axon-cycloidal": {"src": "axon-v2_web_cycloidal-gearbox.webp", "widths": (800, 1500)},
    "axon-planetary": {"src": "axon-v2_web_planetary-gearbox.webp", "widths": (800, 1500)},
    "axon-wrist": {"src": "axon-v2_web_wrist-differential.webp", "widths": (800, 1500)},
    "axon-gripper": {"src": "axon-v2_web_end-effector.webp", "widths": (800, 1500)},
    "axon-iterations": {"src": "axon-v2_web_design-iterations.webp", "widths": (800, 1500)},
    "axon-panels": {"src": "axon-v2_web_panels-removed.webp", "widths": (700, 1200)},
    "ax-workspace": {"src": "ax_workspace.webp", "crop": (.02, .02, .98, .98), "widths": (800, 1600)},
    "ax-stop-shoulder": {"src": "ax_stop_shoulder.webp", "widths": (700, 1190)},
    "ax-stop-elbow": {"src": "ax_stop_elbow.webp", "widths": (800, 1600)},
    "ax-dexterity": {"src": "ax_dexterity.webp", "widths": (800, 1600)},
    "ax-repeat": {"src": "ax_repeat.webp", "widths": (854,)},
    "ax-torque": {"src": "ax_torque.webp", "widths": (1414,)},
    "ax-electrical": {"src": "ax_electrical.webp", "widths": (790,)},
    "ax-render-internal": {"src": "ax_render_internal.webp", "widths": (673,)},
    "ax-grip-benchy": {"src": "ax_grip_benchy.webp", "widths": (400, 700)},
    "ax-grip-glasses": {"src": "ax_grip_glasses.webp", "widths": (400, 700)},
    "ax-grip-billiard": {"src": "ax_grip_billiard.webp", "widths": (400, 700)},
    "ax-grip-egg": {"src": "ax_grip_egg.webp", "widths": (400, 700)},
    "ax-grip-pencil": {"src": "ax_grip_pencil.webp", "widths": (400, 700)},
    "ax-grip-mouse": {"src": "ax_grip_mouse.webp", "widths": (400, 700)},
    "ax-grip-brush": {"src": "ax_grip_brush.webp", "widths": (400, 700)},
    "ax-grip-speaker": {"src": "ax_grip_speaker.webp", "widths": (400, 700)},
    "ax-grip-tape": {"src": "ax_grip_tape.webp", "widths": (400, 700)},
    "ax-grip-knife": {"src": "ax_grip_knife.webp", "widths": (400, 700)},
    "axon-folded": {"src": "axon-v2_web_folded-over.webp", "crop": (0, .1, 1, .9), "widths": (700, 1200)},
    "v1-exploded": {"src": "v1_exploded.webp", "crop": (.02, .02, .98, .98), "widths": (800, 1600)},
    "v1-built": {"src": "v1_built.webp", "crop": (0, .06, 1, .94), "widths": (700, 1200)},
    "v1-section": {"src": "v1_section.webp", "crop": (.03, .02, .97, .98), "widths": (700, 1200)},
    "v1-electronics": {"src": "v1_electronics.webp", "crop": (0, .05, 1, .95), "widths": (700, 1200)},
    "v1-internals": {"src": "v1_internals.webp", "widths": (603,)},
    "v1-rig": {"src": "v1_rig.webp", "crop": (0, 0, 1, .82), "widths": (700, 1200)},
    "v1-render": {"src": "v1_render.webp", "crop": (.3, 0, .7, 1), "widths": (432,)},
    "chess-cover": {"src": "orig_chessrobot.webp", "crop": (0, .12, 1, .87), "widths": (700, 1400)},
    "chess-setup": {"src": "chess-robot_1.webp", "widths": (908,)},
    "chess-cad": {"src": "chess-robot_3.webp", "widths": (768,)},
    "cyclo-run": {"src": "cycloidal-drive_2.webp", "widths": (363,)},
    "cyclo-section": {"src": "cycloidal-drive_1.webp", "widths": (651,)},
    "light-cover": {"src": "orig_lightflipper.webp", "crop": (.04, .08, .96, .92), "widths": (700, 1400)},
    "light-mounted": {"src": "light-flicker_1.webp", "widths": (432,)},
    "light-side": {"src": "light-flicker_3.webp", "widths": (432,)},
    "light-lit": {"src": "light-flicker_4.webp", "widths": (432,)},
    "vd-path": {"src": "vehicle-dynamics_1.webp", "widths": (418,)},
    "vd-sweep": {"src": "vehicle-dynamics_2.webp", "widths": (417,)},
    "vent-cover": {"src": "orig_vent.webp", "crop": (0, .1, 1, .85), "widths": (700, 1400)},
    "vent-compare": {"src": "vent-flap_2.webp", "widths": (779,)},
    "vent-cad": {"src": "vent-flap_3.webp", "crop": (.15, 0, .85, 1), "widths": (538,)},
    "pw-1": {"src": "pw_containment_1.webp", "widths": (320,)},
    "pw-2": {"src": "pw_containment_2.webp", "widths": (405,)},
    "warg-gear-fea": {"src": "warg_landing-gear_3.webp", "widths": (322,)},
    "warg-clamp-photo": {"src": "warg_arm-clamp_1.webp", "widths": (432,)},
    "warg-clamp-render": {"src": "orig_clamp.webp", "widths": (800, 1600)},
    "warg-clamp-exploded": {"src": "warg_arm-clamp_3.webp", "widths": (576,)},
    "warg-gear-drone": {"src": "orig_landinggear.webp", "crop": (0, .05, 1, .95), "widths": (800, 1483)},
    "warg-gear-part": {"src": "warg_landing-gear_1.webp", "widths": (768,)},
    "warg-pdb-photo": {"src": "warg_pdb-housing_1.webp", "widths": (605,)},
    "warg-pdb-exploded": {"src": "orig_pwm-case.webp", "widths": (800, 1335)},
    "warg-pdb-render": {"src": "warg_pdb-housing_3.webp", "widths": (768,)},
    "tbm-night": {"src": "watdig_tbm_2.webp", "widths": (807,)},
    "tbm-pit": {"src": "watdig_tbm_1.webp", "widths": (615,)},
    "tbm-site": {"src": "watdig_tbm_3.webp", "widths": (615,)},
    "tbm-artic": {"src": "tbm_articulation.webp", "widths": (800, 1297)},
    "tbm-cad": {"src": "tbm_cad_full.webp", "crop": (.08, .12, .92, .88), "widths": (800, 1134)},
    "tbm-cad-head": {"src": "tbm_cad_head.webp", "widths": (800, 1350)},
}

# --------------------------------------------------------------------------- home

PITCH = "I design robots and the machines that build and test hardware."
HERO_SUB = ("My last two internships were at Neuralink, where I built a robotic cell that makes surgical needles "
            "and a fleet of lifetime testers for brain implants. Before that I designed stamped and die-cast parts "
            "for Cybertruck and Robotaxi at Tesla.")

TITLE_BLOCK = [
    ("School", "University of Waterloo, Mechanical Engineering, Mechatronics option"),
    ("Graduating", "April 2027, 96.0% average"),
    ("Internships", "Neuralink (2x), Tesla, Pratt &amp; Whitney Canada, S&amp;C Electric"),
    ("Looking for", "Full-time robotics and mechanical design roles from summer 2027"),
    ("Work status", "Canadian citizen, eligible for TN status in the US"),
]

BALLOONS = [
    {"x": 27, "y": 83, "label": "Rotating base", "spec": "5:1 belt drive, holds the electronics", "href": "sub-1"},
    {"x": 41, "y": 30, "label": "Shoulder cycloidal gearbox", "spec": "58.5:1, 30 Nm", "href": "sub-2"},
    {"x": 66.8, "y": 14.8, "label": "Elbow cycloidal gearbox", "spec": "52:1, 8.3 Nm", "href": "sub-2"},
    {"x": 74.5, "y": 25, "label": "Planetary elbow roll", "spec": "4:1, the sixth axis", "href": "sub-3"},
    {"x": 84.5, "y": 50, "label": "Differential wrist", "spec": "Bevel gears, pitch and roll", "href": "sub-4"},
    {"x": 87.5, "y": 77, "label": "Fin-ray gripper", "spec": "Parallel four-bar, 70 mm", "href": "sub-5"},
]

WORK_INTRO = ("Five internships since 2023. A lot of the Neuralink and Tesla work is under NDA, "
              "so those entries stick to what I can share and have no photos.")

ROLES = [
    {
        "company": "Neuralink", "dates": "May to Nov 2026", "place": "South San Francisco, CA",
        "title": "Mechanical Engineering Intern, Robotics",
        "lead": ("I designed, built and validated a robotic cell that laser-mills, cleans and inspects microscopic surgical needles "
                 "on its own. Before it, loading, moving parts between stations and cleaning were done by hand, and the line made "
                 "about 100 needles a month."),
        "figures": [("25x", "capacity, to 2,500 needles a month"), ("99%+", "yield in validation"),
                    ("8 min", "cycle per needle"), ("8 to 12 h", "unattended overnight runs")],
        "points": [
            "Owned all of the mechanical and electrical design, then built and wired the cell myself.",
            "Designed the femtosecond laser milling fixture for sub-micron needle positioning, plus the custom gripper fingers and transfer mechanisms that handle the needle cartridges.",
            "Worked on the Python sequencer that runs a UR arm, a hexapod and stepper axes, with error recovery, an operator GUI and per-needle logging.",
            "Took more than 50 machined, turned, 3D-printed and injection-molded parts through overseas vendors with GD&amp;T drawings and DFM reviews.",
            "Designed the laser-safe enclosure, with an interlock, a lock and a safety shutter.",
            "The cell saves about 20 to 40 technician hours a week. When my term ended it was validated and waiting for production release.",
        ],
        "tools": "<span>Tools</span> SOLIDWORKS, GD&amp;T, DFM, Python, URScript, RTDE, ACS motion control",
    },
    {
        "company": "Neuralink", "dates": "May to Dec 2025", "place": "Fremont, CA",
        "title": "Mechanical Engineering Intern, Brain Interfaces",
        "lead": ("I designed and scaled an accelerated lifetime tester for neural implants. By the end of the term 10 to 20 of them "
                 "were running, and their data went into an FDA submission."),
        "figures": [("4 months", "cut from implant design iteration"), ("5 to 10x", "accelerated aging"),
                    ("0.1%", "fluid chemistry and temperature control"), ("10 to 20", "testers running")],
        "points": [
            "Designed a cyclic-tension fatigue tester for neural threads and built it into the lifetime tester.",
            "Owned the closed-loop fluid system that feeds a neural proxy solution to more than 10 testers and holds its pH, conductivity and temperature within 0.1% of target.",
            "Designed four revisions of PCBAs in KiCad for motor control and sensing (load, displacement, temperature, flow, pH, conductivity and level), and wrote the ESP32 firmware in C++ on FreeRTOS with a Python data pipeline.",
            "Owned more than 30 parts and assemblies from concept through validation, and ran strength and durability studies on 10 implant components in COMSOL.",
            "Led a rework of the tester UI that cut setup time by an hour per sample.",
        ],
        "tools": "<span>Tools</span> SOLIDWORKS, DFMA, GD&amp;T, KiCad, ESP32, C++, FreeRTOS, I2C, Python, COMSOL",
    },
    {
        "company": "Tesla", "dates": "Aug to Dec 2024", "place": "Fremont, CA",
        "title": "Mechanical Design Engineering Intern, Body Structure Repair",
        "lead": ("I designed stamped and high-pressure die-cast service parts for Cybertruck and Robotaxi. They let a technician "
                 "repair one section instead of replacing a large assembly, and across the fleet they're projected to save "
                 "customers $10M a year. Everything I worked on was released."),
        "figures": [("$10M", "projected yearly savings for customers"), ("10", "GD&amp;T drawings released"),
                    ("10%", "faster fender bracket install"), ("4", "Model Y repair procedures")],
        "points": [
            "Modelled each part in CATIA and worked through tolerance stack-ups, GD&amp;T and formability with the suppliers.",
            "Designed an adjustable Cybertruck fender bracket that cut install time by 10% and closed up large panel gaps.",
            "Used CAE crash results to refine 5 structural designs against FMVSS, and checked designs with 3D-printed test parts.",
            "Wrote 4 Model Y structural repair procedures and the fastening strategy that goes with them.",
            "Earned Tesla's Advanced GD&amp;T certification.",
        ],
        "quote": ("He managed to consistently complete assigned tasks, demonstrating exceptional quality and speed of execution, "
                  "handled multiple time critical tasks, and proactively supported other team members in meeting their targets.",
                  "Karol Sobczak, my manager at Tesla"),
        "tools": "<span>Tools</span> CATIA V5, 3DEXPERIENCE, GD&amp;T, tolerance stack-ups, stamping, HPDC, DFM",
    },
    {
        "company": "Pratt &amp; Whitney Canada", "dates": "Jan to Apr 2024", "place": "Mississauga, ON",
        "title": "Mechanical Engineering Intern, Structural FEA",
        "lead": ("I ran FEA on jet engine subassemblies and changed the CAD based on the results. My blade-off containment study "
                 "produced data for FAA engine certification, and a composite study I led showed a 42% weight saving."),
        "figures": [("42%", "weight saving in a composite study"), ("8", "LS-DYNA containment runs"),
                    ("10+", "designs flagged against FAA and P&amp;W rules"), ("3", "technical reports presented")],
        "points": [
            "Ran FEA in the ANSYS suite, LS-DYNA and Altair HyperWorks, and updated geometry in CATIA and SpaceClaim from the results.",
            "Led a study in ANSYS ACP on replacing an aluminum part with a composite.",
            "Simulated hail and ice ingestion on a proposed composite bypass vane.",
        ],
        "tools": "<span>Tools</span> ANSYS Workbench, ACP, LS-DYNA, HyperMesh, CATIA V5, SpaceClaim, Enovia VPM",
        "link": ("projects/blade-off-containment/", "Read the containment study"),
    },
    {
        "company": "S&amp;C Electric Canada", "dates": "May to Aug 2023", "place": "Etobicoke, ON",
        "title": "Quality Assurance Engineering Intern",
        "lead": ("My first internship. I inspected high-voltage interrupter switches against GD&amp;T drawings and wrote a Python "
                 "tool that automated inspection data and photo collection. The whole department adopted it."),
        "figures": [("43%", "faster inspections"), ("0", "defective returns")],
        "points": [
            "Ran more than 30 gauge R&amp;Rs, audits, hipot tests and hardness tests a week.",
            "Led a package inspection project that uses Dori AI to catch parts missing from orders.",
            "Assembled switches and subassemblies, which taught me a lot about DFMA from the shop floor.",
        ],
        "tools": "<span>Tools</span> Python, GD&amp;T inspection, gauge R&amp;R, hipot and hardness testing",
    },
]

TEAMS = [
    {"name": "WatDig", "role": "Mechanical Team Lead, Chassis &amp; Propulsion", "dates": "2024 to 2025",
     "href": "projects/watdig-tbm/", "link": "Tunnel boring machine"},
    {"name": "Waterloo Aerial Robotics Group", "role": "Mechanical Design Team Member", "dates": "2023 to 2024",
     "href": "projects/warg-drone/", "link": "Drone hardware"},
    {"name": "Waterloo Rocketry", "role": "Airframe Team Member", "dates": "2022 to 2023",
     "note": "Machined and assembled carbon fibre airframe sections"},
]

PROJECTS_INTRO = ("Personal builds, design team hardware and course work. "
                  "Each one has its own page with photos, CAD and the numbers.")

BIO = [
    ("I've liked building things for as long as I can remember. It started with marble tracks that were far taller than they "
     "needed to be, Rube Goldberg machines and contraptions in Minecraft. Now it's robot arms and gearboxes."),
    ("I want to understand how the things around me work, and I'm happiest when I own a design from the first sketch to the "
     "part running on the bench. Over five internships that has meant mechanisms, PCBAs, firmware and a lot of time with "
     "vendors working out how a part will get made."),
]

AWARDS = [
    "3x First in Class Engineering Scholarship",
    "President's Scholarship of Distinction",
    "4x Dean's Honours List",
    "2x Term Distinction",
    "2x President's International Experience Award",
]
CERTS = [
    "Tesla Advanced GD&amp;T (Levels 1, 2 and Advanced)",
    '<a href="https://cv.virtualtester.com/qr/?b=SLDWRKS&amp;i=C-B58MTUSYWR" target="_blank" rel="noopener">SOLIDWORKS CSWA</a>',
]
SKILLS = [
    ("Mechanical design", "SOLIDWORKS, CATIA V5 and 3DEXPERIENCE, Onshape, GD&amp;T, tolerance stack-ups, DFM and DFMA, gearboxes and mechanisms"),
    ("Manufacturing", "CNC and lathe parts through vendors, injection molding, stamping, die casting, FDM and SLA printing, laser and waterjet cutting"),
    ("Electronics and code", "KiCad, ESP32, FreeRTOS, C and C++, Python, URScript, Arduino"),
    ("Analysis", "ANSYS, LS-DYNA, Altair HyperMesh, COMSOL, SOLIDWORKS FEA, MATLAB"),
]

COLLAR_SVG = """<svg class="diagram" viewBox="0 0 560 400" role="img" aria-label="Block diagram of the collar's power and haptics system">
<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="currentColor"/></marker></defs>
<g fill="none" stroke="currentColor" stroke-width="1.4">
<rect x="20" y="40" width="130" height="56"/><rect x="215" y="40" width="130" height="56"/><rect x="410" y="40" width="130" height="56"/>
<rect x="215" y="172" width="130" height="56"/><rect x="410" y="172" width="130" height="56"/>
<rect x="215" y="304" width="130" height="56"/><rect x="410" y="304" width="130" height="56" class="acc"/>
<path d="M150 68 H213" marker-end="url(#ar)"/><path d="M345 68 H408" marker-end="url(#ar)"/>
<path d="M475 96 V140 H280 V170" marker-end="url(#ar)"/><path d="M345 200 H408" marker-end="url(#ar)"/>
<path d="M475 228 V266 H280 V302" marker-end="url(#ar)"/><path d="M345 332 H408" marker-end="url(#ar)"/>
</g>
<g font-family="IBM Plex Mono, monospace" font-size="13" fill="currentColor" text-anchor="middle">
<text x="85" y="66">Charging</text><text x="85" y="82">input</text>
<text x="280" y="66">LiPo charger</text>
<text x="475" y="66">1200 mAh LiPo</text><text x="475" y="82">+ fuel gauge</text>
<text x="280" y="198">3.3 V LDO</text>
<text x="475" y="198">MCU, sensors</text><text x="475" y="214">and radios</text>
<text x="280" y="330">ERM driver</text>
<text x="475" y="330">Haptic motor</text><text x="475" y="346">0.5 to 1.5 g</text>
</g></svg>"""


# --------------------------------------------------------------------------- project bodies

def sec(title, *parts, anchor=None, wide=False):
    a = f' id="{anchor}"' if anchor else ""
    w = " wide" if wide else ""
    return f'<section class="psec{w}"{a}><h2>{title}</h2><div class="psec-body">{"".join(parts)}</div></section>'


def P(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)


def UL(*items):
    return '<ul class="ticks">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def grid(*figs, cols=2, cls=""):
    return f'<div class="figgrid c{cols} {cls}">{"".join(figs)}</div>'


SUBSYSTEMS = [
    {"n": 1, "key": "axon-base", "name": "Rotating base", "spot": [(54.1, 72.3)],
     "text": "A belt drive turns the whole arm on bearings. The base also holds the electronics, with two fans pushing air out through vents in the side.",
     "spec": "NEMA 17 · 5:1 belt · 1.9 Nm · ±170°"},
    {"n": 2, "key": "axon-cycloidal", "name": "Cycloidal gearboxes", "spot": [(44.3, 4.9), (19.6, 40.9)],
     "text": "Used at the shoulder and the elbow. A belt drives the eccentric input shaft, and the cycloidal discs roll against fixed pins in the housing. The housing is the output, so the gearbox doubles as the joint.",
     "spec": "Shoulder · NEMA 23 · 58.5:1 · 30 Nm · −5° to 225°<br>Elbow · NEMA 17 · 52:1 · 8.3 Nm · ±100°"},
    {"n": 3, "key": "axon-planetary", "name": "Planetary elbow roll", "spot": [(69, 18)],
     "text": "The sixth axis. A planetary stage rolls the forearm so the gripper can tilt sideways as well as up and down.",
     "spec": "NEMA 14 · 4:1 · 0.56 Nm · ±150°"},
    {"n": 4, "key": "axon-wrist", "name": "Differential wrist", "spot": [(86.6, 35.9)],
     "text": "Two servos drive a set of bevel gears. Turning both the same way pitches the wrist, and turning them in opposite directions rolls it.",
     "spec": "2 × 25 kg·cm servos · 2.6 Nm · pitch ±90°, roll ±170°"},
    {"n": 5, "key": "axon-gripper", "name": "Fin-ray gripper", "spot": [(95, 58.2)],
     "text": "A parallel four-bar keeps the fingers parallel as they close. The fin-ray fingers bend around whatever they grab, so it can hold an egg, a pencil or a billiard ball.",
     "spec": "20 kg·cm servo · 70 mm opening"},
]

JOINTS = [
    ("Base", "NEMA 17 stepper", "5:1 belt", "1.89", "±170°"),
    ("Shoulder", "NEMA 23 stepper", "58.5:1 belt + cycloidal", "30.33", "−5° to 225°"),
    ("Elbow pitch", "NEMA 17 stepper", "52:1 belt + cycloidal", "8.26", "±100°"),
    ("Elbow roll", "NEMA 14 stepper", "4:1 planetary", "0.56", "±150°"),
    ("Wrist pitch, roll", "2 × 25 kg·cm servo", "Bevel differential", "2.57", "±90°, ±170°"),
    ("Gripper", "20 kg·cm servo", "Parallel four-bar", "", "70 mm opening"),
]

COST = [("Motors and electronics", 89.90), ("Rotating base", 69.24), ("Elbow pitch gearbox", 34.06),
        ("Wrist differential", 32.66), ("Shoulder gearbox", 31.70), ("Gripper", 20.35),
        ("Shoulder and elbow structures", 12.32), ("Elbow roll gearbox", 6.48)]


def axon_v2_body(fig, p):
    spots, panels, tabs = [], [], []
    for s in SUBSYSTEMS:
        for (x, y) in s["spot"]:
            spots.append(f'<button type="button" class="spot" data-sub="{s["n"]}" style="--x:{x}%;--y:{y}%" aria-label="{s["n"]}. {s["name"]}"></button>')
        tabs.append(f'<button type="button" class="tab" data-sub="{s["n"]}" role="tab" aria-selected="{"true" if s["n"] == 1 else "false"}"><span>{s["n"]}</span>{s["name"]}</button>')
        panels.append(f"""<article class="sub" id="sub-{s["n"]}" data-sub="{s["n"]}" role="tabpanel">
  {fig(s["key"], f'Labelled section view of the {s["name"].lower()}', f'{s["name"]}, section view. Click to enlarge.', sizes="(min-width: 1240px) 820px, 100vw", fill=True)}
  <div class="sub-text"><h3>{s["name"]}</h3><p>{s["text"]}</p><p class="spec">{s["spec"]}</p></div>
</article>""")
    explorer = f"""<div class="explorer">
  <div class="ex-map">
    <div class="ex-img">{_img("axon-labelled", "Render of Axon V2 with its five subsystems numbered", sizes="(min-width: 1100px) 440px, 100vw", prefix=p)}{"".join(spots)}</div>
    <div class="tabs" role="tablist" aria-label="Subsystems">{"".join(tabs)}</div>
  </div>
  <div class="ex-panels">{"".join(panels)}</div>
</div>"""
    rows = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a, b, c, d, e in JOINTS)
    joints = f"""<h3 class="mini-h">Joints</h3><div class="table-wrap"><table class="data">
<thead><tr><th scope="col">Joint</th><th scope="col">Actuator</th><th scope="col">Reduction</th><th scope="col">Expected torque (Nm)</th><th scope="col">Range</th></tr></thead>
<tbody>{rows}</tbody></table></div>"""
    mx = max(v for _, v in COST)
    bars = "".join(f'<li><span class="c-l">{k}</span><span class="c-bar"><span style="width:{v / mx * 100:.1f}%"></span></span><span class="c-v">${v:.2f}</span></li>' for k, v in COST)
    cost = f'<h3 class="mini-h">Parts cost</h3><ul class="cost">{bars}</ul><p class="cost-total">Total $296.70 in parts. The arm weighs 5.5 kg, or 11.3 kg on its steel base plate.</p>'

    specs = [("Reach", "Over 0.40 m", "0.69 m"), ("Approach orientations", "10", "10"), ("Degrees of freedom", "6", "6"),
             ("Repeatability", "Within 5 mm", "1.08 mm average"), ("Grasp time", "Under 2 s", "0.5 s"),
             ("Pick and place cycle", "Under 25 s", "20 s"), ("Largest object", "Over 30 mm", "70 mm"),
             ("Parts cost", "Under $300", "$296.70")]
    spec_rows = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td class="ok">{c}</td></tr>' for a, b, c in specs)
    spec_table = f"""<div class="table-wrap"><table class="data specs">
<thead><tr><th scope="col">Spec</th><th scope="col">Target</th><th scope="col">Result</th></tr></thead>
<tbody>{spec_rows}</tbody></table></div>"""

    grips = [("benchy", "Benchy"), ("glasses", "Glasses"), ("billiard", "Billiard ball"), ("egg", "Egg"), ("pencil", "Pencil"),
             ("mouse", "Mouse"), ("brush", "Vacuum brush"), ("speaker", "Speaker"), ("tape", "Tape roll"), ("knife", "Knife")]
    grip_figs = "".join(fig("ax-grip-" + k, f"Axon V2 gripper closing on a {v.lower()}", v, sizes="(min-width: 1100px) 170px, 45vw", fill=True) for k, v in grips)
    grip_grid = f'<div class="gripgrid">{grip_figs}</div><p class="group-cap"><span class="fig-n">FIG. 1</span> The ten gripping tests, in rough order of difficulty.</p>'

    repeat = [("1", "0.5 mm"), ("2", "2.0 mm"), ("3", "1.7 mm"), ("4", "0.1 mm"), ("Average", "1.08 mm")]
    repeat_rows = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in repeat)
    repeat_table = f"""<div class="table-wrap narrow"><table class="data"><thead><tr><th scope="col">Cycle</th><th scope="col">Error</th></tr></thead><tbody>{repeat_rows}</tbody></table></div>"""

    return "".join([
        sec("Approach", P(
            "I started from constraints and criteria, then sketched the layout and ran first-principles torque calculations for every joint before modelling anything in Onshape. Those numbers set the motor sizes (a NEMA 23 at the shoulder, NEMA 17s and a NEMA 14 further out) and the reductions, up to 58.5:1 at the shoulder.",
            "Everything is designed for 3D printing around off-the-shelf bearings, belts and motors, which made each iteration quick to print and test."),
            fig("ax-torque", "Torque equations and a results table for the shoulder and elbow", "Torque sizing for the shoulder and elbow, which set the motors and reductions.", n=1)),
        sec("Subsystems", '<p class="hint">Pick a number on the render or a subsystem from the list.</p>', explorer, anchor="subsystems", wide=True),
        sec("Electronics and control", P(
            "I owned the electrical side, from the schematics for 4 stepper motors and 3 servos through the wiring and the robot control firmware. The steppers run on TMC2209 drivers on an Arduino CNC shield, each current-limited below its rating so nothing overheats, and a buck converter drops the supply voltage for the servos.",
            "Inverse kinematics I wrote runs on a laptop and streams joint targets to the Arduino over serial. The arm runs a homing sequence at startup, and the wrist uses servos so it never needs homing."),
            grid(fig("ax-electrical", "Block diagram of the power supply, stepper drivers, buck converter, servos, Arduino and laptop", "Electrical architecture. One supply feeds the stepper drivers directly and the servos through a buck converter.", n=1),
                 fig("ax-render-internal", "Render of Axon V2 with the electronics visible in the base", "The electronics live in the base, cooled by two fans.", n=1))),
        sec("Iterations", P("The arm went through three versions. Later ones added mechanical hard stops, two cooling fans in the base, and magnetic cover panels that snap on with clearance for the moving parts and wires, and come off for repairs."),
            fig("axon-iterations", "Three versions of the arm side by side, labelled V1, V2 and V3", "The three versions, left to right.", n=1, fill=True),
            fig("axon-panels", "Axon V2 with its magnetic cover panels removed", "Cover panels off.", n=1, fill=True, cls="mid")),
        sec("Verification", P("Each design spec had its own test."), spec_table,
            '<h3 class="v-h">Reach and range of motion</h3>',
            P("The arm reaches from 22 mm to 690 mm out from the base axis. Every joint has a mechanical hard stop at its limit, which lets the arm zero itself against them."),
            fig("ax-workspace", "Render of the arm inside its reachable workspace, shown as two shaded spheres", "Reachable workspace.", n=1, fill=True, cls="mid"),
            grid(fig("ax-stop-shoulder", "Section views of the shoulder at both hard stops", "Shoulder hard stops at −5° and 225°.", n=1),
                 fig("ax-stop-elbow", "Section views of the elbow at both hard stops", "Elbow hard stops at −100° and 100°.", n=1), cls="hs"),
            '<h3 class="v-h">Dexterity</h3>',
            P("The target was 10 orthogonal approach orientations, up from 4 once the sixth axis went in. The arm reached all 10."),
            fig("ax-dexterity", "Four photos of the arm approaching objects on a table from different directions", "Approaching objects from different directions.", n=1, fill=True),
            '<h3 class="v-h">Gripping</h3>',
            P("The fin-ray gripper was tested on ten objects, from a 3D-printed Benchy to an egg, a pencil and a knife."),
            grip_grid,
            '<h3 class="v-h">Load</h3>',
            P("The shoulder lifted 3 kg, and the shoulder and elbow each held 1.5 kg at full reach. At 3 kg the wrist starts to flex."),
            '<h3 class="v-h">Repeatability</h3>',
            '<div class="split">',
            P("A dial indicator measured how close the arm returns to the same point. It moved away and back four times, and the average error was 1.08 mm against a 5 mm target."),
            repeat_table, '</div>',
            fig("ax-repeat", "Axon V2 pressing against a dial indicator on the table", "Dial indicator setup for the repeatability test.", n=1, cls="mid")),
        sec("Specifications", joints, cost),
    ])


def axon_v1_body(fig, p):
    return "".join([
        sec("What it is", P(
            "A two-axis robotic wrist, built as the first piece of a 6-DOF arm. Two steppers drive a 3D-printed differential through timing belts, which also multiply the torque. An Arduino Uno running AccelStepper keeps both axes in sync using a synchronization routine I wrote, and you can drive it with an analog joystick or send serial commands for tuning."),
            grid(fig("v1-built", "The finished Axon V1 wrist with its white printed covers", "The finished wrist.", n=2, fill=True),
                 fig("v1-section", "Section view of the wrist assembly showing the gears, bearings and belt drive", "Section view of the wrist assembly.", n=3, fill=True), cls="matched-tall")),
        sec("How I built it", UL(
            "Set constraints and criteria first, then sketched and researched the overall layout.",
            "Modelled it in Onshape for 3D printing, with off-the-shelf hardware where it made sense.",
            "Ran it open loop on TMC2208 drivers, with both steppers homing off a single limit switch.",
            "Stress tested it on a rig I designed to find its limits, and wrote it all up in a 25-page report."),
            grid(fig("v1-electronics", "Arduino Uno and two stepper drivers wired on a breadboard", "Arduino Uno and the two TMC2208 drivers.", n=4, fill=True),
                 fig("v1-internals", "The wrist with its covers removed, showing the motor and frame", "Covers off.", n=5, fill=True),
                 fig("v1-rig", "The wrist mounted on its stress test rig", "Stress testing on the rig I designed.", n=6, fill=True), cols=3, cls="matched-tall")),
        sec("What I learned", P(
            "It met every constraint I set, with about 1.3 Nm of output torque, smooth coordinated motion and close to zero backlash, for under $50. It also gave me a list for the next version, with closed-loop control, contactless homing and better wire routing at the top. Most of that went into Axon V2.")),
    ])


def chess_body(fig, p):
    return "".join([
        sec("What it is", P(
            "I led a team of four building a robot that plays a full game of chess against a person with no help. A camera and OpenCV pick up the opponent's move, the Stockfish engine chooses a reply, and Python sends instructions to an EV3 brick running RobotC, which drives a 3-axis gantry with a gripper to move the piece."),
            '<div class="video"><iframe src="https://player.vimeo.com/video/843717067?h=3e0f911d2c&amp;dnt=1&amp;title=0&amp;byline=0&amp;portrait=0" title="The chess robot playing a game" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe></div>'),
        sec("How we built it", UL(
            "Built the gantry from belts, racks and pinions, wheels, LEGO and Tetrix parts, plus housings, racks and guides I modelled in SOLIDWORKS and AutoCAD and then 3D printed or laser cut.",
            "Ran SOLIDWORKS FEA to choose a structure that spread the load and wouldn't tip.",
            "Planned the term with a work breakdown structure and Gantt chart, and finished on schedule."),
            grid(fig("chess-setup", "The full setup, with a laptop running the vision and engine beside the board", "The full setup. The laptop runs vision and the engine.", n=2),
                 fig("chess-cad", "CAD render of a 3D-printed gantry part", "One of the printed gantry parts in CAD.", n=3))),
        sec("Results", UL(
            "Moved pieces correctly more than 95% of the time.",
            "Read the opponent's move correctly more than 95% of the time.",
            "Never lost a game, with a theoretical rating of 3620 Elo.")),
    ])


def cycloidal_body(fig, p):
    return "".join([
        sec("Why I built it", P(
            "A lot of robots use cycloidal drives in their joints and I wanted to understand them properly before designing one into an arm. So I built one that's fully 3D printed, with no bearings at all.")),
        sec("How", UL(
            "Read up on how cycloidal drives work and worked out the 9:1 geometry by hand.",
            "Modelled it in Onshape for printing.",
            "Drove it with a stepper motor, an Arduino and a stepper driver."),
            fig("cyclo-section", "Section view of the 3D-printed cycloidal reducer", "Section view of the reducer.", n=2)),
        sec("Results", P(
            "It ran at 9:1 as designed, and it showed me several things to fix. Those fixes went straight into the Axon V2 shoulder and elbow gearboxes.")),
    ])


def light_body(fig, p):
    return "".join([
        sec("Why I built it", P(
            "I got tired of getting out of bed to turn the light off. This servo unit sits over a normal wall switch and flips it when it gets a signal from an IR remote. I did the mechanical, electrical and software sides myself.")),
        sec("How", UL(
            "Sized the servo and battery with basic dynamics and power calculations.",
            "An IR receiver takes commands from the remote, and a microcontroller turns them into servo motion.",
            "Designed the housings in Onshape with heat-set inserts for fastening, and soldered the electronics.",
            "Wrote all of the control code in C++."),
            grid(fig("light-mounted", "Servo unit mounted over a wall light switch", "Mounted over the switch.", n=2),
                 fig("light-side", "Small printed housing mounted on the wall beside the switch", "Printed housing on the wall.", n=3),
                 fig("light-lit", "Black printed housing with a blue light inside", "Housing with its status light on.", n=4), cols=3)),
        sec("Results", UL(
            "Flips the switch correctly 99% of the time.",
            "The battery lasts about 3 days.",
            "You can still flip the switch by hand, and it comes off without leaving a mark, which matters in a rental.")),
    ])


def collar_body(fig, p):
    return "".join([
        sec("What it is", P(
            "Our capstone is a collar that tracks a dog's breathing, heart rate (by ECG) and skin temperature against that dog's own baseline, so it can warn the owner about early signs of illness. It can also call the dog back with a silent haptic cue, and locate it over BLE or GPS and cellular.")),
        sec("My part", UL(
            "I'm the electrical lead, and I ran the sensor trade study that picked the ECG, IMU respiration, temperature and GPS and cellular parts.",
            "I designed the power and haptics architecture, with the battery sized against an 8-hour runtime and a 12-hour charge target.",
            "I drew the power and haptics schematic in KiCad, and I own PCB revision A, due in early 2027.")),
        sec("Targets", UL(
            "Respiration within 5 breaths a minute and heart rate within 10 bpm.",
            "Location within 10 m, updated at least every 30 seconds.",
            "IP52, survives a 1 m drop, and skin temperature stays at or under 41 °C."),
            '<p class="note">Still in progress. I\'ll add results once we test in the winter term.</p>'),
    ])


def vehicle_body(fig, p):
    return "".join([
        sec("The assignment", P(
            "The goal was to recommend vehicle parameters and driving behaviour that keep a car safe in bad conditions. I modelled the car as a bicycle model with Ackermann steering, wrote the physics as a system of ODEs and solved it with RK4 in MATLAB.")),
        sec("Results", UL(
            "A general simulator that takes any set of vehicle parameters and driving inputs.",
            "Handling behaviour, understeer or oversteer, mapped across a range of conditions, with design and driving recommendations.",
            "The report got 100%, and Prof. Zhao Pan uses it as an example of good mathematical modelling."),
            fig("vd-sweep", "Plots of vehicle paths and yaw response across several parameter sets", "Paths and response across parameter sets.", n=2)),
    ])


def vent_body(fig, p):
    return "".join([
        sec("The problem", P(
            "Several of the exterior vent flaps on our house were broken and I couldn't find replacements at a reasonable price. So I took the critical dimensions off an intact flap with calipers, modelled it in SOLIDWORKS and printed new ones in PETG for weather resistance. They snap in without tools."),
            grid(fig("vent-compare", "An original vent flap above a printed PETG replacement", "Original flap above, printed replacement below.", n=2),
                 fig("vent-cad", "SOLIDWORKS model of the vent flap", "The SOLIDWORKS model.", n=3))),
        sec("Results", UL(
            "Prints without supports and opens properly when the vent runs.",
            "Saved $40 over buying replacements.",
            "I posted the model for free, and 30 other people have printed it to fix their own vents.")),
    ])


def warg_body(fig, p):
    return "".join([
        P("The Waterloo Aerial Robotics Group builds autonomous drones for the Aerial Evolution Association of Canada (AEAC) competition. I spent a year on the mechanical team and designed three parts for the competition drone. All three flew at AEAC."),
        sec("X-frame arm clamps", P(
            "The arms of the X-frame had play in them, which showed up as vibration in flight. I designed four clamps that lock each arm down, can be tuned by how far you tighten the screws, and still let the arms come out for transport. The aluminum parts were waterjet cut, drilled and tapped from my GD&amp;T drawings, and the rest printed in carbon-fibre PETG without supports. The design lived in SOLIDWORKS PDM."),
            '<dl class="figures">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in [("56%", "less arm play"), ("34 g", "per clamp"), ("&lt; 3 h", "to print, no supports"), ("2025", "flew at AEAC")]) + "</dl>",
            grid(fig("warg-clamp-photo", "Printed and machined clamp installed on the drone", "Installed on the drone.", n=2),
                 fig("warg-clamp-exploded", "Exploded render of the clamp parts", "Exploded view of the clamp.", n=3)), anchor="clamps"),
        sec("Carbon fibre landing gear", P(
            "The landing gear had to take repeated landings at different angles and protect the expensive carbon fibre tubes if the drone crashed. I put frangible printed joints between the tubes and the frame, so the joints break first and take the impact. I used FEA to check load distribution and the centre of mass, tuned the print settings of the joints for impact absorption, and drew the GD&amp;T drawing for the machined aluminum."),
            '<dl class="figures">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in [("300 g", "total"), ("130°", "effective landing angle"), ("2024", "flew at AEAC")]) + "</dl>",
            fig("warg-gear-drone", "Render of the drone standing on the carbon fibre landing gear", "The gear on the competition drone.", n=4, fill=True),
            grid(fig("warg-gear-part", "Render of one landing gear leg with its printed joint", "One landing gear leg in CAD.", n=5),
                 fig("warg-gear-fea", "FEA stress plot on the landing gear joint", "FEA on the landing gear joint.", n=6)), anchor="landing-gear"),
        sec("Power distribution board housing", P(
            "The electrical team gave me their board and their constraints. The housing snaps onto the frame and is held with screws, keeps fingers away from the points that could short, and has a vent pattern that keeps the board within its rated temperature. I checked the venting with FEA, and designed it to print without supports and go together easily."),
            '<dl class="figures">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in [("12 g", "printed in PLA"), ("&lt; 2 h", "to print, no supports"), ("2024", "flew at AEAC")]) + "</dl>",
            grid(fig("warg-pdb-exploded", "Exploded render of the housing around the power distribution board", "Exploded view around the board.", n=7, fill=True),
                 fig("warg-pdb-photo", "Printed housing installed among the drone's wiring", "Installed on the drone.", n=8)), anchor="pdb"),
    ])


def watdig_body(fig, p):
    return "".join([
        sec("The team", P(
            "WatDig is Waterloo's team for The Boring Company's Not-a-Boring Competition, where student teams build tunnel boring machines. I led a team of four on the chassis, propulsion and articulation (steering) systems for the 2025 machine.")),
        sec("Articulation system", P(
            "The articulation joint is how the machine steers. I designed a motorized and hydraulic system based on a Stewart platform, with hydraulics for power and sensors for control, that steers against 3 kNm of torque. I worked out the steering force with hand calculations and FEA to set the hydraulic actuator specs, and modelled the system in Onshape."),
            fig("tbm-artic", "CAD render of the articulation system, six hydraulic legs joining two hull sections", "The articulation system, a Stewart platform of hydraulic legs between two hull sections.", n=2, fill=True),
            fig("tbm-cad-head", "Close-up CAD render of the front of the machine", "Front of the machine in CAD.", n=3, fill=True)),
        sec("At the competition", P(
            "I also designed and made several of the structural parts. The machine competed at NaBC 2025 in Texas, and the team raised more than $10,000 in sponsorship along the way."),
            fig("tbm-night", "The WatDig tunnel boring machine being assembled under a tent at night", "Assembly at the competition site.", n=4),
            grid(fig("tbm-pit", "Crew lowering the boring machine into the launch pit", "Lowering the machine into the launch pit.", n=5),
                 fig("tbm-site", "Team members working on the machine at the competition site", "Work on site.", n=6))),
    ])


def containment_body(fig, p):
    return "".join([
        sec("The question", P(
            "If a compressor blade breaks off in flight, the engine case has to contain it. During my internship at Pratt &amp; Whitney Canada I ran a blade-off containment study on a compressor with new design changes, following FAA guidance and P&amp;W best practice.")),
        sec("How I ran it", P(
            "I defeatured the compressor assembly in CATIA and SpaceClaim, meshed and prepped it in Altair HyperMesh, and applied the boundary conditions for the LS-DYNA solver. Then I worked through 8 runs of increasing complexity, each one closer to the real event. Getting the inputs meant working with several departments, and I wrote the study up in a formal report and presentation."),
            grid(fig("pw-1", "LS-DYNA model of the containment case with the released blade inside", "Blade released inside the case.", n=1),
                 fig("pw-2", "Stress contour on the case where the blade strikes it", "Stress on the case at impact.", n=2))),
        sec("Result", P(
            "The study confirmed the blade stays contained with the new design changes, and its data went toward FAA engine certification.")),
        sec("The rest of the term", UL(
            "Led a study in ANSYS ACP on replacing an aluminum part with a composite, which showed a 42% weight saving.",
            "Simulated hail and ice ingestion on a proposed composite bypass vane.",
            "Flagged more than 10 designs that didn't meet FAA or company guidelines, and presented 3 technical reports.")),
    ])


# --------------------------------------------------------------------------- project list (order = index order)

PROJECTS = [
    {
        "slug": "axon-v2", "title": "Axon V2 robotic arm", "kind": "Personal project · 2026",
        "short": "A 6-DOF arm on custom cycloidal and planetary gearboxes. 3 kg payload and about 1 mm repeatability for under $300.",
        "fact": "3 kg payload, 690 mm reach, ~1 mm repeatability, $297 in parts",
        "lede": "A six-axis arm built around custom 3D-printed cycloidal and planetary gearboxes. It lifts 3 kg, reaches 690 mm and repeats to about 1 mm, and the parts cost $296.70.",
        "cover": "hero", "index_cover": "axon-folded", "cover_alt": "Axon V2 robot arm on a wooden ledge",
        "hero_caption": "Axon V2 on its weighted base plate.",
        "meta": [("My role", "Mechanical and electrical design"), ("When", "2026"),
                 ("Tools", "Onshape, 3D printing, NEMA 14, 17 and 23 steppers, TMC2209, servos")],
        "figures": [("3 kg", "max payload"), ("690 mm", "reach"), ("~1 mm", "repeatability"), ("$297", "in parts")],
        "body": axon_v2_body,
        "links": [("Live CAD in Onshape", "https://cad.onshape.com/documents/89cf0009362a9f4b36c676c7/w/fa1475b775bea1364fdb21dd/e/bf43eb84fbcd42c9c9dab1a0?renderMode=0&amp;uiState=6a7958dae6e9bfac068b8839"),
                  ],
    },
    {
        "slug": "warg-drone", "title": "Drone hardware for WARG", "kind": "Design team · 2023 to 2024",
        "short": "Arm clamps, carbon fibre landing gear and a power board housing. All three flew at AEAC.",
        "fact": "Arm play down 56%, landing gear 300 g with a 130° landing angle",
        "lede": "Three parts I designed for the Waterloo Aerial Robotics Group's competition drone, from first sketch to flying hardware.",
        "cover": "warg-gear-drone", "cover_alt": "Render of the WARG drone on its carbon fibre landing gear", "fit": "contain",
        "hero": "warg-clamp-render", "hero_caption": "The X-frame arm clamp, rendered in place under the frame.",
        "meta": [("My role", "Mechanical design team member"), ("When", "Sept 2023 to Aug 2024"),
                 ("Tools", "SOLIDWORKS and PDM, FEA, GD&amp;T, waterjet, 3D printing")],
        "figures": [("3", "parts designed and flown"), ("56%", "less arm play"), ("130°", "landing angle"), ("12 g", "board housing")],
        "body": warg_body,
    },
    {
        "slug": "watdig-tbm", "title": "Tunnel boring machine", "kind": "Design team · 2024 to 2025",
        "short": "Led chassis, propulsion and a hydraulic steering system for The Boring Company's Not-a-Boring Competition.",
        "fact": "Steering against 3 kNm, competed at NaBC 2025 in Texas",
        "lede": "I led four people on the chassis, propulsion and steering of WatDig's tunnel boring machine, which competed at NaBC 2025.",
        "cover": "tbm-cad", "index_cover": "tbm-artic", "cover_alt": "CAD render of the full WatDig tunnel boring machine",
        "meta": [("My role", "Mechanical Team Lead, Chassis &amp; Propulsion"), ("When", "May 2024 to 2025"),
                 ("Tools", "Onshape, hand calculations, FEA, hydraulics")],
        "figures": [("4", "people on my subteam"), ("3 kNm", "steering torque"), ("NaBC", "2025, Texas")],
        "hero_caption": "CAD of the full machine.",
        "body": watdig_body,
    },
    {
        "slug": "blade-off-containment", "title": "Blade-off containment study", "kind": "Internship · Pratt &amp; Whitney Canada · 2024",
        "short": "An LS-DYNA study of a compressor blade breaking off in flight. The data went toward FAA engine certification.",
        "fact": "8 LS-DYNA runs, data used for FAA engine certification",
        "lede": "An LS-DYNA study showing that a compressor blade stays inside the engine case if it breaks off in flight.",
        "cover": "pw-2", "cover_alt": "Stress contour on a jet engine containment case at blade impact", "fit": "contain",
        "hero_html": "",
        "meta": [("My role", "Structural FEA intern"), ("When", "Jan to Apr 2024"),
                 ("Tools", "LS-DYNA, LS-PrePost, Altair HyperMesh, CATIA V5, SpaceClaim")],
        "figures": [("8", "runs, each more detailed"), ("FAA", "certification data"), ("42%", "saving in a separate composite study")],
        "body": containment_body,
    },
    {
        "slug": "axon-v1", "title": "Axon V1 differential wrist", "kind": "Personal project",
        "short": "A two-axis belt-driven differential wrist. 1.3 Nm, near-zero backlash, under $50.",
        "fact": "1.3 Nm output, close to zero backlash, under $50",
        "lede": "The two-axis wrist I built before the full arm, to learn differentials, stepper control and synchronized motion.",
        "cover": "v1-exploded", "cover_alt": "Exploded render of the Axon V1 wrist",
        "hero_caption": "Exploded view of the wrist.",
        "meta": [("My role", "Solo design and build"), ("Tools", "Onshape, Arduino, AccelStepper, TMC2208")],
        "figures": [("1.3 Nm", "output torque"), ("~0", "backlash"), ("&lt; $50", "in parts"), ("25 pages", "design report")],
        "body": axon_v1_body,
        "links": [("Live CAD and BOM in Onshape", "https://cad.onshape.com/documents/6f3381f7019f99a0050790c5/w/73012f0bdf031a2263803ee2/e/5793963b5aeb29827f76694e?renderMode=0&amp;uiState=683cbac90496457e6057e083"),
                  ("Wiring diagram", "https://app.cirkitdesigner.com/project/1e2f7573-cb2f-44a8-8ccd-d9841350be9a")],
    },
    {
        "slug": "chess-robot", "title": "Autonomous chess robot", "kind": "Course project · 2023",
        "short": "Computer vision, Stockfish and a 3-axis gantry. It never lost a game.",
        "fact": "Over 95% move success, never lost a game",
        "lede": "A robot that sees its opponent's move and plays back on a real board. I led the team of four.",
        "cover": "chess-cover", "cover_alt": "The chess robot's gantry over a board mid-game",
        "hero_caption": "The gantry over the board, mid-game.",
        "meta": [("My role", "Team lead, team of 4"), ("When", "Jan to Apr 2023, ME 101"),
                 ("Tools", "SOLIDWORKS, AutoCAD, Python, OpenCV, RobotC, EV3")],
        "figures": [("95%+", "moves made correctly"), ("95%+", "opponent moves read correctly"), ("0", "games lost")],
        "body": chess_body,
        "links": [("Design report (PDF)", "assets/docs/chess-robot-report.pdf")],
    },
    {
        "slug": "cycloidal-drive", "title": "Cycloidal drive study", "kind": "Personal project",
        "short": "A fully printed 9:1 cycloidal reducer with no bearings, built to learn the mechanism.",
        "fact": "9:1 reduction, fully 3D printed",
        "lede": "A bearing-free, fully printed cycloidal reducer I built to understand the mechanism before using it in Axon V2.",
        "cover": "cyclo-run", "cover_alt": "Printed cycloidal drive wired to an Arduino on a breadboard", "fit": "contain",
        "hero_fill": False, "hero_caption": "Running off an Arduino and a stepper driver.",
        "meta": [("My role", "Solo"), ("Tools", "Onshape, Arduino, stepper driver, 3D printing")],
        "figures": [("9:1", "reduction"), ("0", "bearings")],
        "body": cycloidal_body,
    },
    {
        "slug": "light-switch", "title": "Remote light switch", "kind": "Personal project",
        "short": "An IR-controlled servo that flips a wall switch. 99% success and a 3-day battery.",
        "fact": "99% flip success, 3-day battery, no permanent changes",
        "lede": "A servo unit that flips my bedroom light switch from an IR remote, and comes off without a trace.",
        "cover": "light-cover", "cover_alt": "Bench prototype with the microcontroller wired to the switch unit",
        "hero_caption": "Bench prototype, wired up next to the switch.",
        "meta": [("My role", "Solo, mechanical, electrical and firmware"), ("Tools", "Onshape, C++, IR, servo, heat-set inserts")],
        "figures": [("99%", "flip success"), ("3 days", "battery life")],
        "body": light_body,
    },
    {
        "slug": "smart-collar", "title": "Smart dog collar", "kind": "Capstone · 2026 to 2027 · In progress",
        "short": "Electrical lead on a five-person capstone building a collar that tracks a dog's vitals.",
        "fact": "Power and haptics architecture, sized for an 8-hour runtime",
        "lede": "A collar that watches a dog's vitals for early signs of illness. I'm the electrical lead on our five-person team.",
        "cover": None, "cover_alt": "",
        "hero_html": '<figure class="plate fill diagram-plate">' + COLLAR_SVG + '<figcaption><span class="fig-n">FIG. 1</span> The power and haptics architecture I own, simplified.</figcaption></figure>',
        "meta": [("My role", "Electrical lead, sensor trade study lead"), ("When", "Sept 2026 to Apr 2027, MTE 481/482"),
                 ("Tools", "KiCad, power budgeting, LiPo charging, ERM haptics")],
        "figures": [("1200 mAh", "LiPo"), ("8 h", "runtime target"), ("12 h", "max charge time")],
        "body": collar_body,
    },
    {
        "slug": "vehicle-dynamics", "title": "Vehicle dynamics in MATLAB", "kind": "Course project · ME 303",
        "short": "A bicycle-model simulator solved with RK4. Graded 100% and used as a class example.",
        "fact": "Graded 100%, used as a class example",
        "lede": "A vehicle handling simulator I wrote in MATLAB to recommend safe vehicle and driving parameters.",
        "cover": "vd-path", "cover_alt": "Plot of a vehicle's path in an oversteer case", "fit": "contain",
        "hero_fill": False, "hero_caption": "Vehicle path for an oversteering configuration.",
        "meta": [("Course", "ME 303, numerical methods and ODEs"), ("Tools", "MATLAB, RK4")],
        "figures": [("100%", "grade")],
        "body": vehicle_body,
    },
    {
        "slug": "vent-flap", "title": "Vent flap replacement", "kind": "Personal project",
        "short": "Reverse-engineered replacement vent flaps. 30 other people have printed the model.",
        "fact": "Saved $40, printed by 30 other people",
        "lede": "Replacement exterior vent flaps, measured from a broken original and printed in PETG.",
        "cover": "vent-cover", "cover_alt": "Printed white vent flaps installed on a brick wall",
        "hero_caption": "Printed flaps installed on the house.",
        "meta": [("My role", "Solo"), ("Tools", "Calipers, SOLIDWORKS, PETG printing")],
        "figures": [("$40", "saved"), ("30", "other people printed it")],
        "body": vent_body,
    },
]
