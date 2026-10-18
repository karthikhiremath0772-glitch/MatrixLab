# MatrixLab

MatrixLab is a Python project focused on learning and practising vector operations, matrix computations, and image pixel analysis using NumPy and Pillow.

## Features

- **Scalar–Vector Operations:** Perform addition, subtraction, multiplication, and division between a scalar and a vector.
- **Vector–Vector Operations:** Perform arithmetic operations between two vectors.
- **Dot Product:** Calculate the dot product of two vectors using NumPy.
- **Matrix Operations:** Perform matrix addition, subtraction, element-wise multiplication and division, matrix        
    multiplication, and transpose.
- **Matrix Properties:** Explore matrix inverse, determinant, rank, and trace.
- **Image Processing:** Load an image and convert its pixel data into a NumPy array.
- **Pixel Inspection:** Access individual pixel values and examine RGB color components.
- **Image Dimensions:** Understand image dimensions using NumPy's `.shape` attribute.

## Technologies Used

- Python
- NumPy
- Pillow (PIL)

## Project Structure

```text
MatrixLab/
├── app.py
├── matrix.py
├── vectors.py
├── image.jpg
└── README.md
```

## Installation

Make sure Python is installed on your system.

Install the required libraries using:

```bash
python -m pip install numpy pillow
```

## How to Run

Open a terminal in the MatrixLab project directory and run the scripts individually.

**1. Image Pixel Analysis**

```bash
python app.py
```

Loads the image, displays its dimensions, and prints the RGB values of the first pixel.

**2. Vector Operations**

```bash
python vectors.py
```

Demonstrates scalar–vector arithmetic, vector–vector arithmetic, and the dot product.

**3. Matrix Operations**

```bash
python matrix.py
```

Demonstrates matrix arithmetic, matrix multiplication, transpose, inverse, determinant, rank, and trace using pixel values extracted from the image.

## Concepts Learned

### 1. NumPy Arrays

Understand how NumPy arrays store and organize numerical data and how to perform mathematical operations efficiently.

### 2. Vector Operations

Practise scalar–vector and vector–vector arithmetic, including the dot product.

### 3. Matrix Computations

Explore matrix arithmetic, matrix multiplication, transpose, inverse, determinant, rank, and trace.

### 4. Image Dimensions Using `.shape`

NumPy's `.shape` attribute returns a tuple containing the size of each dimension of an array.

For the image used in this project:

```python
pixels.shape
# (853, 1280, 3)
```

The dimensions represent:

- **853:** Number of rows, corresponding to the image height.
- **1280:** Number of columns, corresponding to the image width.
- **3:** Number of color channels — Red, Green, and Blue (RGB).

### 5. Pixel Access and RGB Values

Each pixel in an RGB image contains three intensity values representing red, green, and blue.

For example:

```python
pixels[0, 0]
# [142 138 129]
```

Here, `pixels[0, 0]` accesses the pixel at the first row and first column — the top-left pixel of the image.

### 6. Matrix Properties

Understand how to calculate the determinant, rank, trace, and inverse of a matrix. A singular matrix has no inverse, which is also demonstrated in this project.

## Learning Objectives

- Develop a practical understanding of NumPy arrays and numerical computing.
- Understand the relationship between image pixels and multidimensional arrays.
- Apply vector and matrix operations using Python.
- Practise array indexing and image data inspection.
- Build a foundation for further learning in linear algebra, machine learning, and image processing.

## Future Improvements

- Add input validation and clearer error handling.
- Organize the project into reusable functions.
- Add unit tests for vector and matrix operations.
- Explore additional NumPy operations and image-processing techniques.

## Author

Created as a learning project to practise Python, NumPy, linear algebra, and image pixel analysis.