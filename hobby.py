import random
import numpy as np
import skfuzzy as fuzz
from evolutionary_algo import run_evolutionary_algorithm
from learning_path import learning_paths

# Define your hobbies and their descriptions as before
hobbies = {
    "Gardening": "Growing plants and flowers in a garden.",
    "Photography": "Capturing moments using a camera.",
    "Painting": "Creating artwork using paints.",
    "Cycling": "Riding a bicycle for exercise or leisure.",
    "Cooking": "Preparing food and experimenting with recipes.",
    "Writing": "Expressing thoughts and ideas through written words.",
    "Hiking": "Walking in nature, usually on trails.",
    "Dancing": "Moving rhythmically to music.",
    "Traveling": "Exploring new places and cultures.",
    "Fishing": "Catching fish for recreation or sport.",
    "Reading": "Engaging with written content for pleasure or knowledge.",
    "Knitting": "Creating fabric from yarn using needles.",
    "Crafting": "Making decorative items by hand.",
    "Playing an Instrument": "Making music using a musical instrument.",
    "Yoga": "Practicing physical postures, breathing, and meditation.",
    "Cooking Classes": "Learning to cook through guided instruction.",
    "Gaming": "Engaging in video games for entertainment or competition.",
    "Investing": "Allocating money into assets or stocks with the goal of earning a financial return.",
    "Journaling": "Writing personal reflections or daily entries in a journal or notebook.",
    "Karaoke": "Singing along to recorded music tracks, often in a social setting.",
    "Pottery": "Creating ceramic items by shaping clay and firing it in a kiln.",
    "Birdwatching": "Observing and identifying different species of birds in their natural habitat.",
    "Scrapbooking": "Assembling and decorating a book of memories using photos, mementos, and written content.",
    "Calligraphy": "The art of beautiful handwriting, often used for decorative writing or invitations.",
    "Origami": "The traditional Japanese art of folding paper into intricate designs and shapes.",
    "Martial Arts": "Practicing self-defense techniques and physical fitness through various forms of martial arts.",
    "Blogging": "Writing and publishing content on a website or blog, often about personal interests or experiences.",
    "Woodworking": "Crafting furniture or decorative items from wood using various tools and techniques.",
    "Fitness Training": "Engaging in structured physical exercise to improve health and fitness.",
    "Sculpting": "Creating three-dimensional artworks by shaping materials like clay, stone, or metal.",
    "Homebrewing": "Making beer, wine, or cider at home through fermentation processes.",
    "Geocaching": "Participating in a global treasure hunt using GPS to find hidden containers (geocaches).",
    "Candle Making": "Creating decorative and scented candles from wax and molds.",
    "Virtual Reality Gaming": "Engaging in immersive gaming experiences using virtual reality headsets and technology.",
    "Volunteering": "Offering time and skills to support community service or non-profit organizations.",
    "Sewing": "Creating garments and items from fabric using a needle and thread.",
    "Rock Climbing": "Scaling natural rock formations or indoor climbing walls for sport or recreation.",
    "Astronomy": "Studying celestial objects and phenomena, often through telescopes.",
    "Model Building": "Constructing scale models of vehicles, buildings, or other structures.",
    "Podcasting": "Creating and sharing audio content on various topics through episodes.",
    "Fencing": "Engaging in sword fighting as a competitive sport or recreational activity.",
    "Home Improvement": "Renovating or enhancing living spaces through DIY projects.",
    "Stargazing": "Observing celestial bodies and phenomena in the night sky.",
    "Mindfulness Meditation": "Practicing focused attention and awareness to promote mental well-being.",
    "Graphic Design": "Creating visual content using design software for various media.",
    "Coding": "Writing and developing computer programs or applications.",
    "Collecting": "Gathering items of personal interest, such as stamps, coins, or antiques.",
    "Archery": "Practicing shooting arrows with a bow, either for sport or recreation.",
    "Baking": "Preparing bread, cakes, and pastries, often using an oven and following recipes.",
    "Beachcombing": "Exploring beaches to find interesting shells, stones, and treasures washed ashore.",
    "Flower Arranging": "Creating artistic arrangements with flowers and foliage for decoration.",
    "Metalworking": "Shaping and crafting metal into tools, art, or functional items using various techniques.",
    "Creative Writing": "Expressing thoughts and ideas through imaginative storytelling and narrative.",
    "Herb Gardening": "Growing and cultivating herbs for culinary or medicinal purposes.",
    "Digital Art": "Creating artwork using digital tools and software, such as drawing tablets and graphic design software.",
    "Leatherworking": "Crafting items such as wallets, belts, and bags from leather.",
    "Astral Projection": "Practicing techniques to explore consciousness and experience out-of-body experiences.",
    "Fermenting": "Creating fermented foods and beverages like kimchi, sauerkraut, or kombucha.",
    "Foraging": "Searching for wild food sources, such as mushrooms, herbs, and edible plants in nature.",
    "Birdhouse Building": "Constructing homes for birds to encourage wildlife in your garden.",
    "LARPing (Live Action Role Playing)": "Participating in immersive role-playing games in real-life scenarios.",
    "Cosplay": "Designing and wearing costumes to represent characters from movies, games, or comics.",
    "Beekeeping": "Maintaining beehives and producing honey and beeswax products.",
    "Puzzle Making": "Designing and creating jigsaw puzzles or brain teasers for others to solve.",
    "Stained Glass Art": "Creating art pieces using colored glass.",
    "Creative Writing Workshops": "Participating in group sessions to improve writing skills.",
    "Sculpture": "Creating three-dimensional artworks using materials like clay or metal.",
    "Cartooning": "Drawing comics or cartoons for entertainment.",
    "Music Production": "Composing and producing music using software.",
    "Art Classes": "Taking classes to learn various art techniques.",
    "Cake Decorating": "Designing and decorating cakes for events.",
    "Floral Design": "Arranging flowers for events or home décor.",
    "Fitness Classes": "Participating in group exercise sessions.",
    "Theater": "Participating in or watching live performances.",
    "Self-Defense Classes": "Learning practical self-defense techniques.",
    "Cultural Cooking": "Exploring and preparing dishes from different cultures.",
    "Gardening Workshops": "Attending classes to learn gardening techniques.",
    "Soap Making": "Creating custom soaps with different scents and colors.",
    "Fishing Workshops": "Learning fishing techniques and skills.",
    "Nature Walks": "Taking leisurely walks to observe and enjoy nature.",
    "Language Learning": "Learning new languages for communication and cultural understanding.",
    "Fitness Blogging": "Sharing fitness journeys and tips online.",
    "Stand-up Comedy": "Performing humorous stories or jokes in front of an audience."
}

def fuzzy_inference(age, skill, interest, creativity, physical_activity, social_pref,time_dedication):
    # Ensure all input values are within valid ranges
    age = max(0, min(age, 100))
    skill = max(0, min(skill, 100))
    interest = max(0, min(interest, 100))
    creativity = max(0, min(creativity, 100))
    physical_activity = max(0, min(physical_activity, 100))
    # Ensure social preference is either 0 or 1 (for Solo vs Group)
    social_pref = max(0, min(social_pref, 1))
    time_dedication = max(1, min(time_dedication, 8))

    # Define fuzzy sets for each parameter
    age_levels = [
        fuzz.trimf(np.arange(0, 101, 1), [0, 0, 15]),  # Child
        fuzz.trimf(np.arange(0, 101, 1), [10, 15, 20]),  # Teen
        fuzz.trimf(np.arange(0, 101, 1), [18, 25, 35]),  # Young Adult
        fuzz.trimf(np.arange(0, 101, 1), [30, 45, 60]),  # Middle Aged
        fuzz.trimf(np.arange(0, 101, 1), [55, 70, 100])  # Senior
    ]
    skill_levels = [
        fuzz.trimf(np.arange(0, 101, 1), [0, 0, 50]),  # Beginner
        fuzz.trimf(np.arange(0, 101, 1), [30, 50, 80]),  # Intermediate
        fuzz.trimf(np.arange(0, 101, 1), [60, 100, 100])  # Advanced
    ]
    interest_levels = [
        fuzz.trimf(np.arange(0, 101, 1), [0, 0, 50]),  # Low Interest
        fuzz.trimf(np.arange(0, 101, 1), [30, 50, 80]),  # Medium Interest
        fuzz.trimf(np.arange(0, 101, 1), [60, 100, 100])  # High Interest
    ]
    creativity_levels = [
        fuzz.trimf(np.arange(0, 101, 1), [0, 0, 50]),  # Low Creativity
        fuzz.trimf(np.arange(0, 101, 1), [50, 100, 100])  # High Creativity
    ]
    physical_activity_levels = [
        fuzz.trimf(np.arange(0, 101, 1), [0, 0, 50]),  # Low Physical
        fuzz.trimf(np.arange(0, 101, 1), [50, 100, 100])  # High Physical
    ]

    social_pref_levels = [
        fuzz.trimf(np.arange(0, 2, 1), [0, 0, 1]),  # Solo
        fuzz.trimf(np.arange(0, 2, 1), [0, 1, 1])  # Group
    ]

    time_dedication_levels = [
        fuzz.trimf(np.arange(1, 9, 1), [1, 1, 4]),  # Low Time Dedication (1 to 4 hours)
        fuzz.trimf(np.arange(1, 9, 1), [3, 5, 7]),  # Medium Time Dedication (3 to 7 hours)
        fuzz.trimf(np.arange(1, 9, 1), [6, 8, 8])  # High Time Dedication (6 to 8 hours)
    ]
    # Fuzzy rules for hobby recommendations
    rules = {
        "Gardening": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),  # Solo vs Group preference
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ]),
    ],
    "Painting": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ])
    ],
    "Cycling": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ])
    ],
    "Cooking": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ])
    ],
    "Writing": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ])
    ],
    "Hiking": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ])
    ],
    "Dancing": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ])
    ],
    "Traveling": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ])
    ],
    "Fishing": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ])
    ],
    "Reading": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
            np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
            np.max([1 if social_pref == 0 else 0]),
            np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])  # Time Dedication
        ])
    ],
    "Birdwatching": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Scrapbooking": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Calligraphy": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Origami": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Blogging": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Woodworking": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Fitness Training": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Sculpting": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Homebrewing": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Geocaching": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
    "Candle Making": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Virtual Reality Gaming": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Volunteering": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Sewing": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),  # Solo vs Group preference
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ]),
        ],
    "Rock Climbing": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Astronomy": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Model Building": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Podcasting": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Fencing": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Home Improvement": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Stargazing": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Mindfulness Meditation": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Graphic Design": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Coding": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Collecting": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ]),
        ],
    "Archery": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),  # Prefers Solo
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Baking": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),  # Prefers Solo
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],

    "Beachcombing": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),  # Prefers Solo
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],

    "Flower Arranging": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],

    "Metalworking": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),  # Prefers Solo
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Creative Writing": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),  # Prefers Solo
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],

    "Herb Gardening": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),  # Prefers Solo
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],

    "Digital Art": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),  # Prefers Solo
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
    "Leatherworking": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Astral Projection": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Fermenting": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Foraging": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Birdhouse Building": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "LARPing (Live Action Role Playing)": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Soap Making": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Cosplay": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Beekeeping": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Puzzle Making": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Stained Glass Art": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    "Creative Writing Workshops": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
    "Sculpture": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Cartooning": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Music Production": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Art Classes": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Cake Decorating": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Floral Design": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Fitness Classes": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Martial Arts": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Theater": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Self-Defense Classes": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Photography": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
            ])
        ],
        "Pottery": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
        "Cultural Cooking": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
        "Gardening Workshops": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
        "Fishing Workshops": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
        "Nature Walks": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
        "Language Learning": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
        "Fitness Blogging": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
        "Stand-up Comedy": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max(physical_activity_levels[min(physical_activity // 50, len(physical_activity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
                # Time Dedication
            ])
        ],
    }

    recommendations = {hobby: np.max(rule) for hobby, rule in rules.items()}

    # Sort hobbies by their membership degree
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

    # Randomize the recommendations to avoid the same output
    random.shuffle(sorted_recommendations)

    # Get the top two recommendations
    top_recommendations = sorted_recommendations[:2]

    return top_recommendations

def get_learning_paths(selected_hobby):
    if selected_hobby in learning_paths:
        return learning_paths[selected_hobby]
    else:
        return None
