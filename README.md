# Project Title
FAIS - Big Data Gathering package from twitter and USGS

## Getting Started
FAIS is a python package developed using python 3.7, which is not supported by python2. The package is used as a data gathering tools for USGS flood data and Twitter Data. The user can specifically target the flood station in each State for the historical data or real time data in each State. For Twitter, the user can specified the targeted username or keyword with date gape to gather all the tweets that matched the criteria

### Prerequisites

The package dependencies are:            
 Markup : *  pandas
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

Each states has their own flood monitoring station located throughout the states. The API allows the user to target specific state and get the real time flood information. The user also has choices to either save the data as csv file or return it as a panda dataframe

#### Example 1

The user wants to gather the South Carolina real time data, and save it as a csv file called “sc_realtime.csv”

```python
>>> from fais import usgsgatherer as usgs
>>> usgs.get_realtime_flood_csv(“sc”, “sc_realtime.csv”)

```
The software will download the real time flood reading from every station in South Carolina, deleted the null result, and save it as sc_realtime.csv file at the current directory. The inputs of this function are the targeted State abbreviation and the file name. 



## Authors

* **Nattapon Donratanapat** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
