# Simplified Resource Query Language (SRQL)

## Notes on the state of this document

Debate on resource includes:
* include additional resources as an array always vs as a document for 1 to 1 resources.


## Introduction
Consider two types of resource:

### Collection

Gather a collection:
```
GET someurl.com/resource
[
    { 'id': 1, 'name': 'resource1', 'field': 'another' },
    { 'id': 2, 'name': 'resource2', 'field': 'another' }
]
```

### Instance
Lookup an instance
```
GET someurl.com/resource/1
{
    'id': 1, 'name': 'resource1', 'field': 'another'
}
```

## Interfacing with an API

We will implement a simplified verison of other specifed query languages. Simplified Resource Query Language (SRQL) uses the core concepts of Resource Query Language (RQL) while maintaining the simplicity outlined by Vinay Sahni in Best Practices for a Pragmatic Restful API.

> It's best to keep the base resource URLs as lean as possible. Complex result filters, sorting requirements and advanced searching (when restricted to a single type of resource) can all be easily implemented as query parameters on top of the base URL. - Vinay Sahni @ Enchant (https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)

### Query Types
* Fields: Only include specified fields in response.
* Sorting: Sort the response (asc/desc) by field.
* Includes: Include a related resource in the response.
* Limiting: Return a maximum of limit resources.
* Paging: Fetch the next page of results.
* Grouping: Aggregate response by a specified field.


### Customizing Response Fields with Fields Parameter

When you are only looking for specific fields in a response you can obtain those _only_ those fields by utilizing the `fields` parameter.  

Consider the following request for two fields: `field1` and `field2` from `resource`:
```
GET someurl.com/resource?fields=field1,field2
```
``` json
[
    {
        "field1": "some field",
        "field2": "some field",
    },
    {
        "field1": "some field",
        "field2": "some field",
    }
]
```

### Filtering

Consider the following request searching from all of `resource` where `somefield` is equal to `someval`:
```
GET someurl.com/resource?somefield=someval
```
``` json
[
    {
        "somefield": "someval",
        "...": "..."
    },
    {
        "somefield": "someval",
        "...": "..."
    }
]
```

### Sorting
Consider the following request listing `resource` where field is sorted according to `field`:
```
# Default sort asc
GET someurl.com/resource?sort=field

# Verbose sort asc
GET someurl.com/resource?sort=+field

# Sort desc
GET someurl.com/resource?sort=-field
```
``` json
[
    {
        "field": "z",
        "...": "..."
    },
    {
        "field": "a",
        "...": "..."
    }
]
```

### Includes

Consider a resource `resource` with a *1 to 1* relationship to another resource `resource2`. We can fetch related resources using `include`:
```
GET someurl.com/resource?include=resource2
```
``` json
[
    {
        "field-of-resource": "...",
        "field-of-resource": "...",
        "resource2 ": {
            "field-of-resource2": "...",
            "field-of-resource2": "..."
        }
    },
    {
        "field-of-resource": "...",
        "field-of-resource": "...",
        "resource2 ": {
            "field-of-resource2": "...",
            "field-of-resource2": "..."
        }
    }
]
```

Consider a resource `resource` with a *1 to N* relationship to another resource `resource2`. We can fetch related resources using `include`:
```
GET someurl.com/resource?include=resource2
```
``` json
[
    {
        "field-of-resource": "...",
        "field-of-resource": "...",
        "resource2 ": [
            {
                "field-of-resource2": "...",
                "field-of-resource2": "..."
            },
            {
                "field-of-resource2": "...",
                "field-of-resource2": "..."
            }
        ]
    }
]
```

### Limiting

Consider a resource where you want a subset of results to limit to a set of *N* of resource, we use `limit`:
```
GET someurl.com/resource?limit=1
```
``` json
[
    {
        "field": "...",
        "...": "..."
    }
]
```

### Paging

Not yet defined.

### Grouping

Not yet defined.

## Additional Resources
* [Best Practices](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
