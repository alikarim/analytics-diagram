from diagrams import  Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.aws.database import RDS, Database, Aurora, DMS
from diagrams.custom import Custom
from diagrams.aws.analytics import *

# diagrams.aws.analytics.Analytics
# diagrams.aws.analytics.Athena
# diagrams.aws.analytics.CloudsearchSearchDocuments
# diagrams.aws.analytics.Cloudsearch
# diagrams.aws.analytics.DataLakeResource
# diagrams.aws.analytics.DataPipeline
# diagrams.aws.analytics.ElasticsearchService, ES (alias)
# diagrams.aws.analytics.EMRCluster
# diagrams.aws.analytics.EMREngineMaprM3
# diagrams.aws.analytics.EMREngineMaprM5
# diagrams.aws.analytics.EMREngineMaprM7
# diagrams.aws.analytics.EMREngine
# diagrams.aws.analytics.EMRHdfsCluster
# diagrams.aws.analytics.EMR
# diagrams.aws.analytics.GlueCrawlers
# diagrams.aws.analytics.GlueDataCatalog
# diagrams.aws.analytics.Glue
# diagrams.aws.analytics.KinesisDataAnalytics
# diagrams.aws.analytics.KinesisDataFirehose
# diagrams.aws.analytics.KinesisDataStreams
# diagrams.aws.analytics.KinesisVideoStreams
# diagrams.aws.analytics.Kinesis
# diagrams.aws.analytics.LakeFormation
# diagrams.aws.analytics.ManagedStreamingForKafka
# diagrams.aws.analytics.Quicksight
# diagrams.aws.analytics.RedshiftDenseComputeNode
# diagrams.aws.analytics.RedshiftDenseStorageNode
# diagrams.aws.analytics.Redshift


from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS

from diagrams.aws.analytics import KinesisDataStreams



with Diagram("SCPD Analytics (simplified)", show=False):

    with Cluster("Data Sources", graph_attr = { "bgcolor": "#FFFFFF"}):

        database = Database("Databases")
        api = Custom("APIs", "./media/api.png")
        flat_files = Custom("Flat Files", "./media/csv.png")
        streaming = KinesisDataStreams("Data Streams")



        with Cluster("Databases", graph_attr = { "bgcolor": "#FFFFFF"}):
            databases=[
                Database("Student"),
                Aurora("LMS"),
            ]

        with Cluster("API", graph_attr = { "bgcolor": "#FFFFFF"}):
            api = [Custom("", "./media/marketo.png"),
                Custom("", "./media/qualtrics.png"),
                Custom("", "./media/google_analytics.png"),
                Custom("Other", "./media/api.png"),
                Custom("Flat Files", "./media/csv.png")]

        with Cluster("Flat files", graph_attr = { "bgcolor": "#FFFFFF"}):
            flat_files = [Custom("Flat Files", "./media/csv.png")]

    dms = DMS("Database Migration Service")

    with Cluster("Data Repositories", graph_attr = { "bgcolor": "#FFFFFF"}):
        data_repository = [
            DataLakeResource("DataLakeResource")
            ]
            

    # with Cluster("Data Lake"):
    #     data_lake = [
    #         Analytics("Analytics"),
    #         Athena("Athena"),
    #         DataLakeResource("DataLakeResource"),
    #         Kinesis("Kinesis"),
    #         GlueCrawlers("GlueCrawlers"),
    #         GlueDataCatalog("GlueDataCatalog"),
    #         Glue("Glue"),
    #         DataPipeline("DataPipeline"),
    #         Quicksight("Quicksight"),
    #         Redshift("Redshift")
            
            
    #         ]

        databases >> Edge(color="brown") >> dms >> data_repository
