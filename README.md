# Cross-Asset Macro Impact Tracker

## 📌 Project Overview
This repository contains a high-frequency financial data pipeline designed to analyze the **"Macro Transmission Mechanism."** Using Python and intraday 1-minute market data, the tool isolates specific macroeconomic releases (CPI, NFP, FOMC) and visualizes how a single data "shock" propagates across Equities, Fixed Income, and Foreign Exchange markets simultaneously.

The core of the project uses **Event Study Methodology**, indexing all assets to a base of 100 at $T_0$ (the moment of release) to quantify the immediate beta and divergence of diverse asset classes.

---

## 🚀 Key Features
- **Event Study Framework:** Automatically zooms into the $[-30, +120]$ minute window around a specific release timestamp.
- **Cross-Asset Universe:** Tracks **SPY** (Equities), **TLT** (20Y Treasury Bonds), **UUP** (US Dollar Index), and **GLD** (Gold) to capture a holistic market view.
- **T=0 Normalization:** Uses a relative indexing logic to allow direct comparison of percentage moves across different asset classes.
- **Interactive Visuals:** Built with `Plotly` for high-resolution, hover-active charts used for professional presentations.

---

## 📊 Market Intuition: Case Study (CPI Release)
When a "Hot" CPI (Inflation higher than expected) hits the wires, this tracker is designed to visualize the following regime shift:
1. **Rates (TLT) 📉:** Prices fall (yields rise) as markets price in a more hawkish central bank.
2. **USD (UUP) 📈:** The dollar strengthens due to higher yield differentials.
3. **Equities (SPY) 📉:** Stocks face pressure from higher discount rates and tighter financial conditions.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Source:** `yfinance` (Intraday API)
- **Data Processing:** `Pandas`, `NumPy`
- **Visualization:** `Plotly` (Dark Mode Template)

---

## 🔧 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/cross-asset-macro-tracker.git](https://github.com/YOUR_USERNAME/cross-asset-macro-tracker.git)
   cd cross-asset-macro-tracker
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the Analysis:**
   Open macro_tracker.py and update the event_time_str with any major macro timestamp from the last 30 days.
   ```bash
   python macro_tracker.py

📂 Repository Structure
1. macro_tracker.py: Core logic for data fetching, normalization, and plotting.
2. requirements.txt: List of required Python packages
3. .gitignore: Standard Python configuration to exclude local environments and caches.
4. LICENSE: MIT License.

Author: Amit Singh
Email: amitsinghjobs99@gmail.com
LinkedIn: https://www.linkedin.com/in/amit-singh99/

Disclaimer: This tool is for educational and research purposes only and does not constitute financial advice.
