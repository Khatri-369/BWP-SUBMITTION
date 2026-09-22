<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>Products Price Under 300Rs (XSLT Filter)</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f9;
                    padding: 30px;
                }
                .container {
                    max-width: 650px;
                    margin: 0 auto;
                    background: #ffffff;
                    padding: 25px;
                    border-radius: 8px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                }
                h2 {
                    text-align: center;
                    color: #d9534f;
                    margin-top: 0;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                th, td {
                    border: 1px solid #dddddd;
                    padding: 10px;
                    text-align: center;
                }
                th {
                    background-color: #d9534f;
                    color: #ffffff;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
                .price-tag {
                    color: #5cb85c;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Products List (Price &lt; 300 Rs)</h2>
                <p style="text-align: center; color: #666; font-size: 14px;">Filtered using XSLT <code>&lt;xsl:if test="price &amp;lt; 300"&gt;</code></p>

                <table>
                    <thead>
                        <tr>
                            <th>Item ID</th>
                            <th>Product Name</th>
                            <th>Category</th>
                            <th>Price (Rs)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Filter products with price < 300 -->
                        <xsl:for-each select="items/product">
                            <xsl:if test="price &lt; 300">
                                <tr>
                                    <td><code><xsl:value-of select="id"/></code></td>
                                    <td style="text-align: left;"><strong><xsl:value-of select="name"/></strong></td>
                                    <td><xsl:value-of select="category"/></td>
                                    <td class="price-tag">₹<xsl:value-of select="price"/></td>
                                </tr>
                            </xsl:if>
                        </xsl:for-each>
                    </tbody>
                </table>
            </div>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
