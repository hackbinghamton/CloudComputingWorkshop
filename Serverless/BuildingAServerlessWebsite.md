# Building a Serverless Website

## Introduction to Serverless
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


## Creating a Lambda Function
1. Head back over to the AWS console. You'll find Lambda under **Computer**, below EC2. Once there, you should see this
view:
    <Image Here>
2. Go to "Create a Function".
    1. Select "Author from Scratch"
    2. Name your function something descriptive (our code will be adding something to the fridge, so why not AddToFridge?)
    3. Choose **Python 3.7** as the runtime.
    <Image Here>
3. After a few seconds, our Lambda function will be created and ready for configuration. The screen will look something like
    <Image Here>
4. The first thing we're going to do is make sure our Lambda function can actually access our S3 bucket. To do so, head 
over to the "Permissions" tab and click on the hyperlink to our execution role.
    <Image Here>
This brings us to the IAM console, which will allow us to modify the policies of our Lambda's role.
    <Image Here>
5. Press "Attach Policies", search for AmazonS3FullAccess, and add that policy to the executor role.
    <Image Here>
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
and select **Upload a .zip file**
    <Image Here>
    

    
    

