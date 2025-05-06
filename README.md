# Foundry

**Foundry is a blazing fast, portable and modular toolkit for Ethereum application development written in Rust.**

Foundry consists of:

- **Forge**: Ethereum testing framework (like Truffle, Hardhat and DappTools).
- **Cast**: Swiss army knife for interacting with EVM smart contracts, sending transactions and getting chain data.
- **Anvil**: Local Ethereum node, akin to Ganache, Hardhat Network.
- **Chisel**: Fast, utilitarian, and verbose Solidity REPL.

## Documentation

https://book.getfoundry.sh/

---

## Usage

### Build

```bash
forge build
```

### Test

```bash
forge test
```

### Format

```bash
forge fmt
```

### Gas Snapshots

```bash
forge snapshot
```

### Anvil (Local Ethereum Node)

```bash
anvil
```

### Deploy Script

```bash
forge script script/Counter.s.sol:CounterScript --rpc-url <your_rpc_url> --private-key <your_private_key>
```

### Cast Utility

```bash
cast <subcommand>
```

### Help Commands

```bash
forge --help
anvil --help
cast --help
```

## 📊 Gas Complexity Benchmarking: Analyzing Algorithm Efficiency in Web3

This report summarizes a benchmarking project using **Foundry** to evaluate the gas efficiency of classical sorting algorithms implemented in **Solidity**. Conducted by Saad (2022509) and Ahmed Ali Khan (2022054) at GIKI as part of the *Design and Analysis of Algorithms* course (CS378).

### 🔍 Research Focus

We evaluated 5 sorting algorithms:
- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Counting Sort

**Objective:** Understand how these algorithms perform in terms of gas consumption on the Ethereum Virtual Machine (EVM), and how theoretical time complexity maps (or doesn't) to on-chain performance.

### ⚙️ Experimental Setup
- Blockchain Environment: Ethereum Mainnet Fork via Hardhat
- Tools Used: Foundry v0.2.0, Solidity 0.8.17
- Gas Measurement: Using gasleft() before and after execution
- Input Types: Arrays of unsigned integers (random, sorted, reversed)
- Input Sizes: 5 to 100 elements
- Validation: Deterministic inputs & multiple test runs

### 🧠 Key Insights
- **Counting Sort** had the lowest gas cost for larger datasets despite higher space complexity.
- Theoretical O(n log n) algorithms like **Merge Sort** incurred extra gas due to recursion.
- Algorithms like **Selection Sort** and **Insertion Sort** performed more consistently on-chain due to predictable memory/storage behavior.

### 📉 Sample Implementation (Selection Sort)

```solidity
function selectionSort(uint[] memory arr) internal pure returns (uint[] memory) {
    uint n = arr.length;
    for (uint i = 0; i < n - 1; i++) {
        uint minIndex = i;
        for (uint j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            uint temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
    return arr;
}
```

### 📚 Summary Table

| **Algorithm** | **Theoretical Complexity** | **EVM Gas Characteristics** |
|---------------|----------------------------|----------------------------|
| Bubble Sort | O(n²) | High storage writes |
| Counting Sort | O(n + k) | Memory-intensive, avoids in-place ops |
| Merge Sort | O(n log n) | Recursion gas overhead |
| Selection Sort | O(n²) | Minimal memory, consistent performance |
| Insertion Sort | O(n²) | Early termination helps reduce cost |

### 📌 Conclusion

This work illustrates the gap between traditional algorithm analysis and blockchain environments. Web3 developers should benchmark in the **EVM context** instead of relying solely on Big-O notation when optimizing for **gas cost**.
