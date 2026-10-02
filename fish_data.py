"""Static fish, location, boon, and dialogue data."""

FISH_DATA = {
    # Freshwater Lake
    'Smallmouth Bass': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Common',
        'rarity_weight': 40,
        'weight_kg': (0.3, 2.5),
        'size_cm': (20, 55),
        'description': 'A strong freshwater predator known for its bronze coloring and '
                       'energetic fight. It often hunts around rocky shorelines and '
                       'submerged structure.'
    },
    'Bluegill': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Common',
        'rarity_weight': 55,
        'weight_kg': (0.05, 0.35),
        'size_cm': (8, 30),
        'description': 'A small, deep-bodied sunfish with blue-green coloring. '
                       'Bluegill gather near cover and feed on insects, larvae, and '
                       'other tiny animals.'
    },
    'Brown Trout': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Uncommon',
        'rarity_weight': 25,
        'weight_kg': (0.3, 4.0),
        'size_cm': (20, 70),
        'description': 'A wary trout with dark spots and warm brown coloring. It '
                       'thrives in cool water and feeds on insects, smaller fish, and '
                       'crustaceans.'
    },
    'Rainbow Trout': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Uncommon',
        'rarity_weight': 22,
        'weight_kg': (0.2, 8.0),
        'size_cm': (20, 100),
        'description': 'A colorful trout with a pinkish stripe along its side. It '
                       'prefers cool, oxygen-rich water and feeds on insects and small '
                       'fish.'
    },
    'Carp': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Common',
        'rarity_weight': 35,
        'weight_kg': (1.0, 12.0),
        'size_cm': (35, 90),
        'description': 'A hardy, bottom-feeding freshwater fish that uses sensitive '
                       'barbels near its mouth to find food in the sediment.'
    },
    'Catfish': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Uncommon',
        'rarity_weight': 22,
        'weight_kg': (1.0, 15.0),
        'size_cm': (40, 120),
        'description': 'A whiskered fish that relies on smell and touch to find food, '
                       'often feeding along the bottom in low light.'
    },
    'Muskellunge': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Rare',
        'rarity_weight': 8,
        'weight_kg': (2.0, 18.0),
        'size_cm': (60, 140),
        'description': 'A large ambush predator with a long body and sharp teeth. '
                       'Muskellunge typically lurk near weeds or submerged cover '
                       'before striking.'
    },
    'Perch': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Common',
        'rarity_weight': 45,
        'weight_kg': (0.1, 1.2),
        'size_cm': (10, 45),
        'description': 'A schooling fish with distinctive dark vertical bars. Perch '
                       'feed on insects and small aquatic animals, often around '
                       'vegetation.'
    },
    'Walleye': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Uncommon',
        'rarity_weight': 18,
        'weight_kg': (0.5, 6.0),
        'size_cm': (25, 80),
        'description': 'A predatory freshwater fish with reflective eyes that help it '
                       'hunt in dim light. It often stays near rocky or sandy bottoms.'
    },
    'Largemouth Bass': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Common',
        'rarity_weight': 38,
        'weight_kg': (0.3, 5.0),
        'size_cm': (20, 70),
        'description': 'A popular ambush predator recognized by its broad mouth and '
                       'dark side stripe. It hides near weeds, logs, and other cover.'
    },
    'Pike': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Rare',
        'rarity_weight': 10,
        'weight_kg': (1.0, 15.0),
        'size_cm': (45, 120),
        'description': 'A long-bodied predator with a duck-like snout and sharp teeth. '
                       'Pike lie in wait among aquatic plants to ambush passing prey.'
    },
    'Koi': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Very Rare',
        'rarity_weight': 3,
        'weight_kg': (0.5, 8.0),
        'size_cm': (25, 80),
        'description': 'A colorful ornamental carp bred in many patterns. Koi are '
                       'social, adaptable fish that forage for a variety of foods.'
    },
    'Goldfish': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Rare',
        'rarity_weight': 7,
        'weight_kg': (0.05, 1.0),
        'size_cm': (8, 35),
        'description': 'A domesticated carp known for its bright orange color and '
                       'adaptability. Wild-type goldfish are usually more muted in '
                       'color.'
    },
    'Bayad': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Uncommon',
        'rarity_weight': 18,
        'weight_kg': (0.5, 15.0),
        'size_cm': (25, 120),
        'description': 'A freshwater catfish with barbels around its mouth. It '
                       'searches the bottom for fish and other food, especially in '
                       'African waters.'
    },
    'Boulti': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Common',
        'rarity_weight': 38,
        'weight_kg': (0.1, 4.0),
        'size_cm': (10, 60),
        'description': 'A freshwater tilapia known by the name boulti in some regions. '
                       'It is adaptable and feeds on algae, plants, and small '
                       'organisms.'
    },
    'Capitaine': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Rare',
        'rarity_weight': 8,
        'weight_kg': (1.0, 50.0),
        'size_cm': (30, 200),
        'description': 'A large freshwater fish known by the regional name capitaine. '
                       'In this game it is a powerful predator of smaller fish.'
    },
    'Synodontis': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Uncommon',
        'rarity_weight': 18,
        'weight_kg': (0.05, 4.0),
        'size_cm': (10, 60),
        'description': 'An African freshwater catfish with barbels that help it find '
                       'food. Many synodontis species shelter near rocks or along the '
                       'bottom.'
    },
    'Armored Carp': {
        'locations': ['Freshwater Lake'],
        'rarity': 'Uncommon',
        'rarity_weight': 15,
        'weight_kg': (0.5, 15.0),
        'size_cm': (25, 100),
        'description': 'A sturdy freshwater carp with heavy scales that act as '
                       'protective armor. It feeds along the bottom on plants and '
                       'small animals.'
    },

    # Muddy River
    'Gar': {
        'locations': ['Muddy River'],
        'rarity': 'Uncommon',
        'rarity_weight': 16,
        'weight_kg': (0.5, 40.0),
        'size_cm': (40, 250),
        'description': 'A long-bodied freshwater predator with a narrow snout and '
                       'tough, armor-like scales. Gar ambush fish near the surface.'
    },
    'Minnow': {
        'locations': ['Muddy River'],
        'rarity': 'Common',
        'rarity_weight': 65,
        'weight_kg': (0.001, 0.1),
        'size_cm': (3, 15),
        'description': 'A small schooling fish found in freshwater. Minnows feed on '
                       'tiny invertebrates and are an important food source for larger '
                       'fish.'
    },
    'Pleco': {
        'locations': ['Muddy River'],
        'rarity': 'Common',
        'rarity_weight': 35,
        'weight_kg': (0.02, 3.0),
        'size_cm': (5, 60),
        'description': 'An armored, bottom-dwelling catfish with a sucker-shaped '
                       'mouth. Plecos cling to surfaces and graze on algae and other '
                       'food.'
    },
    'Arapaima': {
        'locations': ['Muddy River'],
        'rarity': 'Very Rare',
        'rarity_weight': 2,
        'weight_kg': (10.0, 200.0),
        'size_cm': (100, 300),
        'description': 'A giant Amazonian freshwater fish that must surface to breathe '
                       "air. It has large scales and hunts fish near the water's "
                       'surface.'
    },
    'Red Bellied Piranha': {
        'locations': ['Muddy River'],
        'rarity': 'Uncommon',
        'rarity_weight': 15,
        'weight_kg': (0.2, 5.0),
        'size_cm': (15, 50),
        'description': 'A South American freshwater fish with a reddish underside and '
                       'strong jaws. It feeds on fish, insects, and other available '
                       'food.'
    },
    'Tambaqui': {
        'locations': ['Muddy River'],
        'rarity': 'Uncommon',
        'rarity_weight': 18,
        'weight_kg': (1.0, 40.0),
        'size_cm': (30, 100),
        'description': 'A large Amazonian relative of the pacu. Tambaqui use strong '
                       'teeth to eat fruits, seeds, and other foods that fall into the '
                       'water.'
    },
    'Electric Eel': {
        'locations': ['Muddy River'],
        'rarity': 'Rare',
        'rarity_weight': 7,
        'weight_kg': (1.0, 20.0),
        'size_cm': (50, 250),
        'description': 'A South American fish that produces electric discharges to '
                       'sense its surroundings, stun prey, and defend itself.'
    },
    'Freshwater Eel': {
        'locations': ['Muddy River'],
        'rarity': 'Uncommon',
        'rarity_weight': 16,
        'weight_kg': (0.05, 5.0),
        'size_cm': (15, 120),
        'description': 'A long, snake-like fish that shelters in mud or underwater '
                       'cover. Many freshwater eels migrate between rivers and the '
                       'sea.'
    },
    'Black Pacu': {
        'locations': ['Muddy River'],
        'rarity': 'Rare',
        'rarity_weight': 8,
        'weight_kg': (1.0, 30.0),
        'size_cm': (30, 100),
        'description': 'A deep-bodied South American freshwater fish related to '
                       'piranhas. It has strong, blunt teeth suited to crushing seeds '
                       'and fruit.'
    },
    'Betta': {
        'locations': ['Muddy River'],
        'rarity': 'Rare',
        'rarity_weight': 6,
        'weight_kg': (0.002, 0.05),
        'size_cm': (3, 10),
        'description': 'A small, brightly colored fish native to shallow Southeast '
                       'Asian waters. Bettas can breathe air at the surface using a '
                       'special organ.'
    },
    'Lungfish': {
        'locations': ['Muddy River'],
        'rarity': 'Rare',
        'rarity_weight': 6,
        'weight_kg': (0.1, 10.0),
        'size_cm': (20, 150),
        'description': 'An ancient freshwater fish that can breathe air. Some lungfish '
                       'survive dry seasons by resting in mud until water returns.'
    },
    'Mudskipper': {
        'locations': ['Muddy River'],
        'rarity': 'Common',
        'rarity_weight': 30,
        'weight_kg': (0.01, 0.3),
        'size_cm': (5, 30),
        'description': 'A small fish from muddy coastal flats that can move over wet '
                       'surfaces and breathe through its moist skin for short periods.'
    },

    # Coastal Reef
    'Red Grouper': {
        'locations': ['Coastal Reef'],
        'rarity': 'Uncommon',
        'rarity_weight': 25,
        'weight_kg': (0.5, 8.0),
        'size_cm': (25, 100),
        'description': 'A reef-dwelling fish that shelters in rocky crevices. Red '
                       'grouper use powerful jaws to feed on fish and bottom-dwelling '
                       'animals.'
    },
    'Lionfish': {
        'locations': ['Coastal Reef'],
        'rarity': 'Uncommon',
        'rarity_weight': 22,
        'weight_kg': (0.2, 1.5),
        'size_cm': (15, 45),
        'description': 'A striking reef fish with broad fins and venomous spines. Its '
                       'spines are for defense, so it should be observed without '
                       'handling.'
    },
    'Yellow Tang': {
        'locations': ['Coastal Reef'],
        'rarity': 'Common',
        'rarity_weight': 40,
        'weight_kg': (0.05, 0.5),
        'size_cm': (8, 25),
        'description': 'A bright yellow reef fish that grazes on algae. Its small, '
                       'blade-like tail spines help it defend itself.'
    },
    'Clownfish': {
        'locations': ['Coastal Reef'],
        'rarity': 'Common',
        'rarity_weight': 45,
        'weight_kg': (0.02, 0.2),
        'size_cm': (5, 18),
        'description': 'A small orange reef fish with white bands. Clownfish live '
                       'among sea anemone tentacles and are protected by a layer of '
                       'mucus.'
    },
    'Sea Robin': {
        'locations': ['Coastal Reef'],
        'rarity': 'Common',
        'rarity_weight': 35,
        'weight_kg': (0.2, 1.2),
        'size_cm': (15, 45),
        'description': 'A bottom-dwelling fish with large pectoral fins. It can use '
                       'free fin rays like little legs to probe the seafloor for food.'
    },
    'Pufferfish': {
        'locations': ['Coastal Reef'],
        'rarity': 'Uncommon',
        'rarity_weight': 20,
        'weight_kg': (0.1, 2.0),
        'size_cm': (10, 45),
        'description': 'A fish able to inflate its body when threatened. Some species '
                       'contain powerful toxins, so they should never be handled or '
                       'eaten casually.'
    },
    'Butterfly Fish': {
        'locations': ['Coastal Reef'],
        'rarity': 'Uncommon',
        'rarity_weight': 28,
        'weight_kg': (0.05, 0.6),
        'size_cm': (8, 25),
        'description': 'A colorful, laterally flattened reef fish with a small mouth '
                       'suited to picking food from coral and rocky surfaces.'
    },
    'Moray Eel': {
        'locations': ['Coastal Reef'],
        'rarity': 'Rare',
        'rarity_weight': 9,
        'weight_kg': (0.5, 8.0),
        'size_cm': (40, 150),
        'description': 'A long reef predator that spends much of its time in crevices, '
                       'waiting to catch fish and crustaceans that pass nearby.'
    },
    'Barracuda': {
        'locations': ['Coastal Reef'],
        'rarity': 'Rare',
        'rarity_weight': 10,
        'weight_kg': (1.0, 15.0),
        'size_cm': (50, 150),
        'description': 'A streamlined predator with a pointed head and prominent '
                       'teeth. Barracuda use quick bursts of speed to catch smaller '
                       'fish.'
    },
    'Bluefish': {
        'locations': ['Coastal Reef'],
        'rarity': 'Common',
        'rarity_weight': 32,
        'weight_kg': (0.3, 5.0),
        'size_cm': (25, 90),
        'description': 'A fast-moving, schooling predator with strong jaws and sharp '
                       'teeth. Bluefish often chase schools of smaller fish near the '
                       'surface.'
    },
    'Blackfish': {
        'locations': ['Coastal Reef'],
        'rarity': 'Uncommon',
        'rarity_weight': 16,
        'weight_kg': (0.5, 10.0),
        'size_cm': (20, 80),
        'description': 'A dark-colored coastal fish that feeds on shellfish and other '
                       'bottom-dwelling animals around rocky habitats.'
    },

    # Open Ocean
    'Eastern Cod': {
        'locations': ['Open Ocean'],
        'rarity': 'Common',
        'rarity_weight': 38,
        'weight_kg': (0.5, 15.0),
        'size_cm': (30, 120),
        'description': 'A bottom-associated marine fish with a chin barbel used to '
                       'sense food. Cod feed on a range of fish and invertebrates.'
    },
    'Eastern Halibut': {
        'locations': ['Open Ocean'],
        'rarity': 'Rare',
        'rarity_weight': 9,
        'weight_kg': (2.0, 40.0),
        'size_cm': (50, 180),
        'description': 'A large flatfish that rests on the seafloor, where its mottled '
                       'coloring helps it blend into sand and gravel.'
    },
    'Western Halibut': {
        'locations': ['Open Ocean'],
        'rarity': 'Rare',
        'rarity_weight': 8,
        'weight_kg': (2.0, 45.0),
        'size_cm': (50, 200),
        'description': 'A broad-bodied flatfish with both eyes on one side of its '
                       'head. It lies camouflaged on the bottom and ambushes passing '
                       'prey.'
    },
    'Western Herring': {
        'locations': ['Open Ocean'],
        'rarity': 'Common',
        'rarity_weight': 50,
        'weight_kg': (0.05, 0.7),
        'size_cm': (10, 35),
        'description': 'A small, silvery fish that forms dense schools in open water. '
                       'Herring feed mainly on plankton and are an important food '
                       'source for larger animals.'
    },
    'Sardine': {
        'locations': ['Open Ocean'],
        'rarity': 'Common',
        'rarity_weight': 55,
        'weight_kg': (0.01, 0.3),
        'size_cm': (5, 30),
        'description': 'A small, silvery schooling fish that feeds on plankton and '
                       'travels in large groups through coastal and open waters.'
    },
    'Pink Salmon': {
        'locations': ['Open Ocean'],
        'rarity': 'Uncommon',
        'rarity_weight': 22,
        'weight_kg': (0.5, 3.0),
        'size_cm': (25, 60),
        'description': 'A migratory salmon with a silvery body at sea. Adults develop '
                       'a pronounced hump on their backs as they return to freshwater '
                       'to spawn.'
    },
    'Sockeye Salmon': {
        'locations': ['Open Ocean'],
        'rarity': 'Rare',
        'rarity_weight': 10,
        'weight_kg': (1.0, 5.0),
        'size_cm': (30, 75),
        'description': 'A migratory salmon that feeds on small organisms in lakes and '
                       'the ocean. Adults turn red during their spawning migration.'
    },
    'Pollock': {
        'locations': ['Open Ocean'],
        'rarity': 'Common',
        'rarity_weight': 42,
        'weight_kg': (0.5, 8.0),
        'size_cm': (30, 90),
        'description': 'A schooling member of the cod family that feeds on plankton, '
                       'crustaceans, and small fish in cool ocean waters.'
    },
    'Bluefin Tuna': {
        'locations': ['Open Ocean'],
        'rarity': 'Very Rare',
        'rarity_weight': 3,
        'weight_kg': (20.0, 300.0),
        'size_cm': (100, 300),
        'description': 'A powerful, highly migratory tuna built for long-distance '
                       'travel and fast swimming. It hunts schooling fish and squid in '
                       'open water.'
    },
    'Angler Fish': {
        'locations': ['Open Ocean'],
        'rarity': 'Very Rare',
        'rarity_weight': 2,
        'weight_kg': (1.0, 25.0),
        'size_cm': (30, 120),
        'description': 'A deep-sea predator that uses a modified fin ray as a '
                       'glowing-looking lure to draw prey close in the darkness.'
    },
    'Krill': {
        'locations': ['Open Ocean'],
        'rarity': 'Common',
        'rarity_weight': 55,
        'weight_kg': (0.001, 0.02),
        'size_cm': (1, 6),
        'description': 'Tiny shrimp-like crustaceans that gather in enormous swarms. '
                       'Krill feed on plankton and support many larger ocean animals.'
    },
    'Coelacanth': {
        'locations': ['Open Ocean'],
        'rarity': 'Legendary',
        'rarity_weight': 1,
        'weight_kg': (20.0, 100.0),
        'size_cm': (100, 200),
        'description': 'A deep-water fish from an ancient lineage once thought '
                       'extinct. Its fleshy paired fins move in an unusual alternating '
                       'pattern.'
    },
}

LOCATIONS = {
    'Freshwater Lake': 'Temperate ponds and streams with cool, clear water and rocky edges.',
    'Muddy River': 'Cloudy tropical water with mud, roots, and brackish shallows.',
    'Coastal Reef': 'Coral reefs full of color, shelter, and reef-dwelling species.',
    'Open Ocean': 'Pelagic waters where fish spend their lives roaming the sea.',
    'Harbor': 'Visit the Aquarium, Fish Market, Ruins, or General Store.'
}

RARITY_COLORS = {'Common': '#222222', 'Uncommon': '#1b5e20', 'Rare': '#1565c0', 'Very Rare': '#6a1b9a', 'Legendary': '#b76e00'}

RARITY_BASE_VALUES = {'Common': 1.0, 'Uncommon': 5.0, 'Rare': 15.0, 'Very Rare': 50.0, 'Legendary': 200.0}

BOON_DATA = {'Plenty': {'description': '25% chance to hook a second fish on a cast.'}, 'Fortune': {'description': 'Improves the odds of finding rarer fish.'}, 'Prosperity': {'description': 'Earn 50% more money when selling fish.'}, 'Giants': {'description': 'Makes larger specimens more likely.'}, 'Fishers': {'description': 'Keeping any fish never reduces Favor.'}, 'Penance': {'description': 'Reduces Favor lost from keeping outlier fish or dumping.'}}

BOON_COST = 120

FAVOR_SYMBOL = '🐚'

FAVOR_POINTS_PER_STEP = 10

FAVOR_CHANGE_LIMIT = 5

FAVOR_RECOVERY_CASTS = 5

FAVOR_CATCH_PENALTY = 0.05

MIN_CATCH_CHANCE = 0.25

HARBOR_BUTTON_WIDTH = 22

HARBOR_BUTTON_HEIGHT = 2

RUPERT_GREETINGS = [
    "Welcome back to the harbor. Let's see what the tide brought in.",
    'That one looks promising. A good catch makes a good day.',
    "Fair price, honest weigh, and no tricks from me.",
    "You're making a fine name for yourself on the docks.",
    "I've seen rougher hauls than that. Keep it coming.",
    'Good to see you. The market always feels brighter when the boats return.',
    "Let me take a look. A careful eye can tell a treasure fish from an ordinary one.",
    'Best not rush the deal — a fair catch deserves a fair exchange.',
    'That haul has character. The town will appreciate it.',
    "Straight dealing, steady work, and a solid catch — that's the harbor way."
]

MOLLY_GREETINGS = [
    'Beautiful specimen. Tell me what you notice first about the fins.',
    "I've been comparing scales and colors all morning. Have you seen anything unusual?",
    'Another catch for the notebook. What patterns do you think it carries?',
    'I could spend all afternoon watching fish move through the water.',
    'Do you think this one is a local, or a traveler from farther waters?',
    "Ah, perfect. I was hoping you'd bring me something curious.",
    'Those markings are fascinating — excellent observational data.',
    'Every fish tells a story. I think this one has several.',
    "You've got a good eye for unusual catches. Keep looking.",
    'Another brilliant find. I feel a new theory coming on.'
]

CELIA_GREETINGS = {
    'low': [
        'Hey, beachcomber. Did your shadow follow you here, or did it take the scenic route?',
        'I found a shell that sounds like a tiny sneeze. Want to hear it, or are you in a hurry?',
        'Careful on the stones. They make me curious, and then I forget where my feet are.',
        'Do you think crabs have favorite directions, or do they just zigzag for fun?',
        'I was counting gulls, but one of them kept moving. Very suspicious behavior.',
        'You seem busy. Quick question: would you trust a seagull with a secret?'
    ],
    'normal': [
        'There you are! I was asking a tide pool whether it gets lonely. It made bubbles, so maybe!',
        'Hiya! If you could ask a seashell one question, what would you ask? I have a list.',
        'I tucked a pebble in my pocket for luck. It is shaped exactly like a sleepy potato.',
        'The breeze smells like salt and important news. Have you heard any from the waves?',
        'Do fish ever get the hiccups? I keep meaning to ask Molly, but then I see a shiny thing.',
        'I waved at a crab and it waved back with both claws. Best manners on the beach.'
    ],
    'high': [
        'My favorite tide-watcher is here! Important question: if a wave had a name, what would it be?',
        'I saved you the smoothest pebble. It feels like a little moon and absolutely knows things.',
        'The gulls were gossiping again. I think they said your name, but gull is tricky to translate.',
        'You came back! I was about to ask the ruins if stones dream about being sand.',
        'I brought my lucky shell and my emergency seaweed snack. Which one should we consult first?',
        'You make this shore more fun. Do you think the tide comes in because it misses the beach?'
    ]
}

RUPERT_GODFREY_NAME = "Rupert Godfrey"

RUPERT_GODFREY_GREETINGS = [
    'Welcome to the General Store. A steady hand and a good heart always find what they need.',
    'Good to see you. We keep practical folk and honest tools here.',
    "Need a bit of help? I'm glad to lend a hand.",
    'Hard work keeps a town standing. That is the kind of work I believe in.',
    "If you're looking for what lasts, you've come to the right place.",
    'The shelves may be quiet, but the service is always warm.'
]

CHARACTER_CHAT = {
    "Celia": {
        "Who are you?": "I'm Celia! Beach wanderer, shell collector, and occasional question-asker. Do you think the moon knows the tide's name?",
        "What do you do here?": "I mind the old Ruins and trade Favor for blessings. I also ask the stones questions. They are excellent listeners, if a little quiet.",
        "How are things?": "Sunny, salty, and full of mysteries! A crab walked sideways past me twice. I think it was trying to make a point.",
        "What do you ask the tide pools?": "Mostly whether they have visitors when I'm not looking. Yesterday one had a tiny bubble parade, so I'm taking that as a yes.",
        "Why collect pebbles?": "Every pebble has a different pocket-feel. This one is smooth like a sleepy moon. I keep it around in case I need advice.",
    },
    "Rusty": {
        "Who are you?": "Name's Rusty. I've worked this harbor market long enough to tell a good catch from a fish story.",
        "What do you do here?": "I buy fish that meet the market's quality mark and pay a fair price. The townsfolk are particular about what goes on their tables.",
        "How are things?": "Tide's in, scales are shining, and the market's lively. Can't complain about a day like that.",
        "What makes a fish market-ready?": "Its points need to meet the lower-quartile mark for its location. A smaller catch can still be a fine fish, just not one I can buy today.",
        "What happens to the fish you buy?": "They go to local kitchens and fishmongers. I make sure every catch is weighed fairly before it leaves the dock.",
    },
    "Rupert Godfrey": {
        "Who are you?": "Rupert Godfrey, shopkeeper and proud keeper of these shelves. I believe good tools and honest service make for a good day.",
        "What do you do here?": "I stock bait, lures, rods, and coolers for anglers setting out from the harbor.",
        "How are things?": "Steady, thank you. The shelves are in order, the kettle is warm, and there's always room for one more customer.",
        "What gear do you recommend?": "Start with a rod that suits your budget, then choose bait for the water you're fishing. A cooler is a wise buy once your cache fills quickly.",
        "How did you start the shop?": "I wanted a place where a new angler could get sound advice along with practical gear. That still feels like worthwhile work.",
    },
    "Molly": {
        "Who are you?": "I'm Molly, a marine biologist. I study fish, their habitats, and the little details that make each specimen worth noticing.",
        "What do you do here?": "I run the Aquarium's research desk. Bring me a species I haven't studied yet and I'll add it to the Fishpedia.",
        "How are things?": "Very well! I've got fresh notes, a clear tank, and three new questions about how fish navigate reefs.",
        "What are you researching?": "Today I'm comparing how fish from different locations adapt to their habitats. Every new specimen helps fill in another piece.",
        "How do you study a fish?": "I record its species, size, weight, and identifying traits, then compare those observations with existing research.",
    },
}

STORE_ITEMS = {
    "wad": {
        "category": "bait",
        "cost": 0.0,
        "description": "A rough, free mash of bait. It works in a pinch, but it rarely tempts the better fish.",
        "bonus": -0.04,
        "location_bonus": {},
        "fish_bonus": {}
    },
    "Worm": {
        "category": "bait",
        "cost": 5.0,
        "description": "A classic freshwater bait that lures fish near the bottom and along the shallows.",
        "bonus": 0.05,
        "location_bonus": {"Freshwater Lake": 0.04, "Muddy River": 0.03},
        "fish_bonus": {"Carp": 0.18, "Catfish": 0.12}
    },
    "Leech": {
        "category": "bait",
        "cost": 5.0,
        "description": "A lively live bait that works well for predatory fish and fish that hunt under cover.",
        "bonus": 0.05,
        "location_bonus": {"Freshwater Lake": 0.03, "Muddy River": 0.04},
        "fish_bonus": {"Muskellunge": 0.20, "Pike": 0.18}
    },
    "Cricket": {
        "category": "bait",
        "cost": 3.0,
        "description": "Small, active bait for fish that feed near the surface and among vegetation.",
        "bonus": 0.04,
        "location_bonus": {"Freshwater Lake": 0.04, "Muddy River": 0.02},
        "fish_bonus": {}
    },
    "Bread": {
        "category": "bait",
        "cost": 2.0,
        "description": "Simple, cheap bait suited to shallow water and slower fish that feed near the bank.",
        "bonus": 0.03,
        "location_bonus": {"Freshwater Lake": 0.03, "Muddy River": 0.02},
        "fish_bonus": {}
    },
    "Corn": {
        "category": "bait",
        "cost": 2.0,
        "description": "A hardy bait that draws bottom-feeders and large, slower fish from muddy water.",
        "bonus": 0.04,
        "location_bonus": {"Freshwater Lake": 0.02, "Muddy River": 0.04},
        "fish_bonus": {}
    },
    "Cheese": {
        "category": "bait",
        "cost": 5.0,
        "description": "A dense, durable bait popular with fish that patrol the bottom in calm shallows.",
        "bonus": 0.05,
        "location_bonus": {"Freshwater Lake": 0.03, "Muddy River": 0.03},
        "fish_bonus": {}
    },
    "Shiner": {
        "category": "bait",
        "cost": 3.0,
        "description": "A lively baitfish that especially helps when chasing larger predatory species.",
        "bonus": 0.06,
        "location_bonus": {"Freshwater Lake": 0.04, "Muddy River": 0.04},
        "fish_bonus": {"Largemouth Bass": 0.20, "Brown Trout": 0.14}
    },
    "Crankbait": {
        "category": "lure",
        "cost": 12.0,
        "description": "A diving lure that excels in freshwater and river channels with cover and depth.",
        "bonus": 0.06,
        "location_bonus": {"Freshwater Lake": 0.05, "Muddy River": 0.04},
        "fish_bonus": {"Walleye": 0.18, "Pike": 0.16}
    },
    "Soft Swimbait": {
        "category": "lure",
        "cost": 15.0,
        "description": "A flexible swimbait made for smooth water and better depth control in open lanes.",
        "bonus": 0.07,
        "location_bonus": {"Coastal Reef": 0.04, "Open Ocean": 0.05},
        "fish_bonus": {"Bluefin Tuna": 0.18, "Barracuda": 0.12}
    },
    "Inline Spinner": {
        "category": "lure",
        "cost": 10.0,
        "description": "A flashing lure that triggers strikes from fast-moving fish in open or moving water.",
        "bonus": 0.05,
        "location_bonus": {"Open Ocean": 0.04, "Coastal Reef": 0.03},
        "fish_bonus": {"Bluefish": 0.15, "Sockeye Salmon": 0.12}
    },
    "Topwater Popper": {
        "category": "lure",
        "cost": 8.0,
        "description": "A surface lure that provokes explosive strikes from fish hunting just below the surface.",
        "bonus": 0.05,
        "location_bonus": {"Freshwater Lake": 0.04, "Coastal Reef": 0.03},
        "fish_bonus": {"Bluefish": 0.14, "Barracuda": 0.12}
    },
    "Round-Head Jig": {
        "category": "lure",
        "cost": 8.0,
        "description": "Heavy enough to reach the bottom, great for fish that patrol near structure and ledges.",
        "bonus": 0.05,
        "location_bonus": {"Muddy River": 0.04, "Coastal Reef": 0.04},
        "fish_bonus": {"Red Grouper": 0.16, "Blackfish": 0.12}
    },
    "Old Rod": {
        "category": "rod",
        "cost": 0.0,
        "description": "An old rod with a worn reel. It gets the job done, but it doesn't help much.",
        "bonus": -0.04,
        "location_bonus": {},
        "fish_bonus": {}
    },
    "Bamboo Rod": {
        "category": "rod",
        "cost": 20.0,
        "description": "A light, simple rod that makes casting more natural and improves overall control.",
        "bonus": 0.04,
        "location_bonus": {},
        "fish_bonus": {}
    },
    "Fiberglass Rod": {
        "category": "rod",
        "cost": 50.0,
        "description": "A durable rod with extra flex, improving cast accuracy and fish handling.",
        "bonus": 0.07,
        "location_bonus": {},
        "fish_bonus": {}
    },
    "Graphite Rod": {
        "category": "rod",
        "cost": 88.0,
        "description": "A precise, responsive rod that helps anglers work lures and land tougher fish.",
        "bonus": 0.10,
        "location_bonus": {},
        "fish_bonus": {}
    },
    "Carbon Composite Rod": {
        "category": "rod",
        "cost": 150.0,
        "description": "A premium rod built for hard casts and consistent power across every location.",
        "bonus": 0.13,
        "location_bonus": {},
        "fish_bonus": {}
    },
    "Small Red Cooler": {
        "category": "cooler",
        "cost": 10.0,
        "description": "Adds room for 12 fish in the cache.",
        "bonus": 0.0,
        "capacity": 12,
        "location_bonus": {},
        "fish_bonus": {}
    },
    "Medium Cooler": {
        "category": "cooler",
        "cost": 80.0,
        "description": "Adds room for 20 fish in the cache.",
        "bonus": 0.0,
        "capacity": 20,
        "location_bonus": {},
        "fish_bonus": {}
    },
    "Name Brand Cooler": {
        "category": "cooler",
        "cost": 140.0,
        "description": "Adds room for 38 fish in the cache.",
        "bonus": 0.0,
        "capacity": 38,
        "location_bonus": {},
        "fish_bonus": {}
    },
    "Industrial Cooler": {
        "category": "cooler",
        "cost": 500.0,
        "description": "Adds room for 69 fish in the cache.",
        "bonus": 0.0,
        "capacity": 69,
        "location_bonus": {},
        "fish_bonus": {}
    }
}
