// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.8.21;

contract Products {
    struct Product {
        string product_id;
        string product_name;
        string product_description;
        string product_category;
        string country_of_origin;
        string date_of_expiry;
        string date_of_manufacturing;
        uint256 price;
        string [] image_url;
    }

    address public owner;

    // Email + Product_id  => T/F
    mapping(string => bool) _exists;

    // Email => [Product_id, Product_id]
    mapping(string => string[]) email_to_list_of_product_id;

    // Encoded Mail_id -> {Product_id -> Proudct STruct}
    mapping(string => mapping(string => Product)) private email_to_product_map;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOnwner() {
        require(msg.sender == owner);
        _;
    }

    modifier checkProduct() {
        require(msg.sender == owner);
        _;
    }

    function addProduct(
        string memory email,
        string memory product_id,
        string memory product_name,
        string memory product_description,
        string memory product_category,
        string memory country_of_origin,
        string memory date_of_expiry,
        string memory date_of_manufacturing,
        uint256 price,
        string [] memory image_url,
        string memory key

    ) public onlyOnwner 
    {
        
            email_to_product_map[email][product_id] = Product(
                product_id,
                product_name,
                product_description,
                product_category,
                country_of_origin,
                date_of_expiry,
                date_of_manufacturing,
                price,
                image_url
            );

            _exists[key] = true;

            email_to_list_of_product_id[email].push(product_id);       
        
    }

    function listProducts(
        string memory email
    ) public view onlyOnwner returns (Product[] memory) {

        uint256 productCount = email_to_list_of_product_id[email].length;
        
        Product[] memory products = new Product[](productCount);

        for (uint256 i = 0; i < productCount; i++) {
            products[i] = email_to_product_map[email][email_to_list_of_product_id[email][i]];
        }

        return products;
    }

    function productDetail(
        string memory email,
        string memory product_id
    ) public view onlyOnwner returns (Product memory) {
        return email_to_product_map[email][product_id];
    }

    function checkProductExist(
        string memory key
    ) public view onlyOnwner returns (bool) {
        return _exists[key];
    }
}
