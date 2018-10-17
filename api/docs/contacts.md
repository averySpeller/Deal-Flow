# Contacts



**Description**: The description of the resource here.  
**Service**: `<ServiceName>`  
**Model**: `Contact`  

Some words here.

## Sample Contact
``` json
{
    "contactId": ":id",
    "first": ":str",
    "last": ":str",
    "email": ":email",
    "phone1": ":str",
    "phone2": ":str",
    "website": ":str",
    "notes": ":str"
}
```

|  Path  |    Resource    |
| :--: | :--: |
| [`/contacts`][contacts]| List [contact][contacts] resources available to the authenticated user. |
| [`/contacts/:id`][contacts]| Instance [contact][contacts] resource available to the authenticated user. |

## Properties

## Relationships

## Collection Endpoints

### List Contacts
```
GET /contacts
[
    {
        "contactId": :id
        ...
    },
    {
        "contactId": :id
        ...
    },
]
```

## Instance Endpoints

### Get Contacts by ID
```
GET /contacts/:id
{
    "contactId": :id
    ...
}
```

### Create a Contact
```
POST /contacts
{
    ... fields ...
}
```
### Update an Existing Contact
```
PUT /contacts/:id
{
    ... fields to update ...
}
```

### Delete a Contact
```
DELETE /contacts/:id
```
