# Dialogue
## Overview
**What you'll learn**

 1. Alexa dialogue terms
 2. How to plan your dialogue
 3. Tips for making utterances

**Prerequisites**

 1. None

**Introduction**
A huge part of Alexa skills is the conversation between Alexa and the user. This section will help you prepare your skill to have smooth conversations and be able to handle different responses from the user.
## Dialogue terms
First off let's review some terms that will be important in this section. The Amazon documentation we sent you to to build a basic Alexa skill briefly touched on intents, slots and utterances. Here's a refresher on that. An **intent** is the action you want Alexa to perform. A **slot** is a key piece of information needed to complete the intent. An **utterance** is a response outlined so that Alexa can utilize the information spoken to her. A user friendly Alexa skill should be equipped with many utterances to handle the different ways people might respond to her.

For example, you might want to know if it's going to rain today. You might ask Alexa

 - Alexa, is it supposed to rain today?
 - Alexa, is it going to precipitate today?
 - Alexa, is it going to be wet outside today?
 - Alexa, do I need an umbrella today?

Each of these utterances is mapped to the same intent, which is to give the chance of rain for today.

## Invoking your skill
Each Alexa skill has an **invocation name**. This is like clicking on an app to open it, but instead you are saying the skill's name. Different utterances can invoke an Alexa skill. For example, "Alexa, ask web m. d. what to do for a burn." and "Alexa, tell me what to do for a burn using web m. d." both invoke the WebMD skill using its invocation name, "Web m. d.".

Your skill should have an invocation name. Think about whether you want to invoke the skill with intent (like the WebMD example above), without intent (ex. "Alexa, open web m. d."), or have both options. Invoking a skill with intent is called a **one-shot utterance** since you are not having a full conversation with Alexa to get the answer you want. If you want to invoke the skill with intent, you need to think about the different ways the invocation name might be used in an utterance. Invocation without intent leads to **in-skill utterances**, which are more conversational.

## Planning dialogue
A key feature for smart assistant enabled devices is that they can converse with the user. We want this conversation to go smoothly. Before even starting to make your Alexa skill, you should plan the entire conversation your skill will hold with the user. Mapping out possible routes the conversation could go will ensure that you know all the intents and slots needed for the skill.

Once you have the possible conversations mapped out, look at every time the user speaks. Since we are interacting via voice, the user can respond with literally anything (hopefully it's relevant!). For example, if Alexa asks a yes or no question, the user could simply say "yes", or they might say "yup", "sure", "indeed", "alright", "absolutely", etc. Now that we know all the points in the conversation where the user is speaking, we need to come up with a list of possible responses for each time.

Once we have a list of the possible responses, we want to format the utterances correctly. Anytime there is a slot being used, wrap the name of the slot in curly brackets. This signals that the words spoken at this point in the response are important to fulfilling the intent of this request.

Here's a list of properly formatted utterances to the question, "What is your full name?"

 - {firstName} {lastName}
 - {firstName}
 - my full name is {firstName} {lastName}
 - my name is {firstName}
 - my name is {firstName} {lastName}
 - i'm {firstName} {lastName}
 - i'm {firstName}

In this example, sometimes the user doesn't tell us their full name. The Alexa skill should be able to handle this and ask for the missing information.

## Things to keep in mind
Here's a short list of things to remember while coming up with utterances:

 - Numbers should be written out instead of using digits.
 - Do not use punctuation unless it is for
 -- Abbreviations (instead of "CS", write "c. s.")
 -- Possession or contraction ("steven moore's", "i'll")
 -- Internal hyphens ("long-term")
 - You can make custom slots to decrease the number of utterances you have to write. If you find yourself writing utterances repeatedly, but interchanging one word every time, you can make a custom slot for those interchangeable words.
 - Don't forget to make lists of utterances for both in-skill and one-shot situations.

## Exercise
List 5 possible utterances for the question, "What is your favorite food?". Here's one to start you off: My favorite food is {food}. 
