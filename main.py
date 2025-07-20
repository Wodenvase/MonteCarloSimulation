from fastapi import FastAPI
from pydantic import BaseModel
from simulator import monte_carlo_simulation

app = FastAPI(title="Monte Carlo Portfolio Value Simulator")

class SimulationRequest(BaseModel):
    initial_investment: float
    expected_return: float
    volatility: float
    years: int
    iterations: int

@app.post("/simulate")
def simulate(req: SimulationRequest):
    result = monte_carlo_simulation(
        initial_investment=req.initial_investment,
        expected_return=req.expected_return,
        volatility=req.volatility,
        years=req.years,
        iterations=req.iterations
    )
    return result 