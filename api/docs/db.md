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
create table user (
    user_id int auto_increment primary key,
    username varchar(255),
    password varchar(255),
    first varchar(255),
    last varchar(255),
    privillege int(2)
);

create table deal (
    deal_id int auto_increment primary key,
    organization_id int,
    organization text,
    contacts text,
    interest varchar(255),
    status varchar(255),
    valuation varchar(255),
    raise_type varchar(255),
    raise varchar(255),
    revenue varchar(255),
    revenue_model varchar(255),
    round varchar(255),
    slide_deck longtext,
    date_added datetime,
    date_viewed datetime,
    notes text
);

create table organization (
    organization_id int auto_increment primary key,
    name varchar(255),
    stock_symbol varchar(255),
    logo longtext,
    vision varchar(255),
    revenue_model varchar(255),
    revenue varchar(255),
    valuation varchar(255),
    phone1 varchar(255),
    phone2 varchar(255),
    line1 varchar(255),
    line2 varchar(255),
    city varchar(255),
    state varchar(255),
    country varchar(255),
    postal varchar(255),
    website varchar(255),
    notes text
);

create table contact (
    contact_id int auto_increment primary key,
    organization_id int(11),
    avatar longtext,
    first varchar(255),
    last varchar(255),
    title varchar(255),
    email varchar(255),
    phone1 varchar(255),
    phone2 varchar(255),
    website varchar(255),
    notes text
);

create table tag (
    tag_id int auto_increment primary key,
    tag_name varchar(255),
    tag_color varchar(255)
);

create table tagmapping (
    tagmapping_id int auto_increment primary key,
    tag_id int(11),
    contact_id int(11),
    organization_id int(11)
);


alter table contact modify avatar longtext;
alter table organization modify logo longtext;
alter table deal modify slide_deck longtext;


Data Import Commands:

curl -i -H "Authorization: Bearer <token>" -d '{}' -X POST "24.138.161.30:5000/organizations"
curl -i -H "Authorization: Bearer <token>" -d '{}' -X POST "24.138.161.30:5000/contacts"
curl -i -H "Authorization: Bearer <token>" -d '{}' -X POST "24.138.161.30:5000/organizations"

curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lX3BheWxvYWQiOiJwYXlsb2FkIiwiZXhwIjoxNTQyMDQ5NTgyfQ.tDZJPBnYTw2exuznE41kM9BWnPYhsdLDFBGFonqJ6UE" -d '{     "name": "Apple",     "stock_symbol": "AAPL",     "logo": "static/imgs/randomLogo8.jpg",     "vision": "Think different.",     "revenue_model": "Manufacturing model",     "revenue": "$52.6 Billion (USD)",     "valuation": "$1 Trillion",     "phone1": "(123) 456-7890",     "phone2": "(408) 606-5775",     "line1": "One Infinite Loop",     "line2": "",     "city": "Cupertino",     "state": "CA",     "country": "USA",     "postal": "95014",     "website": "www.apple.ca",     "notes": "Apple Inc. is an American multinational technology company headquartered in Cupertino"   }' -X POST "24.138.161.30:5000/organizations"



```
