# Spinning Up and Shutting Down An EC2 Instance

## Overview
**What you'll learn**

In this section, you'll learn
 1. What an EC2 Instance is
 2. How to run one for free

**Prerequisites**

 1. An AWS Account

**Introduction**

Let's start with the basics: EC2 stands for Elastic Compute Cloud, and it's one of AWS's most important services. EC2 is essentially a server renting platform, where users and companies pay Amazon a small fee over time in order to use one (or many) of Amazon's countless cloud servers. When we refer to an EC2 **Instance**, we're talking about one single server.

So why would we rent a server from Amazon instead of buying and setting up our own? Well the simple answer is **scalability**. An EC2 instance can be resized on the fly, and more instances can be easily set up or shut down based on increased or decreased demand for whatever service you're running.

Netflix runs almost all of its streaming through AWS because of scalability. When they have an uptick in users streaming, like on the premier of a new show or season, they can automatically scale up their number of servers. When traffic returns to normal levels, they can automatically scale back down again. This helps them pay for exactly the amount of computing power they need, which just isn't possible if you're running your service on your own physical servers.

## Let's Start an EC2 Instance

### Getting to the EC2 Management Console
First, we'll start by going to the AWS Management Console: https://console.aws.amazon.com/console/home?region=us-east-1

From here, click on Services in the top left corner. Now, either type in EC2 in the search bar, or click EC2 under the Compute section. This will bring you to the EC2 management console.

To get started, click on the bright orange Launch Instance button. This will start the process of setting up an EC2 instance.

### Step 1: Choosing an AMI
AMI stands for Amazon Machine Image. This might sound intimidating, but it's essentially just a template for what kind of server you want to start. The AMI you choose will determine what OS and software will be installed on your server when it boots up.

**Note**: If you want to make sure you stay within the free tier of AWS when starting an EC2, make sure you check the Free Tier Only box on the left side of the screen.

**Select the AMI at the top of the list: Amazon Linux 2 AMI (HVM), SSD Volume Type, 64-bit.**

### Step 2: Choosing an Instance Type
Here is where you choose how large/powerful your server will be. Different types will have different amounts of CPU cores, RAM, different network connection speeds, etc.

**Select the t2.micro option, which should say "Free Tier Eligible" beneath it.**

There are many other ways that you can configure an EC2 instance, including changing the amount of storage, adding tags, and adding security groups, but none of this is necessary for the purposes of this demo.

**Click the blue "Review and Launch" button, or click "7. Review" at the top of the page.**

### Step 3: Launching the Instance
On the review page, you can see all of the details of your EC2 instance.

**Once you're ready, click the blue "Launch" button.**

Now you'll see a window pop up asking you for a key pair.

**On the drop down menu, select "Create a new key pair". Then give the key pair a name, and press the "Download" button. This will download a file that you should keep in a safe place, as you'll need it to remotely access your instance once it's launched. Now you'll be able to press the "Launch Instances" button.**

### Step 4: Viewing the Instance
Congrats! Your instance is now launching.

**To view its details, scroll down on the launch status page and click "View Instances". Or, if you've already left that page, you can navigate back to the EC2 Management Console and click "Instances" on the left pane.**

Now you should see one item on the list, with an instance id of i-[a bunch of numbers and letters]. This is your EC2 instance.

**Click on the instance id and you should be taken to an overview of your instance's details. From here, click "Connect" in the top right, then click the orange "Connect" button on the next page.**

This will open a new tab in your browser where you should be greeted by a blank terminal. You're now connected to and controlling your EC2 instance! From here you could do anything you like with the server, like host a web app. Note that you can also connect to your instance outside of your browser using ssh. Instructions on how to do this are available by going back to your AWS console tab, then clicking "SSH Client" instead of "EC2 Instance Connect"

Now that you've spun up an EC2 instance, it's important to know how to take one down.
