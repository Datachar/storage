# storage

Create storage where if will be easy to add and get new series of data

"pytable" have to be used

data example:

  time,col1,col2,col3<br/>
  123,0,0,0<br/>
  124,0,0,0<br/>
  125,0,0,0<br/>
  126,0,0,0<br/>
  127,0,0,0<br/>
  128,0,0,0<br/>
  129,0,0,0<br/>



requiremens:

- records in pytable should be accessed by names. for example: storage.get('name1'). have to return data frame
- have to be ability to add new records into storage. for example: storage.add('name2', new_df). have to add new record into storage

