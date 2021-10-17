# GQL Data loaders 
Test improvement in GraphQL with DataLoaders

## Install project

### Create env

    $ mkvirtualenv --python=/usr/bin/python3 dataloaders  

### Clone project

    $ git clone git@bitbucket.org:SebastianWilde/gql_dataloaders.git

### Install requirements

    $ pip install -r requirements.txt

### Migrate

    $ python manage.py migrate

### Load fixtures

    $ python manage.py loaddata fixtures/*.json

### Run server

    $ python manage.py runserver

## Admin credentials

http://127.0.0.1:8000/admin/

| Username    | Password |
| ----------- | ----------- |
| admin       | admin       |

## Test GraphQL

Test the following query (use Insomnia)

http://127.0.0.1:8000/graphql/

```
{
  _debug {
    sql {
      duration
      sql
    }
  }
  getUser {
    username
    bestFriend {
      username 
      bestFriends {
        bestFriend {
          id
        }
      }
    }
    bestFriends {
      username 
      bestFriends {
        username
      }
    }
  }
}
```
