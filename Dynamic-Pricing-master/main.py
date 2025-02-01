from real_time_pricing import QLearningPricingAgentWithCustomerBehavior, demand_function, competitor_pricing_function
import matplotlib.pyplot as plt

# Initialize the Q-learning pricing agent with customer behavior
agent = QLearningPricingAgentWithCustomerBehavior(base_price=100)

# Simulate the learning process
price_history, sales_history = agent.simulate(demand_function, competitor_pricing_function)

# Plot the price history
plt.figure(figsize=(10, 5))
plt.plot(price_history, label="Price", color="blue")
plt.xlabel("Iterations")
plt.ylabel("Price")
plt.title("Price History Over Time")
plt.legend()
plt.grid()
plt.show()

# Plot the sales history
plt.figure(figsize=(10, 5))
plt.plot(sales_history, label="Sales", color="green")
plt.xlabel("Iterations")
plt.ylabel("Sales")
plt.title("Sales History Over Time")
plt.legend()
plt.grid()
plt.show()

# Calculate and print final statistics
total_revenue = sum([price * sales for price, sales in zip(price_history, sales_history)])
average_price = sum(price_history) / len(price_history)
average_sales = sum(sales_history) / len(sales_history)

print(f"Total Revenue: {total_revenue:.2f}")
print(f"Average Price: {average_price:.2f}")
print(f"Average Sales: {average_sales:.2f}")

# Plot Revenue Trends
revenue_trend = [price * sales for price, sales in zip(price_history, sales_history)]
plt.figure(figsize=(10, 5))
plt.plot(revenue_trend, label="Revenue", color="orange")
plt.xlabel("Iterations")
plt.ylabel("Revenue")
plt.title("Revenue Trend Over Time")
plt.legend()
plt.grid()
plt.show()
