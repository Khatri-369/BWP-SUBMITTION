// Node.js Module for Area Calculation

// Area of Circle: A = pi * r * r
function areaOfCircle(radius) {
    return (Math.PI * radius * radius).toFixed(2);
}

// Area of Rectangle: A = length * width
function areaOfRectangle(length, width) {
    return (length * width).toFixed(2);
}

// Area of Square: A = side * side
function areaOfSquare(side) {
    return (side * side).toFixed(2);
}

// Export module functions
module.exports = {
    areaOfCircle,
    areaOfRectangle,
    areaOfSquare
};
