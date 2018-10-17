# Conventions


Introduction
.
## Databases
* auth
* user
* data


### Auth
```
User ( _ProfileID_, Username, Password )

Auth ( _ProfileID_, Token )
```

### User
```
User ( _ProfileID_, First, Last, JSONStore )
```

### Data
```
Organization (
    _OrganizationID_, Name, Logo, Vision, RevenueModel, Revenue, Phase, Valuation, Phone1, Phone2, Website, Notes, JSONStore
)

Contact (
    _ContactID_, First, Last, Email, Phone1, Phone2, Website, Notes, JSONStore
)

Address (
    _AddressID_, EntityType, EntityID, Address1, Address2, City, State, Country
)

ContactOrganization ( _OrganizationID, ContactID_, Type )

Deal (_OrganizationID, Created_, Updated, Phase, JSONStore)

EntityIndex ( _EntityType, EntityID, Attribute_, Value )

Tag ( _TagID_ )

TagRelation ( _EntityType, EntityID, TagID_ )
```
