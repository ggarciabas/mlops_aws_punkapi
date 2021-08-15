# Machine Learning Platform Engineer - MLOps!

[![](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&labelColor=white&logoColor=yellow&color=yellow)](https://aws.amazon.com/)
[![](https://img.shields.io/badge/serverless-layers?style=for-the-badge&logo=serverless&labelColor=white&color=red&)](https://www.serverless.com/) 
[![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&labelColor=white)](https://www.python.org/)
[![](https://img.shields.io/badge/Colab-Google?style=for-the-badge&labelColor=white&color=orange&logo=googlecolab)](https://colab.research.google.com/)


## Desafio Punk API

> Implementar uma arquitetura completa que consome a [Punk API](https://punkapi.com/documentation/v2), ingere em um S3 Bucket por meio do Kinesis Stream, cria uma tabela com AWS Glue Table e treina um modelo de Machine Learning para classificar as bebidas em seus respectivos `ibus`.

### Colab

Para acessar os notebooks via colab:
- [Exploração da API](https://colab.research.google.com/github/ggarciabas/mlops_aws_punkapi/blob/exp_punkapi/notebooks/Explora_API.ipynb)

## AWS
 
### Serverless Application

#### Model
> The AWS Serverless Application Model (AWS SAM) is an open-source framework that you can use to build serverless applications on AWS.

#### Repository
> The AWS Serverless Application Repository is a managed repository for serverless applications. It enables teams, organizations, and individual developers to store and share reusable applications, and easily assemble and deploy serverless architectures in powerful new ways.

- [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/)
- [Repository](https://serverlessrepo.aws.amazon.com/applications)
- [What is SAM?](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [AWS SAM template anatomy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html)

### Kinesis 

#### Data Firehouse
> Kinesis Data Firehose can invoke your Lambda function to transform incoming source data and deliver the transformed data to destinations. You can enable Kinesis Data Firehose data transformation when you create your delivery stream.

> It invokes the specified Lambda function asynchronously with each buffered batch using the AWS Lambda synchronous invocation mode. The transformed data is sent from **Lambda** to Kinesis Data Firehose. Kinesis Data Firehose then sends it to the destination when the specified destination buffering size or buffering interval is reached, whichever happens first.

- [Amazon Kinesis Data Firehose Data Transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)
- [Writing to Kinesis Data Firehose Using Kinesis Data Streams](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-kinesis-streams.html)
- [Kinesis Data Streams Quotas and Limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html)
- [Kinesis](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-kinesis.html)
- [boto Kinesis putRecord](http://boto.cloudhackers.com/en/latest/ref/kinesis.html#boto.kinesis.layer1.KinesisConnection.put_record)

### Lambda

- [AWS SAM template for a CloudWatch Events application](https://docs.aws.amazon.com/lambda/latest/dg/with-scheduledevents-example-use-app-spec.html)


### Glue

> AWS Glue is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development. AWS Glue provides all of the capabilities needed for data integration so that you can start analyzing your data and putting it to use in minutes instead of months.

- [AWS Glue](https://aws.amazon.com/glue/?did=ft_card&trk=ft_card&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)
- [template](https://gist.github.com/vdparikh/4c5d493fce53b9baf33edb39b17ff864)

### Github action SAM CLI
> This Action enables you to run AWS SAM CLI commands in order to build, package, and deploy serverless applications as part of your workflow.

- [Setup AWS SAM CLI](https://github.com/marketplace/actions/setup-aws-sam-cli)
- [Repos](https://github.com/aws-actions/setup-sam)
- [Using GitHub Actions to deploy serverless applications](https://aws.amazon.com/blogs/compute/using-github-actions-to-deploy-serverless-applications/)

## Referências de estudo

- [Batch Data Processing with AWS Kinesis Firehose and S3 | Overview](https://www.youtube.com/watch?v=DPT3swb6zgI)
- [AWS Kinesis Firehose to S3 Tutorial | Step by Step Setup Guide](https://www.youtube.com/watch?v=UMKnCEgE--k&t=0s)
- [AWS S3 File Upload + Lambda Trigger (Tutorial In Python) | Step by Step Guide](https://youtu.be/H_rRlnSw_5s)
- [Serverless](https://aws.amazon.com/getting-started/deep-dive-serverless/?e=gs2020&p=gsrc)
- [How to Handle your Python packaging in Lambda with Serverless plugins](https://www.serverless.com/blog/serverless-python-packaging)
- [Github and Colab](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb#scrollTo=8QAWNjizy_3O)
- [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/)
- [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/)
- [Using GitHub Actions to deploy serverless applications](https://aws.amazon.com/blogs/compute/using-github-actions-to-deploy-serverless-applications/)
- [Working with stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)
- [Sessions With SAM (S1E4): Building a Kinesis Firehose application for ingesting website access logs](https://www.youtube.com/watch?v=jdTBtaxs0hA)
- [Amazon Kinesis Data Firehose Data Transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)
- [Writing to Kinesis Data Firehose Using Kinesis Data Streams](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-kinesis-streams.html)
- [Writing to Kinesis stream using AWS Lambda Function](https://stackoverflow.com/questions/33824904/writing-to-kinesis-stream-using-aws-lambda-function)

<!-- Icons: https://simpleicons.org/ Shields: https://img.shields.io/badge-->