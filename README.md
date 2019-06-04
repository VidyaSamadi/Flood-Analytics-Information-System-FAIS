# Project Title
Flood Analytics Information System (FAIS) - Big Data Gathering package from twitter and USGS

## Getting Started
FAIS is a python package developed using python 3.7, which is not supported by python2. The package is used as a data gathering tool for USGS flood data and Twitter Data. The user can specifically target the flood station in each State in the US for the historical data as well as real time flood data. To gather Twitter feeds, the user can specified the targeted username or keyword with date gape to gather all the tweets that match the criteria

### Prerequisites

The package dependencies are:            
*  pandas
*  numpy
*  rpy2
*  urllib3
*  requests
*  opencv-python
*  netCDF4
*  matplotlib
*  textblob
*  pyquery
*  tweepy


### Installing

The package can be installed using Pypi installation

    $ pip install fais


## Usage

### Real Time USGS Flood Data

Each state at the US has its own flood monitoring stations that are identified with specific id, coordinates, etc. The API allows the user to target specific state and get the real time flood information. The user also has choices to either save the data as csv file or return it as a panda dataframe.

#### Example 1

The user wants to gather South Carolina real time data, and save it as a csv file called “sc_realtime.csv”

```python
>>> from fais import usgsgatherer as usgs
>>> usgs.get_realtime_flood_csv(“sc”, “sc_realtime.csv”)

```
The software will download the real time flood reading from any station in South Carolina, delete the null result, and save it as sc_realtime.csv file at the specified directory. The inputs of this function are the targeted State abbreviation and the file name. 

#### Example 2
The user wants to gather real time flood data from Arizona and return it as a data frame format. 

```python
>>> from fais import usgsgatherer as usgs
>>> df = usgs.get_realtime_flood_(“az”)

```
The object df is contain a result of the realtime flood data as a panda dataframe format.

#### Example 3

The user wants to gather river cam image at Rocky Creek cam station 021603273 located in South Carolina. 
The station list can be found at [rivercam](https://www.usgs.gov/centers/sa-water/science/river-webcams-south-atlantic-water-science-center-georgia-north-and-south?qt-science_center_objects=0#qt-science_center_objects)

```python
>>> from fais import usgsgatherer as usgs
>>> img = usgs.get_river_cam_sc_color(“021603273”)

```
The image file contains an image array of the real time river cam. The image is supported by 


### Historical USGS Flood Data

#### Example 1
The user wants to gather North Carolina Flood data for Hurricane Matthew, October 06-07, 2016 with specific station number 0212427947, which is REEDY CREEK AT SR NR CHARLOTTE, NC  and save it as a csv file called “nc_mathew.csv”

```python
>>> from fais import usgsgatherer
>>> criteria = usgsgatherer.create_usgs_criteria("NC","0212427947", ["00065", "00045","00060"], "2016-10-06", "2016-10-07")
>>> usgs.get_flood_data_csv(criteria, "nc_matthew.csv")

```
The software will download the flood data from REEDY CREEK AT SR NR CHARLOTTE, NC delete the null result, and save it as nc_mathew.csv file at the specified directory. The inputs of this function are the targeted criteria which include the targeted state, station number, parameters, date and the file name. 
If the user wish to use the result as a data frame object, simply change get_flood_data_csv() to get_flood_data_dataframe()

#### Example 2 
The user can receive a list of flood stations from each state and use the historical data gathering module to collect the data. the module returns the station list from North Carolina and save it as a csv file called “nc_station.csv”

```python
>>>from fais import usgsgatherer
>>>criteria = usgsgatherer.get_station_list_csv("NC", "nc_station.csv")

```


### Twitter Data

#### Example 1
The user wants to gather Tweets from governemnet official twitter account such as the National Weather Service during Hurricane Florence --September 20, 2018 – October 20, 2018 and save it as a csv file called “nws_florence.csv”


```python
>>> from fais import twittergatherer 
>>> twitter_username = "nws"
>>> twitter_keyword = None
>>> twitter_since = "2018-09-20"
>>> twitter_until = "2018-10-20"
>>> twitter_criteria = twittergatherer.create_twitter_criteria(twitter_username, twitter_keyword,twitter_since,twitter_until, 10000)
>>> twittergatherer.get_tweets_csv(twitter_criteria, "nws_florence.csv")
```
The software will download all Tweets posted by National Weather Service’s Twitter account during September 20, 2018 to October 20, 2018 with the maximum of 10,000 tweets.

## Authors


* **Nattapon Donratanapat** 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Jefferson Henrique - [Github](https://github.com/Jefferson-Henrique)

