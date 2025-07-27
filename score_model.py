def calculate_score(features):
    """
    Score wallet from 0 to 1000 based on risk factors
    Higher borrow/collateral ratio or liquidations = higher risk = lower score
    """
    borrow_ratio = features["borrow_ratio"]
    repay_ratio = features["repay_ratio"]
    liquidation_count = features["liquidation_count"]
    tx_count = features["tx_count"]

    # Score components
    score = 1000

    # Borrow risk
    if borrow_ratio > 1.5:
        score -= 300
    elif borrow_ratio > 1.0:
        score -= 200
    elif borrow_ratio > 0.5:
        score -= 100

    # Repayment bonus
    if repay_ratio > 1.0:
        score += 50
    elif repay_ratio < 0.5:
        score -= 100

    # Liquidation penalty
    score -= 100 * liquidation_count

    # Low activity risk
    if tx_count < 20:
        score -= 50

    # Clamp to 0–1000
    score = min(max(int(score), 0), 1000)

    return score
    