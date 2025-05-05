# Overview

I designed and developed a to-do list application using MongoDB, Node.js, Express, and Mongoose. The application is a simple yet effective tool for users to manage their tasks with ease and efficiency.

MongoDB was chosen as the database to store and retrieve the data due to its efficient storage and retrieval capabilities. Node.js was used as the backend of the application, built on top of the Express framework. Mongoose was used to provide a more streamlined approach to working with MongoDB and allowed for the easy definition and manipulation of data models.

The application has a simple and user-friendly interface, allowing users to add, edit, and delete tasks with ease. Throughout the development process, I focused on creating a simple and efficient application. 

Overall, I am proud of the to-do list application that I have developed using MongoDB, Node.js, Express, and Mongoose. It has been a valuable learning experience for me

[Software Demo Video](https://drive.google.com/file/d/19Ectx0qf4DveIQ1d-UBclgjXK_exzLUk/view?usp=share_link)

# Instructions
1. Make sure you have all the proper technologies installed. Look below at helpful links for better direction. You need to have the following:
- Node.js
- MongoDB
- Express
- Mongoose
- JavaScript
- Some sort of editor (I used VS Code)

2. To launch this app. Go to the file linked below where it says "Application Launch" or the file name is index.js.

3. Open a new console

4. type in 
```js
npm start
```

5. The program should connect to a database. NOTE: MAKE SURE YOU CREATE a DATABASE/cluster with MONGODB and get its URL. You will then create a file titled < .env > in the main folder. In the .env file paste the database url or data connection string:
```js
DB_CONNECT = "mongodb+srv://[USERNAME]}:[PASSWORD]a@todolist.mzqzbib.mongodb.net/?retryWrites=true&w=majority"
```

6. Once the server is up go to a browser and type in:

```html
http://localhost:3000
```

7. You should see the app working and its pretty straight forward from there. 



# Table of Contents

- [Application Launch](/index.js)
- [HTML Documents](./views)
- [CSS and Assets](./public)
- [Database Models](./models)

# Development Environment

So, for my to-do list web application, I used **Node.js** as the platform to build the server-side logic. Node.js is really great for building fast and scalable network applications. It uses an event-driven, non-blocking I/O model that makes it lightweight and efficient, so it's perfect for data-intensive real-time applications like mine.

To store the data for my to-do list application, I used **MongoDB**. It stores data in flexible, JSON-like documents, which means I can easily change the data structure over time. Plus, MongoDB is really scalable and can handle large amounts of data.

For the server-side routing and request handling, I used **Express**. It's a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. This made it really easy to customize my application and build it to meet my specific needs.

To allow users to create, read, update, and delete tasks, I used **CRUD** operations. These are the basic operations that any web application that manages data would need to have.

To provide a flexible and scalable interface for client-side interactions, I used **RESTful APIs**. These are really reliable and easy to use, and they allowed me to implement features like search, filtering, and sorting of tasks.

To add interactivity and functionality to my web pages, I used **JavaScript**. It's what allowed me to make my application respond dynamically to user actions, which provides a really seamless user experience.

For the structure and content of my web pages, I used **HTML**. It's what allowed me to define the layout and content of my pages in a really intuitive way.

And finally, for the visual appearance of my web pages, I used **CSS**. It allowed me to define the styles for different elements on my pages, like fonts, colors, and layout. This made my application look really nice and easy to use!

While building my application, I found that using **Google Chrome** as my web browser was really helpful, since it has great developer tools that allowed me to easily debug and troubleshoot any issues that came up. And I used **Visual Studio Code (VS Code)** as my code editor, since it's really powerful and easy to use. It allowed me to write my code more quickly and efficiently, which was really important since I wanted to build my application as quickly as possible.

- Node.js
- MongoDB
- Express
- Mongoose
- JavaScript
- HTML
- CSS



# Useful Websites

{Make a list of websites that you found helpful in this project}

**Node.js**:
- [Official Node.js Documentation](https://nodejs.org/en/docs/) - A comprehensive guide to using Node.js.
- [Node.js Tutorial for Beginners](https://www.tutorialspoint.com/nodejs/index.htm) - A beginner-friendly tutorial on Node.js.

**MongoDB**:
- [Official MongoDB Documentation](https://docs.mongodb.com/manual/) - The official documentation for MongoDB.
- [MongoDB University](https://university.mongodb.com/) - Free online courses on MongoDB, including a course on MongoDB basics.

**Express**:
- [Official Express.js Documentation](https://expressjs.com/) - The official documentation for Express.js.
- [Express.js Tutorial for Beginners](https://www.tutorialspoint.com/expressjs/index.htm) - A beginner-friendly tutorial on Express.js.

**CRUD Operations**:
- [CRUD Operations in MongoDB](https://www.mongodb.com/blog/post/quick-start-crud-operations-mongodb-nodejs) - A tutorial on implementing CRUD operations with MongoDB and Node.js.

**RESTful APIs**:
- [Representational State Transfer (REST) API Tutorial](https://restfulapi.net/) - A beginner-friendly tutorial on RESTful APIs.

**JavaScript**:
- [MDN Web Docs - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - A comprehensive guide to JavaScript.
- [JavaScript Tutorial for Beginners](https://www.tutorialspoint.com/javascript/index.htm) - A beginner-friendly tutorial on JavaScript.

**Coding Language/Syntax**:

**W3Schools**:
- [W3Schools](https://www.w3schools.com/) - An online learning platform that offers tutorials and references on web development technologies such as HTML, CSS, JavaScript, and more.
- [Stack Overflow](https://stackoverflow.com/) - A community-driven Q&A website for programmers to help and learn from each other.
- [GeekforGeeks](https://www.geeksforgeeks.org/) - A website that provides articles, tutorials, and practice problems in various programming languages and computer science topics.
- [ChatGPT](https://chat.openai.com/) - An AI that helped me with troubleshooting and generating various wording and collecting information and summarizing content. 