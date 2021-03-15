# Alexa Skills: Making API Requests
## Overview
### What You'll Learn

In this section you will learn:

1. How to integrate API requests into your Alexa Skills

### Prerequisites

1. [Dialogue](https://github.com/HackBinghamton/CloudComputingWorkshop/blob/master/AlexaSkills/Dialogue.md#dialogue)

### Introduction

So you have a great idea for an Alexa Skill, but realized that you will probably need to use an API to make it happen. 

In order to do this, you need to make an __HTTP Request__ to an API. 

An HTTP request allows you to get data from a remote source. This includes APIs, websites, and other similar things. (To learn more about HTTP requests, there are links at the bottom of the page.)

Most modern languages have HTTP requests as a core functionality. For this workshop, we'll be going over it in Python3, which has a "Requests" library. 

## Our Example API

For this workshop, we'll be using the "Numbers API," which can be found at http://numbersapi.com/

If you go to the site, you can see that they have generated lists of trivia about numbers from a general trivia perspective, a mathematical perspective, and a date/time-based perspective.

If you would like to find other simple (or not so simple) APIs to try this workshop's content on later, some good sources for searching for API's are listed at the bottom of the page!

If you'd like to know more about APIs and working with them, definitely check out our [Webscraping and APIs workshop](https://github.com/HackBinghamton/Webscraping-APIsWorkshop)!

## Voice Interaction

Here is a simple interaction that might occur between the user and their Alexa:


*__User:__ Alexa, ask number facts to give me a fact about seven.*

*__Alexa:__ Seven is the number of main stars in the constellations of the Big Dipper and Orion.*

When __User__ says, *“give me a fact about seven”*, __GetNumberFactIntent__ gets called and the number slot in the API is set to ‘7’. Our skill code makes an __HTTP get request__ to numbersapi.com to get a random fact about the number ‘7’. The GET method is used to retrieve information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data (tutorialspoint).

## Making the Request

Now we'll be going through the code you should use in order to actually use the API in your Alexa Skill (Code snippets are from the Amazon Alexa Skills Kit).

Without using an API, you would have had to "hard-code" every one of the number facts. (Hard-coding refers to putting something directly into your source code rather than from an external source.) Here's what that might have looked like:

```python
number_facts = {
    "1": "is the number of moons orbiting the earth.",
    "2": "is the number of stars in a binary star system (a stellar system consisting of two stars orbiting around their center of mass).",
    "3": "is the number of consecutive successful attempts in a hat trick in sports.",
    "4": "is the number of movements in a symphony.",
    "5": "is the number of basic tastes (sweet, salty, sour, bitter, and umami).",
    "6": "is the number of fundamental flight instruments lumped together on a cockpit display.",
    "7": "is the number of main stars in the constellations of the Big Dipper and Orion.",
    "8": "is the number of bits in a byte.",
    "9": "is the number of innings in a regulation, non-tied game of baseball.",
    "10": "is the number of hydrogen atoms in butane, a hydrocarbon.",
    "11": "is the number of players in a football team."
}
```

If a user asked Alexa to "ask number facts to give me a fact about 7," we would have had to pass 7 to __number_facts__ to find the fact, as shown:

```python
number_facts["7"]
```

This is how we would "look up" the fact for our chosen number.

__Look Up:__

```python
the_number = handlerInput.requestEnvelope.request.intent.slots.number.value
the_fact = number_facts[the_number]
```

Here's the "GetNumberFactHandler" function __before__ we edit it to include our API.

__Handler (Before Updates):__


```python
class GetNumberFactHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("GetNumberFactIntent")(handler_input))
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNumberFactHandler")
        # to enable randint, add "from random import randint" at start of file
        the_number = None
        if is_request_type("IntentRequest")(handler_input):
            the_number = handler_input.request_envelope.request.intent.slots["number"].value
        if the_number is None:
            the_number = str(randint(1,11))
        the_fact = the_number + " " + number_facts[the_number]
        speech = the_number + " " + the_fact + " Would you like to hear another fact?"
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response
```

Hopefully the handler looks somewhat familiar to you if you completed the previous tutorials. This particular snippet is accessing the __number__ slot and looking up the fact using the __number_facts__ object. It's then having the skill state the fact out loud to the user as a response using the __response_builder__.


As you can imagine, this would be terribly limiting (or just terribly inefficient, depending on how much time you want to spend) since you would have to hard code every single number/date/etc. the user could ask for. More than likely, you would get tired of this before creating a substantial amount of number facts. 

To avoid this, we're going to use our "Number Facts" API. Here's how we would do it for the number 7 using the Python "Requests" library:

__Include the Requests library in your skill:__

```python
import requests
```

__Call "requests.get" from inside the intent(GetNumberFactIntent). This will send a query to the API, and return a result.__


```python
class GetNumberFactHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("GetNumberFactIntent")(handler_input))
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNumberFactHandler")
        the_number = None
        if is_request_type("IntentRequest")(handler_input):
            the_number = handler_input.request_envelope.request.intent.slots["number"].value
        if the_number is None:
            the_number = str(randint(1,11))
        url = "http://numbersapi.com/" + the_number
        response = requests.get(url)
        if response.status_code == 200:
            the_fact = response.text
        else:
            the_fact = "I had trouble getting a fact about " + the_number + ".";
        speech = the_fact + " Would you like to hear another fact?"
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response
```

As you can see, the handler includes the URL and the number, gets a response, and returns it. (It also includes an "else" statement in the case of an error, or the website being unable to return a fact at that time.)

This is the general process for accessing an API for your Alexa Skill. Although the specifics will vary significantly depending on what API you are trying to use and what data you're trying to get from it, the general process is the same:

1. Setting up the voice interaction

1. Importing the requests library

1. Modifying the event handler to make a "get request" from the API's URL

1. Retrieving the desired data

1. Building and delivering the response

Steps 3 and 4 is where you'll have the most variation depending on the API, but many professional ones will also have resources to help you along.

Hopefully you found this workshop useful and are able to implement APIs into your future Alexa Skills!

## Helpful Links

#### HTTP requests: 
 - https://www.codecademy.com/articles/http-requests
 - https://www.tutorialspoint.com/http/http_requests.htm

#### API Sources:
 - "A collective list of free APIs for use in software and web development:" https://github.com/public-apis/public-apis
 - "The Largest API Directory on the Web:" https://www.programmableweb.com/apis/directory
 - A categorized list of (non-professional but often high-quality) APIs: https://apilist.fun/





