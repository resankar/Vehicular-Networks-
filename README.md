##Python Based Data Analysis:

The python script Sankaranarayanan.py which is developed to process the .json file can be called from the IDLE shell to extract the unprocessed data, analyze them and assist in various information that the users extract from them. In order to process the data in the file 8 functions are developed, the functionalities of these are as mentioned below.

1. func1: This function opens the JSON file, with the input parameter as the name of the file. The data from the file is in string format, this string is converted to values and the values depict the entries of a dictionary. We hence use a list of dictionaries to process such a file. This function will accept the name of the file as the input parameter and return the contents of the file as an output parameter, which is a list of dictionary.

2. func2: This function reads the first 10 records from the data extracted on the successful execution of the function func1. It takes the list of dictionaries as its input parameter and pretty prints the first 10 signal entries.

3. func3: This function takes the list of dictionaries as the input parameter and identifies all the unique values in the dictionary using the SET command. It also prompts the user to select a signal which is of his interest and calculates the range of that particular signal and the number of occurrences of the signal.

4. func4: This function takes the list of dictionaries as input parameter and returns the total trip time of the vehicle along with the trip distance of the vehicle.

5. func5: This function takes the list of dictionaries as input parameter and plots each signal type versus the timestamp. We would hence obtain a total of 12 plots with respect to timestamp.

6. func6: This function takes the list of dictionaries as the input parameter, it then calculates the total distance the vehicle has travelled by subtracting the maximum and minimum value of the odometer reading and the total time by subtracting the maximum and minimum value of the time stamp. The total distance travelled divided by the total time gives the average speed of the vehicle over the trip. It also determines the max value of the vehicle speed by determining the maximum value in the list created with all the values whose name is ‘vehicle_speed’.

7. func7: This function takes the list of dictionary as an input parameter and splits the latitude and longitude from them to makes a new list, this new list of all the latitude and longitude of the path along which Alice travelled is then plotted on google map to highlight the route Alice takes. This function generates an html file, which will be stored in the current directory. The trace can be viewed by opening this html file or by including the webbrowser package, the map pops up automatically on being generated.

8. func8: This function takes in the list of dictionary as the input parameter and calculates the amount of miles the vehicle can proceed with the current fuel. It uses the average speed of the vehicle and fuel consumption to determine the miles to go.
