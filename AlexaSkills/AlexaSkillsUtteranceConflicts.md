# Alexa Skills: Utterance Conflicts

When creating an Alexa Skill, you create "Utterances" that map to certain intents. Sometimes, you may unintentionally map a single utterance to more than one intent. The developer console has many built-in features to help find these conflicts.

## Types of Conflicts

### Conflict between Two or More Custom Intents

This occurs when an utterance maps to two or more of your own intents. This occurs most commonly when you have the same __sample utterances__ for the intents. This can also occur if there are __slot types__ with duplicate __slot values__.

You don't technically *have* to fix the conflict, since Alexa can resolve the correct intent, but if left unchanged, future edits to the skill *can* change the result, so it's generally in your best interest to make sure the conflict is handled before moving on. If you want to make sure that an utterance *always* resolves to a particular intent, make sure you change your interaction model.

### Conflict between a Built-in and a Custom Intent

Amazon's Alexa has built-in intents. If your utterance is "help," this will conflict with the built-in `AMAZON.HelpIntent`. __Alexa will always prioritize custom intents over the built-in intents,__ so if you personally don't care about the built-in Alexa intents (or if you're building one to replace Alexa's), it's fine to ignore this. However, it's likely that you'll want to keep the built-in ones as-is, and if this is the case, you'll want to pay attention to these conflicts.

### Conflict between a Built-in Intent and Multiple Custom Intents

This type of conflict follows both the rules of the previous two: 

1. Alexa will prioritize the custom intent over the built-in one, so if this is something you don't care about, you can ignore this aspect of your intent.

2. Between the multiple custom intents, Alexa will attempt to resolve the correct custom intent, however, like stated above, if you want to ensure that your intent works how you want, you may want to try to resolve this.

### Conflict Between Built-in Intents Extended by Custom Utterances

If you have extended the Built-in Alexa intents with your own custom utterances that conflict with a built-in intent, this __will affect your skill's accuracy__. It is recommended that you remove the conflicting utterance from the built-in intent. 

## Viewing Your Conflicts

After you build your model, a list of conflicts will be generated and displayed as an alert. (If you don't recieve this alert, it might still be possible you have a conflict, however, it is highly unlikely.) You can see your list of conflicts by going to the __Build__ page and navigating to __Custom > Interaction Model > Utterance Conflicts__.

You will see the following columns:

__Utterance Conflict:__ This displays the utterance and slot values that map to your multiple intents.

__Sample Utterances:__ This will display conflicting sample utterances, with the slots in curly braces ( `{ }` ).

__Intents:__ Displays the intents that map to the utterance conflict. If you click the intent from this page, you will be able to edit it.

__Current Behavior:__ This explains what will happen if you do not change the model and fix the conflict. (Sometimes the current behavior might be acceptable enough that you will choose not to remove it. This can be okay- just make sure you are aware of it!)

## Reworking Your Model

One way to rework your model is to __remove or modify__ the utterance on the intents you do not want returned. You can do this by adding additional words that remove ambiguity.

__Pro:__ This is incredibly simple and quick.

__Con:__ Your utterances may seem less natural, since it's often unnatural for users to add modifiers or clarifying words when their intent can be inferred from context.

You can also __reconsider functionality that introduces intents with ambiguity.__ This will obviously vary significantly depending on your specific skill, but you can probably reimagine what your skills does in a way that keeps the same functionality.

__Pro:__ You will be able to keep natural utterances and can add functionality or modify less-intuitive functionality to your skill.

__Con:__ This takes a lot of time and thought.

You are also able to simply __remove or edit duplicate slot values__ in custom slot types, or __remove or edit utterances that extend built-in intents.__

After making the changes, __rebuild your model__ again and check the Utterance Conflicts page to see if any changes remain.