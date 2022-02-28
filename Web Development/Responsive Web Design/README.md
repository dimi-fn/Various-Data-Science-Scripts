# Responsive Web Design

Contents
=======================

* Coding Files
    * [html_design.html](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/Responsive%20Web%20Design/html_design.html) | [learn_html.html](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/Responsive%20Web%20Design/learn_html.html) | [learn_css.css](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/Responsive%20Web%20Design/learn_css.css)
* [HTML](#html)
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
    * [HTML Semantic Elements](#html-semantic-elements)
* [CSS](#css)
    * [Block vs Inline Level Elements](#block-vs-inline-level-elements)
    * [CSS Selectors](#css-selectors)
        * [Classes & Ids](#classes--ids)
        * [Custom CSS](#custom-css)
    * [Text](#text)
    * [Images](#images)
    * [Types of CSS declaration](#types-of-css-declaration)
        * [Inline](#inline)
        * [Style Block](#style-block)
        * [External](#external)
    * [Padding - Border - Margin](#padding---border---margin)
    * [Length Unitis: Absolute & Relative Units](#length-unitis-absolute--relative-units)
    * [CSS Inheritance](#css-inheritance)
    * [CSS Overriding](#css-overriding)
    * [Colours](#colours)
    * [CSS Variables](#css-variables)
* [Applied Visual Design](#applied-visual-design)


----

# HTML

## TODO

## General

* Comments: 

        <!-- this is a comment -->

* The `div` tag (division element) is a general purpose container elements through which you can divide your content into sections.

* The `span` tags are basically a way to add a CSS or JavaScript hook into a part of text or HTML

-------    

## HTML Tags
* `main`, `header`, `footer`, `nav`, `video`, `article`, `section`, and others
    * `main`: The main HTML5 tag helps search engines and other developers find the main content of your website
        * [more info about the `<main>` tag - w3schools](https://www.w3schools.com/tags/tag_main.asp#:~:text=Definition%20and%20Usage&text=Note%3A%20There%20must%20not%20be,main%3E%20element%20in%20a%20document.)
        * [more info about the `<main>` tag - html.com](https://html.com/tags/main/#:~:text=HTML%205%20specification.-,Usage,footer%3E%20and%20its%20closing%20tag.)

* with the advent of HTML5, these tags do not need a closing tag:
    * `br`, `hr`, `img`        

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

## HTML Semantic Elements

* `<header>`: header of website (it contains e.g. the nav, title, etc)

* `<main>`: main and unique content of a webpage (it ends before "footer")

* `<section>`: defines a certain section of a webpage (e.g. a blog list, contact info)

* `<article>`: defines some content that constructs an article (e.g. a blog post)

* `<aside>`: defines some content related to something else (e.g. similar blogs)

* `<footer>`: e.g. for copyright, contact form, etc



-------    

# CSS

## Block vs Inline Level Elements

**Block-level elements**: (they inherentely carry CSS of the type `display:block;`)
    * A block-level element always starts on a new line, the browsers automatically add some space (a margin) before and after the element, and they always take up the full width available 
    * Block-level elements have padding and margin *all around* the element
        * `p`, `h1..6`, `div`, `ul`, `li`, `table`, `article`, `section` `blockquote`, and etc

You don't want to put block-level elements inside inline elements (e.g. ), but the opposite is possible (e.g.)

**Inline-level elements**: ((they inherentely carry CSS of the type `display:inline;`))
    * An inline element does not start on a new line and it only takes up as much width as necessary
    * Inline elements have padding and margin only to the *left* and *right* of the element (a solution can be: `display:inline-block;`, i.e. to make an inline
    element act as a block-level element)
    * `a`, `button`, `cite`, `img`, `label`, `script`, `select`, `textarea`

https://www.w3schools.com/html/html_blocks.asp

--------------

## CSS Selectors

### Classes & IDs

**Classes**

Way of reference: `.`, E.g.:

    .blue-text {
                color: blue;
                }

* A `class` [is a group of elements that are the same or similar. You can have as many elements as you want in a class. And each element can be the member of multiple classes. Every class has CSS attributes (like color and font-size) that are specific to that class](https://skillcrush.com/blog/understanding-css-classes-vs-ids/).

* You can apply multiple classes to an element using its class attribute, by separating each class name with a space, e.g. `<img class="class1 class2">`

<br>

**IDs**

Way of reference: `#`. E.g.:

    #an-element {
    background-color: green;
    }

In addition to classes, each HTML element can also have an `id` **attribute**.
* benefits of using id attributes: You can use an id to style a single element and later use them to select and **modify** specific elements **with JavaScript**
* for best practice, id attributes should be **unique**. Therefore, <ins>the same id attribute should not be assigned to more than one element</ins>
    * IDs are unique but classes are not because the latter can be used to label a group tags
* you can style id attributes using CSS in the same way as with classes
    * however and as noted above, an <ins>id is not reusable and should only be applied to one element</ins>
    * **an id has a higher specificity (importance) than a class** so if both are applied to the same element and have conflicting styles, the styles of the id will be applied

### Custom CSS

You can also apply styling to elements by their attribute values. E.g. if you want apply specific CSS to all checkboxes then you could do something like:

    [type='checkbox'] {
    margin: 20px 0px 20px 0px;
    }

-----

## Text

* font-size
* font-family
    * the **generic font families** include monospace, serif and sans-serif. The generic font family names are not case-sensitive and they don't need quotes because they are CSS keywords.
        * when one font isn't available, you can tell the browser to "degrade" to another font.

                p {
                    font-family: Helvetica, sans-serif;
                }

    * [Google Fonts](https://fonts.google.com/)
        * [Get Started with the Google Fonts API ](https://developers.google.com/fonts/docs/getting_started)

-----

## Images 

Properties:
* `width` 

-----

## Types of CSS declaration

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


In the code above, a CSS class called blue-text was created within the style tag. You can then apply that class to an HTML element like this: 

        <h2 class="blue-text">An h2 paragraph with a specified CSS class</h2>

N.b.: in your CSS style element, class names start with a period. In your HTML elements' class attribute, the class name does not include the period.

### External

Via external CSS, you declare your CSS preferences in a separate file of the type .css file. This is the most preferred way of styling because:
* better readability of both the HTML and the CSS file which would be in a separate file (applying the principle of separation of concerns)
    * this makes the need for any style modification easier
* the external stylesheet can be used on multiple HTML docs
* external stylesheets allow global changes to be applied easily on the entire HTML doc
* [External CSS vs inline style performance difference?](https://stackoverflow.com/questions/8284365/external-css-vs-inline-style-performance-difference)
* [Why should I use an external stylesheet instead of inline CSS?](https://discuss.codecademy.com/t/why-should-i-use-an-external-stylesheet-instead-of-inline-css/363588)

-----

## Padding - Border - Margin

Three important properties control the space that surrounds each HTML element: `padding`, `border`, and `margin`. [The CSS Box Model](https://www.w3schools.com/css/css_boxmodel.asp)
* An element's `padding` controls the amount of space between the element's content and its border.
    * 4 padding sides: padding-top, padding-right, padding-bottom, and padding-left 
    * however, instead of specifying all four padding sides you could just do something like this: `padding: 10px 20px 10px 20px;`
        * those four values work like a clock: top, right, bottom, left, and they will produce the exact same result as using the side-specific padding instructions
            * https://www.w3schools.com/css/css_padding.asp
* An element's `margin` controls the amount of space between an element's border and surrounding elements.
    * 4 margin properties: margin-top, margin-right, margin-bottom, and margin-left
    * like padding, margins can be assigned likewise, e.g.: `margin: 10px 20px 10px 20px;`
        * https://www.w3schools.com/css/css_margin.asp
* The CSS `border` properties allow you to specify the style, width, and color of an element's border.    
    * https://www.w3schools.com/css/css_border.asp

-----    

## Length Unitis: Absolute & Relative Units

In addition to pixels (`px`) which tell the browser how to size or space an item, we can have:

* **Absolute length units**: physical units of length. E.g., `in` and `mm` refer to inches and millimeters respectively and they approximate the actual measurement on a screen, but there are some differences depending on a screen's resolution.
* **Relative length units**, such as `em` or `rem`, are relative to another length value. E.g., em is based on the size of an element's font. If you use it to set the font-size property itself, it's relative to the parent's font-size.
    * there are several relative unit options that are tied to the size of the viewport.

-----

## CSS Inheritance    

Inheritance controls what happens when no value is specified for a property on an element. **CSS properties** can be categorized into two types:
1. `inherited properties`, which by default are set to the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/computed_value) of the parent element
2. `non-inherited properties`, which by default are set to [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/initial_value) of the property

<br>

* CSS variables are inherited, just like ordinary properties. To make use of inheritance, CSS variables are often defined in the `:root element`.
    * `:root` is a **pseudo-class** selector that matches the root element of the document, usually the html element. By creating your variables in :root, they will be available **globally** and can be accessed from any other selector in the style sheet.

## CSS Overriding

-----

* Browsers read CSS **from top to bottom** (with the bottom element being the prevailing one!), this means that e.g. if we have two classes regarding color in the style block, and if we apply both of the two classes to a text, then the text will get the color of the 2nd class assigned in the style block, hence it will override the color of the 1st class.

E.g. if we have:

    <style>
        .red-text {color: red;}
        .blue-text {color:blue;}
    </style>
    <body>
        <h1 class="red-text blue-text">What is the colour?</h1>
    </body>

, then the colour applied with be blue. N.b. even if we had `class="blue-text red-text"`, then again the blue colour would get applied because what matters is the class order assignment in the style block

* **Id declarations override class declarations**, hence, in our previous example if we add an id regarding the colour again, then the colour of that id would be applied

* **inline CSS declarations overrides id declarations**

E.g. `<h1 style="color: white;" id="blue-text" class="red-text blue-text">Hello World!</h1>`, where the id and class would have previously been declared in the head style section: the colour applied will be white, i.e. the inline CSS has priority

* The only way to override the above sequence is by using `!important` during the id/class declaration. Then that would override everything else: e.g. the following class color will get applied even if an id or an inline CSS is assigned to an element:

        .orange-text {
            color: orange !important;
        }

* therefore, priority in CSS declarations: ` id/class with '!important' > inline CSS > id declaration > class declaration`

-----

## Colours

Apart from explicitly declaring the colour by its name, there are other ways as well:
* `Hexadecimals` (hex) numbers
    * they are base 16 numbers, i.e. it uses 16 distinct symbols. Like decimals, the symbols 0-9 represent the values zero to nine. Then A,B,C,D,E,F represent the values 10 to 15. Altogether, 0 to F can represent a digit in hexadecimal, giving us a total of 16 possible values.
        * The digit `0` is the lowest number in hex code, and represents a complete absence of color.
        * The digit `F` is the highest number in hex code, and represents the maximum possible brightness.
    * [Hexadecimal Number System](https://www.freecodecamp.org/news/hexadecimal-number-system/)
    
* Using `RGB` values, where instead of using 6 hexadecimal digits like you do with hex code, with RGB you specify the brightness of each color with a number between 0 and 255.
    * E.g., the RGB value for black is: `rgb(0, 0, 0)`
    * [What is The RGB Color Model](https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/#whatisthergbcolormodel)

-----

## CSS Variables

* CSS Variables can change many CSS style properties at once by changing only one value, and they can be [inherited](#CSS-inheritance)

* Way to declare a CSS variable, e.g.: `--variable-name: gray;`

* After you create your CSS variable, you can assign its value to other CSS properties by referencing the variable's name, e.g.: `background: var(--variable-name);`

* It is a good practise to attach a **fallback** value on CSS variables (in order to increase browser's compatibility as well as for debugging)

* In the code below, the variable "--green-color" will be applied. If it is not supported then the fallback value of red will be used instead. N.b., browsers read CSS **from top to bottom** (with the bottom element being the prevailing one!), that's why the browser will first try to assign the green colour

        <style>
        :root {
            /* declare a CSS varibale called "--green-color" */
            --green-color: green
        }
        .red-box {
            background: red; /* the fallback value*/
            background: var(--green-color);
            height: 200px;
            width:200px;
        }
        </style>
        <div class="red-box"></div>    

-----

# Applied Visual Design        

