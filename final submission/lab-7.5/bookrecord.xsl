<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>Book Record (XSLT Table Format)</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f9;
                    padding: 30px;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    background: #ffffff;
                    padding: 25px;
                    border-radius: 8px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                }
                h2 {
                    text-align: center;
                    color: #17a2b8;
                    margin-top: 0;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                th, td {
                    border: 1px solid #dddddd;
                    padding: 12px;
                    text-align: center;
                }
                th {
                    background-color: #17a2b8;
                    color: #ffffff;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
                .price {
                    font-weight: bold;
                    color: #28a745;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>📖 Bookstore Records Table</h2>
                <p style="text-align: center; color: #666; font-size: 14px;">Formatted from <code>bookrecord.xml</code> using XSLT stylesheet.</p>

                <table>
                    <thead>
                        <tr>
                            <th>Book Title</th>
                            <th>Category</th>
                            <th>Author</th>
                            <th>Year</th>
                            <th>Publisher</th>
                            <th>Price (₹)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <xsl:for-each select="bookstore/book">
                            <tr>
                                <td style="text-align: left;"><strong><xsl:value-of select="title"/></strong></td>
                                <td><xsl:value-of select="@category"/></td>
                                <td><xsl:value-of select="author"/></td>
                                <td><xsl:value-of select="year"/></td>
                                <td><xsl:value-of select="publisher"/></td>
                                <td class="price">₹<xsl:value-of select="price"/></td>
                            </tr>
                        </xsl:for-each>
                    </tbody>
                </table>
            </div>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
