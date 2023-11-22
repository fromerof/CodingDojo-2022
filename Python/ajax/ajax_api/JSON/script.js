var data = {
    "orders": [
    {
        "date": "June 30, 2088 1:54:23 AM",
        "orderno": 784692,
        "customer": {
        "trackingno": "TN000391",
        "custid": 11045,
        "fname": "Sue",
        "lname": "Hatfield",
        "address": "1409 Silver Street",
        "city": "Ashland",
        "state": "NE",
        "zip": 68003
        }
    },
    {
        "orderno": 784693,
        "date": "March 3, 2088 8:18:14 PM",
        "trackingno": "TN000468",
        "customer": {
        "custid": 11045,
        "fname": "Sue",
        "lname": "Hatfield",
        "address": "1409 Silver Street",
        "city": "Ashland",
        "state": "NE",
        "zip": 68003
        }
    }
    ]
}
console.log(data);
// imprimiría la imagen de abajo
console.log(data.orders);
console.log(data.orders[0].customer);
console.log(data.orders[0].customer.address);