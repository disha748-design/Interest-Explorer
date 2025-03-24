# fuzzy_rules.py

import numpy as np
import skfuzzy as fuzz

# Define age, skill, interest, creativity, and physical activity levels
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
time_dedication_levels = [
    fuzz.trimf(np.arange(1, 9, 1), [1, 1, 4]),  # Low Time Dedication (1 to 4 hours)
    fuzz.trimf(np.arange(1, 9, 1), [3, 5, 7]),  # Medium Time Dedication (3 to 7 hours)
    fuzz.trimf(np.arange(1, 9, 1), [6, 8, 8])  # High Time Dedication (6 to 8 hours)
]

def get_fuzzy_rules(age, skill, interest, creativity, physical_activity, social_pref,time_dedication):
    return {
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
    "Photography": [
        np.min([
            np.max(age_levels[age // 20]),
            np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
            np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
            np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
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
        "Martial Arts": [
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
        "Martial Arts": [
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
        "Calligraphy": [
            np.min([
                np.max(age_levels[age // 20]),
                np.max(skill_levels[min(skill // 30, len(skill_levels) - 1)]),
                np.max(interest_levels[min(interest // 30, len(interest_levels) - 1)]),
                np.max(creativity_levels[min(creativity // 50, len(creativity_levels) - 1)]),
                np.max([1 if social_pref == 0 else 0]),  # Prefers Solo
                np.max(time_dedication_levels[min(time_dedication // 3, len(time_dedication_levels) - 1)])
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