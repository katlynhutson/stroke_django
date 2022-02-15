# Planning

## 02/15

- create another model to hold generic data from people who do not want to create an account
- edit the permissions for both models
- deploy this to heroku

### Project idea

> A first-responder tool to help identify potential strokes, record valuable information at the time of the neurological event, and lessen the burden of memory on civilian first responders. It’s a tool you can turn to if a loved one is behaving strangely, and you need to determine if you should call an ambulance for a possible stroke. The most important piece of information that needs to be gathered for stroke victims is the time of first symptoms. Time since symptom onset decides the potential treatment options. The longer it’s been the less options available and the more brain damage that is incurred. This app is a way of having some pieces of that puzzle without putting the burden on the loved one to remember protocol during an extremely stressful event.

### Tech stack

#### Backend

- Django

#### Database

- PostgreSQL

### Backend models and their properties

#### User

- id
- email
- username
- password

#### Form

- id
- owner
- facial_symptoms
- facial_notes
- arm_symptoms
- arm_notes
- speech_symptoms
- speech_notes
- user_time
- form_time
- additional_notes

### User stories

#### MVP

- As a user I want to be able to , so that .
- As a user I want to be able to access a stroke questionnaire, so that I can recognize a stroke in myself or others..
- As a user I want to be able to record answers to the stroke questionnaire, so that I have a detailed record of symptoms to show the doctors in the ER.
- As a user I want to be able to create an account, so that I have the option/ability to view previous event notes in follow up care visits. .
- As a user I want to be able to see my form response notes on a finished screen, so that I can just screenshot the response answers if the account creation feels like a hindrance or unnecessary.
- As a user I want to be able to see an about page that explains strokes and the background of the app, so that I can learn more about strokes, and have reassurance for the validity of the app.
- As a user I want to be able to only see event logs associated with my username if I’m logged in, so that my privacy and event history is protected.

#### Stretch

- As a user I want to be able to see the time I started the form, so that I do not have to rely on just myself to record important information.
- As a user I want to be able to Update and Destroy old event logs, so that I have agency over my personal information and can add notes to the log if I remember something important later that I didn’t think to write down.
- As a user I want the ability to edit my account information or delete my account, so that I can still access information if I forget the password or delete my account if necessary.
