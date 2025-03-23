pragma solidity ^0.8.28;

interface IEldorion {
    function attack(uint256 damage) external;
}

contract AttackEldorion {
    function multiAttack(address target) external {
        IEldorion eldorion = IEldorion(target);
        eldorion.attack(100);
        eldorion.attack(100);
        eldorion.attack(100);
    }
}
