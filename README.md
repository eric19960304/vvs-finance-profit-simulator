# VVS Finance Profit Simulator

Script to find the best fixed reinvestment (harvest & put back) interval for VVS Finance.

## Explanation

<img src="https://raw.githubusercontent.com/eric19960304/vvs-finance-profit-simulator/main/demo/8000.png">

Which means if you invest 8K USD in [VVS Finance](https://vvs.finance/farms), and the current APR for VVS-USDC pool are 2000%, then the best <b>fixed</b> interval to harvest is every 531 minutes, and [swap](https://vvs.finance/swap) half of the harvested earning to USDC, [convert](https://vvs.finance/add) them to the VVS-USDC LP tokens, and stake them back to the pool in the [farm](https://vvs.finance/farms). In this way, you will earn around 3643.63 USD after 1 week!

As you can see at the examples section below, the higher the capital, the shorter the best fixed reinvestment interval. So to optimize the the profit for large capital, the reinvestment interval should be decreased over time. One way to do it may be update the param (cap & APR) of this script and find again the best fixed reinvestment interval.

## How to use

1. Modify the `Param` section in the script to match your situation.
2. Install dependencies and run the script by:
```
pip install -r requirements.txt
python VVS_Profit_Simulator.py
```

## Other examples

<img src="https://raw.githubusercontent.com/eric19960304/vvs-finance-profit-simulator/main/demo/1000.png">

<img src="https://raw.githubusercontent.com/eric19960304/vvs-finance-profit-simulator/main/demo/3000.png">

<img src="https://raw.githubusercontent.com/eric19960304/vvs-finance-profit-simulator/main/demo/16000.png">

<img src="https://raw.githubusercontent.com/eric19960304/vvs-finance-profit-simulator/main/demo/100000.png">