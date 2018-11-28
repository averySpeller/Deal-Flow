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


curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lX3BheWxvYWQiOiJwYXlsb2FkIiwiZXhwIjoxNTQyMTg4NTk0fQ.7D068S_DYGKwyMr8vb-Y5PdWeGEO4RP9rMC3GSq1S0w" -d '{     "name": "Apple",     "stock_symbol": "AAPL",     "logo": "static/imgs/randomLogo8.jpg",     "vision": "Think different.",     "revenue_model": "Manufacturing model",     "revenue": "$52.6 Billion (USD)",     "valuation": "$1 Trillion",     "phone1": "(123) 456-7890",     "phone2": "(408) 606-5775",     "line1": "One Infinite Loop",     "line2": "",     "city": "Cupertino",     "state": "CA",     "country": "USA",     "postal": "95014",     "website": "www.apple.ca",     "notes": "Apple Inc. is an American multinational technology company headquartered in Cupertino"   }' -X POST "24.138.161.30:5000/organizations"

curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lX3BheWxvYWQiOiJwYXlsb2FkIiwiZXhwIjoxNTQyMTg4NTk0fQ.7D068S_DYGKwyMr8vb-Y5PdWeGEO4RP9rMC3GSq1S0w" -d '{    "name": "Cutting Edge",    "stock_symbol": "",    "logo": "",    "vision": "Better haircuts.",    "revenue_model": "Service",    "revenue": "$4 Million (CAD)",    "valuation": "$100 Million",    "phone1": "(123) 456-7890",    "phone2": "(408) 606-5775",    "line1": "123 someplace",    "line2": "",    "city": "Anywhere",    "state": "On",    "country": "CA",    "postal": "P4N 1K9",    "website": "www.thecuttingedge.ca",    "notes": "A new take on an old industry."}' -X POST "24.138.161.30:5000/organizations"

curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lX3BheWxvYWQiOiJwYXlsb2FkIiwiZXhwIjoxNTQyMTg4NTk0fQ.7D068S_DYGKwyMr8vb-Y5PdWeGEO4RP9rMC3GSq1S0w" -d '{    "name": "Bitfarms",    "stock_symbol": "BLLCF",    "logo": "",    "vision": "Computing to reshape the world",    "revenue_model": "SaaS",    "revenue": "$140 Million (CAD)",    "valuation": "$1 Billion",    "phone1": "(123) 456-7890",    "phone2": "(408) 606-5775",    "line1": "123 someplace",    "line2": "",    "city": "Anywhere",    "state": "On",    "country": "CA",    "postal": "P4N 1K9",    "website": "www.bitfarms.io",    "notes": "Bitfarms is building infrastructure for the future by developing and hosting the ecosystem growing around blockchain-based technologies."}' -X POST "24.138.161.30:5000/organizations"


curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lX3BheWxvYWQiOiJwYXlsb2FkIiwiZXhwIjoxNTQyMTg4NTk0fQ.7D068S_DYGKwyMr8vb-Y5PdWeGEO4RP9rMC3GSq1S0w" -d '{"contact_id": 1, "organization_id": 1, "avatar": "", "first": "Timmy", "last": "Cook", "title": "CEO", "email": "timcook@apple.ca", "phone1": "(123) 456-7890", "phone2": "", "website": "www.timcook.ca", "notes": "Timothy Donald Cook is an American business executive and industrial engineer. Cook is the Chief Executive Officer of Apple Inc."}' -X POST 24.138.161.30:5000/contacts


```
