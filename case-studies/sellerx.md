---
company: SellerX
description: "Why ...."
domain: "https://sellerx.com"
founded: "....."
investors: "......"
stats: [
    {
        "metric": ".......",
        "value": "10x"
    },
    {
        "metric": ".....",
        "value": "5x"
    },
]
meta: [
  {
    "name": "keywords",
    "content": "
      python react,
      python web app,
      python web app framework,
      python web apps,
      react python,
      react with python,
      web app python,
    "
  }
]
---

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages.docs import library
```

!!!! Add image of app here !!!!


Meet SellerX, a Berlin-based, high-growth eCommerce player that aims to consolidate Amazon’s most successful sellers, acquiring them to scale their business and turn their brands into global household names. 

SellerX has become one of the largest eCommerce aggregators in the European market. Today it manages more than 50 ecommerce brands. 


## SellerX's overwhelming data processing pipeline

SellerX has teams that collect a lot of data from Amazon to derive insights on which brands to acquire. This was a very manual process of employees looking up information about products, reviews, and prices so they can understand trends and make decisions on companies to look at investing in. They would have to go to Amazon and go to the companies specific websites, copy this information, put it all manually in excel.

Mike Woodcock, the Head of AI & Automation at SellerX, was placed in charge of working with these teams and finding a way to streamline this process of data sourcing. He needed to build a custom interface for the teams to help them collect their data for efficiently. 

His main requirements were that the final product needed to be a web interface, it needed SSO (single sign-on) capabilities, and they needed to be able to iterate quickly.

His plan was to create an app to extract the information and create insights, therefore streamlining the process. The task would run for a day and then the user would open up the app and the information that they need to make decisions on the companies would be there.



## SellerX's struggles with Streamlit

Mike and his team initially started with [Streamlit]("https://streamlit.io"), a python framework to build simple web apps, but it was very limited. Their first concern was with the inefficiencies of the Streamlit framework.


```md quote
- name: Mike
- role: Head of AI
The way they run the code, it is pretty much linear so it always runs again and again and it's super inefficient. Plus there was a lot of memory leaks and inefficiencies that make it not an option for long term projects.
```

Furthermore, Mike and his team found it hard as Streamlit is not built to be event driven.  

```md quote
- name: Mike
- role: Head of AI
Streamlit is not an event based tool, for example you cannot subscribe to a specific on edit event.
```

Lastly, there were issues with the layout and lack of customizability.


```md quote
- name: Mike
- role: Head of AI
Streamlit had very basic layout and you can just keep it and that's it that you have to use that.
```

Overall they found that when they used Streamlit they always needed to go and build the real app again afterwards. Their alternative approach up until now was to build using React with a FastAPI backend.



## How Reflex empowered SellerX

The app Mike and his team were building had several tables of data with images, links and lots of text data. It included web scrapers as well as many api calls.

The app took advantage of Reflex's background events for long running scraping tasks to extract all the data that they needed.

The app used [AG Grid]({library.tables_and_data_grids.ag_grid.path}), which is built into Reflex, to display the data in a table. AG Grid is a high performance data grid that is used in many fortune 500 companies web applications. 

SSO was a requirement for the app, and Mike used Azure Auth, one of the many options provided by Reflex for authentication.

Finally the code was far more organized and maintainable than their previous Streamlit app, and they were able to write more event based code.

```md quote
- name: Mike
- role: Head of AI
With Reflex the code is much more organized and every time the user does something it's more dynamic, more event based.
```


## Why SellerX chose Reflex

The app that Mike and his team built with Reflex was a huge success. It is allowing a team within SellerX to review 5 times more data than before, essentially allowing them to do a whole month of work in less than a week.


```md quote
- name: Mike
- role: Head of AI
A team of 6 non-technical employees use the app to make decisions based on Amazon information. It is allowing this team to be significantly more efficient and structured in the way they work and they are very happy with the improvements in speed. This team is now able to review 5x more Amazon data than their previous approach.
```

Reflex also allowed the team to iterate much faster than using React but with the confidence that they will not need to rebuild their entire app as they would with Streamlit. 


```md quote
- name: Mike
- role: Head of AI
We are moving significantly faster, which has been very very useful. To have a quick call with the end user of the app and then the next day you have a nice basic interface for them to use, to double check if they like the setup, and see if it's going to work, it's just fantastic.
```

```md quote
- name: Mike
- role: Head of AI
With Reflex it is ten times faster than developing with React and FastApi.
```

Finally deployments have been much more straightforward with Reflex.


```md quote
- name: Mike
- role: Head of AI
Also for deploying and everything is significantly easier. It's all just Python. You just open the right ports, add SSO, and then everyone that needs to have access can use the app.
```
