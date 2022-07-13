pragma solidity 0.8.9;

function getPercOf(
    uint256 _amount,
    uint256 _numer,
    uint256 _denom
) internal pure returns (uint256) {
    return _amount.mul(_numer.mul(DIVISOR_PERC).div(_denom)).div(DIVISOR_PERC);
}