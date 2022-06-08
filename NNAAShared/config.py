import os

os.environ['CosmosEndpoint'] = 'https://localhost:8081'
os.environ['CosmosKey'] = 'C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=='

os.environ["CosmosEnumsDB"] = 'DataStructure'
os.environ["CosmosEnumsCID"] = 'Enums'
os.environ["EnumsName"] = 'AlertStatus'
os.environ["EnumsUniqueKey"] = "5"
os.environ["EnumsApplicableKey"] = "12"
os.environ["EnumsNotApplicableKey"] = "13"

os.environ["CosmosDBName"] = 'ApplicibilityAssessmentDB'
os.environ["CosmosAlertsDB"] = 'AlertsDB'
os.environ["CosmosAlertsCID"] = 'AlertsContainer'