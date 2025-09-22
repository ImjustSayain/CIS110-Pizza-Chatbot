# AI Pizza Order Chatbot 🍕

A simple and interactive command-line chatbot built with Python that simulates taking a pizza order. This was a school project demonstrating basic Python input/output, conditionals, loops, and simple calculations.

## Features

*   **Interactive Conversation:** Guides the user through placing a pizza order with a series of questions.
*   **Input Validation:** Ensures the user provides valid answers for name, pizza size, crust type, and delivery method.
*   **Automatic Pricing:** Calculates the total cost based on pizza size, quantity, and delivery fee, including sales tax.
*   **Dynamic Coupons:** Awards a coupon if the order total is over $50.
*   **Fun Countdown Timer:** Provides a simulated ETA countdown until the pizza is ready.

## How to Run

1.  **Prerequisites:** Ensure you have Python 3 installed on your system.
2.  **Download the Code:** Copy the code from `pizza_chatbot.py` and save it to a file on your computer.
3.  **Run the Script:** Navigate to the script's directory in your command line or terminal and run:
    ```bash
    python pizza_chatbot.py
    ```
4.  **Follow the Prompts:** The chatbot, "Alex," will ask you a series of questions to build your order. Type your responses and press Enter.

## Code Structure

*   **User Input:** Uses `input()` to get information like name, pizza size, flavor, and crust type.
*   **Validation:** Uses `while` loops to validate that input is not blank and matches expected values.
*   **Conditional Logic:** Uses `if`/`elif`/`else` statements to handle pricing, delivery fees, and coupons.
*   **Cost Calculation:** Calculates the total cost with tax and delivery fee.
*   **Timer:** Implements a nested loop with `time.sleep()` to create a visual countdown.

## Example Output
