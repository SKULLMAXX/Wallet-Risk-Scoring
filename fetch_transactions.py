import random

def fetch_wallet_data(wallet_address):
    """
    MOCK function for fetching Compound protocol data.
    In real case, integrate with Etherscan/Covalent/DeFiLlama/Compound subgraph.
    """
    return {
        "total_borrows": random.uniform(0, 10),
        "total_repay": random.uniform(0, 10),
        "collateral_supplied": random.uniform(0, 15),
        "liquidation_count": random.randint(0, 3),
        "tx_count": random.randint(10, 100),
    }
