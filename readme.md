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


- Retrieve Vendor:
  - Request:
    GET /vendors/1/
  - Response:
    Status: 200 OK
    {
        "id": 1,
        "name": "Vendor 1",
        "contact_details": "Contact details of Vendor 1",
        "address": "Address of Vendor 1",
        "vendor_code": "VENDOR001"
    }

- Update Vendor:
  - Request:
    PUT /vendors/1/
    Body:
    {
        "name": "Updated Vendor Name",
        "contact_details": "Updated contact details",
        "address": "Updated address",
        "vendor_code": "UPDATEDVENDOR001"
    }
  - Response:
    Status: 200 OK
    {
        "id": 1,
        "name": "Updated Vendor Name",
        "contact_details": "Updated contact details",
        "address": "Updated address",
        "vendor_code": "UPDATEDVENDOR001"
    }

- Delete Vendor:
  - Request:
    DELETE /vendors/1/
  - Response:
    Status: 204 No Content

- Vendor Performance:
  - Request:
    GET /vendors/1/performance/
  - Response:
    Status: 200 OK
    {
        "id": 1,
        "vendor": 1,
        "date": "2024-05-13T12:00:00Z",
        "on_time_delivery_rate": 0.95,
        "quality_rating_avg": 4.5,
        "average_response_time": 24.5,
        "fulfillment_rate": 0.85
    }

Purchase Order Endpoints (continued):
- Retrieve Purchase Order:
  - Request:
    GET /purchase_orders/1/
  - Response:
    Status: 200 OK
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
    }

- Update Purchase Order:
  - Request:
    PUT /purchase_orders/1/
    Body:
    {
        "status": "Completed",
        "quality_rating": 4.5,
        "acknowledgment_date": "2024-05-14T12:00:00Z"
    }
  - Response:
    Status: 200 OK
    {
        "id": 1,
        "po_number": "PO001",
        "vendor": 1,
        "order_date": "2024-05-13T12:00:00Z",
        "delivery_date": "2024-05-20T12:00:00Z",
        "items": [{"name": "Item 1", "quantity": 10}, {"name": "Item 2", "quantity": 20}],
        "quantity": 30,
        "status": "Completed",
        "quality_rating": 4.5,
        "issue_date": "2024-05-13T12:00:00Z",
        "acknowledgment_date": "2024-05-14T12:00:00Z"
    }

- Delete Purchase Order:
  - Request:
    DELETE /purchase_orders/1/
  - Response:
    Status: 204 No Content

- Purchase Order Performance:
  - Request:
    POST /purchase_orders/1/performance/
  - Response:
    Status: 200 OK

