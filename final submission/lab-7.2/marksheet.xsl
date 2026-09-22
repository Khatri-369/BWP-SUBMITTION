<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>Semester Marksheet (XSLT)</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f9;
                    padding: 30px;
                }
                .marksheet-box {
                    max-width: 750px;
                    margin: 0 auto;
                    background: #ffffff;
                    padding: 25px;
                    border-radius: 8px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                }
                h2 {
                    text-align: center;
                    color: #007bff;
                    margin-top: 0;
                }
                .student-info {
                    margin-bottom: 20px;
                    background-color: #e9ecef;
                    padding: 12px;
                    border-radius: 4px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 15px;
                }
                th, td {
                    border: 1px solid #dddddd;
                    padding: 10px;
                    text-align: center;
                }
                th {
                    background-color: #007bff;
                    color: #ffffff;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
            </style>
        </head>
        <body>
            <div class="marksheet-box">
                <h2>Semester Academic Marksheet</h2>
                <div class="student-info">
                    <p><strong>Student Name:</strong> <xsl:value-of select="marksheet/student/name"/></p>
                    <p><strong>Roll No:</strong> <xsl:value-of select="marksheet/student/rollno"/></p>
                    <p><strong>Semester:</strong> <xsl:value-of select="marksheet/student/semester"/></p>
                    <p><strong>Course:</strong> <xsl:value-of select="marksheet/student/course"/></p>
                </div>

                <table>
                    <thead>
                        <tr>
                            <th>Subject Code</th>
                            <th>Subject Title</th>
                            <th>Max Marks</th>
                            <th>Marks Obtained</th>
                            <th>Grade</th>
                        </tr>
                    </thead>
                    <tbody>
                        <xsl:for-each select="marksheet/subject">
                            <tr>
                                <td><xsl:value-of select="code"/></td>
                                <td style="text-align: left;"><strong><xsl:value-of select="title"/></strong></td>
                                <td><xsl:value-of select="max-marks"/></td>
                                <td><xsl:value-of select="obtained"/></td>
                                <td><strong><xsl:value-of select="grade"/></strong></td>
                            </tr>
                        </xsl:for-each>
                    </tbody>
                </table>
            </div>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
