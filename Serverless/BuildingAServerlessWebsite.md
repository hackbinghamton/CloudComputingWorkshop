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
