// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CountingSort {
    function sort(uint[] memory arr, uint maxValue) public pure returns (uint[] memory) {
        uint[] memory count = new uint[](maxValue + 1);
        for (uint i = 0; i < arr.length; i++) count[arr[i]]++;
        uint k = 0;
        for (uint i = 0; i <= maxValue; i++) {
            for (uint j = 0; j < count[i]; j++) {
                arr[k++] = i;
            }
        }
        return arr;
    }
}
