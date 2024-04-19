# fintech_innovators

### Welcome to README of Fintech Innovators project backend on Django REST Framework.

### Deploy is on: https://fintech-innovators-r04f.onrender.com

### Video Presentations is on: https://drive.google.com/drive/folders/1BR_qLzhz5P1JVFfpLAKOqZHvO-NuY4hR?usp=sharing
(If You are having a problems with opening a video please let me know)

In the main page you will just see ERROR 404 Because first of all, I dont have anything in landing page, and second of all, I turned Debug=False, so that other people will not see logs unless you are a developer that works on this project.![In the main page you will just see ERROR 404 Because I turned off Debug=True, so that other people will not see logs unless you are a developer that works on this project.](<images/Screenshot 2024-04-16 at 19.47.29.png>) 
![alt text](<images/Screenshot 2024-04-16 at 19.47.11.png>)
And if you make Debug=True, you can this log page which shows existing urls.
![alt text](<images/Screenshot 2024-04-19 at 14.51.05.png>)
Here are the screenshots from swagger documentation, that shows the api endpoints for Payment application and Users application. For users there are all possible CRUDs. As you could notice in the payments part, You can see your balance and transations by urls below. For that you should send GET requests. And to make a transaction you should send POST request with api /scheme/![Here are the screenshots from swagger documentation, that shows the api endpoints for Payment application and Users application.](<images/Screenshot 2024-04-19 at 14.50.25.png>) 
![alt text](<images/Screenshot 2024-04-19 at 14.50.29.png>) 
![alt text](<images/Screenshot 2024-04-19 at 14.50.33.png>) 
![alt text](<images/Screenshot 2024-04-19 at 14.50.35.png>) 
You can see in the pictures below the tables in both Payments and Users app. It is shown below which fields you should fill and which data types they should be.
And if could notice you should authenticate with JWT token which you can obtain from endpoints.

