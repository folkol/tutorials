# React – from the ground up

We will build a React app, starting with a static index.html and no pre-processors.

When the app is 'done', we might port it to a npm webpack project with JSX.

> **N.b.** To build a real app, start with something like [Create Creact App](https://github.com/facebookincubator/create-react-app]).

## End game

IMAGE GOES HERE

## Steps

> N.b. A code for each step can be found under solutions.

### Step 1 – index.html

1.1) Create a text file called index.html.

```
<!--DOCTYPE html-->
<html>
  <head>
    <meta charset="utf-8">
    <title>React – from the ground up</title>
  </head>
  <body>
    <div id="app">
      <p>Hello, world!</p>
    </div>
  </body>
</html>
```

1.2) Include `react.js` and `react-dom.js`

```
...
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/react/15.6.1/react.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/react/15.6.1/react-dom.js"></script>
...
```

1.3) Re-render the p-tag with React




## Notes

- If children of React.createElement is null, undefined or false, it will not be rendered.

## References

 - [http://buildwithreact.com/tutorial/jsx]()
 - [https://facebook.github.io/react/blog/2015/10/01/react-render-and-top-level-api.html]()
 - [https://reactarmory.com/guides/learn-react-by-itself/react-basics]()
 - 