
# Fourth Milestone Project by Holly Horwood

[Keto Pantry Website](https://keto-pantry.herokuapp.com)
[![Build Status](https://travis-ci.org/Holly-Horwood/keto_pantry.svg?branch=master)](https://travis-ci.org/Holly-Horwood/keto_pantry)
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
    - [Surface](#Surface) 
- [Wireframes](#Wireframes)     
- [User Story](#UserStory)
- [Technologies Used](#Technologies-Used)    
- [Testing](#Testing)
    - [Automated Testing](#Automated-Testing)
    - [Manual Testing](#Manual-Testing)
- [Future Updates](#Future-Updates) 
- [Deployment](#Deployment)   
- [Credits](#Credits)
	

## **Motivation/Purpose**
This is my fourth milestone project for the Full Stack Software Development course through Code Institute.  I decided to create this website which in the future I plan to link with my previous project [Keto Kitchen](https://keto-pantry.herokuapp.com).  I focused both sites on a Keto/Low Carb lifestyle which is essential for good health among Type 1 diabetics like myself. People with this condition often struggle to find diet appropriate food in this modern world of processed and sugary products, so I have created this site as an easy way for people to find the items they need to make healthy food choices.  In the future when the two sites are blended, I hope to make this a business for myself helping those following this lifestyle to easily find the information and resources they need.

---

## **UX** 

### **_Strategy_**

**Research:**

 Keto and Low Carb are very similar, the main difference is the amount of carbs allowed daily, those eating Low Carb (Low Carbohydrate) will consume usually between 50gm to 100gm of carbs per day whereas a Keto (Ketogenic) diet is stricter, limiting the daily intake to less than 50gm per day to maintain a state of ketosis in the body. 
 
 I consider myself quite knowledgeable in this area as I have lived the low carb lifestyle for many years now. I also created my own low carb Facebook page for diabetics in New Zealand that at the time of writing this has over 1600 members and continues to grow almost daily.  Via my Facebook page I am able to discuss, learn, teach and share ideas, the page was a great inspiration for this project. I intend to eventually extend on this site to include restaurant recommendation for people looking for places to eat that offer low carb friendly options.  My Facebook page alone has already changed so many lives for the better and I see this project as the start of another venture that will continue to help make diabetics lives easier and improve their health along the way.

**Audience:** 

 Anyone with diabetes or anyone following a low carb/keto lifestyle.

### **_Scope_**

**Features:**

**Home Page**

The home/index page shows a navbar at the top of the screen with links to all pages plus a keyword search bar, on the far left is the websites name "Keto Pantry".  The navbar contains the following items when initially visited:
-   Register
-   Login
-   Blog
-   Shop
-   Cart

Unregistered users are able to view the blog page only, in order to shop a user must first register and login, this is by design so that all users are encouraged to register in order to have full access. As the site is used and items are added to the cart a fontawesome shopping cart icon will show next to cart nav item and display the number of items currently in the cart.
The entire container is taken up by a background image and a banner has been added with a 'start shopping' button to encourage users to click and go straight to the shop/products page.  A simple footer is at the bottom of each page with copyright info.

**Authentication Pages**

When visiting the site initially the navbar on the home screen shows two authentication options _Register_ and _Login_.  Users can opt to go to the registration page where they can fill out their user, contact information and create a password.  User that are already registered can simply click on the _Login_ menu option and enter their credentials to login.  Once a user is logged in the menu will change now only showing the option to _Log Out_.  If the logged in users is an _administrator_ of the site they will also have an _Admin_ tab on the navbar to access the backend so that they are able to update the website.  Any time a user logs in or out a message will appear on the screen to confirm the action.  Only logged in users will have the ability to shop on the site.

**Blog Page**

The blog page offers a simple list of responsive posts.  Each post has an image, authors name, views, and published date.  If a post includes a link this can be clicked on and the user is redirected to a separate page to view more information, HTML target="_blank" is used here so that the Keto Pantry page is still open so the user can easily return to it.

**Shop Page**

User must be logged on to access the shop page, if they are not logged in the site will redirect them to the registration page so that they can register if needed, if all ready registered they can click the _sign in_ link to login.  On a smaller device like a mobile phone all products will display vertically one by one and on larger devices they will show as a Bootstrap card-deck side by side up to 6 across at a time. Each card shows an image of the product and below that are the product details, price and input field where the user can select a quantity, clicking the add button will add the product to their shopping cart. On any pages other than the home/index page "Keto Pantry" can be clicked for quick access to the home/index page.
 

**Cart Page**

The cart page shows the users a list 6 columns wide including, image, product name, unit price, quantity, line price, remove.  Any products the user has added to their cart will be displayed and at the bottom the total price is shown as well as a _proceed to checkout_ button.  In the cart area the user is able to increase or decrease the amount of any product or delete them from the cart entirely. Once the user is happy with their order they can click _proceed to checkout_ to purchase.

**Checkout Page**

All products selected for purchase are shown first or on the right on smaller screens as bootstrap cards so that the user can easily see what they are buying.  There is a form that the user must fill out with their details including credit card information to be processed.  Once complete the user can click on submit payment which will then redirect them and show a confirmation message that the purchase was successful.  The order line items are saved in the admin section so that packers would then be able to see what was ordered and gather all items for delivery, the cart after checkout is emptied and a new cart is created so that the user is then able to continue shopping if they wish or shop with a new cart next time they log in. 


### **_Skeleton_**

###### **Wireframes**

Created using [Balsamiq](https://balsamiq.com/) only the main wireframes are shown here, all other pages use Django form templates with some CSS styling.

-   [Index Wireframe](https://ketopantry.s3-ap-southeast-2.amazonaws.com/static/media/Wireframes/MockupIndex.png)
-   [Blog Wireframe](https://ketopantry.s3-ap-southeast-2.amazonaws.com/static/media/Wireframes/MockupBlog.png)
-   [Shop Wireframe](https://ketopantry.s3-ap-southeast-2.amazonaws.com/static/media/Wireframes/MockupProducts.png)
-   [Cart Wireframe](https://ketopantry.s3-ap-southeast-2.amazonaws.com/static/media/Wireframes/MockupCart.png)
-   [Checkout Wireframe](https://ketopantry.s3-ap-southeast-2.amazonaws.com/static/media/Wireframes/MockupCheckout.png)

### **_Surface_** 

I designed this site using modern neutral colours.  Different variations of green are used throughout the site to represent healthy living.  There is a logo and favicon for easy identification of the site.  The navbar is transparent however on scroll it becomes white otherwise the user may get frustrated if they try to click on anything behind the navbar as it won't work.  The bootstrap card deck was used to make it easy to identify individual recipes and where applicable the search container is at the top of the screen so the user can easily search the site.

---


## **User Story**

As a user on the website I want the ability to easily find diet friendly recipe ingredients and food. 

**End user goal:** Find an ingredient or food. 

**End business goal:** Make finding health conscious supplies easier.

**Acceptance criteria:** Able to search the site for ingredients or food and purchase chosen items.

---

## **Technologies Used**

**HTML & HTML5**
- HyperText Markup Language was used to create the structure and layout of the index.html document. 
  
**CSS & CSS3**
- Used to add style to the web page.
  
**Bootstrap**
- Bootstrap was mainly used for positioning with its grid system to position containers. The card deck component was used to house each ingredient.  Bootstrap was also used to create buttons, dropdowns and navbar.

**Javascript**
- Used for integration with Stripe

**JQuery**
- Used for the navbar colour change on scroll.

**Python**
-   Python was used to implement the logic of this project.

**SQLite3**
-   Was used as the database during local development.

**Postgres**
-   Was used as the database once deployed to Heroku.

**Pillow**
-   Used to view images in Django.

**Stripe**
- Payment platform used for eCommerce.

**WhiteNoise**
-   Used to serve static files

**Google Fonts**
-   Montserrat|Roboto fonts used throughout project.


**Travis**
-   Travis was used for continuous integration testing.

**PEP8**
- Used as a guide for correct and consistent Python formatting.


**Heroku**
- Used in the deployment of this application.

**Font Awesome**
- Used for icons on the page such as search icon.

### **Other resources:**

**Stack Overflow**
- Used as a resource to find help with code issues

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

- Click on the following link to access the live site at Github pages [Keto Pantry on GitHub](https://github.com/Holly-Horwood/keto_pantry) or for Heroku [Keto Pantry on Heroku](https://keto-pantry.herokuapp.com/)

**Test Planning:**
  Automated testing was implemented using Djangos [TestCase](https://docs.djangoproject.com/en/2.2/topics/testing/overview/)Test files can be viewed under each app *tests_views.py* and  *tests_forms.py*. All remaining tests were carried out manually by humans.  For the browser testing the users will interact with all pages of the site as well as click on all links and buttons and fill out all forms to observe the results as well as viewing the site on different viewports. 

### **Automated Testing**

**TestCase**
-   TestCase was used for automated testing it uses Pythons standard library unittest.   I built different tests for most of my Python views, forms and models.  All tests created passed.

**Travis**
-   Was used for continuous integration testing, checks all packages are valid and project compiles. Once configured all builds are passing.
[![Build Status](https://travis-ci.org/Holly-Horwood/keto_pantry.svg?branch=master)](https://travis-ci.org/Holly-Horwood/keto_pantry)

**Coverage**
-   Coverage was used to identify any areas that had been missed in my TestCase builds, I could then add any extra tests that were needed.  With the time I had left to finish this project I managed to achieve 70% overall coverage, at a later date I will add more testing to improve on this.

**Lighthouse**
    I also used chromes _Lighthouse_ extension.

> Performance 96%
> Accessibility 91%
> Best practices 86%
> SEO 90%

The highest possible score is 100%

### **Manual Testing**

**Implementation:** 
 Users clicked on all buttons and links and interacted with each page in all possible variations, users also changed screen sizes throughout the process to make sure the site was responsive from as small as 375px.

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

**Home/Index**

- Any errors found via validators were corrected.  The user clicked on registration and filled out the registration form before logging out and back in again to test that login was also working.  The user also clicked on all navbar tabs to ensure each page loaded as expected and clicked on the 'start shopping' button to check it redirected as intended.  All colour and text is consistent, all elements are aligned correctly.

**Blog**

- Any errors found via validators were corrected.  All blogs display as expected and are responsive changing layout as the viewports size is changed.  Posts are linking correctly with database and displaying the correct text, images and working links.  Each link redirects to a separate page using `target="_blank"` All colour and text is consistent, all elements are aligned correctly.

**Shop**

-  Any errors found via validators were corrected.  Page was tested for responsiveness and behaved as expected.  Database is connected and all products are displayed with the correct information.  Adding a product updated the cart as intended. All colour and text is consistent, all elements are aligned correctly.

**Cart**

- Any errors found via validators were corrected. Page was tested for responsiveness and behaved as expected.  Cart displayed all products added during the shop process.  Quantity amend was increased and decreased to check that each item updated correctly which they did.  The Remove button was clicked to delete the line item, this was then checked against the database to ensure the line item was removed entirely which it was.  'Proceed to checkout' was also checked to ensure it redirected correctly and behaved as expected. All colour and text is consistant, all all elements are aligned correctly.

**Checkout**

- Any errors found via validators were corrected. Page was tested for responsiveness and behaved as expected.  The summary was viewed and showed the expected summary and breakdown of each line item and correct total.  The form was filled out using a dummy credit card number to ensure the Stripe payment was processed.  The database was then checked and all cart line items were deleted as expected and the stripe developers website showed that the payment had gone through successfully. All colour and text is consistent, all elements are aligned correctly.

#### **External Testing**

**Responsive**
-   Responsive design testing was done using google chrome dev tools to resize the screen on each page, all pages are responsive as intended.

**W3C Markup & CSS Valiadators**
- Used to check validity of HTML and CSS code used in this project, both returned no errors at completion.  

**JSHint**
- Used to check all JS code for errors, none present on completion of this project.

#### **Issues:**

- Initially Stripe checkout wasn't working and the console complained it was due to an error with the Stripe key.  I spoke with Stripe and it was actually an issue with the cart id which was resolved.

- Due to issues with my own email service provider I was unable to get real email responses to work on the site for authentication purposes.  I have however setup *email backend* in the *settings.py* file for testing.

- It was noticed that the orders had at some point stopped storing the order history in *Admin* this was a case of some code that wasn't replaced after some changes and was quickly rectified.

---

## **Future Updates**

- An additional view to showcase categories making finding items easier.

-   With more time I would add a profile section so that the customer can also look back at their order history, at the moment the order history is saved in the backend so there is a record which can be viewed for the purpose of packing and dispatching the orders.

- More options for the Keyword search bar.

- Shopper product review section.

- Add email configuration for authentication email replies.

-   Add a more customized checkout page with more information about delivery etc.

-   Style Django messages so that they don't push all other content down when they are displayed.

---

## **Deployment**

It's recommended to work within a virtual environment.  Please note that Python 2.7 was used for this project.

To run this project locally you will need the following:

-   IDE I used [Microsoft Visual Studio Code](https://code.visualstudio.com/)
-   [Python](https://www.python.org/downloads/) to run the application
-   [PIP](https://pip.pypa.io/en/stable/installing/) to install all requirements



#### **Running The Code Locally:**

- Go to my repository https://github.com/Holly-Horwood/keto_pantry
- Click on the clone or download button
- In the Clone with HTTPs section, click  to copy the clone URL for my repository.
- Open your environment terminal
- Type `git clone` into the command line and then paste my URL that you copied.
- Press enter and the clone will be created.
-   In the terminal type `cd env/bin` then `. activate` then `cd ../../` to create a virtual environment and return to the app folder

#### **GitHub** 

All coding was committed and pushed to my Github repository at:

https://github.com/Holly-Horwood/keto_pantry


#### **Deploying to Github Once Cloned and Edited** ###

- In your terminal type `git add .` to stage all pending updates
- Type `git commit -m "example massage"` add your own message explaining what you are committing.
- Type `git push -u origin master` to push to my repository


#### **Remote Deployment**

- I created a new app in [Heroku](https://heroku.com) called keto-pantry.
<br>
-   Create a requirements.txt file
     * `pip3 freeze --local > requirements.txt`
<br>
- Add a *Procfile* with the following:

    *   `web: gunicorn keto_pantry.wsgi:application >Procfile`
    *   `release: python manage.py migrate >Procfile`
<br>
-   Go to the [Heroku](https://heroku.com) website to sign up. Create your new project by clicking the *New* button. 
<br>
-   Click on the *Resources* tab and click on *add-ons* and search for *Heroku Postgres*. Select the free Hobby level (this creates a remote database that you will use instead of sqlite3) Back in your IDE you will need to update your env.py file with your new database url.
<br>
-   In the Heroku *Settings* tab click on *the *Reveal Config Vars* to add your environmental variables. 
<br>
- Update your IDE settings.py file to connect to the remote database.  For example: 
    *   `import os`
    *   `import dj_database_url`
    *   `if "DATABASE_URL" in os.environ:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else:
    print("Database URL not found. Using SQLite instead")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }`
<br>
-   Re-build the migrations and create a superuser for your postgres database.
<br>
-   Go to [Amazon AWS](https://aws.amazon.com/) to create an account so that you can host your static and media files. You'll need to create an S3 Bucket, here's a video to help [S3 Tutorial](https://www.youtube.com/watch?v=9HsEMyKrlnw)

- To push your static files to AWS type `python manage.py collectstatic` into your terminal and select *yes* when prompted.

-   Go to [Stripe](https://stripe.com/ie) payment gateway to sign up for a free account. In the `Developers` tab click on API Keys. Here you will find a *publishable key* and *secret key* both will need to be added to your env.py as environment variables so they can then be linked to in the project.
<br>
- You should now be ready for remote deployment.


---

## **Credits**

**Content:**

All content written by Holly Horwood.

**Media:**

-   Images were supplied by Pixabay, Upsplash and Flickr
- Favicon was generated using favicon.io
-   You Tube. JS to change nav colour on scroll - Code courtesy of System 22 I.T. Solutions https://www.youtube.com/watch?v=AM-GT_0Uu5w
-   Google fonts: Roboto and Montserrat
-   Registration and login background photo by Kelly Sikkema on Unsplash

**Acknowledgements:**

Thanks to Sebastian Immel my mentor for all of his help and patience.  Thanks also to the students and staff at Code Institute especially my tutor Dick Vlaanderen.








