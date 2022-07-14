from diagrams import  Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.aws.database import Database, DMS
from diagrams.custom import Custom
from diagrams.aws.storage import SimpleStorageServiceS3BucketWithObjects, S3
from diagrams.aws.compute import LambdaFunction, Lambda
from diagrams.aws.management import CloudwatchEventEventBased
from diagrams.aws.analytics import GlueCrawlers, Glue, Quicksight, Athena
from diagrams.aws.security import Cognito
from diagrams.aws.network import APIGateway
from diagrams.aws.ml import MachineLearning, Forecast
from diagrams.aws.general import Users
from diagrams.aws.management import ManagementAndGovernance

graph_attr = {
    "fontsize": "32",
}


with Diagram("Analytics MVP (simplified)", show=False, direction="LR", graph_attr=graph_attr):


    graph_attr = {
        "fontsize": "22"
    }
    
    athena = Athena("Athena")
    quicksight = Quicksight("Quicksight")
    dashboard = Custom("Analytics Website", "./media/dashboard.jpeg")

    with Cluster("Data Sources", graph_attr=graph_attr):

        databases = Database("Databases")
        apis = Custom("APIs", "./media/api.png")
        flat_files = Custom("Flat Files", "./media/csv.png")

    with Cluster("Data Migration", graph_attr=graph_attr):
        dms = DMS("Database Migration Service")
        injestion = LambdaFunction("Custom Scripts")

    with Cluster("Data Repositories", graph_attr=graph_attr):
        curated = SimpleStorageServiceS3BucketWithObjects("Curated Datasets")
        raw = SimpleStorageServiceS3BucketWithObjects("Raw Data")
        published = SimpleStorageServiceS3BucketWithObjects("Published Data")

    # event = CloudwatchEventEventBased("Cloudwatch Events")

    with Cluster("Data Processing", graph_attr=graph_attr):
        glue_crawler = GlueCrawlers("Glue Crawlers")
        glue_job = Glue('Glue Jobs')
        spark = Spark("")

    with Cluster("Data Governance & Data Democratization", graph_attr=graph_attr):
        governance = ManagementAndGovernance("Governance")
        democratization = Users('Democratization')

    with Cluster("AI & Machine Learning", direction='LR', graph_attr=graph_attr):
        ml = MachineLearning("Machine Learning")
        # personalize = Personalize('Personalize')
        forecast = Forecast('Forecast')

    with Cluster("Web Application", graph_attr=graph_attr):
        web_app = LambdaFunction("Lambda")
        api_gateway = APIGateway("APIGateway")
        cognito = Cognito("Single Sign On (Cognito)")


    with Cluster("Other Consumers", graph_attr=graph_attr):
        rstudio = Custom("", "./media/r-studio.png")
        

    event = CloudwatchEventEventBased("Cloudwatch Events")  
    
    databases >> Edge(color="blue") >> dms >> raw
    apis >> Edge(color="blue") >> injestion >> raw
    flat_files >> Edge(color="blue") >> injestion >> raw
    event >> glue_job 
    raw >> glue_job >> spark >> curated
    ml >> published
    glue_job >> athena
    curated >> athena
    athena >> quicksight >> web_app >> api_gateway >> cognito >> dashboard
    governance >> dashboard
    governance >> web_app
    rstudio >> athena
    rstudio >> raw
    

