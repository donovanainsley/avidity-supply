# Avidity Supply

![Website on different screen sizes](media/amir_avidity_supply.png)

## Testing

### Code Validation

#### HTML
The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the site's pages to ensure there were no syntax errors.

<details><summary>Home</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Bag</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Checkout</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Checkout Success</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Products</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Product Detail</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Product Management</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Add Product</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Edit Product</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Add Review</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

<details><summary>Contact</summary>
<img src="documentation/testing/html-validation.png" alt="">
</details>

#### CSS
The [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate custom css styling.

<details><summary>base.css</summary>
<img src="documentation/testing/css-validation.png" alt="">
</details>

<details><summary>checkout.css</summary>
<img src="documentation/testing/css-validation.png" alt="">
</details>

<details><summary>profile.css</summary>
<img src="documentation/testing/css-validation.png" alt="">
</details>

#### JS
[JS HINT](https://jshint.com/) was used to test JaveaScript.

<details><summary>stripe_element.js</summary>
<img src="documentation/testing/stripe-element-validation.png" alt="">
</details>

<details><summary>countryfield.js</summary>
<img src="documentation/testing/countryfield-validation.png" alt="">
</details>

#### Python
[CI Pythong Linter](https://pep8ci.herokuapp.com/#) has been used to validate my python code and esnured it's pep8 compliant.

All python code created or automatically generated was validated and corrected and now displays no errors, so I have only provided the single screenshot.
- Note - some lines were too long and in an effort not to causes issues with my project '# NOQA' was used.

<details><summary>Python Validation</summary>
<img src="documentation/testing/python-validation.png" alt="">
</details>

### Manual Testing

#### Testing User Stories

##### VIEWING & NAVIGATION 
| As a    | I want to be able to            | So that I can | Image |
|---------|---------------------------------|---------------|----------------------------------|
| Shopper | Easily navigate the site        | Find products to purchase                                                               | <img src="documentation/nav-bar.png">  |
| Shopper | View products by category       | Find specific items I am interested in without having to scroll through all products    | <img src="documentation/testing/apparel-dropdown.png">  |
| Shopper | View details of each product    | Learn more about each product                                                           |  <img src="documentation/product-detail-all-devices.png">   |
| Shopper | View the items I have in my bag | Check whether I still wish to purchase the items and amend the quantity if required     |  <img src="documentation/bag-page.png"> |

#### REGISTRATION & USER ACCOUNTS
| As a    | I want to be able to  | So that I can | Image |
|---------|------------------------|--------| ---------- |
| Shopper | Register an account                         | Have an account with the site and view my profile   | <img src="documentation/profile.png">   |
| Registered User | Receive an email to confirm my registration | Verify my account was created successfully    | <img src="documentation/testing/confirmation-email.png"> |
| Registered User | Log in and out                              | Keep my account information secure                       |  <img src="documentation/login.png">  |
| Registered User | View a profile page                         | Set a default delivery address and view previous orders  |  <img src="documentation/profile.png">  |
| Registered User | Reset my password                           | Recover my account                                       |  <img src="documentation/reset.png"> |

#### SORTING & SEARCHING
| As a    | I want to be able to | So that I can | Image |
|---------|----------------------|---------------|-------|
| Shopper | Search for a product by name or description | Find a specific product I'd like to purchase | <img src="documentation/nav-bar.png">  |
| Shopper | Find products from a specific category      | Only see products from that category         | <img src="documentation/testing/apparel-dropdown.png"> |

#### PURCHASING & CHECKOUT
| As a    | I want to be able to | So that I can| Image |
|---------|----------------------|--------------|-------|
| Shopper | Easily select the quantity of a product when purchasing it  | Ensure I don't accidentally select the wrong product quantity | <img src="documentation/product-detail-all-devices.png"> |
| Shopper | View all items in my bag  | Make sure I haven't accidentally added the wrong product in my bag | <img src="documentation/bag-page.png"> |
| Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout | <img src="documentation/testing/remove-product.png"> |
| Shopper | Easily enter my payment information | Check out quickly and with no hassle | <img src="documentation/testing/checkout-fullview.png"> |
| Shopper | Save all address info | I don't have to enter them again on my next order | <img src="documentation/testing/save-delivery.png"> |
| Shopper | View an order confirmation after checkout | Make sure my order was successfully placed and double check that all details are correct  | <img src="documentation/testing/confirmation-email.png"> |
| Shopper | Save all orders on my Profile | Easily access all orders anytime | <img src="documentation/profile.png"> |
| Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records | <img src="documentation/testing/order-recieved.png"> |

#### REVIEW
| As a    | I want to be able to | So that I can | Image |
|---------|----------------------|---------------|-------|
| Shopper | Read product reviews | Find out what other shoppers think about the product | <img src="documentation/testing/read-review.png"> |
| Shopper | Add a product review | Share my experience using the product with other shoppers| <img src="documentation/testing/add-review.png"> |
| Registered User | Delete a review if enetered incorrectly | Share my experience using the product with other shoppers| <img src="documentation/testing/delete-review.png">|
| Store Owner | Delete a review | Remove product review if deemed inaccuarte or entered incorrectly | <img src="documentation/testing/delete-review.png"> |

#### CONTACT
| As a    | I want to be able to  | So that I can| Image |
|---------|-----------------------|--------------|-------|
| Shopper/User | Contact the admin team | Make an enquiry | <img src="documentation/contact.png"> <img src="documentation/testing/contact-button.png"> |

#### ADMIN & STORE MANAGEMENT
| As a | I want to be able to | So that I can | Image |
|------|----------------------|---------------|-------|
| Store Owner/Admin | Add a product | Add new items to my store | <img src="documentation/product-management.png"> |
| Store Owner/Admin | Edit a product | Update product details | <img src="documentation/testing/edit-product.png"> |
| Store Owner/Admin | Delete a product | Remove items that are no longer for sale | <img src="documentation/testing/delete-product.png"> |
| Store Owner/Admin | Delete a product review | Remove product review if deemed inaccuarte or entered incorrectly | <img src="documentation/testing/delete-review.png"> |


#### Lighthouse

The Chrome Developer Tools lighthouse feature was employed to assess performance, adherence to best practices, accessibility, and Search Engine Optimisation (SEO). Both desktop and mobile tests were conducted.

- Several lighthouse tests performed, were below where I'd like them to be but due to time constraints, I was unable to improve the score but would in future implementations.

| Page | Results |
| --- | --- |
| Home | <img src="documentation/testing/home-lighthouse-desktop.png" alt=""> |
| Home (mobile) | <img src="documentation/testing/home-lighthouse-mobile.png" alt=""> |
| Products | <img src="documentation/testing/products-lighthouse-desktop.png"> |
| Products (mobile) | <img src="documentation/testing/products-lighthouse-mobile.png"> |
| Bag | <img src="documentation/testing/bag-lh-desktop.png" alt=""> |
| Bag (mobile) | <img src="documentation/testing/bag-lh-mobile.png" alt=""> |
| Checkout | <img src="documentation/testing/checkout-lh-desktop.png" alt=""> |
| Checkout (mobile) | <img src="documentation/testing/checkout-lh-mobile.png" alt=""> |
| Profile | <img src="documentation/testing/profile-lh-desktop.png" alt=""> |
| Profile (mobile) | <img src="documentation/testing/profile-lh-mobile.png" alt=""> |
| Contact | <img src="documentation/testing/contact-lighthouse-desktop.png" alt=""> |
| Contact (mobile) | <img src="documentation/testing/contact-lighthouse-mobile.png" alt=""> |
| Add Review | <img src="documentation/testing/addreview-lh-desktop.png" alt=""> |
| Add Review (mobile) | <img src="documentation/testing/addreview-lh-mobile.png" alt=""> |

#### Devices used for testing:
- MacBook Pro
- Samsung Galaxy S23+
- Samsung Galaxy S23
- iPhone 14

#### Browsers Used for Testing
- Google Chrome
- Monzila FireFox
- Safari 
No issues found