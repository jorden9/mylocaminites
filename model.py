import pandas as pd
import folium

shop=pd.read_csv("Data/NewShopping_Data.csv")
shop1=pd.read_csv("Data/NewShopping.csv")
med=pd.read_csv('Data/NewMedical.csv')
stat=pd.read_csv('Data/Stationary.csv')
elec=pd.read_csv('Data/electronics.csv' ,encoding='latin-1')
grocery=pd.read_csv('Data/NewGrocery.csv')
food=pd.read_csv('Data/NewFood.csv')

shop_final= pd.concat((shop,shop1,med,stat,elec,grocery,food),axis=0,ignore_index=True)
datamapping= {
    "School" : 1,
    "Gym" : 2,
    "Gov" : 3,
    "Shopping" : 4,
    "Medical" : 5,
    "Stationary" : 6,
    "Electronics" : 7,
    "Grocery" : 8,
    "Food" :9
}

df=shop_final

df['Type'] = df['Type'].map(datamapping)

df = df.astype({'Rating':'float'})

df = df.astype({'Rating':'int'})

def map(school,gym,gov,shopping,medical,stationary,Electronics,Grocery,Food):
 name1=df['Name']
 long = df['Long']
 lat = df['Lat']
 rat=df['Rating'].astype(int)
 tar = df['Type']
 fg=folium.FeatureGroup(name="any")
 m = folium.Map(location=[19.383923, 72.829269], zoom_start=30)

 for i in range(633):
  tarvalue=tar[i]
  if school == 1 and tarvalue== 1 :
    if rat[i] > 4 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='darkgreen')))
    elif rat[i] > 3 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='green')))
    else :
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='lightgreen')))
  if gym == 1 and tarvalue ==2 :
    if rat[i] > 4 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='darkred')))
    elif rat[i] > 3 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='red')))
    else :
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='lightred')))
  if gov == 1 and tarvalue == 3 : 
    if rat[i] > 4 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='darkblue')))
    elif rat[i] > 3 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='blue')))
    else :
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='lightblue')))
  if shopping == 1 and tarvalue ==4 :
    if rat[i] > 4 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='black')))
    elif rat[i] > 3 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='gray')))
    else :
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='lightgray')))
  if medical == 1 and tarvalue == 5 :
    if rat[i] > 4 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='darkpurple')))
    elif rat[i] > 3 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='darkpurple')))
    else :
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='purple')))
  if stationary == 1 and tarvalue == 6 :
    if rat[i] > 4 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='lightpink')))
    elif rat[i] > 3 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='lightpink')))
    else :
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='pink')))
  if Electronics == 1 and tarvalue == 7 :
    if rat[i] > 4 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='darkorange')))
    elif rat[i] > 3 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='orange')))
    else :
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='orange')))
  if Grocery == 1 and tarvalue == 8 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='beige')))
  if Food == 1 and tarvalue == 9 : 
      fg.add_child(folium.Marker([long[i],lat[i]],popup=name1[i],icon=folium.Icon(color='cadetblue'))) 
 return m.add_child(fg) 
    

map(1,0,1,0,1,1,0,0,1)