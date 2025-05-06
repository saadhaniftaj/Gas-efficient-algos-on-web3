// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MergeSort {
    function sort(uint[] memory arr) public pure returns (uint[] memory) {
        if (arr.length <= 1) return arr;
        uint mid = arr.length / 2;
        uint[] memory left = new uint[](mid);
        uint[] memory right = new uint[](arr.length - mid);
        for (uint i = 0; i < mid; i++) left[i] = arr[i];
        for (uint i = mid; i < arr.length; i++) right[i - mid] = arr[i];
        left = sort(left);
        right = sort(right);
        return merge(left, right);
    }

    function merge(uint[] memory left, uint[] memory right) internal pure returns (uint[] memory) {
        uint[] memory result = new uint[](left.length + right.length);
        uint i = 0; uint j = 0; uint k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) result[k++] = left[i++];
            else result[k++] = right[j++];
        }
        while (i < left.length) result[k++] = left[i++];
        while (j < right.length) result[k++] = right[j++];
        return result;
    }
}
