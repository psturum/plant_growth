import pygame

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (56, 117, 215)
YELLOW = (255, 255, 0)
GREY = (100, 100, 100)
GREY1 = (200, 200, 200)

PLANT_NAMES = [
    "Lupin", "Ært", "Amarant", "Quinoa", "Hvidmelet gåsefod", "Hestebønne", "Linser",
    "Rødkløver", "Hvidkløver", "Rajgræs", "Mikroalge", "Makroalge", "Raps", "Hvedegræs"
]



PLANT_DESCRIPTIONS = ["Lupiner kommer fra Middelhavsområdet ved ækvator, men har spredt sig naturligt i det nordlige Europa. Lupinplanten har evnen til at kunne binde nitrogen i jorden ved hjælp af bakterier, og kan derfor leve i jorde med et lavt indhold af næring.",
                      "Ærter kommer fra Middelhavsområdet, dog trives planten meget i lande som f.eks. Østrig. Ærteplanten er i stand til at binde nitrogen i jorden ved hjælp af bakterier, og kan derfor overleve i jorde med mindre næringsindhold. Ærter gror også bedst i vinter/forårsperioden i varmere lande.",
                      "Amaranter kommer oprindeligt fra den tropiske del af Asien, men bliver også dyrket i flere lande i Afrika. Amarant-planterne gror bedst i sommerperioden, hvor nattemperaturerne ikke går under 15 °C. De gror også bedst i næringsrige jorde og i områder med færre dagtimer, da den ellers ikke vil lave blomst.",
                      "Quinoa kommer fra Andesbjergene i Sydamerika. Da planten oprindeligt kommer fra et bjergområde, er den i stand til at overleve frostgrader om natten. Quinoa er en plante, som kan klare meget saltholdige jorde, men for at være i stand til at overleve det store saltindhold, har planten brug for kalium. Planten gror bedst i områder med færre dagtimer, da den ellers ikke vil lave blomst.",
                      "Man mener, at hvidmelet gåsefod oprindeligt kommer fra Europa, men senere har spredt sig meget til tempererede og subtropiske klimazoner. Planten bliver i mange lande kaldt ukrudt, mens den i andre lande bruges som afgrøder, da den gror hurtigt og kan gro i meget næringsfattige jorde. Planten gror bedst i områder med færre dagtimer, da den ellers ikke vil lave blomst.",
                      "Hestebønnen kommer fra Middelhavsområdet, men gror over hele Eurasien (kontinentet hvor Asien og Europa indgår). Hestebønne-planten kan gro i de fleste områder, så længe der er nok vand til stede. Planten er derudover i stand til at binde nitrogen i jorden ved hjælp af bakterier.",
                      "Linser kommer fra Sydøstasien og Middelhavsområdet, hvor de gror bedst i tempererede klimazoner, men gror flere forskellige steder. Linseplanten er i stand til at overleve tørke og hedebølger, samt gro i jord med meget sand.",
                      "Rødkløver kommer fra Europa og Asien, og er i familie med hvidkløveren. Rødkløver er kortere i højden, men har et større planteudbytte end hvidkløver. Rødkløveren er i stand til at binde nitrogen i jorden ved hjælp af bakterier. Planten gror i de fleste typer landskab, undtagen ørkener og høje bjerge.",
                      "Hvidkløver har oprindelse i Europa, og er almindelig i hele Danmark. Den blomstrer typisk fra juni til august, og trives bedst i køligere klima. Hvidkløver er i stand til at binde nitrogen i jorden, men har behov for store mængder af andre nærringstoffer for at trives.",
                      "Rajgræs trives i vejkanten eller enge i Danmark. Planten er nem at så og er en kold-sæson græs, hvilket betyder, at den trives bedst under moderate eller køligere klimaforhold. Den har sin primære vækstperiode om foråret og efteråret.",
                      "Chlorella er en alge, som vokser i ferskvand. Chlorella kan også dyrkes i landbruget i f.eks. gennemsigtige rør. I den forbindelse kan der tilføres en bestemt mængde lys, CO2 og næringsstoffer (primært i form af nitrogen og fosfor).",
                      "Wakame er en brunalge, der stammer fra det nordvestlige Stillehav (Korea, Japan og Kina). Den vokser bedst i køligt vand og langs kysten. Makronæringsstofferne nitrogen og fosfor er afgørende for Wakames vækst, mens kalium sjældent er en begrænsning.",
                      "Brassica napus, også kendt som \"vinterraps\", vokser i Europa. Den blomstrer samt starter modningen af sine frø i sommeren. Rapsens vækst påvirkes i høj grad af næringsindholdet i jorden, og den har et stort behov for nitrogen.",
                      "Hvedegræs kommer fra Europa og det vestlige Asien. Det er en græsart, der trives i køligere sæsoner som forår og efterår. Derfor vokser Hvedegræs også bedst i tempererede og nordlige klimaer."
                      ]

IMG_NAMES = [
    "lupin.jpg", "ært.jpg", "amarant.jpg", "quinoa.jpg", "hvidmelet gåsefod.jpg", "heste bønne.jpeg", "linser.jpeg",
    "rødkløver.jpeg", "hvidkløver.jpeg", "rajgræs.jpeg", "mikroalger.jpeg", "makroalger.jpeg", "raps.jpeg", "hvedegræs.jpeg"
]

PLANT_DATA = {
    'Lupin': {
        'Gode egenskaber': ['Høj proteinkvalitet', 'Højt proteinindhold', 'Højt udbytte'],
        'Temperatur:': (15, 20),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((15, 35),(20, 30)),
            'Næring P:': (41, 55),
            'Næring K:': (41, 55)
        }
    },
    'Ært': {
        'Gode egenskaber': ['Høj proteinkvalitet', 'Højt udbytte', 'Få antinæringstoffer'],
        'Temperatur:': (13, 19),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((15, 35),(20, 30)),
            'Næring P:': (48, 62),
            'Næring K:': (43, 57)
        }
    },
    'Amarant': {
        'Gode egenskaber': ['Lav bitterhed', 'Hurtig vækst', 'Højt indhold af næringstoffer'],
        'Temperatur:': (21, 30),
        'Lys:': ((8, 14), (10, 12)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((155, 175),(160, 170)),
            'Næring P:': (58, 72),
            'Næring K:': (45, 59)
        }
    },
    'Quinoa': {
        'Gode egenskaber': ['Høj proteinkvalitet', 'Tørkeresistent', 'Sydgomdsresistent'],
        'Temperatur:': (19, 24),
        'Lys:': ((8, 14), (10, 12)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((30, 50),(35, 45)),
            'Næring P:': (53, 67),
            'Næring K:': (113, 127)
        }
    },
    'Hvidmelet gåsefod': {
        'Gode egenskaber': ['Lav bitterhed', 'Hurtig vækst', 'Tolerere dårlige jordbetingelser'],
        'Temperatur:': (10, 30),
        'Lys:': ((8, 14), (10, 12)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((5, 20),(5, 15)),
            'Næring P:': (33, 47),
            'Næring K:': (33, 47)
        }
    },
    'Hestebønne': {
        'Gode egenskaber': ['Høj proteinkvalitet', 'Højt proteinindhold', 'Lav frøkast'],
        'Temperatur:': (18, 30),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((20, 40),(25, 35)),
            'Næring P:': (38, 52),
            'Næring K:': (41, 55)
        }
    },
    'Linser': {
        'Gode egenskaber': ['Lav højde', 'Højt proteinindhold', 'Få antinæringstoffer'],
        'Temperatur:': (18, 30),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': (0,1),
        'Næring:': {
            'Nitrogen': ((10, 30),(15, 25)),
            'Næring P:': (33, 47),
            'Næring K:': (13, 27)
        }
    },
    'Rødkløver': {
        'Gode egenskaber': ['Lav højde', 'Få antinæringstoffer', 'Få antinæringstoffer'],
        'Temperatur:': (15, 23),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((12, 32),(17, 27)),
            'Næring P:': (60, 74),
            'Næring K:': (15, 29)
        }
    },
    'Hvidkløver': {
        'Gode egenskaber': ['Lav højde', 'Lav bitterhed', 'Tørkeresistent'],
        'Temperatur:': (15, 23),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((12, 32),(17, 27)),
            'Næring P:': (60, 74),
            'Næring K:': (15, 29)
        }
    },
    'Rajgræs': {
        'Gode egenskaber': ['Lav højde', 'Lav bitterhed', 'Hurtig vækst'],
        'Temperatur:': (17, 20),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((60, 80),(65, 75)),
            'Næring P:': (43, 57),
            'Næring K:': (43, 57)
        }
    },
    'Mikroalge': {
        'Gode egenskaber': ['Høj proteinkvalitet', 'Højt proteinindhold', 'Hurtig vækst'],
        'Temperatur:': (20, 30),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 2,
        'Næring:': {
            'Nitrogen': ((13, 29),(18, 24)),
            'Næring P:': (1, 3),
            'Næring K:': (0, 50)
        }
    },
    'Makroalge': {
        'Gode egenskaber': ['Højt udbytte', 'Hurtig vækst', 'Få antinæringstoffer'],
        'Temperatur:': (10, 15),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 2,
        'Næring:': {
            'Nitrogen': ((13, 29),(18, 24)),
            'Næring P:': (1, 3),
            'Næring K:': (0, 50)
        }
    },
    'Raps': {
        'Gode egenskaber': ['Lav bitterhed', 'Højt udbytte', 'Hurtig vækst'],
        'Temperatur:': (15, 25),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((170, 190),(175, 185)),
            'Næring P:': (83, 97),
            'Næring K:': (113, 127)
        }
    },
    'Hvedegræs': {
        'Gode egenskaber': ['Lav bitterhed', 'Få antinæringstoffer', 'Lang rodlængde'],
        'Temperatur:': (15, 24),
        'Lys:': ((12, 18), (14, 16)),
        'Vand:': 1,
        'Næring:': {
            'Nitrogen': ((114, 129),(119, 124)),
            'Næring P:': (55, 69),
            'Næring K:': (23, 37)
        }
    }
}



units = [
    "°C",
    "t",
    ("Tør", "Fugtig", "Våd"),
    "mg/m²",
    "mg/m²",
    "mg/m²"
]

ranges = [
    (0,40),
    (0,24),
    (0,2),
    (0,200),
    (0,200),
    (0,200)
]

parameters = [
    "Temperatur:",
    "Lys:",
    "Vand:",
    "Næring N:",
    "Næring P:",
    "Næring K:"
]

initial_values = [20, 12, 1, 100, 100, 100]
window_width = 1200
window_height = 600
grid_width = 2  # Width of the grid in squares
grid_width1 = 7  # Width of the grid in menu
grid_height = 2  # Height of the grid
cell_width = window_width // grid_width  # Width of each cell in squares
cell_width1 = window_width // grid_width1  # Width of each cell in menu
cell_height = window_height // grid_height  # Height of each cell
img_heightyhh = cell_height * 3 // 4
img_widthyhh = cell_width - 120
img_x = 60
img_y = cell_height // 4 - 20
font_header = pygame.font.Font(None, 32)
font_param = pygame.font.Font(None, 24)

# Draw white grid
xgrid_x = window_width - 570
xgrid_y = 370
xgrid_width = 4
xgrid_height = 2
xgrid_cell_width = 135
xgrid_cell_height = 110
xgrid_image_width = xgrid_cell_width - 10
xgrid_image_height = xgrid_cell_height - 10

egenskaber_text = font_header.render("Beskrivelse", True, GREY1)
egenskaber_x = (cell_width // 2) - egenskaber_text.get_width() // 2
egenskaber_y = cell_height + 20
parametre_text = font_header.render("Parametre", True, GREY1)
parametre_x = cell_width + (cell_width // 2) - parametre_text.get_width() // 2
param_x = cell_width + 20
param_y = 65 - 10
param_spacing = 35

# Create button
button_rect = pygame.Rect(650, 315, 200, 35)
button_color = (47,85,151)
button_text = font_param.render('Gro', True, GREY1)
button_text_rect = button_text.get_rect(center=button_rect.center)

# Load life images
life_image = pygame.image.load("assets/images1/life.png")
life_width = 30
life_height = 30
life_spacing = 30
lives_x = button_rect.right + life_spacing