# Animal Categories with English to Hindi Translation, with separate Pet and Wild animal options

animal_categories = {
    "Mammals": {
        "hindi": "स्तनधारी",
        "pet": [
            ("Dog", "कुत्ता"), ("Cat", "बिल्ली"), ("Horse", "घोड़ा"), ("Cow", "गाय"),
            ("Goat", "बकरी"), ("Rabbit", "खरगोश"), ("Sheep", "भेड़"), ("Camel", "ऊंट"),
            ("Buffalo", "भैंस"), ("Rat", "चूहा")
        ],
        "wild": [
            ("Elephant", "हाथी"), ("Lion", "सिंह"), ("Tiger", "बाघ"), ("Bear", "भालू"),
            ("Fox", "लोमड़ी"), ("Wolf", "भेड़िया"), ("Bat", "चमगादड़"), ("Deer", "हिरण"),
            ("Monkey", "बंदर"), ("Leopard", "तेंदुआ")
        ]
    },
    "Birds": {
        "hindi": "पक्षी",
        "pet": [
            ("Parrot", "तोता"), ("Canary", "कैनरी"), ("Pigeon", "कबूतर"), ("Budgerigar", "बजरीगर"),
            ("Cockatiel", "कॉकटील"), ("Lovebird", "लवबर्ड"), ("Dove", "कबूतर"), ("Finch", "फिंच"),
            ("Chicken", "मुर्गी"), ("Duck", "बत्तख")
        ],
        "wild": [
            ("Eagle", "गरुड़"), ("Peacock", "मोर"), ("Sparrow", "गौरैया"), ("Crow", "कौआ"),
            ("Owl", "उल्लू"), ("Penguin", "पेंगुइन"), ("Flamingo", "फ्लेमिंगो"), ("Hawk", "बाज"),
            ("Seagull", "सीगल"), ("Kingfisher", "रामचिरैया")
        ]
    },
    "Reptiles": {
        "hindi": "सरीसृप",
        "pet": [
            ("Turtle", "कछुआ"), ("Gecko", "गेक्को"), ("Corn Snake", "कॉर्न स्नेक"),
            ("Leopard Gecko", "तेंदुआ गेको"), ("Ball Python", "बॉल पाइथन")
        ],
        "wild": [
            ("Cobra", "नाग"), ("Python", "अजगर"), ("Crocodile", "मगरमच्छ"), 
            ("Lizard", "छिपकली"), ("Chameleon", "गिरगिट"), ("Iguana", "इगुआना"), 
            ("Komodo Dragon", "कोमोडो ड्रैगन"), ("Anaconda", "एनाकोंडा"),
            ("Viper", "वाइपर"), ("Monitor Lizard", "गोही")
        ]
    },
    # Additional categories can be added here
}

def display_categories():
    print("Select a category of animals:")
    for i, (category, details) in enumerate(animal_categories.items(), 1):
        print(f"{i}. {category} ({details['hindi']})")
    print("0. Exit")

def display_pet_wild_options(category_index):
    category_keys = list(animal_categories.keys())
    category = category_keys[category_index]
    details = animal_categories[category]
    
    print(f"\nYou selected: {category} ({details['hindi']})")
    print("1. Pet Animals")
    print("2. Wild Animals")
    print("0. Back")
    print("9. Exit")

def display_examples(category_index, pet=True):
    category_keys = list(animal_categories.keys())
    category = category_keys[category_index]
    details = animal_categories[category]
    
    if pet:
        examples = details.get("pet", [])
        print(f"\nPet examples of {category} ({details['hindi']}):")
    else:
        examples = details.get("wild", [])
        print(f"\nWild examples of {category} ({details['hindi']}):")
        
    for example in examples:
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
                display_pet_wild_options(category_choice - 1)
                type_choice = input("\nEnter 1 for Pet Animals, 2 for Wild Animals, or 0 to go back: ").strip()
                
                if type_choice == "1":
                    while True:
                        display_examples(category_choice - 1, pet=True)
                        back_choice = input("\nEnter 0 to go back or 9 to exit: ").strip()
                        if back_choice == "0":
                            break
                        elif back_choice == "9":
                            print("Exiting program.")
                            exit()
                        else:
                            print("Invalid input. Try again.")
                
                elif type_choice == "2":
                    while True:
                        display_examples(category_choice - 1, pet=False)
                        back_choice = input("\nEnter 0 to go back or 9 to exit: ").strip()
                        if back_choice == "0":
                            break
                        elif back_choice == "9":
                            print("Exiting program.")
                            exit()
                        else:
                            print("Invalid input. Try again.")
                
                elif type_choice == "0":
                    break
                elif type_choice == "9":
                    print("Exiting program.")
                    exit()
                else:
                    print("Invalid input. Try again.")
        else:
            print("Invalid category. Try again.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
