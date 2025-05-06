import re
import pandas as pd

lines = []
with open("foundry_output.txt") as f:
    for line in f:
        if line.startswith("[GAS]"):
            # Format: [GAS],Algorithm,Size,Gas
            _, algo, size, gas = line.strip().split(",")
            lines.append({"Algorithm": algo, "Size": int(size), "Gas": int(gas)})

df = pd.DataFrame(lines)
df.to_csv("web3_gas.csv", index=False)
print(df)