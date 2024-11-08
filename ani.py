# Animal Categories with English to Hindi Translation and Examples

animal_categories = {
    "Mammals": {
        "hindi": "स्तनधारी",
        "examples": [
            ("Elephant", "हाथी"), ("Lion", "सिंह"), ("Tiger", "बाघ"), ("Bear", "भालू"),
            ("Dog", "कुत्ता"), ("Cat", "बिल्ली"), ("Horse", "घोड़ा"), ("Cow", "गाय"),
            ("Goat", "बकरी"), ("Pig", "सूअर"), ("Monkey", "बंदर"), ("Rabbit", "खरगोश"),
            ("Fox", "लोमड़ी"), ("Wolf", "भेड़िया"), ("Bat", "चमगादड़"), ("Sheep", "भेड़"),
            ("Camel", "ऊंट"), ("Buffalo", "भैंस"), ("Deer", "हिरण"), ("Rat", "चूहा")
        ]
    },
    "Birds": {
        "hindi": "पक्षी",
        "examples": [
            ("Eagle", "गरुड़"), ("Parrot", "तोता"), ("Peacock", "मोर"), ("Sparrow", "गौरैया"),
            ("Crow", "कौआ"), ("Pigeon", "कबूतर"), ("Duck", "बत्तख"), ("Swan", "हंस"),
            ("Owl", "उल्लू"), ("Woodpecker", "कठफोड़वा"), ("Kingfisher", "रामचिरैया"),
            ("Penguin", "पेंगुइन"), ("Flamingo", "फ्लेमिंगो"), ("Hawk", "बाज"),
            ("Turkey", "टर्की"), ("Quail", "बटेर"), ("Vulture", "गिद्ध"), ("Robin", "रॉबिन"),
            ("Canary", "कैनरी"), ("Seagull", "सीगल")
        ]
    },
    "Reptiles": {
        "hindi": "सरीसृप",
        "examples": [
            ("Cobra", "नाग"), ("Python", "अजगर"), ("Crocodile", "मगरमच्छ"),
            ("Lizard", "छिपकली"), ("Turtle", "कछुआ"), ("Chameleon", "गिरगिट"),
            ("Iguana", "इगुआना"), ("Komodo Dragon", "कोमोडो ड्रैगन"), ("Anaconda", "एनाकोंडा"),
            ("Alligator", "घड़ियाल"), ("Gecko", "गेक्को"), ("Viper", "वाइपर"),
            ("Rattlesnake", "रैटलस्नेक"), ("Boa Constrictor", "बोआ"), ("Monitor Lizard", "गोही"),
            ("Garter Snake", "गार्टर सांप"), ("Sea Snake", "समुद्री सांप"), ("Copperhead", "कॉपरहेड"),
            ("Horned Lizard", "सींग वाली छिपकली"), ("Sidewinder", "साइडवाइंडर")
        ]
    },
    # Additional categories can be added here
}

def display_categories():
    print("Select a category of animals:")
    for i, (category, details) in enumerate(animal_categories.items(), 1):
        print(f"{i}. {category} ({details['hindi']})")
    print("0. Exit")

def display_examples(category_index):
    category_keys = list(animal_categories.keys())
    category = category_keys[category_index]
    details = animal_categories[category]
    
    print(f"\nExamples of {category} ({details['hindi']}):")
    for example in details["examples"]:
        print(f" - {example[0]} ({example[1]})")
    print("\n0. Back")
    print("9. Exit")

# Main Program
while True:
    display_categories()
    try:
        category_choice = int(input("\nEnter the number of the category you want to see (or 0 to exit): "))
        if category_choice == 0:
            print("Exiting program.")
            break
        elif 1 <= category_choice <= len(animal_categories):
            while True:
                display_examples(category_choice - 1)
                back_choice = input("\nEnter 0 to go back or 9 to exit: ").strip()
                
                if back_choice == "0":
                    break
                elif back_choice == "9":
                    print("Exiting program.")
                    exit()
                else:
                    print("Invalid input. Try again.")
        else:
            print("Invalid category. Try again.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
