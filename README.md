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

### Serverless Application Repository
> The AWS Serverless Application Repository is a managed repository for serverless applications. It enables teams, organizations, and individual developers to store and share reusable applications, and easily assemble and deploy serverless architectures in powerful new ways.

- [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/)

### Kinesis Data Firehouse
> Kinesis Data Firehose can invoke your Lambda function to transform incoming source data and deliver the transformed data to destinations. You can enable Kinesis Data Firehose data transformation when you create your delivery stream.

> It invokes the specified Lambda function asynchronously with each buffered batch using the AWS Lambda synchronous invocation mode. The transformed data is sent from **Lambda** to Kinesis Data Firehose. Kinesis Data Firehose then sends it to the destination when the specified destination buffering size or buffering interval is reached, whichever happens first.

- [Amazon Kinesis Data Firehose Data Transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)


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

<!-- Icons: https://simpleicons.org/ Shields: https://img.shields.io/badge-->