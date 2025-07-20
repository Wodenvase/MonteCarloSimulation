import numpy as np

def monte_carlo_simulation(initial_investment: float, expected_return: float, volatility: float, years: int, iterations: int):
    days = years * 252  # Trading days in a year
    daily_return = expected_return / 252
    daily_volatility = volatility / np.sqrt(252)

    # Simulate random daily returns
    results = np.zeros(iterations)
    for i in range(iterations):
        daily_returns = np.random.normal(daily_return, daily_volatility, days)
        cumulative_return = np.cumprod(1 + daily_returns)[-1]
        results[i] = initial_investment * cumulative_return

    p10 = np.percentile(results, 10)
    p50 = np.percentile(results, 50)
    p90 = np.percentile(results, 90)
    return {"P10": round(float(p10), 2), "P50": round(float(p50), 2), "P90": round(float(p90), 2)} 