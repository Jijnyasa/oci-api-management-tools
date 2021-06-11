# API Management Service

## Problem Statement

- Developers often interact with API's while developing features, while testing changes in preprod or production.
- Even people doing operations sometimes interact with the API's for looking some configurations or just debugging a issue.
- Even though we have amazing tools such as CLI/SDK , no one can overlook the importance of API's in one's life. 
- People working with UI have little knowledge about tool such as CLI/SDK and API's are more handy for them even if they get something like api-sec.
- Now when we have devenv(local development setup), need to interact with API has increased as now we want to interact with each microservice.

## Solution

- We need some kind of a directory for API's like a phone directory, you just narrow down your search to a particular person and just call him.
- This directory should be very intuitive to use and should be very handy.
- This directory should not have a different piece of software, it should be something which can be a added on to something lets say a browser.
- This directory should have a support for national as well as international numbers , in context of distributed system we could look up for our own service as well as sister service.
- Even the endpoint should be intuitive as well.
- Whenever there is some change in API specs , it should be reflected without any additional effort.

## Pre-Requisite Knowledge

- Every browser has a thing known as bookmarks. We must be familiar with as we use that feature daily to save our quick go to links, manage important pages.
- Most of the resources have a api-spec which has the specifications for all endpoints including its return point and params.
- This can be automated very easily with some intelligent logics such as grouping endpoints, abbreviating them.

## How this looks

<img width="1440" alt="Screenshot 2020-07-09 at 5 07 01 PM" src="https://user-images.githubusercontent.com/46473694/121732026-5111c880-cb0f-11eb-9e4a-b98cfe65c1a1.png">

###Setup Tools

1. tar -xvf oci-api-management-tool
2. cd oci-api-management-tools
3. virtualenv -p /usr/bin/python2.7 env
4. source env/bin/activate
5. pip install -r requirements.txt

###Generate Bookamark

1. ipython
2. from bookmark_manager.bookmark_handler import BookmarkHandler
3. a=BookmarkHandler()
4. a.do_magic()
