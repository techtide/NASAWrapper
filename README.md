# NASA Wrapper
<p align="center"> 
<img src="https://www.festisite.com/static/partylogo/img/logos/nasa.png">
</p>

Please refer to my [in-depth guide and introduction to these APIs](https://github.com/techtide/space-demos) before you begin using this.

This is how the plan is for the wrapper.
* ``data.py`` This will get the data from NASA and read through a configuration text file. It'll make it super easy to get started.
* ``brain.py`` Here's the brains behind the network. Quite simple. Just an image classifier.
* ``run.py`` This is the file which you run. It handles all of the runtime things and executes the pre-trained model for your project.

You should have your own ``brain.py`` and modified ``data.py`` to suit your needs. This isn't meant to do your project for you. It's a template to help you get your data which wraps around the API nicely.

Remember to refer to the custom docs linked above on my GitHub. They show you how to use bowshock. This can be useful when making modifications. The library pyNASA can also be useful, but it doesn't provide access to the latest datasets found [here](https://data.nasa.gov/).

Also please remember that anything you do with artificial intelligence is not just a _pick and choose_ process. It's not a supermarket. Make sure to think about what you're including in your mdoel.

On