# Building a Serverless Website

## Overview
**What you'll learn**

In this section, you'll learn
1. What serverless computing is
2. How to set up Amazon Lambda functions to interface with APIs

...and you'll build a website using all of the above technologies!

**Prerequisites**
1. An AWS Account
2. How to set up a static website using S3 - [Hosting a Static Website Using Amazon S3](https://github.com/HackBinghamton/CloudComputingWorkshop/blob/master/S3/StaticWebsiteUsingS3.md)

## Introduction

Serverless computing is a model of cloud programming where a cloud provider operates the server which handles back-end needs. This can be really useful, because it allows you to run large applications without needing to purchase and maintain servers!

A reasonable person might find themselves scratching their head upon hearing the phrase "serverless". After all, how can 
a website exist without some kind of servers powering it? What kind of machinery allows this to happen? Is serverless
more expensive than a server-based approach?

Fortunately, "serverless" is a bit deceptive. A serverless application is simply an application where the developers
don't have to worry about the underlying hardware powering their application. While a server-based approach would require
a developer to worry about spinning up EC2 instances and scaling their EC2 fleet up and down, a serverless approach
would abstract away all of these concerns. A serverless approach yields several benefits, including

1. Effortless scaling - No code or infrastructure needs to be developed to scale a service up or down. This is all handled 
by the cloud provider (AWS).
2. A pay for what you use pricing model. If your website requires 24/7 uptime but is only used for 12 hours of the day,
you're paying for 12 wasted hours of compute time. A serverless website will only incur fees when it is used.


## Serverless AWS Services
AWS offers several serverless services (phew, what a sentence!). Here are some notable services - the bolded ones will 
be covered in this section.

**S3** - A simple object-based file system.

DynamoDB - A NoSQL, document-based database.

**Lambda** - AWS's serverless computing solution. EC2 is to Lambda what server-based is to serverless.

**API Gateway** - Allows invocation of Lambda functions via exposed API endpoints.

SQS - The first AWS service ever created, this allows tasks to be produced and consumed from a shared queue.


## Our First Serverless Website 
We're going to create a serverless website that allows users to put images on a shared digital refrigerator (yes, literally).
We'll accomplish this goal by doing the following:
1. Creating an S3 bucket that will contain
    1. The most recent fridge picture
    2. Our website's static code
2. Creating an AWS Lambda function that adds a new image to the fridge and updates the fridge picture in the S3 bucket
3. Creating a REST API in API Gateway that invokes this Lambda function
4. Creating static code for our website that calls the REST API and gives it an image URL

Let's dive in!


## Setting Up Our S3 Bucket
*Disclaimer: This section assumes that you've worked with S3 before, so it will be a little less descriptive than the following
sections. If you find yourself struggling, check out the S3 section of our workshop!*

1. Go to the AWS console > Storage > S3
2. Create a new bucket
3. Leave the "configure options" section with its preset values
4. **Disable** block all public access, since we're only working with two files that need to be public anyways.
5. Finish creation, and upload the website.html and fridge.png files provided in this directory of the repository, 
granting public read access to both of them.
6. Go to `fridge.png`'s properties, and update its metadata so that the `Content-Type` is "image/png".


## Creating a Lambda Function
1. Head back over to the AWS console. You'll find Lambda under **Computer**, below EC2.
2. Go to "Create a Function".
    1. Select "Author from Scratch"
    2. Name your function something descriptive (our code will be adding something to the fridge, so why not AddToFridge?)
    3. Choose **Python 3.7** as the runtime.
3. After a few seconds, our Lambda function will be created and ready for configuration.
4. The first thing we're going to do is make sure our Lambda function can actually access our S3 bucket. To do so, head over to the "Permissions" tab and click on the hyperlink to our execution role. This brings us to the IAM console, which will allow us to modify the policies of our Lambda's role.
5. Press "Attach Policies", search for AmazonS3FullAccess, and add that policy to the executor role.
6. With that out of the way, let's take a look at the `lambda_function.py` file located in this repository. It's not 
important to understand what's going on with the image manipulation code, but it is important to understand the code
that interacts with our S3 bucket. 
    * All Python lambda function files must be called `lambda_function.py`
    * They must also have an entry function with the signature `lambda_handler(event, context)`
7. Replace the bucket name with your actual bucket name and add `lambda_function.py` to `function.zip`
    * This zip file contains the libraries you need to run this code on AWS Lambda. It was, in the most unparliamentary language,
    a MASSIVE pain in the ass to get PIL working with Lambda, so using this zip file will make your life much easier. 
    * On Linux and OS X, can do `zip -g function.zip lambda_function.py`
    * Not sure on Windows, but all you have to do is replace the `lambda_function.py` in the zip file with your own
8. Head back to the configuration view in the Lambda console. Scroll down to the **Function code** section, go to **Actions**, 
and select **Upload a .zip file**.
9. We need to increase the capacity and timeout of our Lambda function, since this task will take a bit long to perform.
Go to **Basic settings**, press **Edit**, and set the memory to **512 MB** and the timeout to **2 minutes**
    
## Creating an API for Our Lambda Function
1. Head over to the AWS console. Scroll down to **Networking and Content Delivery**, where you'll find **API Gateway**,
which is the service we'll be using to create an API endpoint for our Lambda function.
2. Select **Build a REST API**.
3. Create a **New API**, naming it something descriptive and leaving the two other fields as their defaults.
4. Go to **Actions > Create Method > POST** and click the checkmark.
5. Our integration type will be a **Lambda function**, we will **use Lambda proxy integration**, and our Lambda Function will be whatever we created earlier.
6. Let's test our method. In the following screen, click "test" and add a request body with the format `{"image_url": "<url>"}`. If all goes well, you'll receive a status code of 200.
7. Next, we need to configure our API to enable Cross Origin Resource Sharing (CORS). The bane of all web developers, a misconfigured CORS policy will prevent other websites from calling our API. To do this, go to **Actions** and select **Enable CORS**. 
8. Lastly, we'll need to deploy our API for the changes to take effect. Go to **Actions** and select **Deploy API**. Create a new stage with the name `prod` and hit deploy.

## Creating the Fridge Webpage

Check out the `index.html` file in this repo to see how to integrate the API with an HTML file that you host on S3. Make sure to swap out the active API link! 

## Room for Improvement
This demo actually isn't perfect. Perhaps the most glaring issue pertains to security - making everything public in an S3
bucket can be dangerous (which is why AWS warned us when we did it), and our Lambda function could've used a narrower policy
than the S3 Full Access policy. If you're curious, read more about AWS Identity Access Management and AWS security best practices.

The other glaring area of improvement (to me, at least - there could be more!) is the inability of this website to handle 
race conditions. If two users submit a new image at the same time, it's very possible that one of their images doesn't get 
added to the fridge. To prevent this, a good approach would be to first add all new image requests to a queue with AWS 
Simple Queue Service, which was alluded to at the beginning of this workshop.

**Make sure to spin down all your resources when you are done!**

