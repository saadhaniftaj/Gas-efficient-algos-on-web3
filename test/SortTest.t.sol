// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "forge-std/Test.sol";
import "forge-std/console.sol";
import "../src/InsertionSort.sol";
import "../src/MergeSort.sol";
import "../src/CountingSort.sol";
import "../src/BubbleSort.sol";
import "../src/SelectionSort.sol";

contract SortTest is Test {
    InsertionSort insertion;
    MergeSort merge;
    CountingSort counting;
    BubbleSort bubble;
    SelectionSort selection;

    function setUp() public {
        insertion = new InsertionSort();
        merge = new MergeSort();
        counting = new CountingSort();
        bubble = new BubbleSort();
        selection = new SelectionSort();
    }

    function getSampleArray(uint size, uint seed) internal pure returns (uint[] memory) {
        uint[] memory arr = new uint[](size);
        for (uint i = 0; i < size; i++) {
            arr[i] = uint(keccak256(abi.encodePacked(seed, i))) % (size * 10 + 1);
        }
        return arr;
    }

    function logGas(string memory algo, uint size, uint gas) internal pure {
        console.log(string(abi.encodePacked("[GAS]", ",", algo, ",", vm.toString(size), ",", vm.toString(gas))));
    }

    function testAllSorts() public view {
        uint[] memory sizes = new uint[](5);
        sizes[0] = 5; sizes[1] = 10; sizes[2] = 20; sizes[3] = 50; sizes[4] = 100;

        for (uint s = 0; s < sizes.length; s++) {
            uint size = sizes[s];
            uint[] memory arr = getSampleArray(size, 42);

            uint gasStart;
            uint gasUsed;

            // Insertion Sort
            gasStart = gasleft();
            insertion.sort(arr);
            gasUsed = gasStart - gasleft();
            logGas("Insertion", size, gasUsed);

            // Merge Sort
            gasStart = gasleft();
            merge.sort(arr);
            gasUsed = gasStart - gasleft();
            logGas("Merge", size, gasUsed);

            // Counting Sort
            gasStart = gasleft();
            counting.sort(arr, size * 10);
            gasUsed = gasStart - gasleft();
            logGas("Counting", size, gasUsed);

            // Bubble Sort
            gasStart = gasleft();
            bubble.sort(arr);
            gasUsed = gasStart - gasleft();
            logGas("Bubble", size, gasUsed);

            // Selection Sort
            gasStart = gasleft();
            selection.sort(arr);
            gasUsed = gasStart - gasleft();
            logGas("Selection", size, gasUsed);
        }
    }
}