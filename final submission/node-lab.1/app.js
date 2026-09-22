// Main Application File using areaModule.js
const http = require('http');
const areaModule = require('./areaModule');

// Sample dimensions
const radius = 7;
const rectLength = 10;
const rectWidth = 5;
const squareSide = 4;

// Calculate areas using imported module
const circleArea = areaModule.areaOfCircle(radius);
const rectArea = areaModule.areaOfRectangle(rectLength, rectWidth);
const squareArea = areaModule.areaOfSquare(squareSide);

// Print results to Console
console.log("=== Node.js Area Calculation Module Results ===");
console.log(`Area of Circle (radius ${radius}): ${circleArea}`);
console.log(`Area of Rectangle (${rectLength} x ${rectWidth}): ${rectArea}`);
console.log(`Area of Square (side ${squareSide}): ${squareArea}`);

// Create HTTP Server to display results in web browser
const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Node.js Area Calculation Module</title>
            <style>
                body { font-family: Arial, sans-serif; background: #f4f6f9; padding: 40px; }
                .box { max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
                h2 { color: #007bff; text-align: center; }
                ul { font-size: 18px; line-height: 2; }
            </style>
        </head>
        <body>
            <div class="box">
                <h2>📐 Node.js Area Calculation Module</h2>
                <hr>
                <ul>
                    <li><strong>Area of Circle</strong> (r = ${radius}): <code>${circleArea} sq units</code></li>
                    <li><strong>Area of Rectangle</strong> (${rectLength} x ${rectWidth}): <code>${rectArea} sq units</code></li>
                    <li><strong>Area of Square</strong> (side = ${squareSide}): <code>${squareArea} sq units</code></li>
                </ul>
            </div>
        </body>
        </html>
    `);
    res.end();
});

const PORT = 3001;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
