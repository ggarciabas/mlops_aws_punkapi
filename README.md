# Machine Learning Platform Engineer - MLOps!

[![](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&labelColor=white&logoColor=yellow&color=yellow)](https://aws.amazon.com/)
[![](https://img.shields.io/badge/serverless-layers?style=for-the-badge&logo=serverless&labelColor=white&color=red&)](https://www.serverless.com/) 
[![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&labelColor=white)](https://www.python.org/)
[![](https://img.shields.io/badge/Colab-Google?style=for-the-badge&labelColor=white&color=orange&logo=googlecolab)](https://colab.research.google.com/)
[![](https://img.shields.io/badge/VsCode-007ACC?style=for-the-badge&labelColor=white&color=007ACC&logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com/)
[![](https://img.shields.io/badge/Github-181717?style=for-the-badge&labelColor=white&color=181717&logo=github&logoColor=181717)](https://code.visualstudio.com/)


## Desafio Punk API

> Implementar uma arquitetura completa que consome a [Punk API](https://punkapi.com/documentation/v2), ingere em um S3 Bucket por meio do Kinesis Stream, cria uma tabela com AWS Glue Table e treina um modelo de Machine Learning para classificar as bebidas em seus respectivos `ibus`.

### Arquitetura
<!-- Aprensentar arquitetura -->

![](https://github.com/ggarciabas/mlops_aws_punkapi/raw/main/img/arquitetura_final.png)


### Colab

Para acessar os notebooks via colab:
- :heavy_check_mark: [Exploração da API](https://colab.research.google.com/github/ggarciabas/mlops_aws_punkapi/blob/master/notebooks/Explora_API.ipynb)
- :heavy_check_mark: [Modelo ML](https://colab.research.google.com/github/ggarciabas/mlops_aws_punkapi/blob/master/notebooks/Modelagem_Final.ipynb)


### SAM
<!-- Adicionar caminhos para os scripts -->

- :heavy_check_mark: [Configurações SAM](https://github.com/ggarciabas/mlops_aws_punkapi/blob/analise/sam-aws/sam-aws-punkapi.yml)
- :heavy_check_mark: [Função Lambda para consultar API](https://github.com/ggarciabas/mlops_aws_punkapi/blob/analise/sam-aws/punkapi_cli/app.py)
- :heavy_check_mark: [Função Lambda para limpar dados](https://github.com/ggarciabas/mlops_aws_punkapi/blob/analise/sam-aws/punkapi_clean/app.py)

### Github actions

- :heavy_check_mark: [Workflow para criar arquitetura na AWS](https://github.com/ggarciabas/mlops_aws_punkapi/blob/analise/.github/workflows/sam-pipeline.yml)

#### SAM CLI
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
- [aws-samples/sessions-with-aws-sam](https://github.com/aws-samples/sessions-with-aws-sam)
- [Amazon Kinesis Data Firehose Data Transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)
- [Writing to Kinesis Data Firehose Using Kinesis Data Streams](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-kinesis-streams.html)
- [Writing to Kinesis stream using AWS Lambda Function](https://stackoverflow.com/questions/33824904/writing-to-kinesis-stream-using-aws-lambda-function)
- [How do I give permissions to my Lambda functions by using policies and roles in AWS SAM templates?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-sam-template-permissions/)
- [SVS317-R Serverless stream processing pipeline best practices](https://d1.awsstatic.com/events/reinvent/2019/REPEAT_1_Serverless_stream_processing_pipeline_best_practices_SVS317-R1.pdf)
- [ANT316 Choosing the right service for your data streaming needs](https://d1.awsstatic.com/events/reinvent/2019/Choosing_the_right_service_for_your_data_streaming_needs_ANT316.pdf)
- [ANT326 Building a streaming data platform with Amazon Kinesis](https://d1.awsstatic.com/events/reinvent/2019/REPEAT_1_Building_a_streaming_data_platform_with_Amazon_Kinesis_ANT326-R1.pdf)
- [Building real time data pipelines with AWS Kinesis](http://www.lifeisafile.com/Building-data-pipelines-with-AWS-Kinesis/)

<!-- Icons: https://simpleicons.org/ Shields: https://img.shields.io/badge-->
