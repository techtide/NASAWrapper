# The 2nd Part: Using These APIs With Python for ML
by arman (techtide)

Are you looking for data? This is the place to go (along with Kaggle), so go to it:
* https://data.nasa.gov/

Now the library we will be using is [this](https://github.com/emirozer/bowshock), courtesy of *emirozer* on GitHub. 
It's pretty cool.

1. get your python environment up and running
  a. for mac https://www.youtube.com/watch?v=YYXdXT2l-Gg&vl=en
  b. for windows https://www.youtube.com/watch?v=M4ztKyNkDIM

2. install bowshock
``pip install bowshock``

3. you need to setup an environment variable with your api key from the earlier part, if you haven't done this go back to step 1 of the original tutorial
  a. on windows click start> My Computer >Properties > Advanced System Settings > Environment Variables > in user variables, press new variable and create ``NASA_API_KEY``, and set the value to that api key
  b. on macOS and linux open up terminal and run the following command;
    ``touch .profile && cat export NASA_API_KEY <REPLACE THIS ALONG WITH THE BRACKETS WITH UR API KEY> >> .profile``
    and follow what it says inside the < > please. if you have trouble with this just ask me.

4. install pip on windows (youtube/google it), you might have it possibly already on your machine 

5. ``pip install bowshock``

6. open up Python IDLE on your PC/Mac

##now you have bowshock, what is it?
Bowshock is this really great Python library we're going to use to communicate with the NASA api. I've attached the usage of bowshock below from their readme,
copy and paste the APIs you need access to. Talk to a mentor to figure out which API you want to use.

##### Apod
```python
from bowshock import apod

# with specific date and tags - For apod all args are optional
apod.apod(date="2015-02-02", concept_tags=True)

```

-
##### Asterank
```python
from bowshock import asterank

# all args mandatory
asterank.asterank(
            	query={"e": {"$lt": 0.1},
               	       "i": {"$lt": 4},
                       "a": {"$lt": 1.5}},
                  limit=1)

```


-
##### Earth
```python
from bowshock import earth

# imagery endpoint lon & lat mandatory, rest optional
earth.imagery(lon=100.75,
                    lat=1.6,
                    dim=0.0025,
                    date="2015-02-02",
                    cloud_score=True)
# assets endpoint lon & lat & begin mandatory, end optional
earth.assets(lon=100.75, lat=1.6, begin="2015-02-02", end="2015-02-10")
```

-
##### HelioViewer
```python
from bowshock import helioviewer

# args are mandatory
helioviewer.getjp2image(date='2014-01-01T23:59:59', sourceId=14)
#args are mandatory
helioviewer.getjp2header(Id=7654321)

```


-
##### MAAS
```python
from bowshock import maas

# mandatory date begin / end
maas.maas_archive('2012-10-01', '2012-10-31')

maas.maas_latest()

```

-
##### Patents
```python
from bowshock import patents

# only query is mandatory, rest is optional
patents.patents(query="temperature", concept_tags=True, limit=5)

```


-
##### PredictTheSky
```python
from bowshock import predictthesky

#args are mandatory
predictthesky.space_events(lon=100.75, lat=1.5)

```


-
##### Star API
```python
from bowshock import star

star.stars()
star.search_star("Sun")

star.exoplanets()
star.search_exoplanet("11 Com")

star.local_group_of_galaxies()
star.search_local_galaxies("IC 10")

star.star_clusters()
star.search_star_cluster("Berkeley 59")

```


-
##### Skymorph
```python
from bowshock import skymorph

# mandatory obj id
skymorph.search_target_obj("J99TS7A")

#TODO : add search_position() , search_target_obj()

```


-
##### temperature anomalies
```python
from bowshock import temperature_anomalies

# end arg is optional, rest is mandatory
temperature_anomalies.coordinate(lon=100.3, lat=1.6, begin="1990", end="2005")


```


-
##### techport
```python
from bowshock import techport

techport.techport(Id="4795")
