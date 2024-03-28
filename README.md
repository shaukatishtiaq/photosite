# PhotoSite

PhotoSite is a Django web application that lets you upload photos and automatically creates watermarked versions of the images. Additionally, users can make payments using the integrated Stripe Payment Gateway to download the original, non-watermarked versions of the images.

## Features

- **Upload Photos**: Ppload photos to the website.
- **Automatic Watermarking**: The application automatically adds a watermark to the uploaded images to protect them.
- **Secure Payments**: Users can make payments to download the original, non-watermarked versions of the images securely.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your_username/PhotoSite.git
    ```

2. Navigate to the project directory:

    ```
    cd photosite
    ```

3. Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```
    python manage.py migrate
    ```

5. Start the development server:

    ```
    python manage.py runserver
    ```

6. Access the application at `http://localhost:8000/`.

## Usage
1. Upload your photos through the provided interface.
2. Watermarked versions of your images will be automatically generated.
3. To download the original, non-watermarked versions, make a payment.
4. Once the payment is successful, you can download the original images.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.
