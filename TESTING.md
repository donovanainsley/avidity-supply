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