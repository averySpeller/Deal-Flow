# Organizations

**Description**: The description of the resource here.  
**Service**: `<ServiceName>`  
**Model**: `Organization`  

Some words here.

## Sample Organization
``` json
{
    "organizationID": "_OrganizationID_",
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
```


|  Path  |    Resource    |
| :--: | :--: |
| [`/organizations`][organizations]| List [organizations][organizations] resources available to the authenticated user. |
| [`/organizations/:id`][organizations]| Instance [organization][organization] resource available to the authenticated user. |

## Properties

## Relationships

## Collection Endpoints

### List Organizations
```
GET /organizations
[
    {
        "organizationId": :id
        ...
    },
    {
        "contactId": :id
        ...
    },
]
```

## Instance Endpoints

### Get Organization by ID
```
GET /organizations/:id
{
    "organizationId": :id
    ...
}
```

### Create an Organization
```
POST /organizations
{
    ... fields ...
}
```
### Update an Existing Organization
```
PUT /organizations/:id
{
    ... fields to update ...
}
```

### Delete a Organization
```
DELETE /organizations/:id
```
