# Function to convert degrees Celsius to degrees Fahrenheit
# tc = input value (in degrees C)
# tf = output value (in degrees F)
def convert(tc):
    tf = tc * 1.8 + 32
    return tf

# list to store the values
dataC = []
dataF = []

# open file and read the data in it
try:
    file_to_read = open(input("Enter file path: "))
    print("File " + str(file_to_read) + " is now open")
except IOError:
    print('File is not found or filename is incorrect')

try:
    # read the data and store it in a list
    dataC = file_to_read.readlines()
except:
    print("Something went wrong")
    file_to_read.close()
finally:
    # Check whether the file is closed
    print('Is the file closed?:', file_to_read.closed)
    if str(file_to_read.closed) == 'False':
        file_to_read.close()
        print("Close the file")

# convert the data
dataC = [x[:-2] for x in dataC]

for i in range(0, len(dataC)):
    dataC[i] = int(dataC[i])

for i in range(0, len(dataC)):
    dataF.append(convert(dataC[i]))

for i in range(0, len(dataF)):
    dataF[i] = str(dataF[i]) + 'F\n'

# open new file and write the data in it
try:
    file_to_write = open(input('Enter file to write converted values: '), "a+")
    print("File " + str(file_to_write) + " is now open")
except IOError:
    print('File is not found or filename is incorrect')

try:
    file_to_write.writelines(dataF)
except:
    print("Something went wrong and data couldn't be writen")
    file_to_write.close()
finally:
    # Check whether the file is closed
    print('Is the file closed?: ', file_to_write.closed)
    if str(file_to_write.closed) == 'False':
        file_to_write.close()
        print("Close the file")