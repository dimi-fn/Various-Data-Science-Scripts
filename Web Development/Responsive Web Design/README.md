# Responsive Web Design

Contents
=======================

* [HTML](#html)
    * [HTML Tags](#html-tags)
    * [Images](#images)
    * [Links](#links)
        * [External Links](#external-links)
        * [Internal Links](#internal-links)
        * [More about Links](#more-about-links)
* [CSS]()

----

# HTML

Comments: 

    <!-- this is a comment -->

## HTML Tags
* `main`, `header`, `footer`, `nav`, `video`, `article`, `section`, and others
    * `main`: The main HTML5 tag helps search engines and other developers find the main content of your website

## Images   

* Use the `img` *element* and the `src` *attribute*
    * e.g. `<img src="https://www.freecatphotoapp.com/your-image.jpg">`

* img elements must have an `alt` *attribute*. The text inside an alt attribute is used for screen readers to improve accessibility and is displayed if the image fails to load.  
    * Ideally the alt attribute should not contain special characters unless needed
    * You can also use `title` to display a message when you hover over the image. [This is different from using the alt attribute](https://stackoverflow.com/questions/872389/html-img-tag-title-attribute-vs-alt-attribute)


E.g. this code: `<img src="https://www.freecatphotoapp.com/your-image.jpg" alt="A business cat wearing a necktie." title="A nice cat">` will give the following:

<img src="https://www.freecatphotoapp.com/your-image.jpg" alt="A business cat wearing a necktie." title="A nice cat">



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

