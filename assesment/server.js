// server.js
const express = require('express');
const app = express();
const port = 3000;

// Middleware to serve static files (like HTML, CSS, JS)
app.use(express.static('frontend'));

// Route to handle GET requests
app.get('/api/message', (req, res) => {
    res.json({ message: 'Hello from the server!' });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
