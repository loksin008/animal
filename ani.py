# Animal Categories with English to Hindi Translation, including Pet, Wild, and Famous Animals by Country

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
    "Famous Animals by Country": {
        "countries": {
            "India": [("Bengal Tiger", "बंगाल टाइगर"), ("Indian Elephant", "भारतीय हाथी"), ("Peacock", "मोर")],
            "Australia": [("Kangaroo", "कंगारू"), ("Koala", "कोआला"), ("Emu", "एमू")],
            "China": [("Giant Panda", "विशाल पांडा"), ("Golden Monkey", "स्वर्ण बंदर")],
            "USA": [("Bald Eagle", "बॉल्ड ईगल"), ("American Bison", "अमेरिकी बाइसन")],
            "South Africa": [("African Lion", "अफ्रीकी शेर"), ("African Elephant", "अफ्रीकी हाथी")],
            "Brazil": [("Jaguar", "जगुआर"), ("Macaw", "मकाव")],
            "Canada": [("Beaver", "बीवर"), ("Moose", "मूस")],
            "Russia": [("Siberian Tiger", "साइबेरियन टाइगर"), ("Brown Bear", "भूरा भालू")],
            "Japan": [("Japanese Macaque", "जापानी मकाक"), ("Red-Crowned Crane", "लाल ताज वाला सारस")],
            "Egypt": [("Nile Crocodile", "नील मगरमच्छ"), ("Sacred Ibis", "पवित्र आईबिस")]
        }
    }
}

def display_categories():
    print("Select a category of animals:")
    for i, (category, details) in enumerate(animal_categories.items(), 1):
        print(f"{i}. {category} ({details.get('hindi', '')})")
    print("0. Exit")

def display_pet_wild_options(category_index):
    category_keys = list(animal_categories.keys())
    category = category_keys[category_index]
    print(f"\nYou selected: {category} ({animal_categories[category].get('hindi', '')})")
    print("1. Pet Animals")
    print("2. Wild Animals")
    print("0. Back")
    print("9. Exit")

def display_examples(category_index, pet=True):
    category_keys = list(animal_categories.keys())
    category = category_keys[category_index]
    details = animal_categories[category]
    
    examples = details["pet"] if pet else details["wild"]
    label = "Pet" if pet else "Wild"
    print(f"\n{label} examples of {category} ({details.get('hindi', '')}):")
    for example in examples:
        print(f" - {example[0]} ({example[1]})")
    print("\n0. Back")
    print("9. Exit")

def display_famous_animals_by_country():
    print("\nFamous Animals by Country:")
    for i, country in enumerate(animal_categories["Famous Animals by Country"]["countries"].keys(), 1):
        print(f"{i}. {country}")
    print("0. Back")
    print("9. Exit")

def display_country_animals(country_index):
    country_keys = list(animal_categories["Famous Animals by Country"]["countries"].keys())
    country = country_keys[country_index]
    animals = animal_categories["Famous Animals by Country"]["countries"][country]
    
    print(f"\nFamous animals from {country}:")
    for animal in animals:
        print(f" - {animal[0]} ({animal[1]})")
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
        
        elif category_choice == 3:  # Famous Animals by Country
            while True:
                display_famous_animals_by_country()
                country_choice = input("\nEnter the number for the country or 0 to go back: ").strip()
                
                if country_choice == "0":
                    break
                elif country_choice == "9":
                    print("Exiting program.")
                    exit()
                elif country_choice.isdigit() and 1 <= int(country_choice) <= len(animal_categories["Famous Animals by Country"]["countries"]):
                    country_index = int(country_choice) - 1
                    while True:
                        display_country_animals(country_index)
                        back_choice = input("\nEnter 0 to go back or 9 to exit: ").strip()
                        if back_choice == "0":
                            break
                        elif back_choice == "9":
                            print("Exiting program.")
                            exit()
                        else:
                            print("Invalid input. Try again.")
                else:
                    print("Invalid input. Try again.")
        
        elif 1 <= category_choice <= 2:
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
