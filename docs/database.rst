Structure de la base de données
===============================

Modèle Profile :
----------------
- user : FK vers User
- favorite_city : CharField

Modèle Letting :
----------------
- title : CharField
- address : OneToOne vers Address

Modèle Address :
----------------
- number : int
- street : str
- city : str
- state : str
- zip_code : str
- country_iso_code : str

Base : SQLite en local, PostgreSQL sur Render
