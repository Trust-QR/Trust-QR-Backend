// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

contract Authentication {
    // bytes32 private userName;
    // bytes32 private password;
    mapping(string => string) private credential;
    mapping(string => bool) private isExists;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(owner == msg.sender);
        _;
    }

    function isUserExists(
        string memory _user_id
    ) public view onlyOwner returns (bool) {
        return isExists[_user_id];
    }

    function addUser(
        string memory _user_id,
        string memory _password
    ) public onlyOwner {
        credential[_user_id] = _password;
        isExists[_user_id] = true;
    }

    function validateUser(
        string memory _user_id
    ) public view onlyOwner returns (string memory) {
        return credential[_user_id];
    }
}
