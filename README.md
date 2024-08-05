# Price Comparator

[Price Comparator Demo](https://youtu.be/5spwqQI_0PQ)

## Setup Guide
Follow these steps to set up and run the tool locally on your machine.

1. ### Prerequisites
    Make sure you have Python 3.6 or higher installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

2. ### Clone the Repository
   Open your terminal and run:
   ```bash
   git clone https://github.com/Souvik-Cyclic/Price-Comparator.git
   ```

3. ### Navigate to the Project Directory
   Change into the project directory:
   ```bash
   cd Price-Comparator
   ```

4. ### Install Dependencies
   Install the required Python packages using `pip`. Run:
   ```bash
   pip install -r requirements.txt
   ```

5. ### Run the script
   ```bash
   python price_comparator.py
   ```

6. ### Use the Tool
   1. When prompted, enter the name of the product you want to search for.
   2. The script will fetch and display product information from Amazon and Flipkart.

7. ### Example Output
   ```yaml
   Enter the product name: Laptop
   Searching for product on Amazon and Flipkart...
   
   Amazon Product:
   Title: XYZ Laptop
   Price: ₹50,000
   Amazon Link: https://www.amazon.in/dp/B08XYZ
    
   Flipkart Product:
   Title: XYZ Laptop
   Price: ₹49,999
   Flipkart Link: https://www.flipkart.com/xyz-laptop/p/itmb07xyz
   ```

8. ### Troubleshooting
   - **If you encounter errors:** Make sure all dependencies are correctly installed and check for any typos in the product name.
   - **No results:** The tool may not find results if the product is not available or if the HTML structure of the websites has changed.
