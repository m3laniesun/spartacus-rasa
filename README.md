# Spartacus - Rasa Integration

### Setting up Rasa - https://rasa.com/docs/rasa/installation/

### Local Mode - https://rasa.com/docs/rasa-x/installation-and-setup/install/local-mode

### Commands - https://rasa.com/docs/rasa/command-line-interface/ 

### Rasa Masterclass - https://www.youtube.com/watch?v=rlAQWbhwqLA&list=PL75e0qA87dlHQny7z43NduZHPo6qd-cRc

This tutorial helped me learn the basics of Rasa. I highly recommend watching this.

## In the user interface directory, yarn must be installed to run the UI. More information can be found in its readme.md 
https://yarnpkg.com/getting-started/install

### Install dependencies 
```yarn install```
### Build chatroom
```
yarn watch
yarn build
yarn serve
```

To train Spartacus on the command line, open the directory where the code is located and run: 
```
rasa train
```

To run the rasa server for the UI, have another command terminal open and run:

```
rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"**
```



## MAIN FILES THAT ARE CHANGED DURING TRAINING


### stories.yml - https://rasa.com/docs/rasa/stories/
When you train the bot, the story serves as the main dialogue flow. 
Under each story, there are steps that indicate pieces of the conversation.
Each story involves an intent and an action (utterance) that follows. 
When you create new intents and utterances, this file allows you to link the two together.
https://rasa.com/docs/rasa/writing-stories/

### rules.yml - https://rasa.com/docs/rasa/rules

This file is similar to stories.yml but rules specify steps that will always follow the same path. 
This file is underdeveloped, as we covered what we need in stories.
As more intents and responses are created, it would be ideal to use this file.

### domain.yml - https://rasa.com/docs/rasa/domain

https://rasa.com/docs/rasa/next/responses
Under responses, we have all of the utterances that Spartacus will say in response to a user intent.
Each response will start with the prefix “utter-”.
Responses can have an image, buttons, and text. 
Sentences should be split up by a new line since the bot will stop reading the text after a certain amount of characters. 

### nlu.yml -  https://rasa.com/docs/rasa/training-data-format
In the nlu file, this is where we specify intents which are possible user messages that will be sent to Spartacus.
Under each intent, examples are specified.

### actions.py - https://www.youtube.com/watch?v=rvHg7N8ux2I
This file handles custom actions that we want Spartacus to do.
Slot and entity code for custom personalized messages is handled here.
Database code will be located here.
