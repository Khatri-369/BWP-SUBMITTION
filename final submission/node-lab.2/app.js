// Node.js Program to read number from file and check Armstrong
const fs = require('fs');
const http = require('http');

// Function to check Armstrong Number
function isArmstrong(num) {
    const numStr = num.toString().trim();
    const len = numStr.length;
    let sum = 0;

    for (let i = 0; i < len; i++) {
        const digit = parseInt(numStr[i]);
        sum += Math.pow(digit, len);
    }

    return sum === parseInt(num);
}

// Read file 'number.txt' asynchronously
fs.readFile('number.txt', 'utf8', (err, data) => {
    if (err) {
        console.error("Error reading file:", err);
        return;
    }

    const number = parseInt(data.trim());
    const result = isArmstrong(number);

    console.log("=== Node.js Armstrong Number Checker ===");
    console.log(`Number read from file 'number.txt': ${number}`);
    if (result) {
        console.log(`RESULT: ${number} IS an Armstrong number.`);
    } else {
        console.log(`RESULT: ${number} is NOT an Armstrong number.`);
    }

    // Start HTTP Server to present output on Browser
    const server = http.createServer((req, res) => {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(`
            <!DOCTYPE html>
            <html>
            <head>
                <title>Armstrong Number Checker - Node.js</title>
                <style>
                    body { font-family: Arial, sans-serif; background-color: #f4f6f9; padding: 40px; }
                    .card { max-width: 500px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; }
                    .badge-yes { background-color: #28a745; color: white; padding: 10px 20px; font-size: 18px; border-radius: 4px; display: inline-block; margin-top: 15px; }
                    .badge-no { background-color: #dc3545; color: white; padding: 10px 20px; font-size: 18px; border-radius: 4px; display: inline-block; margin-top: 15px; }
                </style>
            </head>
            <body>
                <div class="card">
                    <h2>🔢 Armstrong Number Check</h2>
                    <p>Number read from <code>number.txt</code>: <strong>${number}</strong></p>
                    <div class="${result ? 'badge-yes' : 'badge-no'}">
                        ${result ? `✅ ${number} is an Armstrong Number` : `❌ ${number} is NOT an Armstrong Number`}
                    </div>
                </div>
            </body>
            </html>
        `);
        res.end();
    });

    const PORT = 3002;
    server.listen(PORT, () => {
        console.log(`Server running at http://localhost:${PORT}/`);
    });
});
