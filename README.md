# graphql-flask-postgres

Simple CRUD app with Python Flask, SQLAlchemy, PostgreSQL, and GraphQL (Graphene)


## Data
   The database contains two tables: **_person_** and **_article_**.
   
   - **_person_** table has three fields: _person_id_, _username_, and _fullname_
   - **_article_** tables has four fields: _article_id_, _title_, _article_text_, and _person_id_

## Examples
**Find all people in _person_ table:**
```
query{
  people {
    edges {
      node {
        personId
        username
        fullname
      }
    }
  }
}
```

**Create a new person:**
```
mutation {
  createPerson(input: { 
    username: "@bob"
    fullname: "Bob"
  }) {
    person {
      personId
      username
      fullname
    }
  }
}
```

**Find first five articles associated with person whose person_id is 1:**
```
query{
  person(uuid:1){
    fullname
    username
    Articles(first:5){
      edges{
        node{
            title
            articleText
        }
      }
    }
  }
}
```
