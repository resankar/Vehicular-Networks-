######################################################################################################################
### My first Python Project
#749c Project 1
#UID 113637384
# Input File = alicedata.json
# Processing Functions:
# Func1() ---> Open the file and convert the string to dictionary type
# Func2() ---> Print the first 10 records of the file using pretty print
# Func3() ---> Find the unique signal names and find the number of occurance and range for the user selected signal
# Func4() ---> Find the total distance travelled by the vehicle and the total time the vehicle has been in travel for
# Func5() ---> Plot each of the signals with respect to time
# Func6() ---> Calculating the Average Speed of the vehicle
# Func7() ---> Trace the path of the vehicle in google maps
# Func8() ---> Calculate the number of miles the vehicle can travel with the present fuel level
######################################################################################################################

###############################################################################
# Func1() ---> Open the file and convert the string to dictionary type
# Input is the json file ---> alicedata.json
# Output is data extracted from the file is converted into a list of dictionary
###############################################################################
def func1(file_name):
    import json
    import os
    file=os.path.abspath("/Users/renga/documents/python/"+file_name)
    dictionary=[]
    with open(file) as data:
        for each_dict in data:
            dictionary.append(json.loads(each_dict))
    return dictionary



###############################################################################
# Func3() ---> Find the unique signal names and find the number of occurance and range for the user selected signal
# Input is the json file ---> list of dictionary
# Output is generate a list of all the unique signal names and gives the number of ocurance and range of a selected signal
###############################################################################

def func3(data):
    signal=[]
    for d in data:
        temp = []
        temp = temp + [d['name']]
        signal = signal + temp

    signal=set(signal)
    print('The different signals are :')
    for x in signal:
        print (x)
            

    signal_name = input('Enter the signal name: ')
    
    value = []
    for sig in data:
        if sig['name'] == signal_name:
            value = value + [sig['value']]

    value.sort()
    
    print('The number of occurences of '+signal_name+' is '%d , len(value))
    print('The value range for '+signal_name+' is between '+str(value[0])+
          ' and '+str(value[-1])+'.')

###############################################################################
# Func4() ---> Find the total distance travelled by the vehicle and the total time the vehicle has been in travel for
# Input is the json file ---> list of dictionary
# Output is the total distance and the total time the vehicle has travelled will be printed
###############################################################################

def func4(data):
    value=[]
    for sig in data:
        if sig['name']=='odometer':
            value=value+[sig['value']]

    total_distance_covered=value[-1]-value[0]
    print("The Total Distance travelled by the vehice is :",total_distance_covered)

    value1=[]
    for sig in data:
        value1=value1+[sig['timestamp']]
        
    total_time=value1[-1]-value1[0]
    print("The Total time the vehicle has been in travel is :",total_time)

###############################################################################
# Func5() ---> Plot each of the signals with respect to time
# Input is the json file ---> list of dictionary
# Output is a plot of various signals with respect to the time
###############################################################################

def func5(data):
    signal=[]
    for d in data:
        temp = []
        temp = temp + [d['name']]
        signal = signal + temp

    signal=set(signal)

    for sig in signal:
        x=[]
        t=[]
        for i in data:                        
            if i['name'] == sig:
                if(i['name']=='transmission_gear_position'):
                    if(i['value']=='neutral'):
                        i['value']=0
                    elif(i['value']=='first'):
                        i['value']=1
                    elif(i['value']=='second'):
                        i['value']=2
                    elif(i['value']=='third'):
                        i['value']=3
                    elif(i['value']=='fourth'):
                        i['value']=4
                if(i['name']=='break_pedal_status'):
                    if(i['name']=='True'):
                        i['value']=1
                    if(i['name']=='False'):
                        i['value']=0
                x=x+[i['value']]
                t=t+[i['timestamp']]
        import matplotlib.pyplot as p1           
        p1.plot(t,x)
        p1.xlabel('Timestamp')
        p1.ylabel(sig)
        p1.show()

###############################################################################
# Func6() ---> Calculating the Average Speed of the vehicle
# Input is the json file ---> list of dictionary
# Output is the max speed and the average speed of the vehicle
###############################################################################


def func6(data):
    x=[]
    t=[]
    for sig in data:
        if sig['name']=='vehicle_speed':
            x=x+[sig['value']]
            t=t+[sig['timestamp']]
    t.sort()
    print("The Max Speed is :", max(x))

    value=[]
    for sig in data:
        if sig['name']=='odometer':
            value=value+[sig['value']]

    total_distance_covered=value[-1]-value[0]
    print(total_distance_covered)
    print(t[-1]-t[0])
    average_speed=total_distance_covered/(t[-1]-t[0])
    print("The Avg Speed of the vehicle is :",average_speed)

###############################################################################
# Func7() ---> Trace the path of the vehicle in google maps
# Input is the json file ---> list of dictionary
# Output is the trace of the path in google maps along which the vehicle traverses
###############################################################################
    
def func7(data):
    latitude=[]
    longitude=[]
    for sig in data:
        if sig['name']=='latitude':
            latitude=latitude+[sig['value']]
        if sig['name']=='longitude':    
            longitude=longitude+[sig['value']]

    import pygmaps 
    import webbrowser
    mymap = pygmaps.maps(latitude[0], longitude[0], 16)
    mymap.draw('/Users/renga/documents/python/mymap.draw.html')
    path=[]
    for i in range(int(len(latitude)/10)):
        path.append((latitude[i*10], longitude[i*10]))
    print(path)
    mymap.addpath(path,"#FF0000")
    mymap.draw('/Users/renga/documents/python/mymap.draw.html')
        

    
        
 
    

    

            
            
    




      
    
            
            
    


        
    


    


    

    


    

    


    

    

    
    
