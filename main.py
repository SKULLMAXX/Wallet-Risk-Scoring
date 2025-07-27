import pandas as pd
from fetch_transactions import fetch_wallet_data
from feature_engineering import extract_features
from score_model import calculate_score

# Load wallets
wallets_df = pd.read_csv("data/Wallet.csv")
wallets_df.columns = ['wallet_id']

# Final results list
results = []

for wallet in wallets_df['wallet_id']:
    print(f"Processing wallet: {wallet}")

    tx_data = fetch_wallet_data(wallet)
    features = extract_features(tx_data)
    score = calculate_score(features)

    results.append({'wallet_id': wallet, 'score': score})

# Save to CSV
result_df = pd.DataFrame(results)
result_df.to_csv("output/wallet_scores.csv", index=False)
print("Scoring complete. Output saved to output/wallet_scores.csv")
