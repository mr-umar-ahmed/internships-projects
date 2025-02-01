import numpy as np
import matplotlib.pyplot as plt
import random

# Customer Behavior Class to simulate personalized pricing based on user interactions
class CustomerBehavior:
    def __init__(self, base_price):
        self.base_price = base_price
        self.browsing_history = []  # Track viewed products
        self.purchase_likelihood = 0.0  # Probability of purchase based on behavior

    def view_product(self, product_id):
        """Simulate a customer viewing a product."""
        # Simulate customer behavior with a small chance of viewing a product
        if random.random() < 0.3:  # 30% chance of viewing
            self.browsing_history.append(product_id)
            self.update_purchase_likelihood()

    def update_purchase_likelihood(self):
        """Update the likelihood of purchasing based on browsing history."""
        # Simple rule: more views = higher purchase likelihood
        self.purchase_likelihood = min(1.0, len(self.browsing_history) * 0.1)  # Capped at 1.0

    def personalized_price(self):
        """Adjust price based on purchase likelihood."""
        # If likelihood is high, offer a small discount, else increase price slightly
        if self.purchase_likelihood > 0.5:
            return self.base_price * 0.9  # 10% discount
        else:
            return self.base_price * 1.1  # 10% markup


# Q-learning Pricing Agent that integrates Customer Behavior
class QLearningPricingAgentWithCustomerBehavior:
    def __init__(self, base_price, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, max_iterations=100):
        self.base_price = base_price  # Starting price
        self.learning_rate = learning_rate  # How quickly the agent learns
        self.discount_factor = discount_factor  # How much future rewards are considered
        self.exploration_rate = exploration_rate  # Exploration vs exploitation balance
        self.max_iterations = max_iterations  # Number of iterations to run the simulation
        self.q_table = {}  # Store Q-values for state-action pairs
        self.price_history = []  # To track the price history
        self.sales_history = []  # To track the sales history
        self.customer_behavior = CustomerBehavior(base_price)  # Initialize customer behavior class

    def get_q_value(self, state, action):
        """Get the Q-value for a state-action pair (returns 0 if not seen before)."""
        return self.q_table.get((state, action), 0.0)

    def update_q_value(self, state, action, reward, next_state, next_action):
        """Update the Q-value for a state-action pair."""
        # Q-learning formula: Q(s, a) = (1 - alpha) * Q(s, a) + alpha * (reward + discount_factor * max(Q(s', a')))
        old_q_value = self.get_q_value(state, action)
        max_future_q = max([self.get_q_value(next_state, a) for a in [-1, 0, 1]])  # Possible actions: decrease, keep, increase price
        new_q_value = old_q_value + self.learning_rate * (reward + self.discount_factor * max_future_q - old_q_value)
        self.q_table[(state, action)] = new_q_value

    def choose_action(self, state):
        """Choose an action based on exploration vs exploitation."""
        if np.random.rand() < self.exploration_rate:
            # Exploration: Randomly choose an action (price adjustment)
            action = np.random.choice([-1, 0, 1])  # Decrease, keep, or increase price
        else:
            # Exploitation: Choose the action with the highest Q-value
            action_values = [self.get_q_value(state, a) for a in [-1, 0, 1]]
            action = [-1, 0, 1][np.argmax(action_values)]
        return action

    def simulate(self, demand_function, competitor_pricing_function):
        """Simulate real-time pricing adjustments with Q-learning, customer behavior, and market trends."""
        state = self.base_price
        for iteration in range(self.max_iterations):
            # Simulate customer interactions (e.g., product views)
            product_id = random.randint(0, 10)  # Simulate a product the customer views
            self.customer_behavior.view_product(product_id)

            # Get personalized price and customer behavior impact
            personalized_price = self.customer_behavior.personalized_price()

            # Get demand and competitor pricing with seasonal adjustments
            demand = demand_function(iteration)
            seasonality_factor_value = seasonality_factor(iteration)  # Get seasonality factor
            competitor_price = competitor_pricing_function(iteration, seasonality_factor_value)

            # Apply customer segment behavior
            customer_behavior_modifier = customer_segment_behavior(iteration)
            personalized_price *= customer_behavior_modifier

            # Choose action based on exploration vs exploitation
            action = self.choose_action(state)

            # Adjust price
            new_price = personalized_price + action  # Action = -1 (decrease), 0 (keep), 1 (increase)
            new_price = max(new_price, 0)  # Prevent negative prices

            # Calculate reward (revenue - cost)
            revenue = max(demand * new_price, 0)
            reward = revenue - 50  # Subtract fixed cost (for simplicity)

            # Choose the next action (for future reward calculation)
            next_action = self.choose_action(new_price)

            # Update the Q-value for the state-action pair
            self.update_q_value(state, action, reward, new_price, next_action)

            # Record price and sales history
            self.price_history.append(new_price)
            self.sales_history.append(demand)

            # Update state for next iteration
            state = new_price

        return self.price_history, self.sales_history


# Define the demand function (simulating demand fluctuations)
def demand_function(iteration):
    """Simulate demand fluctuation over time."""
    return max(100 - 0.5 * iteration + np.random.uniform(-10, 10), 0)  # Random noise added

# Define the competitor pricing function (simulating competitor price changes)
def competitor_pricing_function(iteration, seasonality_factor=1.0):
    """Simulate competitor pricing dynamically, considering market conditions and seasonality."""
    base_competitor_price = 50  # Base competitor price
    price_fluctuation = np.random.uniform(-5, 5)  # Random price fluctuation
    competitor_price = base_competitor_price + price_fluctuation
    competitor_price *= seasonality_factor  # Apply seasonality factor
    return competitor_price

# Seasonality factor function to adjust prices based on time
def seasonality_factor(iteration):
    """Adjust prices based on seasonality (e.g., higher demand during holidays)."""
    if 30 <= iteration <= 60:  # Simulating a holiday season (for example)
        return 1.2  # 20% increase during holidays
    return 1.0  # No seasonal adjustment in other periods

# Customer segmentation behavior based on customer ID
def customer_segment_behavior(customer_id):
    """Simulate different customer segments and price sensitivity."""
    if customer_id % 2 == 0:
        return 0.8  # Price sensitive customer (lower likelihood to purchase at higher prices)
    else:
        return 1.2  # Less price sensitive customer (higher likelihood to purchase at higher prices)

# Main function to run the simulation
if __name__ == "__main__":
    # Initialize the Q-learning pricing agent with customer behavior
    agent = QLearningPricingAgentWithCustomerBehavior(base_price=100)

    # Simulate the learning process
    price_history, sales_history = agent.simulate(demand_function, competitor_pricing_function)

    # Plot the price history
    plt.plot(price_history)
    plt.xlabel("Iterations")
    plt.ylabel("Price")
    plt.title("Q-learning with Customer Behavior: Real-Time Pricing Adjustments")
    plt.show()

    # Optionally, print the sales history
    print("Sales History:", sales_history)
