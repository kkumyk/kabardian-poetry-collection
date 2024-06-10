# Kabardian Poems Collection

[DEPLOYED SITE](https://kabardian-poems-collection-b906b8b63b33.herokuapp.com/)

## Tech Stack
  <tr>
    <td><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python" width="110" height="28"></td>
    <td><img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="django" width="110" height="30"></td>
    <td><img src="https://img.shields.io/badge/javascript-fdd663.svg?style=for-the-badge&logo=javascript&logoColor=fbbc04" alt="js" width="90" height="28"></td>
    <td><img src="https://img.shields.io/badge/PostgreSQL-34517d.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white" alt="postgres" width="110" height="28"></td>
    <td><img src="https://img.shields.io/badge/Git-fc6d26?style=for-the-badge&logo=git&logoColor=white" alt="git" width="70" height="28"></td>
    <td><img src="https://img.shields.io/badge/heroku-4173c9.svg?style=for-the-badge&logo=Heroku&logoColor=white" alt="heroku" width="90" height="28"></td>
</tr>

<!-- ## Project Overview  -->

## Project Structure

├── kabardian_poetry | Django project <br>
├── poems | Django app <br>
├── about | Django app <br>
├── vocabulary | Django app <br>
├── env.py <br>
├── manage.py <br>
├── Procfile <br>
├── README.md <br>
├── requirements.txt <br>
└── runtime.txt 

<!-- ### GitHub Project

Find out project board here: [project board](https://github.com/users/kkumyk/projects/2) -->

<hr>

## User Stories

### First Time Users
- can view site's content - poems and about pages - and register

### Returning User
- can log in and view site's content - poems and about pages - and have access to a vocabulary page
- can save words from the poem specific pages to their vocabulary page
- can delete words from their vocabulary page

## Database Design

### Poem Model
|Key|Name|Type|
|---|---|---|
|PK |id   |int|
|   |title|CharField(300)   |
|   |author   |CharField(200)   |
|   |text   |TextField   |

### Word Model
|Key|Name|Type|
|---|---|---|
|PK |id   |int|
|   |word|CharField(100)   |
|   |type|CharField(100)   |
|   |eng_transl|CharField(100)   |
|   |rus_transl|CharField(100)   |
|   |ipa|CharField(100)   |


### Poems Words Join Table
|Key|Name|Type|
|---|---|---|
|PK |id   |int|
|Foreign Key   |poem_id|int   |
|Foreign Key   |word_id|int   |

### Vocabulary Model
|Key|Name|Type|
|---|---|---|
|PK |id   |int|
|Foreign Key|user_id|int   |
|Foreign Key|word_id|int   |
