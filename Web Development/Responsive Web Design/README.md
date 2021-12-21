# Responsive Web Design

Contents
=======================

* [HTML](#html)
    * [learn_html.html](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/Responsive%20Web%20Design/learn_html.html) & [html default paradigm design](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/Responsive%20Web%20Design/html_design.html)
    * [General](#general)
    * [HTML Tags](#html-tags)
    * [Images](#images)
    * [Links](#links)
        * [External Links](#external-links)
        * [Internal Links](#internal-links)
        * [More about Links](#more-about-links)
    * [Lists](#lists)
    * [Input Forms](#input-forms)
        * [Text Fields](#text-fields)
        * [Buttons](#buttons)
* [CSS](#css)
    * [Text](#text)
    * [Images](#images)
    * [Types of CSS](#types-of-css)
        * [Internal](#internal)
        * [Style Block](#style-block)
        * [External](#external)

----

# HTML

## General

* Comments: 

    <!-- this is a comment -->

* The `div` element (division element) is a general purpose container for other elements.

-------    

## HTML Tags
* `main`, `header`, `footer`, `nav`, `video`, `article`, `section`, and others
    * `main`: The main HTML5 tag helps search engines and other developers find the main content of your website

-------

## Images   

* Use the `img` *element* and the `src` *attribute*
    * e.g. `<img src="https://www.freecatphotoapp.com/your-image.jpg">`

* img elements must have an `alt` *attribute*. The text inside an alt attribute is used for screen readers to improve accessibility and is displayed if the image fails to load.  
    * Ideally the alt attribute should not contain special characters unless needed
    * You can also use `title` to display a message when you hover over the image. [This is different from using the alt attribute](https://stackoverflow.com/questions/872389/html-img-tag-title-attribute-vs-alt-attribute)


E.g. this code: `<img src="https://www.freecatphotoapp.com/your-image.jpg" alt="A business cat wearing a necktie." title="A nice cat">` will give the following:

<img src="https://www.freecatphotoapp.com/your-image.jpg" alt="A business cat wearing a necktie." title="A nice cat">

-------

## Links

### External Links

Use the `a` *anchor element* that points to a specific url (external link), and provide an anchor text alongside with that.
* E.g. of an external link: `<a href="https://www.freecodecamp.org">this links to freecodecamp.org</a>` will give this: <a href="https://www.freecodecamp.org">this links to freecodecamp.org</a>

### Internal Links

To create an internal link, you assign a link's `href` *attribute* to a hash symbol `#` plus the value of the *id attribute* for the element that you want to internally link to, usually further down the page. You then need to add the same id attribute to the element you are linking to. An id is an attribute that uniquely describes an element.
* Example: 

        <a href="#contacts-header">Contacts</a>
        ...
        <h2 id="contacts-header">Contacts</h2>

### More about Links

* Use the `target="_blank"` anchor tag attribute in the anchor tag to open the link to a new window tab.

* Turn an **image into a link**: you can nest your image within an `a` element. E.g. this code: `<a href="#"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="Three kittens running towards the camera."></a>` will give the image below and you can click upon that:

<a href="#"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="Three kittens running towards the camera."></a>

-------

## Lists

* unordered: `<ul>` element followed by `<li>` elements
* ordered: `<ol>` element followed by `<li>` elements

-------

## Input Forms

### Text Fields

[HTML forms](https://www.w3schools.com/html/html_forms.asp) are used to collect user **input**, which is often sent to a server for processing by specifying an `action` attribute.

* `<input type="text">`
    * use `placeholder` for displaying a default text upon the text field

* Example of input form with placeholder text and a form action:

        <form action="https://www.freecatphotoapp.com/submit-cat-photo">
        <input type="text" placeholder="cat photo URL">
        </form>  

* For required text input field use: `<input type="text" required>`

### Buttons

* **Radio** buttons are a type of input.
* Each of your radio buttons can be nested within its own `label` element. By wrapping an input element inside of a label element it will automatically associate the radio button input with the label element surrounding it.
* All related radio buttons should have the same `name` attribute to create a radio button group. By creating a radio group, selecting any single radio button will automatically deselect the other buttons within the same group ensuring only one answer is provided by the user.
* It is considered best practice to set a `for` attribute on the label element, with a value that matches the value of the `id` attribute of the *input* element. This allows assistive technologies to create a linked relationship between the label and the related input element.
* When a form gets **submitted**, the data is sent to the server and includes entries for the options selected. Inputs of type radio and checkbox report their values from the `value` attribute. If values is empty then its default value is `on` (which is not useful, and the value should always be specified)

<br>

Types can be (type=""):
* radio
* checkbox

-------    

# CSS

## Text

* font-size
* font-family
    * the **generic font families** include monospace, serif and sans-serif. The generic font family names are not case-sensitive and they don't need quotes because they are CSS keywords.
        * when one font isn't available, you can tell the browser to "degrade" to another font.

                p {
                    font-family: Helvetica, sans-serif;
                }

    * [Google Fonts](https://fonts.google.com/)

-----

## Images 

Properties:
* `width` 

-----

## Types of CSS

### Inline

In general, it is not a good practice and it should be avoided
    * It is a good practice to end inline style declarations with a `;` 
    * E.g.: `<h2 style="color: red;">This is a red heading</h2>`
    
### Style Block

`Style block` at the *head* section by defining each element's style rule(s)
* E.g.: style all h2 elements to be red:

            <style>
                h2 {
                    color: red;
                }
            </style>

* You can combine inline CSS with style blocks via CSS `classes`. Classes allow you to use the same CSS styles on multiple HTML elements. E.g.:

            <style>
                .blue-text {
                color: blue;
            }
            </style>


In the code above, a CSS class was created called blue-text within the style tag. You can then apply that class to an HTML element like this: 

        <h2 class="blue-text">An h2 paragraph with a specified CSS class</h2>

N.b.: in your CSS style element, class names start with a period. In your HTML elements' class attribute, the class name does not include the period.

N.b.: you can apply multiple classes to an element using its class attribute, by separating each class name with a space, e.g. `<img class="class1 class2">`


### External

