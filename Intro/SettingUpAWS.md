# Setting Up AWS

## Overview
### What You'll Learn

In this section you will learn:

1. What cloud computing is
2. The benefits of cloud computing
3. What Amazon Web Services (AWS) is
4. How to set up an AWS account

### Prerequisites
None!

### Introduction

#### What is cloud computing?

Cloud computing is the use of computing services - like servers, storage, databases, networking, and software - over the internet. Instead of having to manage these resources yourself, which can be complicated, expensive, and time consuming, you can access and use these resources managed by some other company. Essentially, you can rent out resources from a cloud provider (like AWS) on an on-demand basis without worrying about the underlying management.

#### What are the benefits of cloud computing?

Cloud computing allows your technology developments to be increasingly flexible, cost effective, and scalable.

Because you can request resources from a cloud provider on an on-demand basis, you can easily spin up or spin down resources and take advantages of existing services. Without the need to buy and manage resources yourself, you can focus on innovating and building your ideas much faster. This fundamental aspect of cloud computing also allows developers, like yourselves, the freedom to explore and experiment without upfront commitment.

By taking advantage of the cloud, you avoid spending a vast amount of money on resources like hardware, software, servers, costs for maintaining data centers, time, and labor.

Along with the ease of provisioning and terminating resources, cloud computing allows you to scale the capacity, power, bandwidth of resources up and down depending on your needs. Plus, by taking advantage of a cloud provider's global infrastructure, you can quickly scale your application globally.

#### What is AWS?

Amazon Web Services, or AWS, is Amazon's cloud service provider. It is one of the top cloud computing platforms and gives customers access to a wide array of services. AWS is used by thousands of companies and millions of people worldwide!

Other popular cloud providers are [Google Cloud Platform](https://cloud.google.com/) and [Microsoft Azure](https://azure.microsoft.com/en-us/).

**In this workshop, you will be using AWS to get yourselves acquainted with cloud computing.**

## Setting up an AWS Account

### Steps

1. Go to this [link](https://portal.aws.amazon.com/billing/signup?WIAWS=tile&tile=hero#/start) to create an AWS account

2. You will then be asked to enter:
    - An email
    - A password
    - An username

3. Then you will need to put in your contact information:
    - Account type
    - Company name
    - Phone number
    - Country
    - Address

4. You will need to put in your credit card information.
    - **Even though you enter your credit card information, you will NOT BE CHARGED throughout this workshop and if you choose to have a free tier account.**

5. Enter your phone number in order to receive a verification code.

6. After verifying, you can choose the type of your account. **Free tier is sufficient enough to go through this workshop.**

### Free Tier

#### What can you do with it?
The AWS Free Tier provides the ability to explore and try out AWS services free of charge up to specified limits for each service. The Free Tier is comprised of three different types of offerings, a 12-month free tier, an always free, and short term trials. For a full list, check their [site](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc).

#### Basic pricing model
Like most cloud service providers, the basic pricing model for AWS is only pay for what you use and pay as you go. Keep this pricing model in mind. Scale down any resources that can be scaled down, and shut down or terminate any resources that you aren't using.

**So, just remember to delete resources you spin up in this workshop once you are done using them so you don't accumulate resource usage and stray off from free tier. HackBU is not responsible for any charges that you incur over the course of this workshop.**

### AWS Management Console

After you log in to your AWS account, you are taken to the AWS Management Console. This is the place where you access and manage the AWS cloud and its services in one web interface.

It lists all the services organized under categories like Compute, Storage, Database, etc. When you click on a service, it will take you to its dashboard where you can manage its resources and settings. At the top of the page (left of the navigation bar), the Services drop-down will pull up a full list of services as well.

To the right of the navigation bar, you can see your name and it will give you a drop-down list to access your profile/account. You will also see a "N. Virginia" drop down list where you can specify the current region where your resources are managed (if applicable depending on the service). A region is a location where AWS holds their physical data centers. The default region is set to "US East (N. Virginia)", and you can leave that as the region for this workshop.
