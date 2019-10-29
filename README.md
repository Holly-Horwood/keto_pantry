
# Fourth Milestone Project by Holly Horwood

[Keto Pantry Website](https://keto-pantry.herokuapp.com)

---

## **Disclaimer:** 
This website was designed for educational purposes only for the Code Institute.  All best endeavours have been made to ensure all content has been obtained legally and all good practice guidelines for web development have been followed.

---

## **Table of Contents**

- [Motivation](#Motivation/Purpose)
- [UX](#UX)
	- [Strategy](#Strategy)
    - [Scope](#Scope)
    - [Skeleton](#Skeleton)
        -[Wireframes](#Wireframes:)
    - [Surface](#Surface)
- [User Story](#UserStory)
- [Technologies Used](#Technologies-Used)    
- [Testing](#Testing)
    - [Automated Testing](#Automated-Testing)
    - [Manual Testing](#Manual-Testing)
- [Future Updates](#Future-Updates) 
- [Deployment](#Deployment)   
- [Credits](#Credits)
	

## **Motivation/Purpose**
This is my fourth milestone project for the Full Stack Software Development course through Code Institute.  I decided to create this website which in the future I plan to link with my previous project [Keto Kitchen](https://keto-pantry.herokuapp.com).  I focused both sites on a Keto/Low Carb lifestyle which is essential for good health among Type 1 diabetics like myself. People with this condition often struggle to find diet appropriate food in this modern world of processed and sugary products, so I have created this site as an easy way for people to find the items they need to make healthy food choices.  In the future when the two sites are blended I hope to make this a business for myself helping those following this lifestyle to easily find the information and resources they need.

---

## **UX** 

### **_Strategy_**

**Research:**

 Keto and Low Carb are very similar, the main difference is the amount of carbs allowed daily, those eating Low Carb (Low Carbohydrate) will consume usually between 50gm to 100gm of carbs per day whereas a Keto (Ketogenic) diet is stricter, limiting the daily intake to less than 50gm per day to maintain a state of ketosis in the body. 
 
 I consider myself quite knowledgeable in this area as I have lived the low carb lifestyle for many years now. I also created my own low carb Facebook page for diabetics in New Zealand that at the time of writing this has over 1600 members and continues to grow almost daily.  Via my Facebook page I am able to discuss, learn, teach and share ideas, the page was a great inspiration for this project. I intend to eventually extend on this site to include restaurant recommendation for people looking for places to eat the offer low carb friendly options.  My Facebook page alone has already changed so many lives for the better and I see this project as the start of another venture that will continue to help make diabetics lives easier and improve their health along the way.

**Audience:** 

 Anyone with diabetes or anyone following a low carb/keto lifestyle.

### **_Scope_**

**Features:**

**Home Page**

The home/index page shows a navbar at the top of the screen with links to all pages plus a keyword search bar, on the far left is the websites name "Keto Pantry".  The navbar contains the following items when intially visited:
-   Register
-   Login
-   Blog
-   Shop
-   Cart

As the site is used and items are added to the cart a fontawesome cart icon will show next to cart and display the number of items currently in the cart.
The entire container is taken up by a background image and a banner has been added with a 'start shopping' button to encourage users to click and go straight to the shop/products page.  A simple footer is at the bottom of each page with copyright info.

**Authentication Pages**

When visiting the site initially the navbar on the home screen shows two authentcation options _Register_ and _Login_.  Users can opt to go to the registration page where they can fill out their user, contact information and create a password.  User that are already registered can simply click on the _Login_ menu option and enter their crudentials to login.  Once a user is logged in the menu will change now only showing the option to _Log Out_.  If the logged in users is an _administrator_ of the site they will also have an _Admin_ option on the navbar to access the backend so that they are able to update the website.  Any time a user logs in or out a message will appear on the screen to confirm the action.  Only logged in users will have the ability to shop on the site.

**Blog Page**

The blog page offers a simple list of responsive posts.  Each post has an image, authors name, views, and published date.  If a post includes a link this can be clicked on and the user is redirected to a separate page to view more information, HTML target="_blank" is used here so that the Keto Pantry page is still open so the user can easily return to it.

**Shop Page**

User must be logged on to access the shop page, if they are not logged in the site will redirect them to the registration page so that they can register if needed, if all ready registered they can click the _sign in_ link to login.  On a smaller device like a mobile phone all products will display vertically one by one and on larger devices they will show as a Bootstrap card-deck side by side up to 6 across at a time. Each card shows an image of the product and below that are the product details, price and input field where the user can select a quantity, clicking the add button will add the product to their shopping cart. On any pages other than the home/index page "Keto Pantry" can be clicked for quick access to the home/index page.
 

**Cart Page**

The cart page shows the users a list 6 columns wide including, image, product name, unit price, quantity, line price, remove.  Any products the user has added to their cart will be dispalyed and at the bottom the total price is shown as well as a _proceed to checkout_ button.  In the cart area the user is able to increase or decrease the amount of any product or delete them from the cart entirely. Once the user is happy with their order they can click _proceed to checkout_ to purchase.

**Checkout Page**

All products selected for purchase are shown first or on the right on smaller screens as bootstrap cards so that the user can easily see what they are buying.  There is a form that the user must fill out with their details including credit card information to be proceesed.  Once complete the user can click on submit payment which will then redirect them to a confirmation page. 


### **_Skeleton_**

**Wireframes:**

Created using [Balsamiq](https://balsamiq.com/)

[Keto Pantry Wireframes](https://github.com/Holly-Horwood/keto_pantry/static/media/images/Wireframes)

### **_Surface_** 

I designed this site using modern neutral colours.  Different variations of green are used throughout the site to represent healthy living.  There is a logo and favicon for easy identification of the site.  The navbar is transparent however on scroll it becomes white otherwise the user may get frustrated if they try to click on anything behind the navbar as it wont work.  The bootstrap card deck was used to make it easy to identify individual recipes and where applicable the search container is at the top of the screen so the user can easily search the site.

---


## **User Story**

As a user on the website I want the ability to easily find diet friendly recipe ingrediants and food. 

**End user goal:** Find an ingrediant or food. 

**End business goal:** Make finding health conscious supplies easier.

**Acceptance criteria:** Able to search the site for ingrediants or food and purchase chosen items.

---

## **Technologies Used**

**HTML & HTML5**
- HyperText Markup Language was used to create the structure        and layout of the index.html document. 
  
**CSS & CSS3**
- Used to add style to the web page.
  
**Bootstrap**
- Bootstrap was mainly used for positioning with its grid system to position containers. The card deck component was used to house each recipe.  Bootstrap was also used to create buttons, dropdowns and navbar.

**Javascript**
- ??????????????????????????

**JQuery**
- Used for the navbar colour change on scroll.

**Python**
-   Python was used to implement the logic of this project.

**Pillow**
-   Used to view images in Django.

**Stripe**
- Payment platform used for eCommerce.

**WhiteNoise**

**Google Fonts**
-   Montserrat|Roboto fonts used throughout project.


**Travis**
-   Travis was used for continuous integration testing.

**PEP8**
- Used as a guide for correct and consistant Python formating.


**Heroku**
- Used in the deployment of this application.

**Ratings Widget**
- JS widget used for the star rating of each recipe.
https://rating-widget.com/

**Font Awesome**
- Used for icons on the page such as the footer links and search icon.

### **Other resources:**

**Stack Overflow**
- 

**YouTube**
- Navbar colour change on scroll - Code courtesy of System 22 I.T. Solutions https://www.youtube.com/watch?v=AM-GT_0Uu5w

**W3C Markup & CSS Validators**
- Used to check validity of HTML and CSS code used in this project.

**JSHint**
- Used to check all JS code for errors.

**MDN** 
- Main resource for research and help.

---

## **Testing**

**Running the Code**

- Click on the following link to access the live site at Github pages https://github.com/Holly-Horwood/keto_kitchen or for Heroku https://keto-kitchen-hollyci.herokuapp.com/

**Test Planning:**
  Automated testing was implemented using Pythons [unittest](https://docs.python.org/3/library/unittest.html) and can be viewed in the *test.py* file. All remaining tests were carried out manually by humans.  For the browser testing the users will interact with the map and click on all links and buttons and observe the results as well as viewing the site on different viewports. 

### **Automated Testing**

**Travis**
-   Was used for continuous integration testing, checks all packages are valid and project compiles. Once configured all builds are passing.
[![Build Status](https://travis-ci.org/Holly-Horwood/keto_pantry.svg?branch=master)](https://travis-ci.org/Holly-Horwood/keto_pantry)

**Coverage**

**Lighthouse**
    I also used chromes _Lighthouse_ extension.

> Performance 96%
> Accessibility 91%
> Best practices 86%
> SEO 90%

The highest possible score is 100%

### **Manual Testing**

**Implementation:** 
 Users clicked on all buttons and links and interacted with the recipes in all possible variations, users also changed screen sizes throughout the process to make sure the site was responsive.

**Results:** 
 All buttons and links behaved as expected, and site overall worked as intended.

#### Browser Testing: #### 

**Chrome**

Passed.  No issues were found when used on Chrome.

**Opera**

Passed. No issues were found when used on Opera.

**Firefox**

Passed. No issues were found when used on Firefox.

**Edge**

Passed. No issues were found when used on Edge.

#### **Individual Page Testing:**

**Home**

- Any errors found via validators were corrected.  Several different searches were entered into the search area, when search was clicked the page redirected to the results page as expected and showed any recipes matching the search criteria selected.  The image on the card for each recipe was clicked to ensure this redirected to the correct full recipe, all images behaved as expected.  From the full recipe page the 'recipe' nav item was clicked and that returned the user to the idex.html page again.  All recipes are showing the correct names and details as per the database.  The 'full recipe' card button was also clicked on each recipe to ensure the user would be redirected to the correct page, this worked as expected. The login nav item was also clicked, this links to a non functioning login modal, this will be made functional in the future but for this project is not required to work, the modal behaves as intended at this stage.  All colour and text is consistant, all all elements are aligned correctly.

**Full Recipe**

- Any errors found via validators were corrected.  Each recipe was checked to ensure the layout was as expected which it was.  Clicking on the Keto Kitchen logo on the top left redirects to the home page.  The 'edit' button redirects to the appropriate recipe ID in 'editrecipe.html' and the 'delete' button removes the recipe from the website and database respectively. All colour and text is consistant, all all elements are aligned correctly.

**Edit Recipe & Add Recipe**

-   Both pages are almost identical and any errors found via validators have been corrected.  In both all fields are editable and once the update or add recipe button is clicked the page will save everything to the database and populate the website.  There are some checks in place that ensure all fields are completed so if any are left blank the user is prompted to fill them out before continuing, all areas on this page are working as expected.  The images also have Javascript to check for image sizes before they are uploaded, images will also be previewed so the user can ensure they have selected the correct image for their recipe. Clicking on the Keto Kitchen logo on the top left redirects to the home page. All colour and text is consistant, all all elements are aligned correctly.

**Search Results**

- Any errors found via validators were corrected. The page was tested by searching for several different recipes and ensuring the returned results matched the Mongo database.  All search options appear to be working correctly and returning the expected results.  The search area itself is populated with the original search criteria as expected so the user can see what they originally searched for. Clicking on the Keto Kitchen logo on the top left redirects to the home page. All colour and text is consistant, all all elements are aligned correctly.

#### **External Testing**

**Responsive**
-   Responsive design testing was done using google chrome dev tools to resize the screen on each page, all pages are responsive as intended.

**W3C Markup & CSS Valiadators**
- Used to check validity of HTML and CSS code used in this project, both returned no errors at completion.  W3C did see Jinja as errors even though they were not.

**JSHint**
- Used to check all JS code for errors, none present on completion of this project.

#### **Issues:**

- The preview images for the edit recipe add recipe pages are not working correctly for aspect ration.  In the future some type image size control will be added to handle this problem.

- On edit the image must be added again or it will default to the alt, this will be fixed in a future update.

---

## **Future Updates**

- A functioning modal and user authentication including registration.

- Keyword search bar and more search options.

- User review section and change the current ratings widget to something better.

- Print recipe button.

- Connect to Pinterest.

- Pagination for all sized devices and scroll down arrow for smaller devices.

- Image aspect ratio control for uploaded images.

-   Add in new line functionality for adding and editing recipes.


---

## **Deployment**

This project was created using Visual Studio Code (VSCode).  Preparation for deployment is as follows:

### **Running The Code Locally:**

- Go to my repository https://github.com/Holly-Horwood/keto-kitchen
- Click on the clone or download button
- In the Clone with HTTPs section, click  to copy the clone URL for my repository.
- Open your environment terminal
- Type `git clone` into the command line and then paste my URL that you copied.
- Press enter and the clone will be created.

### **GitHub** ###

All coding was committed and pushed to my Github repository at:

https://github.com/Holly-Horwood/keto-kitchen

It was also published on Github pages at:

https://holly-horwood.github.io/keto-kitchen/

### **Deploying to Github Once Cloned and Edited** ###

- In your terminal type `git add .` to stage all pending updates
- Type `git commit -m "example massage"` add your own message explaining what you are committing.
- Type `git push -u origin master` to push to my repository


### **Heroku**

- I created a new app in heroku called keto-kitchen-hollyci.
<br>
-  In the terminal intiialise a new git repository:
    *    `git init` we want to link the GitHub repo to the app in heroku 
    *   `https://keto-kitchen-hollyci.herokuapp.com/`
<br>
- In VSCode *app.py* set the environment variables for Heroku
    *   ```app.run(host=os.environ.get('IP', '127.0.0.1'),  port=int(os.environ.get('PORT', '8080')),```
<br>
-   Then in *config.py* add:
    *   `MONGO_URI = os.environ.get('MONGO_URI')` 
<br>
- Go back to *Heroku* and in the project under *settings* and *config vars* add: 
    *   `IP = '0.0.0.0'`
    *   `PORT = 5000`
    *   `MONGO_URI = mongodb+srv://nz_user:password@myfirstcluster-clbrq.mongodb.net/keto_kitchen?retryWrites=true&w=majority`
<br>
- Add a *Procfile* with the following:

    *   `echo web: python run.py >Procfile`
    * In the Procfile add `web: python app.py -p $PORT`  *this is how Heroku runs the application*
    * `heroku ps:scale web=1` *This will start the app once it has deployed*

<br>

- Push to Github:
  * In terminal type `git add .`
  * `git commit -m "add a meaningful message here"`
  * `git push -u origin master`
  * enter username:
  * enter password:
<br>
- In Heroku go to the *deploy* tab

- Scroll down to *manual deploy* and select *deploy branch*

- After build is successful go back up and select to *auto deploy*

- Finally login to *Travis* to check testing is still working


---

## **Credits**

**Content:**

All content written by Holly Horwood.

**Media:**

-   Most images were supplied by Pixabay and Flickr
- All other images supplied by Holly Horwood
- Favicon was generated using favicon.io
-   You Tube. JS to change nav colour on scroll - Code courtesy of System 22 I.T. Solutions https://www.youtube.com/watch?v=AM-GT_0Uu5w
-   Google fonts: Roboto and Montserrat
-   Registration and login background photo by Kelly Sikkema on Unsplash

**Acknowledgements:**

Thanks to Sebastian Immel my mentor for all of his help and patience.  Thanks also to the students and staff at Code Institute especially my tutors Sebastian and Dick.





Star ratings app from rating widget https://rating-widget.com/get/rating/javascript/#editor


