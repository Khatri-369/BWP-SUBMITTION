// Node.js Server to read student.json and display information for given PRN in tabular format
const http = require('http');
const fs = require('fs');
const url = require('url');

const PORT = 3003;

const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    const queryPRN = parsedUrl.query.prn || "202600101"; // Default PRN if not specified

    // Read student.json from server
    fs.readFile('student.json', 'utf8', (err, data) => {
        res.writeHead(200, { 'Content-Type': 'text/html' });

        if (err) {
            res.write("<h3>Error reading student.json file from server.</h3>");
            return res.end();
        }

        const students = JSON.parse(data);
        const student = students.find(s => s.PRN === queryPRN);

        let html = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>Student Information - PRN ${queryPRN}</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f4f6f9; padding: 40px; }
                .card { max-width: 700px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
                h2 { color: #007bff; text-align: center; }
                .search-box { text-align: center; margin-bottom: 25px; }
                input[type="text"] { padding: 8px; font-size: 15px; width: 200px; border: 1px solid #ccc; border-radius: 4px; }
                button { padding: 8px 16px; background-color: #007bff; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                td, th { padding: 12px; border: 1px solid #ddd; font-size: 15px; }
                th { background-color: #007bff; color: white; text-align: left; width: 30%; }
                .no-found { text-align: center; color: #dc3545; font-weight: bold; font-size: 16px; margin-top: 20px; }
            </style>
        </head>
        <body>
            <div class="card">
                <h2>🎓 Student Information Lookup (Node.js Server)</h2>
                <div class="search-box">
                    <form action="/" method="GET">
                        <label><strong>Enter PRN No:</strong></label>
                        <input type="text" name="prn" value="${queryPRN}" placeholder="Enter PRN">
                        <button type="submit">Search PRN</button>
                    </form>
                </div>
        `;

        if (student) {
            html += `
                <table>
                    <tr><th>Student Name</th><td><strong>${student.name}</strong></td></tr>
                    <tr><th>PRN No</th><td><code>${student.PRN}</code></td></tr>
                    <tr><th>Branch</th><td>${student.Branch}</td></tr>
                    <tr><th>Semester</th><td>${student.Semester}</td></tr>
                    <tr><th>Address</th><td>${student.address}</td></tr>
                    <tr><th>Subject Name</th><td>${student.subjectName}</td></tr>
                </table>
            `;
        } else {
            html += `<div class="no-found">❌ No Student record found for PRN: ${queryPRN}</div>`;
        }

        html += `
            </div>
        </body>
        </html>
        `;

        res.end(html);
    });
});

server.listen(PORT, () => {
    console.log(`Node.js Student PRN Server running at http://localhost:${PORT}/`);
});
