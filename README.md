# storage

Create storage where if will be easy to add and get new series of data

"pytable" have to be used

data example:

time,col1,col2,col3
123,0,0,0
124,0,0,0
125,0,0,0
126,0,0,0
127,0,0,0
128,0,0,0
129,0,0,0



requiremens
records in pytable should be accessed by names. for example 
storage.get('name1') have to return data frame


and have to be ability to add new records into storage
storage.add('name2', new_df)

