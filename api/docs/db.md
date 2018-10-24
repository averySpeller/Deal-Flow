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


```
create table contact (
    contact_id int auto_increment primary key,
    organization_id int,
    first varchar(75),
    last varchar(75),
    email varchar(75),
    phone1 varchar(75),
    phone2 varchar(75),
    website varchar(75),
    notes text,
    json_store text
);

create table organization (
    OrganizationID int auto_increment primary key,
    Name varchar(75),
    Logo varchar(75),
    Vision varchar(75),
    RevenueModel varchar(75),
    Revenue varchar(75),
    Phase varchar(75),
    Valuation varchar(75),
    Phone1 varchar(75),
    Phone2 varchar(75),
    Website varchar(75),
    Notes text,
    JSONStore text
);
```
