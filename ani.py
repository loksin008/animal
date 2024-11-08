# Animal Categories with English to Hindi Translation, including Dissolved and Undissolved examples

animal_categories = {
    "Mammals": {
        "hindi": "स्तनधारी",
        "dissolved": [
            ("Whale", "व्हेल"),
            ("Dolphin", "डॉल्फिन"),
            ("Seal", "सील"),
            ("Manatee", "मेनाटी"),
            ("Otter", "ओटर"),
            ("Sea Lion", "समुद्री सिंह"),
            ("Narwhal", "नारव्हाल"),
            ("Beluga", "बेलुगा"),
            ("Walrus", "वालरस"),
            ("Sea Cow", "समुद्री गाय")
        ],
        "undissolved": [
            ("Elephant", "हाथी"),
            ("Lion", "सिंह"),
            ("Tiger", "बाघ"),
            ("Bear", "भालू"),
            ("Dog", "कुत्ता"),
            ("Cat", "बिल्ली"),
            ("Horse", "घोड़ा"),
            ("Cow", "गाय"),
            ("Goat", "बकरी"),
            ("Pig", "सूअर")
        ]
    },
    "Birds": {
        "hindi": "पक्षी",
        "dissolved": [
            ("Seagull", "सीगल"),
            ("Pelican", "पेलिकन"),
            ("Albatross", "अल्बाट्रॉस"),
            ("Cormorant", "कॉरमोरेंट"),
            ("Heron", "बगुला"),
            ("Kingfisher", "रामचिरैया"),
            ("Duck", "बत्तख"),
            ("Swan", "हंस"),
            ("Crane", "सारस"),
            ("Flamingo", "फ्लेमिंगो")
        ],
        "undissolved": [
            ("Eagle", "गरुड़"),
            ("Parrot", "तोता"),
            ("Peacock", "मोर"),
            ("Sparrow", "गौरैया"),
            ("Crow", "कौआ"),
            ("Pigeon", "कबूतर"),
            ("Owl", "उल्लू"),
            ("Robin", "रॉबिन"),
            ("Canary", "कैनरी"),
            ("Turkey", "टर्की")
        ]
    },
    # Add more categories following the same structure
}

def display_categories():
    print("Select a category of animals:")
    for i, (category, details) in enumerate(animal_categories.items(), 1):
        print(f"{i}. {category} ({details['hindi']})")

def display_examples(category_index, dissolved=True):
    category_keys = list(animal_categories.keys())
    if 0 <= category_index < len(category_keys):
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
    else:
        print("Invalid category selected.")

# Main Program
while True:
    display_categories()
    try:
        choice = int(input("\nEnter the number of the category you want to see examples for (or 0 to exit): ")) - 1
        if choice == -1:
            print("Exiting program.")
            break
        dissolved_choice = input("Do you want dissolved (d) or undissolved (u) examples? ").strip().lower()
        display_examples(choice, dissolved=(dissolved_choice == 'd'))
    except ValueError:
        print("Invalid input. Please enter a number.")
