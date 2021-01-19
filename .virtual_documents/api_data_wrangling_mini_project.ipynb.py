# Store the API key as a string - according to PEP8, constants are always named in all upper case
API_KEY = ''


# First, import the relevant modules
import requests


# Now, call the Quandl API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned
url = "https://www.quandl.com/api/v3/datasets/FSE/AFX_X/data.json?start_date=2017-01-01&end_date=2017-12-31&api_key=" + API_KEY
url


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure
r= requests.get(url)
json = r.json()
json


#2. Convert the returned JSON object into a Python dictionary.
AFX_X = {}
for k in json.keys():
    AFX_X[k] = json[k]


#3. Calculate what the highest and lowest opening prices were for the stock in this period.
max_open=0
min_open=AFX_X['dataset_data']['data'][0][1]

for i in range(len(AFX_X['dataset_data']['data'])):
    if AFX_X['dataset_data']['data'][i][1] is None:
        continue
        
    if AFX_X['dataset_data']['data'][i][1] > max_open:
        max_open = AFX_X['dataset_data']['data'][i][1]
    
    if AFX_X['dataset_data']['data'][i][1] < min_open:
        min_open = AFX_X['dataset_data']['data'][i][1]
        
print(f"Opening Max: ${max_open}\nOpening Min: ${min_open}")
   


#4. What was the largest change in any one day (based on High and Low price)?
max_change = 0
for i in range(len(AFX_X['dataset_data']['data'])):
    if AFX_X['dataset_data']['data'][i][2] is None or AFX_X['dataset_data']['data'][i][3] is None :
        continue
        
    change = abs(AFX_X['dataset_data']['data'][i][2] - AFX_X['dataset_data']['data'][i][3])
    if change > max_change:
        max_change = change

print("Largest change in one day: $get_ipython().run_line_magic(".2f"", " %max_change)")


#5. What was the largest change between any two days (based on Closing Price)?
max_change = 0
for i in range(len(AFX_X['dataset_data']['data'])):
    try:
        if AFX_X['dataset_data']['data'][i][4] is None or AFX_X['dataset_data']['data'][i+1][4] is None :
            continue
        
        change = abs(AFX_X['dataset_data']['data'][i][4] - AFX_X['dataset_data']['data'][i+1][4])
        if change > max_change:
            max_change = change
    except:
        break
print("Largest change in one day: $get_ipython().run_line_magic(".2f"", " %max_change)")


#6. What was the average daily trading volume during this year?
avg=0
value_present=0
for i in range(len(AFX_X['dataset_data']['data'])):
    avg += AFX_X['dataset_data']['data'][i][6]
    if AFX_X['dataset_data']['data'][i][6] is not None:
        value_present += 1
print(f"Average daily trading volume: {avg/value_present}")


#7. What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

median=set()

for i in range(len(AFX_X['dataset_data']['data'])):
    median.add(AFX_X['dataset_data']['data'][i][6])
    
print(f"Median trading volume: {int(list(median)[len(median)//2])}")
