Hey All!

This GitHub Repository contains the final completed project that was assigned to me for SportsHi's intern screening process.

In order to test this implementation without any difficulty, I have listed some easy steps to follow in order to make the testing process really simple.

1) Clone this repository in order to have full access to the django application.
2) I used Postman in order to make requests to my API so the steps following this will illustrate how to make requests                        using said API Development tool. If you haven't already downloaded Postman, here's a link (https://www.getpostman.com/downloads/) to do so for your respective platform. However, feel free to use whichever medium you are most      comfortable with in order to make requests to the API.
3) Once you have downloaded Postman successfully, proceed to launch it and then you'll be prompted to create an account. Once that is successfully completed, you will be guided to the LaunchPad section of Postman. 
4) Next to the tab that says LaunchPad, there will be a plus icon to add a new tab. Click on it and it will open up an untitled request tab.
5) In this tab, you will see a search bar where you can enter a request URL. That URL should be http://0.0.0.0:8000/notes 
6) It is automatically set to send a GET request first so we'll start with that which is simple. Just click the blue SEND button and you will receive a JSON response with the contents of the API, with the most recent on top.
7) Next, we'll send a POST request which takes a couple more steps. First, we need to go to the dropdown menu which is occupied by GET at the moment and change it to POST.
8) You will see a menu bar under the URL containing the sections "Params", "Authorization", and so on. In this menu bar, you will find the Body section, that's what we need to modify so go ahead and select it.
9) You'll see another set of options but select "raw" because that is where we will specify what we want to post. Also change TEXT to JSON in the dropdown menu.
10) This will introduce you to an empty editor where you should enter the following parameters exactly as shown below:
              {
                 "id": "YOUR ID NUMBER HERE",
                 "note_content": "THE CONTENTS OF YOUR NOTE HERE"
              }
11) Once you fill in your id and your message, we are ready to send the POST request.
12) If all goes well, you will receive a "Status: 200 OK" which means that your POST request was successful.
13) Finally, send another GET request to ensure that your note has been added to the API.
          

Please feel free to email me at rahuljoseph246@gmail.com if you have any questions!

Thank you again for this opportunity! I look forward to hopefully being selected to work with SportsHi as an intern!
