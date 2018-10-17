# Deals

**Description**: The description of the resource here.  
**Service**: `<ServiceName>`  
**Model**: `Deal`  

Some words here.

## Sample Deal
``` json
{
    "dealID": "_DealID_",
    "deals": [
        {
            "name": "Name",
            "logo": "Logo",
            "vision": "Vision",
            "revenueModel": "RevenueModel",
            "revenue": "Revenue",
            "phase": "Phase",
            "valuation": "Valuation",
            "phone1": "Phone1",
            "phone2": "Phone2",
            "website": "Website",
            "notes": "Notes",
            "jsonStore": "JSONStore"
        },
        {
            "name": "Name",
            "logo": "Logo",
            "vision": "Vision",
            "revenueModel": "RevenueModel",
            "revenue": "Revenue",
            "phase": "Phase",
            "valuation": "Valuation",
            "phone1": "Phone1",
            "phone2": "Phone2",
            "website": "Website",
            "notes": "Notes",
            "jsonStore": "JSONStore"
        }
    ]
}
```


|  Path  |    Resource    |
| :--: | :--: |
| [`/deals`][deals]| List [deals][deals] resources available to the authenticated user. |
| [`/deals/:id`][deals]| Instance [deal][deal] resource available to the authenticated user. |

## Properties

## Relationships

## Collection Endpoints

### List Deals
```
GET /deals
[
    {
        "dealId": :id
        ...
    },
    {
        "dealId": :id
        ...
    },
]
```

## Instance Endpoints

### Get Deal by ID
```
GET /deals/:id
{
    "dealId": :id
    ...
}
```

### Create an Deal
```
POST /deals
{
    ... fields ...
}
```
### Update an Existing Deal
```
PUT /deals/:id
{
    ... fields to update ...
}
```

### Delete a Deal
```
DELETE /deals/:id
```
