# Serverless Computing with API Gateway and Lambdas

## Overview
**What you'll learn**

In this section, you'll learn
1. What serverless computing is
2. How to set up Amazon Lambda functions to interface with APIs

**Prerequisites**
1. An AWS Account
2. How to set up a static website using S3 - [Hosting a Static Website Using Amazon S3](https://github.com/HackBinghamton/CloudComputingWorkshop/blob/master/S3/StaticWebsiteUsingS3.md)

## Introduction

**Serverless Computing**

Serverless computing is a model of cloud programming where a cloud provider operates the server which handles back-end needs. This can be really useful, because it allows you to run large applications without needing to purchase and maintain servers!

**Our Project**

We're going to combine a lot of the information we've learned so far in cloud computing and web development! First, we'll create a static website which accepts a URL for an image and sends that URL to an API. This API will be registered with AWS API gateway Then, it'll put the image on our glorious HackBU fridge using a Lambda function.

## Setting Up the Static Website

For information about basic HTML, check out our [Web Development Workshop!](https://github.com/HackBinghamton/WebDevelopmentWorkshop) All you'll need is HTML and a little bit of JS to take user input. [This tutorial](https://www.w3schools.com/jsref/dom_obj_text.asp) also has useful information on how to accept user input in your static website.

We also have a [tutorial about setting up S3 buckets](https://github.com/HackBinghamton/CloudComputingWorkshop/blob/master/S3/StaticWebsiteUsingS3.md) where you can learn to upload your website to a bucket.
