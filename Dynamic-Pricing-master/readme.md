# Dynamic Pricing Model for E-Commerce with Reinforcement Learning

## **Overview**
This project implements a dynamic pricing engine for e-commerce using **Reinforcement Learning (Q-learning)**. The model optimizes prices in real-time by considering:
- **Customer behavior**: Tracks browsing history and purchase likelihood to offer personalized pricing.
- **Competitor pricing**: Adjusts prices dynamically to remain competitive.
- **Market trends and seasonality**: Incorporates demand fluctuations and seasonal effects into pricing decisions.

The goal is to maximize profits while maintaining competitiveness in a dynamic market environment.

---

## **Features**
- **Real-Time Pricing**: Dynamically adjusts prices in response to changing demand, competitor actions, and seasonal trends.
- **Customer Behavior Tracking**:
  - Tracks user interactions like browsing history.
  - Adjusts prices based on purchase likelihood (personalized pricing).
- **Competitor Pricing Integration**:
  - Simulates competitor price changes and adapts pricing accordingly.
- **Seasonality Adjustments**:
  - Adjusts prices during high-demand periods (e.g., holidays).
- **Reinforcement Learning**:
  - Uses Q-learning to learn optimal pricing strategies over time.

---

## **Setup and Requirements**
### **Prerequisites**
- Python 3.x
- Install the required libraries:
   ```bash
   pip install numpy matplotlib
   ```

### **Files**
- **`real_time_pricing.py`**: Contains the logic for the pricing engine (Q-learning, customer behavior, demand simulation).
- **`main.py`**: Executes the pricing engine, generates graphs, and calculates revenue.

### **How to Run the Project**
1. Clone the repository or download the project files.
2. Ensure you have Python and the required libraries installed.
3. Run the `main.py` file:
   ```bash
   python main.py
   ```
4. View the outputs:
   - **Graphs**: Price trends, sales history, revenue trends.
   - **Console Outputs**: Total revenue, average price, and sales.

---

## **Outputs**
The project generates the following outputs:
1. **Price History Graph**: Shows how prices are adjusted over time.
2. **Sales History Graph**: Displays demand fluctuations based on price changes.
3. **Revenue Trend Graph**: Tracks how revenue evolves over time.

### **Sample Output**
- **Graph Example**:
  <img alt="Sample Graph" src="&quot;C:\Users\Umar Ahmed\OneDrive\Pictures\Screenshots\Screenshot 2024-12-12 115840.png&quot;"/>

- **Console Output Example**:
   ```
   Total Revenue: 15200.25
   Average Price: 105.35
   Average Sales: 95.50
   ```

---

## **Project Structure**
- `real_time_pricing.py`: Core logic for the pricing engine.
- `main.py`: Runs the engine and generates outputs.
- `README.md`: Project documentation.

---

## **Future Enhancements**
Potential improvements include:
1. **Multi-Product Pricing**:
   - Extend the model to handle multiple products with unique demand curves and competitor pricing.
2. **Advanced Reinforcement Learning**:
   - Implement more sophisticated RL algorithms like Deep Q Networks (DQN).
3. **Real-Time Data Integration**:
   - Use APIs to fetch live competitor pricing and market data.
4. **Improved Customer Behavior**:
   - Add realistic customer interactions, such as cart abandonment or price elasticity.

---

## **Acknowledgments**
This project was developed to explore the application of Reinforcement Learning in e-commerce pricing strategies.

