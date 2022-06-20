# NASA Satelite Imagery Wrapper

<p align="center"> 
<img src="https://www.festisite.com/static/partylogo/img/logos/nasa.png">
</p>

## Documentation
Please refer to my [in-depth guide and introduction to these APIs](docs-tutorials/). This is an extensive guide to using the API wrapper and will guide you through a sample project. Should you have any additional questions, feel free to contact me through e-mail.

## Outline
* ``data.py`` This will get the data from NASA and read through a configuration text file. It'll make it super easy to get started.
* ``brain.py`` Here's the brains behind the network. Quite simple. Just an image classifier.
* ``run.py`` This is the file which you run. It handles all of the runtime things and executes the pre-trained model for your project.

You should have your own ``brain.py`` and modified ``data.py`` to suit your needs. This isn't meant to do your project for you. It's a template to help you get your data which wraps around the API nicely.

## Notes for Participants in TeensInAI Hackathon 
Remember to refer to the custom docs linked above on my GitHub. They show you how to use bowshock. This can be useful when making modifications. The library pyNASA can also be useful, but it doesn't provide access to the latest datasets found [here](https://data.nasa.gov/).
