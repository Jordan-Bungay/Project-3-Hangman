# Hangman Game

I have created this Hangman game to show my ability to work with Python.

Hangman is a game where you have to find the hidden word by trying different letters one-by-one to eventually uncover the whole word. Each correct letter will reveal part of the word and each incorrect answer will add a part to the hangman picture, 6 incorrect guesses and you lose.

![Preview for the website on different screen sizes](assets/readme-assets/project-2-display.png)

### The live website can be seen by clicking [here](https://jordan-bungay.github.io/Project-2-Rock-Paper-Scissors/)

## UX

I want this game to be a fun introduction to the rock, paper and scissors game, showing you how its played through a fun interactive way. I want the user to enjoy learning the game through the exciring text and fun buttons to press.

## User stories

The goal of this game is to get people interested in how to play this game and enjoy playing rock, paper and scissors. The following points are from my user point of view:

* As a user, I want to learn how to play this game.
* As a user, I want to be able to play Rock, Paper and Scissors.
* As a user, I want to be able to play the game without any issues.
* As a user, I want to play a fun insteractive version of the game.

## Strategy

I want the game to be easy to pick up and play and to teach the player how to play Rock, Paper and scissors. I want the player to enjoy playing the game.

## Scope

I want the users to experience the game of rock,paper and scissors while also seeing my skills in creating code in javascript. I want the user to enjoy playing the game while learning it without it being too complex but enough to know how to play by the end.

## Structure

The structure of this game is to not be a lot of content to have to navigate through with everything being on one page. There is the button for the instructions you can toggle to show you how to play.

## Skeleton

I designed the website to be simple but show case all the relevant information and pictures required to get the users interested and to play the game.

**Wireframe**

I used Figma to create my wireframe for my website. The wireframe shows the very basic structure of what I saw in my head and gave guidence in to how i wanted my website structured.

You can view the screenshots from my wireframe from clicking the following:

[Click me](assets/readme-assets/Project-2-Wireframe.png)

## Surface

The Colors I have used in the website are used to match the theme of the images, and matches the main colors seen in the game. The colors I chose worked well together and gave a more exciting feel to the game.

### Color palette used

![Color palette used](assets/readme-assets/Project-2-colour-palette.png)

## Technologies

* I have used HTML for the main page structure, images and text content.
* I have used CSS for the styling and positioning of all the HTML content.
* I have used JS for the functionality of the game and making it playable.
* I have used Figma for the wireframe plan of my website.

## Features

**Title and Instructions**

* This section features the title of the game and the button for the instructions.
* When you click on the instructions button it will bring up a modal with the content on how to play.
  
![Title and Instructions button](assets/readme-assets/Instructions-button.png)
![Instructions content](assets/readme-assets/Instructions-how-to-play.png)

**Player options**

* This section shows the players options: Rock, Paper and Scissors.
* This part is interactive it allows you to click on the images to choose your option.

![Player Options](assets/readme-assets/Player-options.png)

**Round outcome**

* This section will display text of the outcome of the battle.
* It will show what you chose vs what the computer chose.
* It will then tell you if you won, lost or if it was a draw.

![Round Outcome](assets/readme-assets/Round-outcome.png)

**Score tally**

* This section keeps track of when you win, lose or draw with the computer.
* It will update the tally when each round is decided.

![Score tally](assets/readme-assets/Score-Tally.png)

**Entertainment images**

* This section just showcases some images for the users entertainment and give a bit of character to the page.

![Entertainment images](assets/readme-assets/Entertainment-images.png)

**End result**

* This is showing the whole page of everything working together.

![End result](assets/readme-assets/Finished-product.png)

## Testing

* I tested the site, and it works in different web browsers Chrome, Firefox, and Microsoft Edge.
* On mobile devices, I tested my site on a iPhone 12 with the Safari browser.
* I confirmed that the site is responsive and functions on different screen sizes using the devtools device toolbar.
* I confirmed that all the buttons works, they activate what is supposed to happen when clicked.

## Validator Testing

**HTML**
  
  No errors were found when passing through the official [W3C validator](assets/readme-assets/html-validator.png)

**CSS**
  
  No errors were found when passing through the official [(Jigsaw) validator](assets/readme-assets/css-validator.png)

**JS**

  No errors were found when passing through the official [Jshint validator](assets/readme-assets/jshint-validator.png)
  
**Accessibility**
  
  I confirmed that the colors and fonts chosen are easy to read and accessible by running it through [Lighthouse DevTools](assets/readme-assets/project-2-lighthouse.png)

## Bugs

A bug I encountered when making the JS was when creating the score tally section it wasn't updating the draw tally, so I had to trial and error and eventually figured out why it wasn't working and managed to fix it. The rule in the function wasn't in the correct place therefor the function wasn't able to see it.

## Deployment

I used the following steps to deploy my project:

* Go to my Github repository.
* Click on the settings tab.
* Under General, go to Code and Automation and select 'Pages'.
* In the Build and Deployment section for Source, select 'Deploy from a branch' from the drop-down list.
* For Branch, select 'main' from the drop-down list and Save.
* On the top of the page, the link to the complete website is provided.

## Credit

### Pictures

* icon used are from "https://fontawesome.com/"
* rock-paper-scissors-battle-1 taken from "https://memebase.cheezburger.com/verydemotivational/tag/rock-paper-scissors"
* rock-paper-scissors-battle-2 taken from "https://www.pinterest.co.uk/pin/237987161528881940/"
* rock-paper-scissors-battle-buttons taken from "https://www.freepik.com/premium-vector/character-design-from-game-rock-paper-scissors_69112068.htm"
* battle icons image taken from "https://www.flaticon.com/free-icon/battle_3522092"

### Content

* Some of the code for the JS was taken from the [Love Maths project]
* Some of the Code for the JS was taken from [RobertAhli rps-project2b]

### Acknowledgements

* Inspiration is from [RobertAhli rps-project2b].
* Ideas were taken from the Code Institute's Love Maths project.
* The the Code Institute tutor support team for helping me with the correct guidance.
* My mentor, Medale Oluwafemi, for his invaluable guidance.
