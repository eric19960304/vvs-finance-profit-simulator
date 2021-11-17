# vvs-finance-profit-simulator

Script to find the best harvest (and put back) interval for VVS Finance.

## Example

With init cap 8000.00 USD and APR 2300.00%, best reinvest interval is every 7 hour 19 minutes (439) which yields 4311.83 USD profits.

<img src="https://raw.githubusercontent.com/eric19960304/vvs-finance-profit-simulator/main/demo/8000_2300.png">

## How to use

1. Modify the `Param` section in the script to match your situation.
2. Install dependencies and run the script by:
```
pip install -r requirements.txt
python VVS_Profit_Simulator.py
```