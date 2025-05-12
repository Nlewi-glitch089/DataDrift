## 📦 DataDrift

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

## ⚙️ Optimization for Clarity, Efficiency, and Usability

- **Input Awareness:** The program checks the API response to make sure the ZIP code is valid before trying to show location info. This prevents user confusion and avoids errors.

- **Reusable Structure:** The code is written in a way that could easily be turned into a user-defined function with parameters, making it easier to reuse and scale.

- **Error Prevention Strategy:** While a basic error check is in place, there are plans to add a try-except block in the future to handle internet issues or API problems without crashing the program.

- **Planned Enhancements:** Future updates may include input validation (e.g. checking if ZIP codes are exactly 5 digits) and clearer output formatting to improve the user experience.

---

## 🌐 ZIP Code Location Finder

```python
# Fetching place name from ZIP code
BASE_URL = "http://api.zippopotam.us/US/"
zip_code = input("Enter a ZIP code: ")
response = requests.get(BASE_URL + zip_code)
if response.status_code == 200:
    data = response.json()
    print("Location:", data["places"][0]["place name"])
else:
    print("Invalid ZIP code.")
