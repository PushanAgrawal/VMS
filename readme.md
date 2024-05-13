Token Obtain Endpoint:
- Request:
  POST /token/
  Body:
  {
      "username": "example_user",
      "password": "example_password"
  }
- Response:
  Status: 200 OK
  {
      "access": "<access_token>",
      "refresh": "<refresh_token>"
  }

Token Refresh Endpoint:
- Request:
  POST /token/refresh/
  Body:
  {
      "refresh": "<refresh_token>"
  }
- Response:
  Status: 200 OK
  {
      "access": "<new_access_token>"
  }

Vendor Endpoints:
- List Vendors:
  - Request:
    GET /vendors/
  - Response:
    Status: 200 OK
    [
        {
            "id": 1,
            "name": "Vendor 1",
            "contact_details": "Contact details of Vendor 1",
            "address": "Address of Vendor 1",
            "vendor_code": "VENDOR001"
        },
        ...
    ]

- Create Vendor:
  - Request:
    POST /vendors/
    Body:
    {
        "name": "New Vendor",
        "contact_details": "Contact details of New Vendor",
        "address": "Address of New Vendor",
        "vendor_code": "NEWVENDOR001",
        "password": "new_vendor_password"
    }
  - Response:
    Status: 201 Created
    {
        "id": 2,
        "name": "New Vendor",
        "contact_details": "Contact details of New Vendor",
        "address": "Address of New Vendor",
        "vendor_code": "NEWVENDOR001"
    }
  ...

Purchase Order Endpoints:
- List Purchase Orders:
  - Request:
    GET /purchase_orders/
  - Response:
    Status: 200 OK
    [
        {
            "id": 1,
            "po_number": "PO001",
            "vendor": 1,
            "order_date": "2024-05-13T12:00:00Z",
            "delivery_date": "2024-05-20T12:00:00Z",
            "items": [{"name": "Item 1", "quantity": 10}, {"name": "Item 2", "quantity": 20}],
            "quantity": 30,
            "status": "Pending",
            "quality_rating": null,
            "issue_date": "2024-05-13T12:00:00Z",
            "acknowledgment_date": null
        },
        ...
    ]

- Create Purchase Order:
  - Request:
    POST /purchase_orders/
    Body:
    {
        "po_number": "PO002",
        "vendor": 1,
        "order_date": "2024-05-13T12:00:00Z",
        "delivery_date": "2024-05-20T12:00:00Z",
        "items": [{"name": "Item 1", "quantity": 10}, {"name": "Item 2", "quantity": 20}],
        "quantity": 30,
        "status": "Pending",
        "issue_date": "2024-05-13T12:00:00Z"
    }
  - Response:
    Status: 201 Created
    {
        "id": 2,
        "po_number": "PO002",
        "vendor": 1,
        "order_date": "2024-05-13T12:00:00Z",
        "delivery_date": "2024-05-20T12:00:00Z",
        "items": [{"name": "Item 1", "quantity": 10}, {"name": "Item 2", "quantity": 20}],
        "quantity": 30,
        "status": "Pending",
        "quality_rating": null,
        "issue_date": "2024-05-13T12:00:00Z",
        "acknowledgment_date": null
    }
  ...

