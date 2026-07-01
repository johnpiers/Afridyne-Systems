import os
import json
import shutil

icons_dir = "overrides/.icons"
js_file_path = "docs/javascripts/iconsearch.js"
site_assets_dest = "docs/assets/local_icons"

if not os.path.exists(icons_dir):
    print(f"Error: Could not find icons directory at: {icons_dir}")
    exit(1)

os.makedirs(site_assets_dest, exist_ok=True)
for root, dirs, files in os.walk(icons_dir):
    for file in files:
        if file.endswith(".svg"):
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(src_file, icons_dir)
            dest_file = os.path.join(site_assets_dest, rel_path)
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            if not os.path.exists(dest_file) or os.path.getmtime(src_file) > os.path.getmtime(dest_file):
                shutil.copy2(src_file, dest_file)

icon_database = []

for root, dirs, files in os.walk(icons_dir):
    for file in files:
        if file.endswith(".svg"):
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, icons_dir)
            clean_path_forward = rel_path.replace("\\", "/")
            
            if clean_path_forward.endswith(".svg"):
                clean_path = clean_path_forward[:-4]
            else:
                clean_path, _ = os.path.splitext(clean_path_forward)
            
            icon_handle = clean_path.replace("/", "-")
            shortcode = f":{icon_handle}:"
            pure_filename, _ = os.path.splitext(file)
            
            icon_set_string = "root"
            if "bootstrap-icons" in clean_path_forward:
                icon_set_string = "bootstrap-icons"
            elif "fontawesome" in clean_path_forward:
                icon_set_string = "fontawesome"
            elif "octicons" in clean_path_forward:
                icon_set_string = "octicons"
            elif "simple" in clean_path_forward:
                icon_set_string = "simple"
            
            icon_database.append({
                "name": icon_handle.replace("-", " ").lower(),
                "shortcode": shortcode,
                "set": icon_set_string,
                "iconName": pure_filename,
                "path": clean_path_forward,
                "type": "icons"
            })

print("Processing multi-color emoji asset map index...")

emoji_hex_map = {
    "smile": "1f642", "laughing": "1f606", "blush": "1f60a", "smiley": "1f603", 
    "heart_eyes": "1f60d", "winking_eye": "1f609", "kissing_heart": "1f618", 
    "thump": "1f440", "heart": "2764", "broken_heart": "1f494", "star": "2b50", 
    "sparkles": "2728", "fire": "1f525", "rocket": "1f680", "100": "1f4af", 
    "thumbsup": "1f44d", "thumbsdown": "1f44e", "clap": "1f44f", "pray": "1f64f", 
    "eyes": "1f440", "party_popper": "1f389", "tada": "1f389", "warning": "26a0", 
    "exclamation": "2757", "question": "2753", "check": "2705", "x": "274c", 
    "arrow_right": "27a1", "gear": "2699", "computer": "1f4bb", "floppy_disk": "1f4be",
    "coffee": "2615", "beer": "1f37a", "pizza": "1f355", "alien": "1f47d", 
    "ghost": "1f47b", "robot": "1f916", "globe_with_meridians": "1f310", 
    "compass": "1f9ed", "fox": "1f98a", "dinosaur": "1f995", "desktop_computer": "1f5a5", 
    "laptop": "1f4bb", "keyboard": "2328", "mouse": "1f5b1", "printer": "1f5a8", 
    "joystick": "1f579", "minidisc": "1f4bd", "vhs": "1f4fc", "camera": "1f4f7", 
    "video_camera": "1f4f9", "tv": "1f4fa", "radio": "1f4fb", "microphone": "1f3a4", 
    "headset": "1f3a7", "level_slider": "1f39a", "control_knobs": "1f39b", 
    "battery": "1f50b", "electric_plug": "1f50c", "bulb": "1f4a1", "flashlight": "1f526", 
    "candle": "1f56f", "wastebasket": "1f5d1", "oil_drum": "1f6e2", "moneybag": "1f4b0", 
    "credit_card": "1f4b3", "gem": "1f48e", "lock": "1f512", "unlock": "1f513", 
    "lock_with_ink_pen": "1f50f", "closed_lock_with_key": "1f510", "key": "1f511", 
    "hammer": "1f528", "axe": "1fa93", "pick": "26cf", "hammer_and_pick": "2692", 
    "hammer_and_wrench": "1f6e0", "wrench": "1f527", "nut_and_bolt": "1f529", 
    "balance_scale": "2696", "chains": "26d3", "toolbox": "1f9f0", "magnet": "1f9aa", 
    "shield": "1f6e1", "file_folder": "1f4c1", "open_file_folder": "1f4c2", 
    "card_index_dividers": "1f4c7", "calendar": "1f4c5", "tear_off_calendar": "1f4c6", 
    "card_index": "1f4c4", "chart_with_upwards_trend": "1f4c8", "chart_with_downwards_trend": "1f4c9", 
    "bar_chart": "1f4ca", "clipboard": "1f4cb", "pushpin": "1f4cc", "round_pushpin": "1f4cd", 
    "paperclip": "1f4ce", "linked_paperclips": "1f587", "straight_ruler": "1f4cf", 
    "triangular_ruler": "1f4d0", "bookmark_tabs": "1f4d1", "ledger": "1f4d2", 
    "notebook": "1f4d3", "notebook_with_decorative_cover": "1f4d4", "books": "1f4da", 
    "book": "1f4d6", "bookmark": "1f516", "envelope": "2709", "envelope_with_arrow": "1f4e9", 
    "incoming_envelope": "1f4e8", "e-mail": "1f4e7", "package": "1f4e6", 
    "mailbox": "1f4eb", "mailbox_closed": "1f4ea", "mailbox_with_mail": "1f4ec", 
    "mailbox_with_no_mail": "1f4ed", "postbox": "1f4ee", "memo": "1f4dd", 
    "phone": "260e", "telephone_receiver": "1f4de", "pager": "1f4df", 
    "fax": "1f4e0", "satellite": "1f4e1", "bell": "1f514", "no_bell": "1f515", 
    "loudspeaker": "1f4e2", "mega": "1f4e3", "speech_balloon": "1f4ac", 
    "thought_balloon": "1f4ad", "speech_left": "1f5e8", "arrow_up": "2b06", 
    "arrow_down": "2b07", "arrow_left": "2b05", "left_right_arrow": "2194", 
    "arrow_up_down": "2195", "arrow_upper_left": "2196", "arrow_upper_right": "2197", 
    "arrow_lower_right": "2198", "arrow_lower_left": "2199", "leftwards_arrow_with_hook": "21a9", 
    "arrow_right_hook": "21aa", "arrows_clockwise": "1f503", "arrows_counterclockwise": "1f504", 
    "back": "1f519", "end": "1f51a", "on": "1f51b", "soon": "1f51c", 
    "top": "1f51d", "place_of_worship": "1f64f", "atm": "1f3e7", "put_litter_in_its_place": "1f6ae",
    "alarm_clock": "23f0", "alembic": "2697", "alien_monster": "1f47e", "ambulance": "1f691", 
    "american_football": "1f3c8", "amethyst": "1fa9a", "amphora": "1f3fa", "anatomical_heart": "1fac0", 
    "anchor": "2693", "angel": "1f47c", "anger_symbol": "1f4a2", "angry_face": "1f620", 
    "angry_face_with_horns": "1f47f", "anguished_face": "1f627", "ant": "1f41c", "antenna_bars": "1f4f6", 
    "anxious_face_with_sweat": "1f630", "apple": "1f34e", "apron": "1f9ba", "aquarius": "2652", 
    "aries": "2648", "articulated_lorry": "1f69b", "artificial_satellite": "1f6f0", "artist_palette": "1f3a8", 
    "asymmetrical_airplane": "1f6e9", "astonished_face": "1f632", "auto_rickshaw": "1f6fa", "avocado": "1f951", 
    "axe_tool": "1fa93", "accordion": "1fa97", "adhesive_bandage": "1fa79", "admission_tickets": "1f39f", 
    "aerial_tramway": "1f6a1", "airplane": "2708", "airplane_arrival": "1f6ec", "airplane_departure": "1f6eb", 
    "alligator": "1f40a", "almond": "1f95c", "badger": "1f9a1", "baggage_claim": "1f6c4", 
    "baguette_bread": "1f956", "bale_of_cotton": "1f9f1", "balloon": "1f388", 
    "bamboo": "1f38d", "banana": "1f34c", "banjo": "1fa95", "bank": "1f3e6", 
    "barber_pole": "1f488", "basket": "1f9fa", "basketball": "1f3c0", "bat": "1f987", 
    "bathtub": "1f6c1", "beacon": "1f6a8", "beaver": "1f9ab", "bed": "1f6cf", 
    "beer_mug": "1f37a", "beetle": "1f41e", "bell_hop": "1f3ce", "bento_box": "1f371", 
    "beverage_box": "1f9c3", "bicycle": "1f6b2", "bikini": "1f459", "billed_cap": "1f9e2", 
    "biomechanics": "1f9be", "bird": "1f426", "birthday_cake": "1f382",
    "bison": "1f9ac", "biting_lip": "1fae6", "black_heart": "1f5a4", 
    "black_large_square": "2b1b", "black_medium_square": "25fc", "black_nib": "2712", "black_square_button": "1f532", 
    "blossom": "1f33c", "blowfish": "1f421", "blue_book": "1f4d8", "blue_heart": "1f499", 
    "blue_square": "1f535", "blueberry": "1fad0", "boar": "1f417", "bomb": "1f4a3", 
    "bone": "1f9b4", "bookmarked": "1f516", "boomerang": "1fa83", "bottle_with_popping_cork": "1f37e", 
    "bouquet": "1f490", "bow_and_arrow": "1f3f9", "bowl_with_spoon": "1f963", "bowling": "1f3b3", 
    "boxing_glove": "1f94a", "boy_avatar": "1f466", "brain": "1f9e0", "bread": "1f35e", 
    "breast_feeding": "1f931", "brick": "1f9f1", "bridge_at_night": "1f309", "briefcase": "1f4bc", 
    "briefs": "1fa71", "bright_button": "1f550", "broccoli": "1f966", "broom": "1f9f9", 
    "brown_heart": "1f90e", "bubble_tea": "1f9cb", "bubbles": "1fae5", "bucket": "1faa3", 
    "bug_insect": "1f41b", "building_construction": "1f3d7", "bullet_train": "1f685", "burrito": "1f32f", 
    "bus": "1f68c", "bus_stop": "1f68f", "butter": "1f9c8", "butterfly": "1f98b", 
    "cactus": "1f335", "calendar_tear": "1f4c6", "camel": "1f42b", "camera_flash": "1f4f8", 
    "camping": "1f3d5", "canadian_flag": "1f3ca", "canary": "1f424", "cancer_sign": "264b", 
    "candle_stick": "1f56f", "candy": "1f36c", "canned_food": "1f96b", "canoe": "1f6f6", 
    "capricorn": "2651", "car_automobile": "1f697", "card_file_box": "1f4c4", "card_index_box": "1f4c7", 
    "carp_streamer": "1f38f", "carousel_horse": "1f3a0", "carpenter_saw": "1fa9a",
    "carrot": "1f955", "castle": "1f3f0", "cat_avatar": "1f431", "caterpillar": "1f41b", 
    "celebration_balloon": "1f388", "cell_phone": "1f4f1", "centcent": "1f31f", "chain_links": "26d3", 
    "chair": "1fa91", "champagne": "1f37e", "cheese_wedge": "1f9c0", "cherries": "1f352", 
    "cherry_blossom": "1f338", "chess_pawn": "265f", "chestnut": "1f330", "chicken": "1f414", 
    "child": "1f9d2", "children_crossing": "1f6b8", "chili_pepper": "1f336", "chipmunk": "1f43f", 
    "chocolate_bar": "1f36b", "chopsticks": "1f962", "christmas_tree": "1f384", "church": "26ea", 
    "cigarette": "1f6ac", "cinema": "1f3a6", "circus_tent": "1f3aa", "cityscape": "1f3d9", 
    "clapper_board": "1f3ac", "clinking_glasses": "1f37b", "clinking_beer_mugs": "1f37a", "clipboard_task": "1f4cb", 
    "clock_face": "1f550", "closed_mailbox": "1f4ea", "closed_umbrella": "1f302", "cloud_with_lightning": "1f329", 
    "cloud_with_rain": "1f327", "cloud_with_snow": "1f328", "clown_face": "1f921", "club_suit": "2663", 
    "clutch_bag": "1f45c", "coal": "1faa2", "coaster_rail": "1f3a2", "cocktail_glass": "1f378", 
    "coconut": "1f965", "coffin": "26b0", "coin": "1fa99", "cold_face": "1f976", 
    "comet": "2604", "compass_rose": "1f9ed", "computer_disk": "1f4bd", "computer_mouse": "1f5b1", 
    "confetti_ball": "1f38a", "confounded_face": "1f616", "confused_face": "1f615", "construction_sign": "1234", 
    "construction_worker_man": "1f477", "control_knob": "1f39b", "convenience_store": "1f3ea", "cook": "1f468", 
    "cookie": "1f36a", "cooking_pan": "1f373", "cool_button": "1f192", "couch_and_lamp": "1f6cb", 
    "cow_face": "1f42e", "cowboy_hat_face": "1f920",
    "monkey_face": "1f435", "monkey": "1f412", "gorilla": "1f98d", "orangutan": "1f9a7",
    "dog_face": "1f436", "dog": "1f415", "guide_dog": "1f9ae", "service_dog": "1f415_200d_1f9ae",
    "poodle": "1f429", "wolf": "1f43a", "fox_face": "1f98a", "raccoon": "1f99d",
    "cat_face": "1f431", "cat": "1f408", "black_cat": "1f408-200d-2b1b", "lion": "1f981",
    "tiger_face": "1f42f", "tiger": "1f405", "leopard": "1f406", "horse_face": "1f434",
    "horse": "1f40e", "unicorn": "1f984", "zebra": "1f993", "deer": "1f98c",
    "cow_face": "1f42e", "ox": "1f402", "water_buffalo": "1f403",
    "cow": "1f404", "pig_face": "1f437", "pig": "1f416", "boar": "1f417",
    "pig_snout": "1f443", "ram": "1f40f", "ewe": "1f411", "goat": "1f410",
    "camel": "1f42a", "two_horn_camel": "1f42b", "llama": "1f999", "giraffe": "1f992",
    "elephant": "1f418", "mammoth": "1f9a3", "rhinoceros": "1f98f", "hippopotamus": "1f99b",
    "mouse_face": "1f42d", "mouse": "1f401", "rat": "1f400", "hamster": "1f439",
    "rabbit_face": "1f430", "rabbit": "1f407", "chipmunk": "1f43f", "beaver": "1fa9b",
    "hedgehog": "1f994", "bat": "1f987", "bear": "1f43b", "polar_bear": "1f43b-200d-2744-fe0f",
    "koala": "1f428", "panda": "1f43c", "sloth": "1f9a5", "otter": "1f9a6",
    "skunk": "1f9a4", "kangaroo": "1f998", "badger": "1f9a1", "frog": "1f438",
    "crocodile": "1f40a", "turtle": "1f422", "lizard": "1f98e", "snake": "1f40d",
    "dragon_face": "1f432", "dragon": "1f409", "sauropod": "1f995", "t_rex": "1f996",
    "whale_spouting": "1f433", "whale": "1f40b", "dolphin": "1f42c", "seal": "1f9a2",
    "fish": "1f41f", "tropical_fish": "1f420", "blowfish": "1f421", "shark": "1f988",
    "octopus": "1f419", "spiral_shell": "1f41a", "coral": "1fab8", "snail": "1f40c",
    "butterfly": "1f98b", "bug": "1f41b", "ant": "1f41c", "bee": "1f41d",
    "beetle": "1fab2", "ladybug": "1f41e", "cricket": "1f997", "cockroach": "1fab3",
    "spider": "1f577", "spider_web": "1f578", "scorpion": "1f982", "mosquito": "1f99f",
    "fly": "1fab0", "worm": "1fab1", "microbe": "1f9a0", "bouquet": "1f490",
    "cherry_blossom": "1f343", "white_flower": "1f4ae", "rosette": "1f3f5", "rose": "1f339",
    "wilted_flower": "1f940", "hibiscus": "1f33a", "sunflower": "1f33b", "blossom": "1f33c",
    "tulip": "1f337", "lotus_flower": "1fab7", "seedling": "1f331", "potted_plant": "1fab4",
    "evergreen_tree": "1f332", "deciduous_tree": "1f333", "palm_tree": "1f334", "cactus": "1f335",
    "sheaf_of_rice": "1f33e", "herb": "1f33f", "shamrock": "2618", "four_leaf_clover": "1f340",
    "maple_leaf": "1f341", "fallen_leaf": "1f342", "leaf_fluttering": "1f343", "empty_nest": "1fab9",
    "nest_with_eggs": "1faba", "mushroom": "1f344", "turkey": "1f983", "chicken": "1f414",
    "rooster": "1f413", "hatching_chick": "1f423", "baby_chick": "1f424", "front_chick": "1f425",
    "bird": "1f426", "penguin": "1f427", "dove": "1f54a", "eagle": "1f985",
    "duck": "1f986", "swan": "1f9a2", "owl": "1f989", "dodo": "1f9a3",
    "feather": "1fab6", "flamingo": "1f9a9", "peacock": "1f99a", "parrot": "1f99c",
    "black_bird": "1f427", "goose": "1faba", "wing": "1fabd", "phoenix": "1f426_200d_1f525",
    "wood": "1fab5", "shell": "1f41a", "paw_prints": "1f43e", "clover": "1f340",
    "sprout": "1f331", "tree": "1f333", "bamboo": "1f38d", "moss": "1f9ab",
    "log": "1fab5", "bark": "1fab5", "root": "1fab4", "trunk": "1f333",
    "stump": "1fab5", "twig": "1f33f", "seed": "1f331", "bud": "1f337",
    "petal": "1f338", "fern": "1f33f", "weed": "1f344", "seaweed": "1f33e",
    "kelp": "1f33e", "coral_reef": "1fab8", "anemone": "1fab8", "jellyfish": "1f991",
    "starfish": "1f41f", "crab": "1f980", "lobster": "1f99e", "shrimp": "1f9a0",
    "squid": "1f991", "oyster": "1f9aa", "clam": "1f9aa", "urchin": "1f41f",
    "sponge": "1f9fd", "barnacle": "1f41a", "crayfish": "1f99e", "krill": "1f9a0",
    "tadpole": "1f438", "newt": "1f40e", "salamander": "1f40e", "toad": "1f438",
    "gecko": "1f40e", "iguana": "1f40e", "chameleon": "1f40e", "tortoise": "1f422",
    "terrapin": "1f422", "house": "1f3e0", "house_with_garden": "1f3e1",
    "office_building": "1f3e2", "post_office": "1f3e3",
    "hospital": "1f3e4", "bank": "1f3e5", "hotel": "1f3e6", "love_hotel": "1f3e9",
    "convenience_store": "1f3ea", "school": "1f3eb", "department_store": "1f3ec", "factory": "1f3ed",
    "japanese_castle": "1f3ef", "western_castle": "1f3f0", "wedding_church": "1f492", "department": "1f3ec",
    "stadium": "1f3df", "classical_building": "1f3db", "hut": "1f6d6", "elevator": "1f6dd",
    "construction": "1f3d7", "houses": "1fae3", "derelict_house": "1f3d8", "brick": "1f9f1",
    "roof": "1f3e0", "door": "1f6aa", "gate": "1f6aa", "window": "1fa9f",
    "store": "1f3ec", "shop": "1f3ec", "skyscraper": "1f3f0", "tower": "1f5fc",
    "tokyo_tower": "1f5fc", "eiffel_tower": "1f5fc", "statue_of_liberty": "1f5fd", "fountain": "26f2",
    "tent": "26fa", "teepee": "26fa", "cabin": "1f6d6", "shack": "1f6d6",
    "barn": "1f3dc", "farmhouse": "1f3dc", "mill": "1f3dc", "windmill": "1f3dc",
    "silo": "1f3dc", "greenhouse": "1f3dc", "garage": "1f3e0", "carport": "1f3e0",
    "shed": "1f6d6", "warehouse": "1f3ed", "power_plant": "1f3ed", "refinery": "1f3ed",
    "dock": "1f3d5", "pier": "1f3d5", "harbour": "1f3d5", "marina": "1f3d5",
    "bridge": "1f309", "suspension_bridge": "1f309", "viaduct": "1f309", "aqueduct": "1f309",
    "tunnel": "1f307", "underpass": "1f307", "subway_station": "1f687", "train_station": "1f689",
    "airport": "1f6eb", "airfield": "1f6eb", "runway": "1f6eb", "hangar": "1f6eb",
    "bus_stop": "1f68f", "bus_station": "1f68f", "shelter": "1f6d6", "pavilion": "1f3db",
    "gazebo": "1f3db", "pergola": "1f3db", "monument": "1f3db", "obelisk": "1f3db",
    "shrine": "26e9", "temple": "1f54d", "church": "26ea", "mosque": "1f54c",
    "synagogue": "1f54d", "cathedral": "26ea", "chapel": "26ea", "monastery": "26ea",
    "convent": "26ea", "abbey": "26ea", "pagoda": "1f3ef", "stupa": "1f54d",
    "pyramid": "1f5fc", "sphinx": "1f5fc", "amphitheater": "1f3df", "colosseum": "1f3df",
    "pantheon": "1f3db", "parthenon": "1f3db", "arena": "1f3df", "auditorium": "1f3df",
    "theater": "1f3ad", "cinema": "1f3ac", "movie_house": "1f3ac", "playhouse": "1f3ad",
    "museum": "1f3db", "gallery": "1f3db", "exhibition_hall": "1f3db", "library": "1f4da",
    "bookstore": "1f4da", "archive": "1f4da", "vault": "1f512", "bank_vault": "1f512",
    "safe_house": "1f3e0", "bunker": "1f6d6", "fort": "1f3f0", "fortress": "1f3f0",
    "citadel": "1f3f0", "bastion": "1f3f0", "rampart": "1f3f0", "palace": "1f3ef",
    "manor": "1f3e1", "mansion": "1f3e1", "estate": "1f3e1", "villa": "1f3e1",
    "chateau": "1f3f0", "lodge": "1f6d6", "resort": "1f3e6", "motel": "1f3e6",
    "inn": "1f3e6", "hostel": "1f3e6", "tavern": "1f3e6", "pub": "1f3e6",
    "bar": "1f3e6", "saloon": "1f3e6", "cafe": "2615", "coffee_shop": "2615",
    "bistro": "2615", "restaurant": "1f374", "diner": "1f374", "eatery": "1f374",
    "pizzeria": "1f355", "bakery": "1f35e", "patisserie": "1f35e", "confectionery": "1f36c",
    "candy_shop": "1f36c", "ice_cream_parlor": "1f366", "grocery": "1f3ea", "supermarket": "1f3ea",
    "bodega": "1f3ea", "bazaar": "1f3ec", "market": "1f3ec", "marketplace": "1f3ec",
    "mall": "1f3ec", "arcade": "1f3ec", "boutique": "1f3ec", "plaza": "1f3db",
    "square": "1f3db", "courtyard": "1f3db", "atrium": "1f3db", "cloisters": "26ea",
    "campus": "1f3eb", "quad": "1f3eb", "academy": "1f3eb", "college": "1f3eb",
    "university": "1f3eb", "observatory": "1f3ed", "laboratory": "1f3ed", "studio": "1f3ac",
    "crown": "1f451", "womans_hat": "1f452", "glasses": "1f453", "sunglasses": "1f576",
    "necktie": "1f454", "tshirt": "1f455", "jeans": "1f456", "dress": "1f457",
    "kimono": "1f458", "sari": "1f97b", "one_piece_swimsuit": "1f601", "bikini": "1f459",
    "womans_clothes": "1f45a", "purse": "1f45b", "handbag_c": "1f45c", "pouch": "1f45d",
    "shopping_bags": "1f6cd", "backpack": "1f392", "thong_sandal": "1fa74", "womans_flat_shoe": "1f461",
    "high_heeled_shoe": "1f460", "womans_boot": "1f462", "mans_shoe": "1f45e", "running_shoe": "1f45f",
    "hiking_boot": "1f97e", "sneaker": "1f45f", "slipper": "1f97f",
    "socks": "1f9e6", "gloves": "1f9e4", "scarf": "1f9e3", "coat": "1f9e5",
    "lab_coat": "1f97c", "safety_vest": "1f9ba", "goggles": "1f97d", "apron": "1f9bb",
    "briefcase": "1f4bc", "luggage": "1f9f3", "yarn": "1f9f6", "thread": "1f9f5",
    "safety_pin": "1f9f7", "needle": "1f9ea", "scissors": "2702", "razor": "1fa92",
    "mirror": "1fa9a", "comb": "1fa94", "toothbrush": "1fa95", "soap": "1f9fd",
    "basket": "1f9fa", "shopping_cart": "1f6d2", "bellhop_bell": "1f6ce",
    "cigarette": "1f6ac", "coffin": "26b0", "funeral_urn": "26b1", "headstone": "1faa6",
    "plunger": "1faa0", "bucket": "1faa3", "mouse_trap": "1faa4", "ladder": "1faa2",
    "window_c": "1fa9f", "mirror_c": "1fa9a", "chair": "1fa91", "bench": "1f6cf",
    "bed": "1f6cf", "couch_and_lamp": "1f6cb", "toilet": "1f6bd", "shower": "1f6bf",
    "bathtub": "1f6c1", "key_c": "1f511", "old_key": "1f5dd", "door_c": "1f6aa",
    "window_shade": "1fa9f", "curtain": "1fa9f", "blinds": "1fa9f", "rug": "1fa91",
    "carpet": "1fa91", "pillow": "1f6cf", "blanket": "1f6cf", "quilt": "1f6cf",
    "sheet": "1f6cf", "mattress": "1f6cf", "cushion": "1fa91", "stool": "1fa91",
    "desk": "1f4bc", "table": "1fa91", "dresser": "1fa91", "wardrobe": "1fa91",
    "cabinet": "1fa91", "cupboard": "1fa91", "drawer": "1fa91", "shelf": "1fa91",
    "bookcase": "1f4da", "clock": "1f551", "watch": "231a", "hourglass": "231b",
}

for emoji_name, hex_code in emoji_hex_map.items():
    icon_database.append({
        "name": emoji_name.replace("_", " ").lower(),
        "shortcode": f":{emoji_name}:",
        "set": "color-emoji",
        "iconName": hex_code,
        "path": "",
        "type": "emojis"
    })

print(f"Found {len(icon_database)} total assets. Updating javascript file...")

js_template_prefix = """document.addEventListener("DOMContentLoaded", function() {
  const searchContainers = document.querySelectorAll('[data-mdx-component="iconsearch"]');
  const iconDatabase = """

js_template_suffix = r""";

  searchContainers.forEach(container => {
    const input = container.querySelector('[data-mdx-component="iconsearch-query"]');
    const resultList = container.querySelector('.mdx-iconsearch-result__list');
    const select = container.querySelector('[data-mdx-component="iconsearch-select"]');
    const meta = container.querySelector('[data-mdx-component="iconsearch-meta"]');

    function performSearch() {
      const query = input.value.toLowerCase().trim();
      const selectedType = select ? select.value : "all";
      
      if (query.length < 2) {
        resultList.innerHTML = "";
        if (meta) meta.textContent = "";
        return;
      }

      const matches = iconDatabase.filter(item => {
        const matchesQuery = item.name.includes(query) || item.shortcode.includes(query);
        const matchesType = (selectedType === "all") || (item.type === selectedType);
        return matchesQuery && matchesType;
      });

            if (meta) {
        meta.textContent = `${matches.length} matches`;
      }

      if (matches.length === 0) {
        resultList.innerHTML = `<li class="mdx-iconsearch-result__item" style="padding: 12px; color: #888;">No icons found</li>`;
        return;
      }

      const limitedMatches = matches.slice(0, 100);

      resultList.innerHTML = limitedMatches.map(item => {
        let visualHtml = "";
        if (item.type === "emojis") {
          // Rebuild the live open-source open directory layout with zero truncation risk
          const urlParts = ["https:", "", "cdn.jsdelivr.net", "gh", "twitter", "twemoji@14.0.2", "assets", "svg", ""];
          const cleanUrl = urlParts.join("/") + item.iconName + ".svg";
          visualHtml = `<img src="${cleanUrl}" style="width: 24px; height: 24px;" />`;
        } else {
          const maskParts = ["", "assets", "local_icons", item.path];
          const localUrl = maskParts.join("/");
          visualHtml = `<div style="width: 24px; height: 24px; background-color: currentColor; display: inline-block; vertical-align: middle; -webkit-mask: url('${localUrl}') no-repeat center / contain; mask: url('${localUrl}') no-repeat center / contain;"></div>`;
        }
        return `<li class="mdx-iconsearch-result__item" style="display: flex; align-items: center; justify-content: space-between; padding: 8px; border-bottom: 1px solid #222;">
          <div style="display: flex; align-items: center; gap: 12px;">
            ${visualHtml}
            <span style="font-family: monospace; color: #00bedb;">${item.shortcode}</span>
          </div>
          <button class="mdx-iconsearch-copy" onclick="navigator.clipboard.writeText('${item.shortcode}'); this.textContent='Copied!'; setTimeout(() => this.textContent='Copy', 1500);" style="padding: 4px 8px; font-size: 11px; background: #222; border: 1px solid #444; color: #aaa; cursor: pointer; border-radius: 3px;">Copy</button>
        </li>`;
      }).join("");
    }

    if (input) {
      input.addEventListener("input", performSearch);
    }
    if (select) {
      select.addEventListener("change", performSearch);
    }
  });
});"""

with open(js_file_path, "w", encoding="utf-8") as js_file:
    js_file.write(js_template_prefix + json.dumps(icon_database, indent=2) + js_template_suffix)

print("Success: Generated index script updated.")
