# BroBonds
Developed by Team!Alone:

[Joy Zadan](https://github.com/JoyZadan)

[Eduard Viorel Stan](https://github.com/EddieStn)

[Georgina Carlisle](https://github.com/GeorginaCarlisle)

[Radleigh Smith](https://github.com/RadleighSmith)

[Callum Jepps](https://github.com/CJepps)

[Edison Kwan](https://github.com/edisonkwan18)

Image showcasing project to go here



Live link: https://movember1-bac9d403956e.herokuapp.com/

## Contents

[Design](#design)

- [The Strategy Plane](#the-strategy-plane)

- [The Scope Plane](#the-scope-plane)

- [The Structure Plane](#the-structure-plane)

- [The Skeleton Plane](#the-skeleton-plane)

- [The Surface Plane](#the-surface-plane)

[Agile Methodology](#agile-methodology)

[Features](#features)

- [Existing Features](#existing-features)

- [Future Features](#future-features)

[Languages](#languages)

[Tools and Technologies](#tools-and-technologies)

[Testing and Validation](#testing-and-validation)

[Bugs and Fixes](#bugs-and-fixes)

[Deployment](#deployment)

[Credits](#credits)

[Acknowledgements](#acknowledgements)

---

## Design

### The Strategy Plane

#### Project Theme

This project is being created for the “Talking Tech: Men’s Health Reimagined” Movember Hackathon and will focus on Men’s **mental health**.


#### Research into Men's Mental Health

There is clear and well evidenced research showing:

-	Men’s mental health is a very real and current issue.

-	Men are at higher risk of suicide that women, in particular men aged 40-49.

-	There are clear links between loneliness and poorer physical health.

-	There are clear associations between loneliness and poorer mental health.

-	Loneliness is an area where more needs to be done.

However, there is little current research around how loneliness is most effectively tackled. With the suggestion that a 
> range of approaches may be required, tailored to fit people’s individual experiences of loneliness and contexts. 

<details>
<summary>
Detailed account of research
</summary>

[Mental Health Foundation](https://www.mentalhealth.org.uk/explore-mental-health/a-z-topics/men-and-mental-health)

The above website provided key insight into men’s mental health with our takeaways from the information being:
-	Men’s mental health is a very real and current issue. 
-	Three times as many men as women die by suicide.
-	Men aged 40 to 49 have the highest suicide rates in the UK.
-	Men are less likely to access psychological therapies than women.
-	A range of underlying factors make it harder for men to reach out for help and open up.
-	Men may also be more likely to use potentially harmful coping methods (example: drugs, alcohol, escapism) and less likely to talk to family or friends about their mental health.
-	Positively research suggest men will get the help that meets their preferences and is easy, meaningful and engaging.

[Suicide risk factors for middle aged men](https://www.samaritans.org/about-samaritans/research-policy/middle-aged-men-suicide/suicide-risk-factors-middle-aged-men/)

The above document provided further insight into the research around why Men aged 40 to 49 have the highest suicide rates. Key takeaways:
-	In terms of age, gender and socio-economic status, the group most at risk of suicide are middle-aged men from disadvantaged backgrounds.
-	Factors that play a role in suicide risk include: personality traits, masculinity, challenges of mid-life, relationship breakdown, emotional illiteracy and socio-economic factors.
-	Suicide prevention policy and practice must take account of men’s beliefs, concerns and context.
-	Recognition that for men in mid-life, **loneliness is a very significant cause of their high risk of suicide**, and (prevention policy and practice must) **enable men to strengthen their social relationships**.

[Tackling loneliness evidence review: main report](https://www.gov.uk/government/publications/tackling-loneliness-evidence-review/tackling-loneliness-evidence-review-full-report#what-we-know-and-what-we-do-not-know-about-loneliness)

The above document (updated March 2023), which is mainly geared towards building the evidence around loneliness summarised what the **current research** shows. Key quotes from the document:
‘Indeed, there is now **exhaustive work linking loneliness to poorer physical health** during adulthood.’
‘There is now cross-sectional evidence to support the **association between loneliness and a range of psychiatric disorders**, including anxiety, depression, and psychosis, and to support an **association between loneliness and suicidal thoughts and behaviour**.’
‘Evidence from a systematic review and meta-analysis shows **loneliness is a significant predictor of both suicidal ideation and behaviour, with depression potentially the link between loneliness and suicidal ideation/behaviour** (McLelland et al., 2020)’.

The document also went into current research about the effectiveness and acceptability of interventions to address loneliness and mental health problems:
‘Available evidence about the determinants of loneliness in people with mental health problems suggest a **range of approaches may be required, tailored to fit people’s individual experiences of loneliness and contexts. For some, loneliness is strongly linked to social isolation and lack of supportive social contact; for others; psychological factors including perceived social threat and sense of belongingness are important drivers of loneliness.** Different intervention options to meet these needs are desirable.’
However:
“In most cases what we have are preliminary studies that show approaches are feasible and acceptable, but do not provide definitive evidence.”

</details>

#### Project Focus

Our team has chosen to focus on the need for innovation in how we can tackle loneliness, designing a solution tailored towards men and taking into account their preferences and the barriers they may face.

It is to be noted that there are two sides to loneliness:

-	social isolation and lack of supportive social contact

-	psychological factors including perceived social threat and sense of belongingness

Our solution will initial be focused on providing an innovation solution to tackling social isolation and lack of supportive social contact. Once the platform is in use and has been scaled up, the next area of growth will focus on how the platform can be used to tackle the psychological factors associated with isolation.

#### Target User Group

Men with a special focus towards men aged 40-49. 

Note, while this is the target user group it is important that the project created remains open to all.


#### Problem Statement

“I am a man aged 40 – 49 experiencing loneliness due to social isolation and a lack of supportive social contact. I feel shy, anxious about connecting with others and embarrassed to reach out and ask for help. My loneliness is a contributing factor in my decreasing physical and mental health and is also increasing my risk factor for suicide.”

#### Project Aim

To create a plaform where men can come together and connect with others over shared interests. They will be able to create and comment on blog posts and sign up to online and in-person events. 

Uniquely, the platform will be designed to provide as few as possible barriers for men initially joining the platform (no expectations and the option to remain anonymous). As they grow more comfortable and at ease on the platform they can choose to start contributing and become more visible. When ready, they can then take the next steps into asking questions about events and then signing up and going along. 

#### Mission Statement

“When the leap is too great, step by step the impossible becomes achievable. Supporting men across the chasm from loneliness to connection, friendship and belonging, through shared interests.”

The flow chart below plans how users might negotiate that chasm step by step through our site.

![Flow diagram showing how a user might negotiate the chasm between loneliness to connection, friendship and belonging](documentation/readme-images/negotitating-the-chasm.drawio.png)

[Return to contents list](#contents)

---

### The Scope Plane

The scope of this project is provided by user stories, organised below by epic and then role.

#### EPIC - General User Account

As a new user I can register for an account so that I can access registered user only content and create and comment on blogs.

As a registered user I can use my username and password to login to my account so that my account remains secure and only I can login.

As a signed-in user I can easily logout of my account so that I can keep my account secure.

As a registered user I can reset my password so that I can still log into my account if I forget my password

As a signed-in user I can access and edit my profile information so that I can make changes or add additional preference or information.

As a site admin I can remove accounts so that I can prevent unsuitable users from accessing and using the platform.

As a signed-in user I can click on the picture of a fellow user and bring up there about me information so that I can get to know my fellow user

#### EPIC - Facilitator Account

As a registered user I can apply to become a facilitator so that I can support other users, contribute to the platform and create and host events.

As a site admin I can authorise an application to become a facilitator so that I can ensure only suitable users can become facilitators.

#### EPIC - Visiting User Experience

As a new user I can understand what this website is about and the potential value I can gain from it so that I can decide whether I would like to explore the site further and sign up.

As a new user I can read blog posts about a range of interests so that I can gain an idea of the value I might gain by registering for the platform.

As a user I can contact the site owner so that provide feedback or ask any questions I may have.

As a new user I can read frequently asked questions so that I can find out the answers to some of my questions and concerns.

As a new user I can find out who created this platform and why so that I can understand more about what this platform is about and who it was created by.

#### EPIC - Navigation

As a new user I can navigate easily and intuitively to all available content so that I can quickly find what I need.

As a signed-in user I can navigate easily and intuitively to all registered user content so that I can quickly find what I am looking for.



#### EPIC - Blogs

As a signed in user I can view all blogs so that read and find out about different areas of interest.

As a signed-in user I can create a blog so that I can share information about something that interests me.

As a signed-in user I can edit a blog I have created so that I fix any mistakes or make changes.

As a signed-in user I can search the blogs by entering a key term so that I can find specific blogs.

As a signed-in I can view blogs in order of preference based on my interests so that I am shown the blogs most relevant to me first.

As a signed-in user I can filter the blogs according to different options so that I can control the order in which the blogs are shown.

As a site admin I can remove blogs so that I can ensure only positive and relevant blogs are available on the platform.

#### EPIC - Blog Commenting

As a signed-in user I can view all comments associated with a blog so that follow the conversation.

As a signed-in user I can comment on blogs so that I can share my thoughts and contribute.

As a signed-in user I can edit any comments that I have made so that I can fix any mistakes made when posting.

As a signed-in user I can delete any of my comments so that I can change my mind and remove my comment.

As a site admin I can remove comments so that I can ensure the platform remains positive and respectful, was comments inline with the purpose of the platform.

#### EPIC - Events

As a Signed-in user I can view all events so that I see what is coming up.

As a signed-in user I can view events ordered to show my preferences and events close to me first so that I can view the most relevant events first.

As a signed-in user I can choose how to filter and order events so that I can control the order in which the events are shown.

As a signed-in user I can use keywords to search for specific events so that I can locate specific events.

As a signed-in user I can comment on events so that I can ask questions about the event, pass on positive reviews, or let others know I'm thinking of attending.

As a signed-in user I can sign up to attend events so that I can let the organisers know I wish to attend.

As a facilitator I can create and post events so that I can provide opportunities for users to meet and connect through a shared interest.

As a facilitator I can edit event details so that I can fix a mistake or update information should things change.

As a facilitator I can delete events I created so that I remove the details from a past event, or an event that has been cancelled.

As a facilitator I can view a list of users who have signed up to the event so that I know how many people might turn up and who.

As a site admin I can remove events so that I can remove past events, events that may pose a threat or events not inline with the aim of the platform.

As a site admin I can remove event comments so that I can ensure the platform remains positive and respectful.

[Return to contents list](#contents)

---

### The Structure Plane


[Return to contents list](#contents)

---

### The Skeleton Plane

#### Wireframes

Before diving into development, our project harnessed wireframing techniques to meticulously structure the platform's user interface. These wireframes formed the bedrock of our design, mapping out the strategic placement of essential elements and interactions. This early visualization of the layout played a crucial role in refining the user experience, guaranteeing intuitive navigation and seamless interaction for our users. This systematic approach not only guided our development efforts but also paved the way for crafting a polished, user-centric platform interface.

#### Desktop

* Home page

<img src="documentation/readme-images/home-page-wireframe.png">

***
* Blog / Events Page

<img src="documentation/readme-images/blog-event-page-wireframes.png">

***
* Upload Blog / Event Page

<img src="documentation/readme-images/add-blog-event-page-wireframes.png">

***
* Registration Page

<img src="documentation/readme-images/registration-page-wireframes.png">

***
* Login Page

<img src="documentation/readme-images/login-page-wireframes.png">

***
* Account Page

<img src="documentation/readme-images/account-page-wireframes.png">

***

#### Mobile

During UI design, our focus on mobile convenience didn't compromise the desktop experience. We implemented a responsive design approach that seamlessly accommodates both mobile and desktop users. The relocation of the navigation bar to the bottom for mobile usage didn't hinder the functionality or accessibility on desktop. This approach ensured that users, regardless of their device, could navigate the site with ease, offering a consistent and intuitive experience across various platforms.

* Home Page mobile

<img src="documentation/readme-images/home-page-mobile-wireframes.png">

***
* Blog / Events Page mobile

<img src="documentation/readme-images/blogs-events-mobile-wireframes.png">

***
* Upload Blog / Event Page mobile

<img src="documentation/readme-images/add-blog-event-mobile-wireframes.png">

***
* Registration Page mobile

<img src="documentation/readme-images/register-moblie-wireframes.png">

***
* Login Page Mobile

<img src="documentation/readme-images/login-mobile-wireframes.png">

***
* Account Page Mobile

<img src="documentation/readme-images/account-page-mobile-wireframes.png">



[Return to contents list](#contents)

---

### The Surface Plane

#### Typography

##### Headings: Kanit

We've chosen Kanit for our headings to infuse a sense of modernity and elegance into our platform. Kanit's clean and stylish appearance adds visual interest to headers, making them stand out while maintaining readability and professionalism.

##### Body Text: Roboto

For the body text, we've opted for Roboto for its excellent readability across various screen sizes. Roboto's clean and versatile style ensures a comfortable reading experience for users, enhancing content legibility and clarity throughout the platform.


Our choice of Kanit for headings and Roboto for body text from [Google Fonts](https://fonts.google.com/) aims to establish a consistent and unified typographic style. This deliberate selection ensures a seamless visual flow, guiding users through content effortlessly while presenting a cohesive and refined interface.

#### Color Scheme

Our platform is designed as a vibrant and welcoming space, dedicated to fostering connections and combatting loneliness through shared interests. The choice of colours plays a pivotal role in crafting this user experience. The background, adorned with #f5f5f5, sets the backdrop, ensuring content clarity. Headers and footers feature #93B8BF, imbuing a sense of coherence and continuity throughout the platform. To prompt actions and engagements, #FFAE42 energizes the calls to action, inviting users to participate actively in the community. The hero text container, highlighted in #e6e1c5 against hero images, evokes warmth and readability, drawing attention to key messages. Within cards showcasing blogs and events, #667a92 infuses a touch of elegance to titles, adding visual interest and aiding in content categorization. Finally, #000 delivers crisp and legible text, ensuring readability across all interactions, fostering a seamless and engaging experience.

[Colormind.io](http://colormind.io/) played a crucial role in our colour selection process. We used its tools to explore different combinations, aiming for colours that feel inviting, coherent, and engaging. After trying various options, we settled on a palette that reflects our commitment to fostering connections and combating loneliness. These colours blend well, offering a balance between calming backgrounds and vibrant elements like call-to-action prompts, ensuring readability and visual appeal throughout the platform. Colormind.io was instrumental in helping us create a cohesive and inviting visual identity that aligns with our platform's mission.

<img src="documentation/readme-images/colormind-screenshot.png">

Ensuring accessibility and readability for all users is paramount. We utilized [contrast-grid.eightshapes.com](https://contrast-grid.eightshapes.com/) to evaluate and fine-tune our colour choices. By assessing the contrast ratios, we confirmed that our selected palette meets accessibility standards, guaranteeing clear legibility and visual clarity across our platform. This tool enabled us to verify that our colour combinations maintain adequate contrast, supporting inclusivity and a seamless user experience for everyone.

<img src="documentation/readme-images/contrast-grid-screenshot.png">

[Return to contents list](#contents)

## Agile Methodology

Agile values and principles have been followed in the creation of this project. In particular the following common Agile practices have been followed:

- user stories
- product backlog
- prioritization
- information radiators
- iteration cycles

[Return to contents list](#contents)


## Features

### Existing Features

The existing features provide the following project requirements:

### Project Name
<img src="documentation\readme-images\project-name.png">

The project name is displayed consistently at the top of all three pages.

### Footer
#### Footer in laptop view
<img src="documentation\readme-images\footer.png">

#### Footer in mobile view
<img src="documentation\readme-images\mob-footer.png">

The footer is displayed at the bottom of all pages. It has been styled to be sticky. All footer links open in a new tab

The footer includes:
- Photo of every team member
- LinkedIn profile of every team member
- The purpose of the website

### Landing page

There are two landing pages. One is before login and one is after login.

#### Landing page (Before Login)
[image of before]

#### Landing page (After Login)
[image of after]

The landing page includes:
- A short introductory paragraph of BroBonds
- A short slogan to call
- Static image of Hero image for welcome
- Clearly visible buttons to access the signup page
- 3 cards present ‘Latest Blog’, ‘Popular Blog’ & ‘Latest Event’

### Sign-up page
<img src="documentation\readme-images\sign-up.png">

The sign-up includes:
- A short paragraph of declaration to confirm users are 18 years old or above
- A clear link will refer to login page if users have their account.
- A field for users to fill their email address
- A field for users to setup their username (The name shows on blog and event)
- A field for users to setup their password
- A field for users to fill their preset password for validation
- Clearly visible buttons to submit the signup form

### Favicon and page titles
<img src="documentation\readme-images\favicon.png">

A favicon has been included and each page has a title of my app name \"BroBonds\".

### About us page
<img src="documentation\readme-images\about-us.png">

The About us page includes:
- 3 paragraphs to introduce BroBonds
- Static image of mens talk

### FAQ page
<img src="documentation\readme-images\faq.png">

TheFAQ  page includes:
- 6 paragraphs to explain questions asked frequently by user


### Log in page
<img src="documentation\readme-images\log-in.png">

The Log in page includes:
- A clear link will refer to sign up page if users need to sign up their account.
- A field for users to fill their user name
- A field for users to fill their password
- A checkbox to memorize the user log in data
- Clearly visible buttons to submit the form then direct to landing page after log in

### After user log in

### My Profile page (Normal user)
<img src="documentation\readme-images\profile-nonfac.png">

The my profile page includes:
- A user profile image
- User alias to display if they want to be anonymous
- Image file upload for the user profile image
- A field for users to fill their about me information 
- Check to decide to be anonymous (tick = anonymous)
- Clearly visible buttons to submit the request to be a facilitator and wait for decision of admin
- Clearly visible buttons to submit the form

### My Profile page (Facilitator)
<img src="documentation\readme-images\profile-fac.png">

The my profile page includes:
- A user profile image
- User alias to display if they want to be anonymous
- Image file upload for the user profile image
- A field for users to fill their about me information 
- A paragraph of statement of your status as a facilitator
- Clearly visible buttons to submit the request to be a facilitator and wait for decision of admin
- Clearly visible buttons to submit the form

### Blog list page
<img src="documentation\readme-images\blog-list.png">

The blog list page includes:
- Clearly visible buttons to create the blog
- A search function field to search blog with keyword
- Blogs showing detail as below
- Blog title
- Author
- Content
- Create time
- Number of Like
- Number of Comments
- List of interests
- Clearly visible buttons to view the entire blog

### Blog page
<img src="documentation\readme-images\blog.png">

The blog page includes:
- Static image of the blog
- Blog title
- Author & create time
- List of interests
- Content of the blog
- Number of Like and comments
- Clearly visible buttons to like the blog
- Comments section if users leave comment and it will show
- Leave comment section with the name of posting and comment
- Clearly visible buttons to submit the blog

### Create Blog page
<img src="documentation\readme-images\create-blog.png">

The create blog page includes:
- A field for users to fill the title of the blog
- A field for users to fill the content of the blog
- A field for users to fill the interests related to the blog
- A field for users to upload the image related to the blog
- Clearly visible buttons to submit the blog

### Get Together
### Event list page
[image of event list]

The create blog page includes:
- Event title
- Image of the event
- Organizer
- Categorry of interests
- Event type: Face to Face / Hybird / Virtual
- Event date
- Event time
- Location
- Description
- Maximum Participants
- Signup Deadline
- Community members who already registered
- Clearly visible buttons to join the event

### Create event page
[image of create event]

The create blog page includes:
User can fill detail below
- Event title
- Categorry of existing interests
- Categorry of new interests
- Image of the event
- Organizer
- Event type: Face to Face / Hybird / Virtual
- Event date
- Event time
- Location
- Description
- Maximum Participants
- Signup Deadline
- Community members who already registered
- Clearly visible buttons to join the event

### Log out page
<img src="documentation\readme-images\logout.png">

The log out page includes:
User can fill detail below
- a description to gudie user to return home
- Clearly visible buttons to return home


[Return to contents list](#contents)


### Future Features

[Return to contents list](#contents)


## Languages

During the development phase, we leveraged a comprehensive stack of technologies to ensure a robust and efficient web application. HTML served as the backbone for structuring the content and layout of our web pages, allowing us to define elements and organize information effectively.

CSS played a crucial role in enhancing the visual appeal and user experience of our platform. With CSS, we applied styles, customized layouts, and ensured a consistent design language throughout the application, providing an engaging interface for our users.

Python, being the primary programming language, powered the backend of our application. We utilized Django, a powerful Python web framework, to streamline development tasks, manage databases, handle URL routing, and facilitate rapid development. This choice allowed us to build a scalable, maintainable, and secure application.

Moreover, integrating Bootstrap into our project significantly expedited front-end development. The framework offered a collection of responsive design components and pre-styled elements, enabling us to create a user-friendly and visually appealing interface while ensuring compatibility across various devices and screen sizes. Overall, this technology stack facilitated a seamless development process and enabled us to create a feature-rich, user-centric web application.

### Languages:

HTML,
CSS,
Python

### Frameworks/Libraries/Tools:

Django (Python web framework),
Bootstrap (Front-end framework for CSS)

Additional Packages Used:

- asgiref==3.7.2
- black==23.11.0
- certifi==2023.11.17
- cffi==1.16.0
- charset-normalizer==3.3.2
- click==8.1.7
- cloudinary==1.36.0
- colorama==0.4.6
- crispy-bootstrap5==2023.10
- cryptography==41.0.5
- defusedxml==0.7.1
- dj-database-url==2.1.0
- Django==4.2.7
- django-allauth==0.58.2
- django-cloudinary-storage==0.3.0
- django-crispy-forms==2.1
- django-resized==1.0.2
- django-richtextfield==1.6.1
- gunicorn==21.2.0
- idna==3.4
- mypy-extensions==1.0.0
- oauthlib==3.2.2
- packaging==23.2
- pathspec==0.11.2
- Pillow==10.1.0
- platformdirs==4.0.0
- psycopg2==2.9.9
- pycparser==2.21
- PyJWT==2.8.0
- python3-openid==3.2.0
- requests==2.31.0
- requests-oauthlib==1.3.1
- six==1.16.0
- sqlparse==0.4.4
- tomli==2.0.1
- typing_extensions==4.8.0
- tzdata==2023.3
- urllib3==2.1.0

These tools and packages collectively contributed to the successful development of the project, ensuring a robust and feature-rich web application.


[Return to contents list](#contents)


## Tools and Technologies

[GitHub](https://github.com/) - Stores the repository for this project so that it can be contributed to by all members of the team. A number of github tools were also used to aid Agile development.

[git](https://git-scm.com/) - Controlled the building of this project in a series of versions which can be tracked.

[Visual Studio Code](https://code.visualstudio.com/) - The editor in which this project was built. 

[Return to contents list](#contents)


## Testing and Validation

[Return to contents list](#contents)


## Bugs and Fixes

[Return to contents list](#contents)


## Deployment

# Development and Deployment
## Local development
* Create your Django app. In the terminal write the following in order:
    1. Install Django and gunicorn: `pip3 install django gunicorn`
    2. Install database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`
    3. Install Cloudinary libraries to manage photos: `pip3 install dj-3-cloudinary-storage`
    4. Create file for requirements file: `pip freeze --local > requirements.txt`
    5. Create your project: `django-admin startproject your_project_name .` ( remember the . at the end)
    6. Create your app: `django-admin startapp your_app_name`
    7. Migrate: `python3 manage.py makemigrations` and `python3 manage.py migrate`
    8. Run the server to test if the app is installed: `python3 manage.py runserver`

## Heroku deployment
### The site was deployed via Heroku. The live link can be found here - [Inventory](https://)

* To deploy the project through Heroku I followed these steps:

    * Sign up / Log in to Heroku
    * From the main Heroku Dashboard page select `New` and then `Create New App`
    * Give the project a name - in my case inventory-es and select a `region`, then select `create app`.
    * This will create the app within Heroku.
    * For the database, I used ElephantSQL
        * Navigate to ElephantSQL.com and log-in/sign-up.
        * Create new instance
        * Choose a name and the free plan, tags can be left blank
        * Select a region and click Review and then Create
        * From the dashboard, select the created instance and copy the URL to the clipboard
    * To save static and media files, I used Cloudinary
        * Navigate to cloudinary.com and log-in/sign-up.
        * From the dashboard - copy the CLOUDINARY_URL to the clipboard
    * In Heroku navigate to the setting tab and scroll utill you find `Reveal config vars`.
    * Add to the config vars DATABASE_URL as the KEY and paste the URL from your ElephantSQL as the VALUE
    * Add to the config vars CLOUDINARY_URL as the KEY and paste the URL as the VALUE
    * Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
    * This key value pair must be removed prior to final deployment
    * In the root directory of your repository in github create a new file called `env.py` and write the following code:
        ```
        import os

        os.environ["DATABASE_URL"]="postgres://url"
        os.environ["SECRET_KEY"]="your secret key"
        os.environ["CLOUDINARY_URL"]="cloudinary://url"
        ```
    * Add the secret key just created to the Heroku Config Vars. SECRET_KEY as the KEY and the secret key value you created as the VALUE
    * In settings.py write the following code:
        ```
        from pathlib import Path
        import os
        import dj_database_url
        if os.path.isfile('env.py'):
            import env
        ```
    * Replace the secret key that django has in the settings.py with `SECRET_KEY = os.environ.get('SECRET_KEY')`
    * Comment out the default database and replace it with:
        ```
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
        ```
    * Make migrations:
        * python3 manage.py makemigrations
        * python3 manage.py migrate
    * In the following order, add the Cloudinary libraries to the Django settings.py section for installed apps:
        ```
        'cloudinary_storage'
        'django.contrib.staticfiles',
        'cloudinary',
        ```
    * Add the following in settings.py to connect Cloudinary to Django:
        ```
        STATIC_URL = '/static/'
        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        ```
    * Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    * Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
    * For the `ALLOWED_HOSTS` add your heroku url and your localhost:
        ```
        ALLOWED_HOSTS = ['inventory-es.herokuapp.com', 'localhost']
        ```
    * In your root directory, create three new top folders: media, static and templates
    * Create a `Procfile` file in the root directory
    * Within the Procfile add the code - `web: guincorn PROJECT_NAME.wsgi`
    * In the terminal, add the changed files, commit and push to GitHub
    * In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
    * Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

## Final Deployment

* Upon completion of development, change in settings.py DEBUG = True to DEBUG = False
    * To have DEBUG set to true for your local development and false for Heroku:
        * In env.py add another line `os.environ['DEV'] = 'Yes please!'` ( note that the value you set does not matter )
        * In settings.py and DEBUG = False to `DEBUG = 'DEV' in os.environ`
* In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0
* 'Choose a branch to deploy' should be 'main' and search for your repository
* To manually deploy click the button 'Deploy Branch'
* Your app was successfully deployed will be displayed when the app is deployed.
* The deployed app will appear in the browser after you click "view."

## Forking and Cloning

## Forking a repository
### A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.
1. On GitHub.com, navigate to https://github.com/EddieStn/inventory.
2. In the top-right corner of the page, click Fork.

## Cloning your forked repository
### Right now, you have a fork of the Inventory repository, but you do not have the files in that repository locally on your computer.
1. On GitHub.com, navigate to your fork of the inventory repository.
2. Above the list of files, click Code.
3. Copy the URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub username instead of YOUR-USERNAME:
   - git clone https://github.com/YOUR-USERNAME/movember
7. Press Enter. Your local clone will be created.

[Return to contents list](#contents)


## Credits

* [Uizard.io](https://uizard.io/) for facilitating intuitive wireframing and seamless UX design.
* [Draw IO](http://draw.io/) Create flow diagrams during design
* [Google Fonts](fonts.google.com/) Fonts (Kanit, Roboto)
* [Colormind IO](colormind.io/) To generate the color scheme
* [Contrast Grid](contrast-grid.eightshapes.com) For the contrast grid to check accessibility between colors 
* [Favicon](favicon.io) Convert image to favicon
* [Ideogram](ideogram.ai) Design the draft of logo

### image
| Name     | Link                                                                                                                                                                                                                                         | Where or why used            | Author                  |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------- |
| Unsplash | [https://unsplash.com/photos/row-of-four-men-sitting-on-mountain-trail-TkrRvwxjb_8](https://unsplash.com/photos/row-of-four-men-sitting-on-mountain-trail-TkrRvwxjb_8)                                                                       | Used as the Hero Image       | Matheus Ferrero         |
| Pexels   | [https://images.pexels.com/photos/17249634/pexels-photo-17249634/free-photo-of-a-rock-band-with-electric-guitars.jpeg](https://images.pexels.com/photos/17249634/pexels-photo-17249634/free-photo-of-a-rock-band-with-electric-guitars.jpeg) | Used of blog about music     | Siahei Dalivelia        |
| Unsplash | [https://unsplash.com/photos/man-standing-on-rock-looking-towards-lake-BKLHxgbYFDI](https://unsplash.com/photos/man-standing-on-rock-looking-towards-lake-BKLHxgbYFDI)                                                                       | Used of blog about hiking    | Sébastien Goldberg      |
| Unsplash | [https://unsplash.com/photos/a-man-riding-a-bike-down-a-sidewalk-kFVAB4_0Es4](https://unsplash.com/photos/a-man-riding-a-bike-down-a-sidewalk-kFVAB4_0Es4)                                                                                   | Used of blog about cycling 1 | jatinder nagra          |
| Unsplash | [https://unsplash.com/photos/man-in-black-jacket-riding-bicycle-on-road-during-daytime-jWpXo26edEE](https://unsplash.com/photos/man-in-black-jacket-riding-bicycle-on-road-during-daytime-jWpXo26edEE)                                       | Used of blog about cycling 2 | Jordan Brierley         |
| Unsplash | [https://unsplash.com/photos/man-sitting-beside-cup-of-coffee-x7h5HLsBYwo](https://unsplash.com/photos/man-sitting-beside-cup-of-coffee-x7h5HLsBYwo)                                                                                         | Used of blog about reading   | Viktor Forgacs          |
| Unsplash | [https://unsplash.com/photos/three-men-laughing-while-looking-in-the-laptop-inside-room-XkKCui44iM0](https://unsplash.com/photos/three-men-laughing-while-looking-in-the-laptop-inside-room-XkKCui44iM0)                                     | Used of event about reading  | Priscilla Du Preez 🇨🇦 |
| Komoot   | [https://www.komoot.com/smarttour/1189112996](https://www.komoot.com/smarttour/1189112996)                                                                                                                                                   | Used of event about cycling  | Rombea                  |
| Unsplash | [https://unsplash.com/photos/man-in-blue-polo-shirt-talking-to-man-while-drinking-coffee-l4dZ4h6vL6o](https://unsplash.com/photos/man-in-blue-polo-shirt-talking-to-man-while-drinking-coffee-l4dZ4h6vL6o)                                   | Used on the about us page    | <br>Shane Rounce

[Return to contents list](#contents)


## Acknowledgements

[Return to contents list](#contents)
