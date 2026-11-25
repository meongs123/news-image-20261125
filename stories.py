# Slate for Wednesday 25 November 2026 — 44 stories, frozen at ~16:10 WIB.
# Every deck and brief carries its real date. Sources are wire attributions only.
# Trap stories (ICJ 19 Nov, COP31 22 Nov, Merkury 22 Nov, Huang Mon 23 Nov,
# Gibran 12 Nov, Hanoi Tue 24 Nov) are NOT in this slate; they live in DATE_CHECK.

MASTHEAD = "Wednesday 25 November 2026"
SUBHEAD = ("Shenzhou-24 docks with a Pakistani aboard (Wed)  •  "
           "Australia-Solomon treaty signed (Wed)  •  "
           "Iowa blast set for 09:00 local (Wed)")
COUNT_STRIP = "44 STORIES  •  7 REGIONS  •  13 ILLUSTRATED"

NUMBERS = [
    ("50,018.70", "Dow, first close over 50,000 (Tue)"),
    ("-1.48%", "Nasdaq 23,733.54 (Tue close)"),
    ("-6.16%", "KOSPI; Samsung -9.87% (Wed)"),
    ("Tk 17,000", "Garment wage, +36% (Wed)"),
    ("5-1", "Real Madrid beat PSV (Tue eve)"),
    ("9,500 lb", "Lead azide, Iowa blast 09:00 (Wed)"),
]

REGIONS = [
    ("Americas", 9, "#0e6b6b"),
    ("Asia", 13, "#a8232a"),
    ("Europe", 6, "#1f3a6e"),
    ("Africa", 2, "#8a6d1a"),
    ("Middle East", 8, "#7a5a1e"),
    ("World", 2, "#5b3a7a"),
    ("Oceania", 4, "#2a7a8a"),
]

# WEDNESDAY WIRE dropped in fix pass 1: its order (launch -> blast -> docking) was
# false in any single timezone, and the Canberra treaty signing time is unverified.
# Verified Beijing times for the record: launch 08:18, docking 11:56, Cartagena
# storming ~01:00 local = 14:00 Beijing, Iowa blast 09:00 CST = 23:00 Beijing.
# Splash alone carries the structural variation (per design fallback).

# Big leads: (number, kicker, headline, deck, source, art kind, pin lat/lon)
BIG = [
    (1, "SPACE", "PAKISTANI ASTRONAUT DOCKS AT TIANGONG",
     "Shenzhou-24 launches 08:18, docks 11:56 Beijing time Wed; Muhammad Zeeshan Ali, 40, "
     "first Pakistani in orbit and first foreigner aboard the station. Stay 5-10 days.",
     "REUTERS", "rocket", (40.0, 100.0)),
    (2, "PACIFIC", "SOLOMONS SIGN AUSTRALIA SECURITY TREATY",
     "PMs Albanese and Wale sign in Canberra Wed; Australia becomes primary security partner.",
     "PM'S OFFICE", "treaty", (-35.3, 149.1)),
    (3, "USA", "IOWA BRACES FOR 9,500 LB BLAST",
     "Army to detonate 68 barrels of decaying lead azide 09:00 local Wed; 5-mile evacuation cone.",
     "USA TODAY", "blast", (40.8, -91.4)),
]

# Small leads: (number, kicker, headline, deck, source, art kind, pin lat/lon)
SMALL = [
    (4, "MIDDLE EAST", "HOUTHIS CLAIM REFINERY STRIKE",
     "Claims Ras Tanura refinery hit Wed; 4 drones intercepted.",
     "REUTERS", "refinery", (26.6, 50.2)),
    (5, "TRADE", "TARIFFS ON 16 PARTNERS 'SET TO BE UNVEILED'",
     "Section 301 findings due Tue/Wed; no rates announced.",
     "REUTERS", "tariff", (38.9, -77.0)),
    (6, "USA", "TRUMP PARDONS TURKEYS, TOUTS IRAN CAMPAIGN",
     "Freedom and Feathers pardoned Tue; Trump touts Iran campaign.",
     "AP", "turkey", (38.9, -77.1)),
    (7, "GAZA", "GAZA: SECOND HAMAS CHIEF REPORTED DEAD",
     "Chief Abu Nahel killed Tue; second chief reported dead Wed.",
     "REUTERS", "gaza", (31.5, 34.5)),
    (8, "AUSTRALIA", "AUSTRALIA SAYS SORRY TO LGBTQ VETERANS",
     "Marles apologises in parliament Wed; ban lifted 1992.",
     "REUTERS", "sorry", (-35.3, 149.3)),
    (9, "TECH", "CIA AND ODNI HACKED - UNCLASSIFIED ONLY",
     "Unclassified system breached Tue; no classified data taken.",
     "NYT / AP", "hack", (38.9, -77.2)),
    (10, "IRAQ", "BAGHDAD MOVES TO SEIZE KURDISH OILFIELDS",
     "PM orders federal control of oilfields Tue; KRG rejects move.",
     "REUTERS", "oilfield", (33.3, 44.4)),
    (11, "SPORT", "SENEGAL GETS AFCON TITLE BACK",
     "CAS reinstates Senegal as 2025 winners Tue; Morocco to appeal.",
     "REUTERS", "trophy", (14.7, -17.4)),
    (12, "SPORT", "REAL MADRID 5-1 PSV, FIVE FROM FIVE",
     "Mbappe scores twice Tue eve, passes Ronaldo's 104, now 105 in 121 games.",
     "REUTERS", "football", (40.4, -3.7)),
    (13, "USA", "SIX DEAD IN MISSISSIPPI PLANE CRASH",
     "Cessna found off coast early Wed; six aboard, incl. two children.",
     "USA TODAY", "plane", (30.2, -89.3)),
]

# Briefs: 31 one-liners, heroes 4-7 first, then the 27 briefs. All date-tagged.
BRIEFS = [
    "Dow 50,018.70 +0.85% (Tue close), first above 50,000; S&P 7,201.09 -0.50%; Nasdaq 23,733.54 -1.48%.",
    "North Korea expels Swiss envoy, closes Pyongyang office, 48 hours to leave (Wed).",
    "Cartagena siege ends: all hostages freed, 1 captor killed (Wed); Villavicencio bomb injured 23.",
    "Bangladesh garment wage +36% to Tk 17,000/month from 1 Dec (Wed).",
    "Russian jets enter S. Korea air-defence zone (Tue 24 Nov); Seoul scrambles F-15Ks, no airspace entered.",
    "Two arrested after break-in at Prince William's Anmer Hall (Tue 24 Nov); no one home.",
    "Hanoi hot-pot blast kills 6, 10 in intensive care (Tue 24 Nov).",
    "DR Congo rebel group CRP halts advance on Bunia, withdraws (announced Tue 24 Nov).",
    "China graft probe: Shanghai party chief Chen Jining investigated (announced Tue 24 Nov).",
    "Trump awards Medal of Freedom to Rudy Giuliani (Tue 24 Nov).",
    "Tesla + SpaceX name 5 directors to negotiate possible ~$3.5tn merger (Tue 24 Nov).",
    "Tidal to ban fully AI-generated music from 9 Dec (announced Tue 24 Nov).",
    "Broadcom patches 23 VMware flaws incl. critical vCenter bypass (24 Nov).",
    "McDonald's Japan app database breached (reported 24 Nov).",
    "India Supreme Court notice on Khalid / Imam bail pleas (Wed 25 Nov).",
    "Israel: Eisenkot secures first coalition partner, 28 of 61 needed (Wed 25 Nov).",
    "Australia passes Digital Duty of Care Act (24 Nov).",
    "US envoy criticises Australia digital duty law; Canberra vows no step back (Wed 25 Nov).",
    "Iranian rial hits record low, 2.856m rials per dollar (24 Nov).",
    "UN Women: ~47,000 women killed by partner or relative in 2025 (report 24 Nov).",
    "Ras Al Khaimah bus-truck crash kills 13, injures 26 (24 Nov).",
    "Indonesia: MPR sets 11 Dec vote for new vice-president (announced 24 Nov).",
    "Xiamen Airlines orders 50 Boeing 737-8 jets (Wed 25 Nov).",
    "Ex-OpenAI engineer Alfozan granted bail on $1m bond (Wed 25 Nov).",
    "AI safety pioneer Stuart Russell warns on ceding control to AI (Wed 25 Nov).",
    "Shein agrees to pay $100m to settle US lawsuits (reported Wed 25 Nov).",
    "UK sanctions Houthis as entity + 4 figures (Tue 24 Nov).",
    "Murmansk governor Chibis detained in embezzlement probe (reported Wed 25 Nov).",
    "Microsoft declares 'Code Red' after historic 24h Outlook outage (reported Wed 25 Nov; outage 12-13 Nov).",
    "Delhi cafe gang-rape allegation; 3 arrested (24 Nov).",
    "Iran honour-killing case: pregnant 19-year-old killed, parents confessed (Wed 25 Nov).",
]

DATE_CHECK = [
    ("ICJ rules Myanmar committed genocide", "19 Nov"),
    ("COP31 climate talks collapse, Antalya", "Sun 22 Nov"),
    ("Ukraine sinks Russian corvette Merkury", "Sun 22 Nov"),
    ("Huang reinstated as Nvidia CEO", "Mon 23 Nov"),
    ("Indonesia VP Gibran resigns", "12 Nov"),
    ("Dow closes above 50,000", "Tue 24 Nov close"),
    ("Hanoi hot-pot blast, 6 dead", "Tue 24 Nov"),
]

SOURCES = ("Sources: Reuters, AP, USA Today, Australian PM's office, China Daily Asia, "
           "NY Times, WSJ, Australian Dept. of Defence.")
FOOTER_DATE = ("Wednesday 25 November 2026 - the day's biggest stories; "
               "earlier events are dated in the deck.")
