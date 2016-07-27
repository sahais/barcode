# jpl-header

An element that follows the JPL Brand for the Header of applications

## DEMO

https://github.jpl.nasa.gov/pages/PolymerElements/jpl-header/

## Using Element

in your index.html add

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/0.7.7/webcomponents-lite.min.js"></script>
<link rel="import" href="jpl-header.html">
```

### Using element in your project using bower

Edit your bower.json and add the jpl-header to your dependencies

```
"jpl-header": "https://github.jpl.nasa.gov/PolymerElements/jpl-header.git"
```

Run `bower install`

Add the following to your index.html:

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/0.7.7/webcomponents-lite.min.js"></script>
<link rel="import" href="./bower_components/jpl-header/dist/jpl-header.html">
```

## Using Element in Polymer Project

Edit your bower.json and add the jpl-header to your dependencies

```
"jpl-header": "https://github.jpl.nasa.gov/PolymerElements/jpl-header.git"
```

Run `bower install`

Add the following to your elements.html:

```
<link rel="import" href="../../bower_components/jpl-header/jpl-header.html">
```

## Development

### Dependencies

Element dependencies are managed via [Bower](http://bower.io/). You can
install that via:

    npm install -g bower

Then, go ahead and download the element's dependencies:

    bower install


### Playing With Your Element

If you wish to work on your element in isolation, we recommend that you use
[Polyserve](https://github.com/PolymerLabs/polyserve) to keep your element's
bower dependencies in line. You can install it via:

    npm install -g polyserve

And you can run it via:

    polyserve

Once running, you can preview your element at
`http://localhost:8080/components/jpl-header/`, where `jpl-header` is the name of the directory containing it.

### Building an element to use outside of polymer, like Angular 2, React, vanila js

```
vulcanize jpl-header.html --inline-scripts --inline-css --strip-comments > dist/jpl-header.html
```
