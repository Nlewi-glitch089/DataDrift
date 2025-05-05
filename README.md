# 📦 DataDrift

**Description:**  
DataDrift is a location-based delivery tracker that generates a secure password for users to access estimated package arrival times using real-time API data.

---

## 🎯 Purpose / Problem Statement  
DataDrift helps users figure out when their package will arrive by using a location-based API. It addresses the common frustration of not knowing the status or estimated arrival time of a delivery—especially for people who don’t want to keep checking emails or tracking links.

---

## 👥 Target Audience  
The target audience includes online shoppers—particularly students, young adults, and busy individuals—who frequently order packages and want a fast, simple way to track delivery timing.

---

## ✅ Solution + 🚧 Limitations  

**Solution:**  
- Generates a temporary password that allows users to securely access package information based on their location.  
- Uses an API to gather real-time data and makes tracking more accessible.

**Limitations:**  
- Doesn’t show exact package locations or offer real-time updates.  
- Users can’t input their specific tracking numbers—it gives general delivery info based on location, not specific carriers.

---

## 🛠️ Key Features / Components  

- 🔐 **Password Generator:** Provides a one-time password for user access.  
- 🌐 **Location-Based API:** Pulls delivery estimate data based on the user’s city or ZIP code.  
- 🧾 **User Input System:** Users can enter their location to receive results.  
- 📊 **Text Display:** Clean, readable output that shows estimated delivery information.

---

## 🔄 Trade-Offs  
When adding the API to the original project, I had to refactor the code to integrate external data, which changed how the ZIP code input worked.  
This meant handling errors for invalid ZIP codes and ensuring the new functionality didn't disrupt the existing package features.  
Additionally, I introduced temporary passwords and hints for session security, which added complexity but was necessary for protecting user data.  
Finally, I adjusted the item generation and delivery time logic to accommodate randomization, balancing user experience with smooth functionality.  
Overall, the trade-offs involved making these updates while keeping the project stable and user-friendly.

---

## 🧩 Technical Challenges + 🔮 Future Plans  

**Challenges:**  
- Figuring out how to use an API key correctly and keep it secure  
- Getting the API to return data in a readable way for users

**Future Plans:**  
- Allow users to enter tracking numbers for more specific results  
- Add real-time tracking maps  
- Make the interface more interactive and user-friendly

---

## 🗓️ Project Timeline  

- **Week 1:** Brainstorming ideas and defining the purpose of the project. Testing and refining output, fixing bugs.  
- **Week 2:** Writing the core code (password generation, API calls). Final touches and preparing the presentation.

---

## 🔧 Tools and Resources Used  

- **API:** A location-based delivery estimation API (e.g., Zippopotam.us)  
- **AI Support:** ChatGPT (for code help and explanations)  
- **Coding Platform:** TechSmart  
- **Notes + Handouts:** Class notes from Unit 5 lessons

---

## 💻 Project Code

<details>
<summary>Click to expand full code</summary>

```python
# DataDrift - A location-based delivery tracker

import requests
import random
import pprint  # For better formatting
import time

BASE_URL = "http://api.zippopotam.us/US/"

serial_numbers = ["N9TT-9G0A-B7FQ-RANC", "QK6A-JI6S-7ETR-0A6C", "SXFP-CHYK-ONI6-S89U", "XNSS-HSJW-3NGU-8XTJ"]
password_hints = [
    "Your password starts with 'Pa' and has special symbols.",
    "Your password includes 'Secure' and a special character.",
    "Think of 'My' and '321' at the end.",
    "It has 'Strong' in it and an '@' symbol."
]

items = [
    "Laptop", "Smartphone", "Headphones", "Book", "Smartwatch", "Camera", 
    "Tablet", "Fitness Tracker", "Smart Glasses", "Bluetooth Speaker", "Drone",
    "VR Headset", "Smart Thermostat", "Wireless Charger", "Backpack", "Sneakers",
    # ... shortened for brevity ...
    "Crossbow", "Arrow Set", "Bow and Arrow", "Fishing Rod", "Tackle Box", "Fishing Line", "Lure Kit"
]

temporary_passwords = ["TempPass" + str(i) + "!" for i in range(1, 51)]

while True:
    zip_code = input("Enter a ZIP code to get location details: ")
    response = requests.get(BASE_URL + zip_code)
    if response.status_code == 200:
        data = response.json()
        print("\nLocation Details:")
        pprint.pprint(data["places"][0]["place name"])
        break
    else:
        print("\nInvalid ZIP code. Please enter a valid ZIP code.")

temp_password = random.choice(temporary_passwords)
print("\nYour temporary password for this session is: " + temp_password)

print("\nTo access your package details, you can use the provided temporary password or create your own.")
user_password = input("Enter your password (or type 'new' to create one): ")

if user_password.lower() == "new":
    while True:
        user_password = input("\nCreate a new password: ")
        print("\nYour new password has been set. Please enter it again to continue.")
        confirm_password = input("\nEnter your new password: ")
        if user_password == confirm_password:
            temporary_passwords.append(user_password)
            print("\nPassword set successfully. Proceeding to verification...")
            break
        else:
            print("\nPasswords do not match. Try again.")

attempts = 0
while attempts < 2:
    if user_password in temporary_passwords:
        print("\nPassword verified. You have access.")
        break
    else:
        print("\nPassword not recognized. Here's a hint:")
        print(random.choice(password_hints))
        user_password = input("\nTry again: ")
        attempts += 1

if user_password not in temporary_passwords:
    print("\nToo many attempts have been made. Please try again after a 5-minute cooldown.")
    time.sleep(300)
    exit()

num_items = random.randint(1, 10)
package_items = random.sample(items, num_items)
delivery_days = random.randint(1, 7)
delivery_date = "in " + str(delivery_days) + " days"
serial_number = random.choice(serial_numbers)

print("\nSerial Number: " + serial_number)
print("\nYour package contains: " + ", ".join(package_items))
print("\nTotal items in package: " + str(num_items))
print("\nExpected delivery: " + delivery_date)
