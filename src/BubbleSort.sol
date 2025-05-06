// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BubbleSort {
    function sort(uint[] memory arr) public pure returns (uint[] memory) {
        uint n = arr.length;
        for (uint i = 0; i < n; i++) {
            for (uint j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j]);
                }
            }
        }
        return arr;
    }
}
