# 🪙 Wallet Risk Scoring System

This is a simple Python-based risk scoring tool for DeFi wallets. The tool processes wallet transaction data and calculates a **risk score (0–1000)** for each wallet, helping to identify wallets with potentially high financial risk.

## 📌 Project Overview

We evaluate wallets using mock transaction data and compute scores based on:

* Borrow-to-collateral ratio
* Repayment ratio
* Liquidation history
* Transaction activity

## 🧠 Methodology Explained

### ✅ Data Collection Method

* This project uses **mock data** for simulation purposes.
* The function `fetch_wallet_data(wallet_address)` randomly generates values for:

  * Total borrows
  * Total repayments
  * Collateral supplied
  * Liquidation count
  * Transaction count

> In a real-world scenario, you'd integrate with APIs like Etherscan, Covalent, or Compound’s subgraph.

### ✅ Feature Selection Rationale

We selected the following features based on their impact on financial risk:

* **Borrow Ratio**: `total_borrows / collateral_supplied`
  Indicates overleveraging. Higher value = more risk.

* **Repay Ratio**: `total_repay / total_borrows`
  Higher value = responsible wallet.

* **Liquidation Count**: Shows how often the wallet got liquidated. More = higher risk.

* **Transaction Count**: Wallet activity. Very low activity may indicate dormant or bot wallets.

### ✅ Scoring Method

A base score of **1000** is adjusted based on these risk indicators:

| Risk Factor              | Logic                                 | Score Impact  |
| ------------------------ | ------------------------------------- | ------------- |
| Borrow Ratio             | >1.5 = -300, >1.0 = -200, >0.5 = -100 | 🔻 Negative   |
| Repay Ratio              | >1.0 = +50, <0.5 = -100               | 🔺/🔻 Mixed   |
| Liquidation Penalty      | -100 for each liquidation             | 🔻 Negative   |
| Low Transaction Activity | tx\_count < 20 = -50                  | 🔻 Negative   |
| Final Score Clamp        | Score is always between 0 and 1000    | 🔒 Safe limit |

---

## 🛠 Folder Structure

```
.
├── data/
│   └── Wallet.csv              # Input CSV of wallet addresses
├── output/
│   └── wallet_scores.csv       # Output scores will be saved here
├── main.py                     # Main script to run everything
├── fetch_transactions.py       # Simulated transaction data
├── feature_engineering.py      # Feature extraction logic
├── score_model.py              # Score calculation logic
```

---

## ⚙️ How to Run

### Step 1: Install Python dependencies

We didn't use a virtual environment. You can install dependencies directly:

```bash
pip install pandas
```

---

### Step 2: Place your input file

* Make sure your wallet list CSV file is at:
  `data/Wallet.csv`
* CSV should have a column named: `wallet_id`

Example:

```
wallet_id
0xabc123...
0xdef456...
```

---

### Step 3: Run the code

Run the main script:

```bash
python main.py
```

Output will be saved in:

```
output/wallet_scores.csv
```

## ✅ Requirements

* Python 3.x
* pandas

Install with:

```bash
pip install pandas
```

---

## 👀 Output

Final output CSV will look like:

| wallet\_id  | score |
| ----------- | ----- |
| 0xabc123... | 675   |
| 0xdef456... | 480   |
