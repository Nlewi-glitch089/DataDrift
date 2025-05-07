"""
Data Structures
Student Project
Project Title: DataDrift Nationwide

TradeOffs: When adding the API to the original project, I had to refactor the code to integrate external data, which changed how the ZIP code input worked. 
This meant handling errors for invalid ZIP codes and ensuring the new functionality didn't disrupt the existing package features. 
Additionally, I introduced temporary passwords and hints for session security, which added complexity but was necessary for protecting user data. 
Finally, I adjusted the item generation and delivery time logic to accommodate randomization, balancing user experience with smooth functionality. 
Overall, the trade-offs involved making these updates while keeping the project stable user-friendly and readable for me.
"""
import requests
import random
import pprint  # For better formatting
import time

# API setup - This sets up the base URL for the API request
BASE_URL = "http://api.zippopotam.us/US/"

# Account authentication setup - Lists of account details for verification
serial_numbers = ["N9TT-9G0A-B7FQ-RANC", "QK6A-JI6S-7ETR-0A6C", "SXFP-CHYK-ONI6-S89U", "XNSS-HSJW-3NGU-8XTJ"]
password_hints = [  # Hints to help users remember their passwords
    "Your password starts with 'Pa' and has special symbols.",
    "Your password includes 'Secure' and a special character.",
    "Think of 'My' and '321' at the end.",
    "It has 'Strong' in it and an '@' symbol."
]

items = [
    "Laptop", "Smartphone", "Headphones", "Book", "Smartwatch", "Camera", 
    "Tablet", "Fitness Tracker", "Smart Glasses", "Bluetooth Speaker", "Drone", 
    "VR Headset", "Smart Thermostat", "Wireless Charger", "Backpack", "Sneakers", 
    "Jacket", "T-shirt", "Sunglasses", "Coffee Maker", "Air Purifier", "Printer", 
    "Desk Lamp", "Bluetooth Keyboard", "Wireless Mouse", "Power Bank", "Smartphone Case", 
    "Bike", "Skateboard", "Hoverboard", "Electric Scooter", "Skate Shoes", "Guitar", 
    "Keyboard", "Drum Set", "Microphone", "Sound System", "TV", "Gaming Console", 
    "Video Game", "Puzzle", "Board Game", "Jigsaw Puzzle", "Chess Set", "Paint Set", 
    "Easel", "Canvas", "Drawing Pencils", "Art Supplies", "Yoga Mat", "Dumbbells", 
    "Kettlebell", "Resistance Bands", "Jump Rope", "Treadmill", "Boxing Gloves", 
    "Sports Ball", "Tent", "Sleeping Bag", "Camp Stove", "Flashlight", "Pocket Knife", 
    "Binoculars", "Hammock", "Travel Pillow", "Suitcase", "Luggage Tag", "Travel Backpack", 
    "Travel Adapter", "Passport Holder", "Electric Toothbrush", "Hair Dryer", "Curling Iron", 
    "Straightener", "Beard Grooming Kit", "Nail Clippers", "Skincare Kit", "Perfume", 
    "Body Lotion", "Lip Balm", "Soap", "Shampoo", "Conditioner", "Toothpaste", "Razor", 
    "Towel", "Hand Sanitizer", "First Aid Kit", "Ice Pack", "Band-Aids", "Thermometer", 
    "Scale", "Sunglasses Case", "Watch Box", "Jewelry Box", "Wallet", "Purse", "Belt", 
    "Hat", "Scarf", "Gloves", "Umbrella", "Snow Boots", "Beach Towel", "Sunglasses", 
    "Swimwear", "Pool Float", "Ice Cream Maker", "Waffle Maker", "Blender", "Toaster", 
    "Electric Grill", "Rice Cooker", "Juicer", "Electric Skillet", "Air Fryer", "Coffee Grinder", 
    "Espresso Machine", "Mixer", "Pasta Maker", "Cookie Cutter Set", "Knife Set", "Cutting Board", 
    "Glassware", "Mugs", "Plates", "Bowls", "Silverware", "Wine Glasses", "Champagne Flute", 
    "Beer Mugs", "Tupperware", "Picnic Basket", "Lunch Box", "Tea Pot", "Tea Set", "Coffee Mugs", 
    "Reusable Water Bottle", "Collapsible Cup", "Thermos", "Snack Box", "Grocery Basket", 
    "Food Processor", "Dehydrator", "Milk Frother", "Ice Maker", "Deep Fryer", "Meat Thermometer", 
    "Salt Grinder", "Pepper Grinder", "Olive Oil Dispenser", "Spice Rack", "Herb Garden Kit", 
    "Cookie Jar", "Cheese Grater", "Mandoline Slicer", "Garlic Press", "Apron", "Chef's Hat", 
    "Cutting Mat", "Can Opener", "Gravy Boat", "Soup Pot", "Pressure Cooker", "Slow Cooker", 
    "Butter Dish", "Cake Stand", "Cupcake Tin", "Muffin Tin", "Pie Dish", "Loaf Pan", 
    "Casserole Dish", "Baking Sheets", "Pizza Stone", "Cookie Sheets", "Silicone Baking Mats", 
    "Cooling Rack", "Sifter", "Pastry Brush", "Rolling Pin", "Flour Sifter", "Baking Spatula", 
    "Whisk", "Tongs", "Ice Cream Scoop", "Meat Tenderizer", "Canister Set", "Bread Box", 
    "Spice Grinder", "Zester", "Peeler", "Potato Masher", "Roasting Pan", "Griddle Pan", 
    "Grill Pan", "Panini Press", "Toasting Rack", "Bagel Cutter", "Pizza Cutter", "Sushi Mat", 
    "Baguette Pan", "Flour Sack Towels", "Lemon Squeezer", "Milk Jug", "Baking Powder", "Vinegar", 
    "Soy Sauce", "Pasta Strainer", "Cheese Cloth", "Roasting Fork", "Barbecue Brush", "Meat Grinder", 
    "Funnel", "Tea Infuser", "Tea Strainer", "Fruit Basket", "Picnic Blanket", "Tent Lantern", 
    "Hammock Stand", "Air Mattress", "Sleeping Pad", "Camp Chair", "Lantern", "Fire Pit", 
    "S'mores Kit", "Folding Knife", "Multi-tool", "Camp Shovel", "Portable Grill", "Hiking Boots", 
    "Trekking Poles", "Water Filter", "Hydration Pack", "Solar Charger", "Walkie Talkies", 
    "Portable Fan", "Bug Repellent", "Sunscreen", "First Aid Blanket", "Compass", "Tarp", 
    "Campfire Starter", "Thermal Blanket", "Emergency Rations", "Paracord", "Hand Warmers", 
    "Camp Stove Fuel", "Hiking Backpack", "Cliff Bar", "Rope", "Earmuffs", "Ice Axe", "Ice Climbing Crampon", 
    "Crossbow", "Arrow Set", "Bow and Arrow", "Fishing Rod", "Tackle Box", "Fishing Line", "Lure Kit"
] # Possible package contents (this will be randomly selected for the user's package)



# Generate a list of temporary passwords for security purposes
# These will be used to provide the user with a session password
temporary_passwords = ["TempPass" + str(i) + "!" for i in range(1, 51)]

# Main Program - Get ZIP code input from user and retrieve location details
while True:
    # Prompt the user for a ZIP code
    zip_code = input("Enter a ZIP code to get location details: ")
    # Make API request to get location information based on ZIP code
    response = requests.get(BASE_URL + zip_code)  # Make API request
    # Check if the response status is OK (200)
    if response.status_code == 200:
        data = response.json()  # Convert response to JSON format
        print("\nLocation Details:")
        pprint.pprint(data["places"][0]["place name"])  # Pretty-print location name
        break  # Exit the loop if the ZIP code is valid
    else:
        print("\nInvalid ZIP code. Please enter a valid ZIP code.")

# Provide the user with a randomly selected temporary password for session security
temp_password = random.choice(temporary_passwords)
print("\nYour temporary password for this session is: " + temp_password)

# Ask user if they want to use the temporary password or create their own
print("\nTo access your package details, you can use the provided temporary password or create your own.")
user_password = input("Enter your password (or type 'new' to create one): ")

# If the user chooses to create a new password
if user_password.lower() == "new":
    while True:
        # Ask the user to confirm the new password
        user_password = input("\nCreate a new password: ")
        print("\nYour new password has been set. Please enter it again to continue.")
        confirm_password = input("\nEnter your new password: ")
        # If the passwords match, add the new password to the list of valid passwords
        if user_password == confirm_password:
            temporary_passwords.append(user_password)  # Store new password
            print("\nPassword set successfully. Proceeding to verification...")
            break
        else:
            print("\nPasswords do not match. Try again.")

# Allow user two attempts to enter the correct password
attempts = 0
while attempts < 2:
    if user_password in temporary_passwords:
        print("\nPassword verified. You have access.")
        break
    else:
        # If the password is not recognized, provide a hint and ask for another attempt
        print("\nPassword not recognized. Here's a hint:")
        print(random.choice(password_hints))
        user_password = input("\nTry again: ")
        attempts += 1

# If the user fails twice, enforce a cooldown period before retrying
if user_password not in temporary_passwords:
    print("\nToo many attempts have been made. Please try again after a 5-minute cooldown.")
    time.sleep(300)  # 5-minute cooldown
    exit() # Exit the program if too many attempts have been made

# Generate package details
# num_items is randomly generated but limited to the length of the 'items' list
num_items = random.randint(1, 10)  # Randomly determine the number of items in the package

package_items = random.sample(items, num_items)  # Select random items from the list

delivery_days = random.randint(1, 7)  # Random delivery estimate (1-7 days)
delivery_date = "in " + str(delivery_days) + " days"  # Format estimated delivery date
serial_number = random.choice(serial_numbers)  # Assign a serial number to the package

# Display package information
print("\nSerial Number: " + serial_number)
print("\nYour package contains: " + ", ".join(package_items))
print("\nTotal items in package: " + str(num_items))  # Print the number of items in the package
print("\nExpected delivery: " + delivery_date + " days.")  # Print the expected delivery date
