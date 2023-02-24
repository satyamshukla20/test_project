# TEST-CONDUCTING-PROCTORING-EXTENSION(MY FIRST EXTENSION)

## Steps to install the extension:

1. Clone this repository into your system.
2. Get in your virtual environment.
3. Install all the packages mentioned in requirements.txt
4. Start the server by default(127.0.0.1:5000)
5. Go to your Browser and click on the Extension icon and select the manage extensions.
6. On the top right corner of the screen, switch to developer mode and then select Load unpacked.
7. From the drop down menu select the src folder present in the cloned repository.
8. Pin the extension and to start it click on the icon.


## To set up watching photos getting stored on cloud (cloudinary)---this additional feature if you are not doing it then also photos will be stored locally in your system.:

1. Go to cloudinary[https://cloudinary.com/users/register_free#gsc.tab=0] and register if not already. If you are already registered then login [https://cloudinary.com/users/login#gsc.tab=0]
2. get your cloudinary url and set it in the environment variables as 'CLOUDINARY_URL'.

## To Run the project:

1. Start the extension form the website you want to start test let's say ['https://ide.geeksforgeeks.org/']
2. Fill the details like name ,email and invitation code 
3. click on start test.As soon as you do this a new tab to proctor your test will open.
4. If you have not given camera and microphone permission give it.
5. Now you're being proctored and your images are clicked at interval of 5 seconds(the mentioned interval was 3 minutes but i made it 5 for better understanding of project).
6. There's also an Admin dashboard to look at the Test giver's details and photos.
7. For going to admin dashboard hit the url-[http://127.0.0.1:5000/dashboard]
8. you can see all the details of all user who have started the test.
9. Now photos are stored both on the local database as well as the cloud storage(cloudinary).
click on the buttons to check out the phot.



Note: If the extension doesn't show the listed behavior then kindly reload the extension from the browser's extension settings and clear the errors first.



Here's the url for looking at the video of working condition of the project.-[https://drive.google.com/file/d/13NRv-zfrdzBacJZkFehert49cKjw4hfc/view?usp=share_link]



#### Issues while building the project.
Extension was the one thing i had no idea about so learning that was crucial.Also there was issue with not able to get photos from background.js file cause of google's privacy policy so had to changed the approach.Third issue was to ask camera permission which was not provided in manifest.json by google so had to think other way around.But now all these issues have been taken care of and the app works perfectly fine.



Thanks for visiting and Reading.
Om namah shivaay.