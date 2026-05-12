---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 518
---

# Implementation steps

• First, define a contract for your API. A contract will express the capabilities of an API as well as
define strongly typed data objects and fields for the API input and output.
• When you configure APIs in API Gateway, you can import and export OpenAPI Specifications for
your endpoints.
• Importing an OpenAPI definition simplifies the creation of your API and can be integrated with
AWS infrastructure as code tools like the AWS Serverless Application Model and AWS Cloud
Development Kit (AWS CDK).
• Exporting an API definition simplifies integrating with API testing tools and provides services
consumer an integration specification.
• You can define and manage GraphQL APIs with AWS AppSync by defining a GraphQL schema file
to generate your contract interface and simplify interaction with complex REST models, multiple
database tables or legacy services.
• AWS Amplify projects that are integrated with AWS AppSync generate strongly typed JavaScript
query files for use in your application as well as an AWS AppSync GraphQL client library for
Amazon DynamoDB tables.
• When you consume service events from Amazon EventBridge, events adhere to schemas that
already exist in the schema registry or that you define with the OpenAPI Spec. With a schema
defined in the registry, you can also generate client bindings from the schema contract to
integrate your code with events.
• Extending or version your API. Extending an API is a simpler option when adding fields that can
be configured with optional fields or default values for required fields.
• JSON based contracts for protocols like REST and GraphQL can be a good fit for contract
extension.
• XML based contracts for protocols like SOAP should be tested with service consumers to
determine the feasibility of contract extension.
• When versioning an API, consider implementing proxy versioning where a facade is used to
support versions so that logic can be maintained in a single codebase.
