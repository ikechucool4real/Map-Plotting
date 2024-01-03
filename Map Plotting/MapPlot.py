import pandas as pd 
import matplotlib.pyplot as plt

#Reading the data into a data frame
#Read CSV into DataFrame
data = pd.read_csv('./GrowLocations.csv')


#Removing bad values
#Rename column headers
data.rename(columns={
    'Longitude': 'Latitude',
    'Latitude': 'Longitude'
}, inplace = True)

#Filter latitude and longitude within the specified box
data = data[(data['Latitude'] >= 50.681) & 
            (data['Latitude'] <= 57.985) &
            (data['Longitude'] >= -10.592) &
            (data['Longitude'] <= 1.6848)]


#Fixing other problems
#Remove duplicate values
data.drop_duplicates(inplace = True)

#Remove NaN or invalid values
data.dropna(subset=['Latitude', 'Longitude'], inplace = True)


#Plotting the data correctly
#Load the map image
map_image = plt.imread('./map.png')

#Plot the map
plt.imshow(map_image, extent = [-10.592, 1.6842, 50.681, 57.985])

#Plot the data points on the map
plt.scatter(data['Longitude'], data['Latitude'], color = 'blue', label = 'Location')

#Customise the plot
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Plotting the Grow Dataset')
plt.legend()
plt.show()