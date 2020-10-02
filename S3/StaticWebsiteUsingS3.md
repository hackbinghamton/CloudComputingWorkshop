# Hosting a Static Website Using Amazon S3

## Overview
### What You'll Learn

In this section you will learn:

1. What Amazon S3 is
2. The main properties of S3
3. How to set up a static website on S3

### Prerequisites

Before starting this section, you will need:

1. To know what AWS is and have an AWS account - [Setting Up An AWS Account](https://github.com/HackBinghamton/CloudComputingWorkshop/blob/master/Intro/SettingUpAWS.md)

2. Basic knowledge of creating static websites - you can refer back to our [Web Development Workshop](https://github.com/HackBinghamton/WebDevelopmentWorkshop)

## Introduction
### Amazon S3
Amazon S3 stands for Amazon Simple Storage Service. As the name implies, S3 is a storage provider on the cloud designed for simplicity. You can think of it as Amazon's version of Google Drive but on a larger scale.

### S3 Basic Concepts

A *bucket* is a storage container, the place where you put your files (you can basically think of it as a folder). Your files are called *objects* and they must be placed in a *bucket*. S3 is an object-based storage, so do not use it for installing operating systems or databases.

S3, as a simple, durable, scalable, and secure service, is often used in relation with other AWS services. You can use S3 as a standalone storage provider just like Google Drive, but Amazon provides many additional features one of which is static web hosting.

## Steps

It's time to begin creating a static website on Amazon S3. We'll go step by step and explain anything relevant along the way. There's a lot of details that can be covered, but we will not mention everything here. If you would like to explore the topics further on your own, just be aware of the free tier limits.

### 1) Open up the S3 console
Once you log in to your AWS account, find the S3 service through the list of services under the storage category. It will take you to the S3 console which is where you manage your S3 buckets.

### 2) Create a new S3 bucket
When you click on the blue "create bucket" button, you will see the bucket properties you need to set up.

Name and Region:
* *Bucket name* is the name for your bucket and it must be **globally unique**. Common names like "bucket" or "test" are most likely taken by someone else, so you cannot reuse them.
* A *region* is a geographical area where Amazon keeps their physical data centers, and as you can see from the drop down, there are multiple regions to select from. Since the default region is US East (N. Virginia), we will stick with that in this workshop.

Configure Options:
* The properties under this category are for the extra features of S3 that we will not go over in this workshop, so you can ignore these for now.

Set Permissions:
* By default, all buckets are set to private for security purposes. However, since you are creating a website that should be publicly available, your bucket needs to allow your objects to be set to public.
* Uncheck the "block all public access" option, then acknowledge the warning sign that appears.

Review:
* Review your S3 bucket settings and hit "create bucket".

### 3) Upload objects

Now that you made a bucket, click on it to see the contents. To add objects to this bucket, click on the "upload" button or drag and drop the files. You can upload pretty much any type of file -- text, images, videos, html files, etc. There is unlimited space within a bucket, and the maximum size of a *single object* is 5 TB.

Create your index.html that will act as the default home page of your website, and upload that to your bucket. You will see a panel to set your object's properties, but for now, you can leave everything as its default settings and hit the "upload" button on the bottom left.

### 4) Change permission settings of your objects

Click on your index.html object to see more details about it. Under the overview panel, you will see an "Object URL" link. Every object will have a unique URL. If you click on the link, you will see an "access denied" message. This is because every object you upload by default is set to private. In order to view this link, you need to make it public by pressing the "make public" button in the overview panel. Now press the link again, and you should see your index.html page up.

For every object you upload, you will need to specify it to be public. There's multiple ways to do that besides the one from above. Another way is to change the permission in the uploading panel (from step 3), choosing "grant public read access to this object(s)".


### 5) Enable static website hosting

You created a bucket that contains an index.html object. Right now, it's simply acting as a regular storage, not a static website. To change that, you need to enable static website hosting.

Go to the properties panel of the bucket, and you will see "static website hosting" sub-panel. Click on it, and you will see the option to "use this bucket to host a website" and the settings you need to specify:

* The *index document* is the file in your bucket that will become the home page of your website. You uploaded an index.html file, so you can specify that in there.
* The *error document* is the page that will show up if something goes wrong with your website. You can leave it blank for now.
* The *redirection rules* are rules written in XML that you can write to reroute requests based on conditions. You can also leave this part alone.

Take note of the endpoint link. That will be the url to your static website.

Now hit save.

### 6) Check to see that your static website is up and running

Go to your website (endpoint) link and see if your website is properly running. If it is, congrats! You successfully created a static website on Amazon S3.

## Exercise: Continue playing around with S3

Now that you have a static website up and running, continue to familiarize yourself with S3.
* Try adding more objects to your buckets
* Try setting up an error document to see what happens when your index.html cannot load properly
  * You can manually trigger this by setting your index document back to private by changing the object's permissions
* Try to create a new bucket hosting a static website (and see if you can do it without referring back to the steps)

## Additional mentions

As you can see from your website url, your website is available on the Amazon S3 endpoint. If you want/have a registered domain name that you want to change it to, it is possible to do so. You can learn more about how to do that [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html). Registering a domain name will cost money!

From your url, you can also see the website uses HTTP instead of HTTPS. S3 alone does not support HTTPS, so if you want to serve your static website over a secure protocol, you would need to utilize another AWS service called CloudFront. CloudFront is not part of free tier, but if you still want to read about it, you can check [this link](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/) out.

Web browsers follow a security model called the same-origin policy where a browser only permits requests contained within the same origin. For example, if a script from domain A sends a request domain B to retrieve data, the browser will block that request. S3 follows the same policy, so you may encounter blocking errors when building your website. In order to alleviate the strict restrictions, you need to enable CORS, which stands cross-origin resource sharing. It allows you to configure rules to allow web applications in one domain to interact with other domains, preventing requests from being blocked. You can enable CORS in the bucket's permissions, then pass in a configuration file written in XML which you can learn more about [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html#how-do-i-enable-cors).

## Terminating Your S3 Buckets

Before you leave this section of the workshop, delete your objects and buckets just to ensure that you aren't accruing AWS resources. If you are certain that you want to keep your S3 bucket, just be aware of the free tier limits.

Head back to the main S3 console page where it lists all your buckets. Select the bucket and press the "delete" button. All the objects within the bucket will also be deleted. Read the warning and confirm your deletion by entering the name of your bucket.
