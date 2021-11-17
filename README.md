# VVS Finance Profit Simulator

Script to find the best harvest (and put back) interval for VVS Finance.

## Explanation

<img src="https://raw.githubusercontent.com/eric19960304/vvs-finance-profit-simulator/main/demo/8000_2300.png">

Which means if you invest 8K USD in [VVS Finance](https://vvs.finance/farms), and the current APR for VVS-USDC are 2300%, then it is best to harvest the earning every 439 minutes, and [swap](https://vvs.finance/swap) half of the harvested earning to USDC, [convert](https://vvs.finance/add) them to LP tokens, and stake them back to the pool in the [farm](https://vvs.finance/farms). In this way, you will earn around 4311.83 USD after 1 week!

## How to use

1. Modify the `Param` section in the script to match your situation.
2. Install dependencies and run the script by:
```
pip install -r requirements.txt
python VVS_Profit_Simulator.py
```