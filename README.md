# |Aquaria Supplies

**[Live site](https://aquaria-supplies.herokuapp.com/)**

---

<span id="top"></span>

## Index

- <a href="#context">Context</a>
- <a href="#ux">UX</a>
  - <a href="#ux-iud">Ideal User Demographic</a>
  - <a href="#ux-stories">User stories / Strategy</a>
  - <a href="#ux-structure">Structure</a>
  - <a href="#ux-wireframes">Wireframes</a>
  - <a href="#ux-design">Design</a>
- <a href="#features">Features</a>
  - <a href="#features-existing">Existing Features</a>
  - <a href="#features-future">Still to implement</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
  - <a href="#testing-stories">User Stories</a>
  - <a href="#testing-manual">Manual Testing</a>
  - <a href="#testing-automated">Automated Testing</a>
  - <a href="#testing-bugs">Known bugs</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

---

<span id="context"></span>

# **Context**

Aquaria Supplies is an online and physical shop located in Dublin 12. They supply the most popular branded products for all fish and corals, be it freshwater or saltwater. They sell anything you would ever need and also provide help with equipment and tank setups.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="ux"></span>

# **UX**

## **Ideal User Demographic**

<span id="ux-iud"></span>

The ideal users of this website are:
- Fish and Coral hobbyists
- People looking to get into coral/fish

**Strategy** was broken into three categories.
  - Roles
    - Site User
    - Site Admins
  - Demographic
    - Young to mature adults
    - Gifts givers

The website needs to enable the **Site User** to
- Find products that are required to start or upgrade their current aquariums.
- Add their desired products to cart where they can purchase them.
- Filter products throughout the site accordingly to **Users** needs.
- Search products by name, sku or description.
- Modify profile to save their default shipping details and preview past orders.

The website needs to enable the **Site Admin** to
- Add, edit and remove products on the site.
- View placed orders from admin dashboard.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="ux-stories"></span>

## **User stories / Strategy**

The below MOSCOW table consists of user stories with story points and MOSCOW principles. All of the stories in the table below are what I believe I needed in order to produce a good user friendly e-commerce store. I completed all of them within timeframe. Each user story was tested and they can be found HERE.

|User Story Testing                                                     |AS   |I WANT TO BE ABLE TO…                                                 |SO THAT I CAN…                                                                                                      |Story Points|MOSCOW     |
|------------------------------------------------------------------|----------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|------------|-----------|
|                                                                                                        1                                                                 |Shopper   |View a list of products                                               |Purchase them                                                                                             |5           |Must Have  |
|2                                                                 |Shopper   |Access products                                  |Preview them and find out more details                           |4           |Should Have |
|3                                                                 |Shopper   |Search for products                                       |Find specific product I am looking for                                |3           |Could Have  |
|4                                                                 |Shopper   |Select products categories                 |See products that interest me the most                                         |5           |Should Have |
|5                                                                 |Shopper   |View the total of all products in my cart    |I can avoid spending too much                                    |5           |Must Have |
|6                                                                 |Shopper   |Increase or decrease product quantities            |Avoid buying too many or buy more if I want to                                                  |3           |Could Have |
|7                                                                 |Shopper   |Remove products from my cart                 |I can avoid buying products I have added to my cart as an accident                                                                                            |5           |Must Have         
|8                                                                 |Shopper |See alert messages                                        |Know of any issues I am currently experiencing                                                              |4           |Could Have  |
|9                                                                 |Shopper |Use Stripe as my payment method                                                  |Safely proceed with checkout                                                                          |5           |Must Have  |
|10                                                                |Site User |Register an account                        |Preview my previous orders and edit my default shipping details                                                                                        |4           |Must Have  |
|11                                                                |Site User |Login or logout                       |Access my personal information                                                              |5           |Must Have  |
|12                                                                |Site User |Request new password in case I lose it                                        |Recover my account                                        |3           |Should Have|
|13                                                                |Site User |Edit a form             |Update my profile details                                    |2           |Should Have|
|14                                                                |Site User |Access my profile                                      |Preview my past orders                              |4           |Should Have|
|15                                                                |Site User |Receive an email after registeration                                   |Verify my account                                       |3           |Could Have|
|16                                                                |Admin  |Add products                                  |Add new products  |5           |Must Have|
|17                                                                |Admin   |Edit products                   |Update existing information |4           |Should Have|
|18                                                                |Admin   |Delete product                           |Remove products that are no longer for sale.                                                                        |4           |Should HaveHave|
|                                                                  |          |                                                                      |Total Story Points                                                                                                  |73         |           |

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

## **Structure**

<span id="ux-structure"></span>



## **Wireframes**

<span id="ux-wireframes"></span>

The wireframes were successfully converted into a live functioning website across all devices.

The full suite of wireframes for **desktop**, **tablet** and **mobile** devices, can be accessed [here](wireframes/).

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

## **Design**

<span id="ux-design"></span>

### **Colour Scheme**

After looking through different e-commerce shops related to fish/corals, I concluded that the best color scheme would be a simple **plain white background with blue accents**. The below is the colours I have used the most.

![Coolors](docs/aquaria-supplies-coolors.png)

### **Typography**

For fonts I decided to go with something that is simple and elegant. The fonts are as follows, Lato and Sans-serif. I think it gives site nice and clear look and ease of readability.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="features"></span>

# Features

## Existing Features

<span id="features-existing"></span>

### **Every page consits of top navigation bar with consitent and responsive design.**

**Navigation Bar**

- The top navigation bar contains a site logo which brings user back to index page. A search bar to search throughout all products with auto complete popups and account management buttons such as log in, log out, register and my profile.
- There is a sticky bar containing information regarding of how much needs to be spend to get free shipping.
- There is a navigation throughout all the categories. Some categories are dropdowns and you can also sort all products by price or category.
- There is also contact details including phone number and opening hours.

![Top Nav](docs/features/top-nav.png)
![Search](docs/features/search-bar.png)

**Footer**

- Footer is divided into two sections, social and newsletter.
- Social brings you directly to facebook page whereas newsletter lets you subscribe to newsletter to get notified of latest offers.

![Footer](docs/features/footer.png)

**Home Page**

- List of products sorted in order of newest being first.
- Every product preview consists of product image, category, name and price.
- If user is an admin then option for deleting/editing product is also available under each product.

![Home Page](docs/features/index.png)

**Products / Category Page**

- List of all products or sorted by categories.
- Sort by button which lets user sort all products on current page by category, name and price.
- Top of page is treated as breadcrumbs with current category chosen.
- Top left corner of page gives user product count in current selected category and a link to preview all products.
- Every product preview consists of product image, category, name and price.
- If user is an admin then option for deleting/editing product is also available under each product.

![Products](docs/features/products.png)

**Products Detail Page**

- Product detail page contains all information regarding the product.
- The image, name, price, sku, short description, quantity and main description are visible to the user if they were added in the backend for given product.
- Users can change quantity of the product before they add it to the cart

![Products Details](docs/features/products-details.png)

**Shopping Cart**

- List of all products that were added by the user.
- Abilit to update quantity in the cart as well as removing the product.
- The subtotal for each product, subtotal of the cart and then total including the delivery is given to the user.
- Buttons to either proceed to the payment page or go back to shop.

![Cart](docs/features/cart.png)

**Checkout Page**

- Form for user to input their details including delivery address and payment field for debit/credit card.
- Order summary including total quantity of products in cart.
- Each product and their current quantity and subtotal.
- The order total before and after delivery charges have been applied.
- Buttons to either complete the order or go back to the cart to adjust it.

![Checkout Page](docs/features/checkout.png)

**Checkout Success Page**

- Order information that will be sent to given email.
- Details of the order including users address, order number, date and the totals.
- Button to go back shopping.

![Checkout Success Page](docs/features/checkout-success.png)

**User Profile**

- Form for user to input and save their details such as delivery address and their name.
- Button to submit and update users details.
- Order history with order number linked to order success page as above. The date, products and the total.

![Profile](docs/features/profile.png)

**Add/Edit Products**

- Form for admin to input new product details.
- Fields for name, description and price are required. Additional fields such as short description, image or sku are optional but recommended.
- Two additional SEO fields, keywords and descriptions for admins to add per each product as desired.
- Button to either add or update existing product.
- If the form is to edit product then all fields will be prepopulated.

![Add/Edit Products 1](docs/features/add-product-1.png)
![Add/Edit Products 2](docs/features/add-product-2.png)

**Alert Messages**

- Users will get alerted by pop up messages depending on their actions.
- Message pop up are generated as either successful, warning, error and info messages.

![Success Message](docs/features/success-message.png)

**Deleting Products**

- If user is an admin, on each product there will be two additional link buttons for editing and deleting products.
- Once user presses delete, the product gets automatically removed from the shop.

**Account Management**

- Login, logout, registeration and all other options such as account recovery, email confirmation etc. all work via Allauth.
- Users need to confirm their accounts before accessing the store.

## **Features still to implement**

<span id="features-future"></span>

- Add more user control over their own accounts such as changing their passwords.
- Add more details to search auto complete such as product image and the price.
- From the search bar, when click on a product, bring user to the products page.
- Add product variations so each variation will have different sizes depending on bottle/bucket size.
- Add product stock so users are able to find out if the products they are purchasing are in stock.
- Slugs for each product for better SEO.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

# Technologies

<span id="technologies"></span>

### **Main Languages Used**
- HTML5
- CSS
- Python
- JavaScript
- jQuery

### **Frameworks, Libraries and Programs Used**
- Django
- Heroku
- PostgreSQL
- Bootstrap
- Amazon Web Services for static and media files.
- Fontawesome
- Crispy Forms
- Pillow
- Stripe
- Psycopg2
- DJ-database-url
- Boto3
- GitHub
- GitPod

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

# Testing

## User Stories

<span id="testing-stories"></span>

- As a **Shopper** I want to be able to view a list of products so that I can purchase them.
  - To test this shopper story I have created products through importing data via CLI. I then accessed the website to see if all imported products will be visible.
- As a **Shopper** I want to be able to access products so that I can preview them and find out more details.
  - To test this shopper story I have opened open one of my products to see if it will bring me to the products page. I then was able to see each information that I wanted to be able to see in nice and clean way.
- As a **Shopper** I want to be able to search for products so that I can find specific product I am looking for.
  - To test this shopper story I clicked on search bar and I wrote down a product name. I was then given results as a pop up (autocomplete). I then pressed either 'Enter' or search button and all the results were displayed containing my keywords.
- As a **Shopper** I want to be able to select products categories so that I can see prodcuts that interest me the most.
  - To test this shopper story I have clicked on one of the categories in the nav bar section of the page. It then brought me to a category page with products visible for given category.
  - Some of these are categories are accessible as dropdowns so I have tested them also.
- As a **Shopper** I want to be able to view the total of all products in my cart so that I can avoid spending too much.
  - To test this shopper story I have added multiple products to my cart through adding them via products page. I then clicked on the cart button which brought me to cart page. I was given the subtotals and total of my whole cart in euros.
- As a **Shopper** I want to be able to increase or decrease product quantities so that I can avoid buying too many or buy more if I want to.
  - To test this shopper story I accessed product page where I was able to see current product quantity. By the form on each side there is either a 'minus' or 'plus' sign which either increases or decreases the product quantity.
  - I have also tested this in the cart page for each product that is currently within my cart.
- As a **Shopper** I want to be able to remove products from my cart so that I can avoid buying products I have added to my cart by an accident.
  - To test this shopper story I accessed the cart page where then I was able to see a 'delete' anchor element where if pressed, removed the product from my cart.
- As a **Shopper** I want to be able to see alert messages so that I can know of any issues I am currently experiencing.
  - To test this shopper story I added products to my cart where I was notified by a box pop up with a success message alerting me of product being added to my cart and the total.
  - I also tested this with updating/removing products, updating my profile details and using any other form throughout the site.
- As a **Shopper** I want to be able to use Stripe as my payment method so that I can safely proceed with checkout.
  - To test this shopper story I have added products to my cart where then from the cart page I proceed to the checkout page. I filled out all the details in order to test if Stripe is working correctly. The order went through and via Stripe dashboard I was able to see that everything went through successfully too.
- As a **User** I want to be able to register an account so that I can preview my previous orders and edit my details.
  - To test this user story I accessed the registeration page where I filled out all neccessary fields and submit the form. I was notified that account has been created successfully.
- As a **User** I want to be able to login or logout so that I can access my personal information.
  - To test this user story I have logged in and logged out via the main menu using freshly created account. I was brought to different page depending on the user action I was doing and notified by pop up alerts if anything has gone wrong.
- As a **User** I want to be able to request new password in case I lose it so that I can recover my account.
  - To test this user story I pressed on anchor element, 'forgot password' on login page. It brought me to page where I had to input my email I used while I was registering. I then was sent an email with recovery instructions.
- As a **User** I want to be able to edit a form so that I can update my profile details.
  - To test this user story I logged into my account and proceed to my profile page via the nav bar. I then was able to input my name and my address so that I would not have to do it again on my next orders. I have saved my details and proceed through cart to checkout page where I could see everything prepopulated.
- As a **User** I want to be able to access my profile so that I can preview my past orders.
  - To test this user story I created an order that was placed successfully. I then went to my profile page where I was able to see my previous order including details such as order number, date, products and total cost.
- As a **User** I want to be able to receive an email after registeration so that I can verify my account.
  - To test this user story I made a new account. I was then sent an email with a link to verify my account.
- As an **Admin** I want to be able to add products.
  - To test this admin story I logged in as an admin (superuser). I then hovered over nav bar where I could see a button 'Add products'. By clicking it, it brought me to a page where I could fill out all fields regarding new products including adding product image. I created a test product and it was posted successfully to the main site.
- As an **Admin** I want to be able to edit products so that I can update existing information.
  - To test this admin story I accessed product page where I could press anchor element 'Edit'. I pressed it and it brought me to an edit page with all fields prepopulated ready for editing.
  - I have also tested it via the main products view list throughout the site by either accessing categories or having all pages listed on index/products page.
- As an **Admin** I want to be able to delete products so that I can remove products that are no longer for sale.
  - To test this admin story I accessed product page where I could press anchor element 'Delete'. I pressed it on a dummy product which then got removed successfully and I got prompted by an alert message.
  - I have also tested this via the index/products page.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>
