# Animal Categories with English to Hindi Translation, with navigation options for each page

animal_categories = {
    "Mammals": {
        "hindi": "स्तनधारी",
        "dissolved": [
            ("Whale", "व्हेल"), ("Dolphin", "डॉल्फिन"), ("Seal", "सील"), ("Manatee", "मेनाटी"),
            ("Otter", "ओटर"), ("Sea Lion", "समुद्री सिंह"), ("Narwhal", "नारव्हाल"),
            ("Beluga", "बेलुगा"), ("Walrus", "वालरस"), ("Sea Cow", "समुद्री गाय")
        ],
        "undissolved": [
            ("Elephant", "हाथी"), ("Lion", "सिंह"), ("Tiger", "बाघ"), ("Bear", "भालू"),
            ("Dog", "कुत्ता"), ("Cat", "बिल्ली"), ("Horse", "घोड़ा"), ("Cow", "गाय"),
            ("Goat", "बकरी"), ("Pig", "सूअर")
        ]
    },
    "Birds": {
        "hindi": "पक्षी",
        "dissolved": [
            ("Seagull", "सीगल"), ("Pelican", "पेलिकन"), ("Albatross", "अल्बाट्रॉस"),
            ("Cormorant", "कॉरमोरेंट"), ("Heron", "बगुला"), ("Kingfisher", "रामचिरैया"),
            ("Duck", "बत्तख"), ("Swan", "हंस"), ("Crane", "सारस"), ("Flamingo", "फ्लेमिंगो")
        ],
        "undissolved": [
            ("Eagle", "गरुड़"), ("Parrot", "तोता"), ("Peacock", "मोर"), ("Sparrow", "गौरैया"),
            ("Crow", "कौआ"), ("Pigeon", "कबूतर"), ("Owl", "उल्लू"), ("Robin", "रॉबिन"),
            ("Canary", "कैनरी"), ("Turkey", "टर्की")
        ]
    },
    # Additional categories can be added here
}

def display_categories():
    print("Select a category of animals:")
    for i, (category, details) in enumerate(animal_categories.items(), 1):
        print(f"{i}. {category} ({details['hindi']})")
    print("0. Exit")

def display_dissolved_undissolved_options(category_index):
    category_keys = list(animal_categories.keys())
    if 0 <= category_index < len(category_keys):
        category = category_keys[category_index]
        details = animal_categories[category]
        print(f"\nYou selected: {category} ({details['hindi']})")
        print("1. Dissolved")
        print("2. Undissolved")
        print("0. Back")
    else:
        print("Invalid category selected.")

def display_examples(category_index, dissolved=True):
    category_keys = list(animal_categories.keys())
    category = category_keys[category_index]
    details = animal_categories[category]
    
    if dissolved:
        examples = details.get("dissolved", [])
        print(f"\nDissolved examples of {category} ({details['hindi']}):")
    else:
        examples = details.get("undissolved", [])
        print(f"\nUndissolved examples of {category} ({details['hindi']}):")
        
    for example in examples:
        print(f" - {example[0]} ({example[1]})")
    print("\n0. Back")

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
                display_dissolved_undissolved_options(category_choice - 1)
                type_choice = input("\nEnter 1 for Dissolved, 2 for Undissolved, or 0 to go back: ").strip()
                
                if type_choice == "1":
                    while True:
                        display_examples(category_choice - 1, dissolved=True)
                        back_choice = input("\nEnter 0 to go back: ").strip()
                        if back_choice == "0":
                            break
                        else:
                            print("Invalid input. Try again.")
                
                elif type_choice == "2":
                    while True:
                        display_examples(category_choice - 1, dissolved=False)
                        back_choice = input("\nEnter 0 to go back: ").strip()
                        if back_choice == "0":
                            break
                        else:
                            print("Invalid input. Try again.")
                
                elif type_choice == "0":
                    break
                else:
                    print("Invalid input. Try again.")
        else:
            print("Invalid category. Try again.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
