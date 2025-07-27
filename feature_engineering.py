def extract_features(tx_data):
    """
    Process raw transaction data into normalized feature dict
    """
    features = {
        "borrow_ratio": tx_data["total_borrows"] / (tx_data["collateral_supplied"] + 1e-5),
        "repay_ratio": tx_data["total_repay"] / (tx_data["total_borrows"] + 1e-5),
        "liquidation_count": tx_data["liquidation_count"],
        "tx_count": tx_data["tx_count"],
    }
    return features
