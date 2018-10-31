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
    username varchar(75),
    password varchar(150),
    first varchar(75),
    last varchar(75),
    privillege int(2)
);

create table deals (
    deal_id int auto_increment primary key,
    organization_id int,
    organization text,
    contacts text,
    interest varchar(75),
    status varchar(75),
    valuation varchar(75),
    raise_type varchar(75),
    raise varchar(75),
    revenue varchar(75),
    revenue_model varchar(75),
    round varchar(75),
    slide_deck varchar(75),
    notes text
);

create table organization (
    organization_id int auto_increment primary key,
    name varchar(75),
    stock_symbol varchar(75),
    logo varchar(75),
    vision varchar(75),
    revenue_model varchar(75),
    revenue varchar(75),
    valuation varchar(75),
    phone1 varchar(75),
    phone2 varchar(75),
    line1 varchar(75),
    line2 varchar(75),
    city varchar(75),
    state varchar(75),
    country varchar(75),
    postal varchar(75),
    website varchar(75),
    notes text
);

create table contact (
    contact_id int auto_increment primary key,
    organization_id int(11),
    avatar varchar(150),
    first varchar(75),
    last varchar(75),
    title varchar(75),
    email varchar(75),
    phone1 varchar(75),
    phone2 varchar(75),
    website varchar(75),
    notes text
);

insert organization values (1,'Apple', 'AAPL', 'static/imgs/randomLogo8.jpg', 'Think different.', 'Manufacturing model', '$52.6 Billion (USD)', '$1 Trillion', '(123) 456-7890', '(408) 606-5775', 'One Infinite Loop', '', 'Cupertino', 'CA', 'USA', '95014', 'www.apple.ca', 'Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. ');

insert into contact values (1,1,'Tim', 'Cook', 'CEO', 'timcook@apple.ca', '(123) 456-7890','','www.timcook.ca', 'Timothy Donald Cook is an American business executive and industrial engineer. Cook is the Chief Executive Officer of Apple Inc., and previously served as the company\'s Chief Operating Officer under its founder Steve Jobs.');
```
