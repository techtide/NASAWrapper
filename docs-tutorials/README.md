# How to Use NASA Tech in Your Projects
by arman (techtide)

So there are two routes that you can choose to go down. This really all depends on which language you're comfortable with working with. 

my other part of the tutorial, if you want to jump right in - with python : https://github.com/techtide/space-demos/blob/master/data-science.md

If you're using these APIs for offline app things like data science and machine learning (all done with python), then follow my other portion of this guide, which gives you a crash course on another super simple API. You still need an API key, and you should keep it saved on a text file or somewhere accessible. [this is the  guide for python. linked.](https://github.com/techtide/space-demos/blob/master/data-science.md)

1. Start by getting yourself an API key.
![alt text](https://github.com/techtide/space-demos/blob/master/tut1.png?raw=true)
2. Edit the file ``config.json``, with your API key, as an example:
```
{
  "key":MY-SUPER-SECRET-KEY-PLS-DONT-SHARE-ME
}
```
3. If you're using JS to just build a site or something, the NASA default boilerplate is a good enough intro. I expand and actually explain things here:

#### So you want to know what you can do?
If I was going to be super cliche, I'd say that imagination is the limit, but NASA gives you some new things to deal with. Also, don't abuse the API. Nasa is doing this for progression of space tech and public good, be courteous...

![list of apis](https://github.com/techtide/space-demos/blob/master/apilist.png?raw=true)

https://api.nasa.gov/api.html#apod > on the sidebar of this site you'll see a list of the apis you can use and the paramaters

how do you form a get request???
see this example query part? :

EXAMPLE QUERY-
``https://api.nasa.gov/planetary/apod?api_key={YOUR-API-KEY-FROM-EARLIER}``
after the ? you can add things like it says in the question paramaters like ``?api_key={API KEY FROM EARLIER ILL REPLACE}**&**&date=YYYY-MM-DD``

remember nasa uses american date format :)

You'll probably need help with this. Just ask me or another mentor. You can always Whatsapp me.

#### Using the JS Things
Follow this [getting started jsbin](https://api.nasa.gov/index.html#live_example)

### some helpful links.
[data](https://data.nasa.gov/)
[code](https://code.nasa.gov/)
[make your own space rover - not within scope but interesting nonetheless](https://github.com/nasa-jpl/open-source-rover)
